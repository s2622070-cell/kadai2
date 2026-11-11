import sqlite3
import time
import re
import requests
from bs4 import BeautifulSoup

# --- 1. データベースの初期化 ---
conn = sqlite3.connect("google_repos.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS repositories")
cursor.execute("""
CREATE TABLE repositories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    repo_name TEXT NOT NULL,
    language TEXT,
    stars INTEGER
)
""")
conn.commit()

# --- 2. スクレイピング処理 ---
base_url = "https://github.com/orgs/google/repositories?page={}"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

max_pages = 3
ignore_paths = {"/google", "/orgs/google", "/google/sponsors", "/orgs/google/repositories", "/orgs/google/people"}

for page in range(1, max_pages + 1):
    url = base_url.format(page)
    print(f"[{page}/{max_pages}] Fetching: {url}")
    
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(f"  取得失敗 (Status: {res.status_code})")
        break
        
    soup = BeautifulSoup(res.text, "html.parser")
    
    all_links = soup.find_all("a", href=True)
    seen_names = set()
    
    for a in all_links:
        href = a['href']
        
        if href.startswith("/google/") and href not in ignore_paths:
            parts = href.split("/")
            if len(parts) >= 3:
                repo_name = parts[2].split("?")[0].split("#")[0]
                
                if not repo_name or repo_name in seen_names or "/" in repo_name:
                    continue
                
                seen_names.add(repo_name)
                
                # リポジトリ1件分を包む最上位親要素（li / article / Box-row）を取得
                card = a
                while card and card.parent and card.parent.name != 'body':
                    card = card.parent
                    if card.name in ['li', 'article']:
                        break
                    classes = " ".join(card.get('class', [])).lower()
                    if 'box-row' in classes or 'col-12' in classes:
                        break
                
                # --- 主要言語の抽出 ---
                language = "None"
                
                # 方法1: itemprop="programmingLanguage"
                lang_elem = card.find(attrs={"itemprop": "programmingLanguage"})
                
                # 方法2: repo-language-color (言語カラーアイコンの隣または親要素)
                if not lang_elem:
                    color_dot = card.find("span", class_=re.compile(r"repo-language-color"))
                    if color_dot:
                        next_sib = color_dot.find_next_sibling()
                        if next_sib and next_sib.get_text(strip=True):
                            lang_elem = next_sib
                        else:
                            lang_elem = color_dot.parent
                
                # 方法3: クラス名に language が含まれる要素
                if not lang_elem:
                    lang_elem = card.find(class_=re.compile(r"language", re.I))
                
                if lang_elem:
                    language = lang_elem.get_text(strip=True)
                else:
                    # 方法4: カード全体のHTML文字列から正規表現で直接探索
                    card_str = str(card)
                    m_itemprop = re.search(r'programmingLanguage["\']>([^<]+)<', card_str)
                    m_color = re.search(r'repo-language-color[^>]*></span>\s*<span[^>]*>([^<]+)<', card_str, re.DOTALL)
                    m_text = re.search(r'repo-language-color[^>]*></span>\s*([A-Za-z0-9#+\-\.]+)', card_str)
                    
                    if m_itemprop:
                        language = m_itemprop.group(1).strip()
                    elif m_color:
                        language = m_color.group(1).strip()
                    elif m_text:
                        language = m_text.group(1).strip()
                
                # --- スター数の抽出 ---
                star_elem = card.find("a", href=re.compile(r"/stargazers"))
                stars = 0
                if star_elem:
                    raw_text = star_elem.get_text(strip=True).replace(",", "").lower()
                    match = re.search(r'([\d.]+)\s*([km])?', raw_text)
                    if match:
                        num_str, unit = match.groups()
                        try:
                            val = float(num_str)
                            if unit == 'k':
                                stars = int(val * 1000)
                            elif unit == 'm':
                                stars = int(val * 1000000)
                            else:
                                stars = int(val)
                        except ValueError:
                            stars = 0
                
                # データベースに保存
                cursor.execute("""
                INSERT INTO repositories (repo_name, language, stars)
                VALUES (?, ?, ?)
                """, (repo_name, language, stars))

    conn.commit()
    print(f"  -> {len(seen_names)} 件のリポジトリを取得・保存しました")
    
    # 課題要件: 1秒待機
    time.sleep(1)

# --- 3. SELECT文でデータを表示 ---
print("\n=== 保存されたリポジトリ情報 (SELECT文による抽出) ===")
cursor.execute("SELECT id, repo_name, language, stars FROM repositories")
rows = cursor.fetchall()

if not rows:
    print("データが保存されませんでした。")
else:
    print(f"{'ID':<5} | {'Repository Name':<35} | {'Language':<15} | {'Stars':<8}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<35} | {row[2]:<15} | {row[3]:<8}")

conn.close()