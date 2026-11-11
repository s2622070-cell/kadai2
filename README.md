- GithubのGoogleが管理しているリポジトリの情報をスクレイピングして下記の情報を取得する
    - リポジトリ名，主要な言語，スターの数
- 上記のデータを保存するためのDBを作成し、スクレイピングしたデータを保存する
    - GitHubのAPIは使わないこと。スクレイピングの課題なので
    - ちゃんと time.sleep(1) を入れる
- 保存したデータをSELECT文で表示する

=== 保存されたリポジトリ情報 (SELECT文による抽出) ===
ID    | Repository Name                     | Language        | Stars   
----------------------------------------------------------------------
1     | crubit                              | C++             | 1100    
2     | crosvm                              | Rust            | 1400    
3     | j2cl                                | Java            | 1400    
4     | tcmalloc                            | C++             | 5400    
5     | xrblocks                            | TypeScript      | 513     
6     | tunix                               | Python          | 2500    
7     | XNNPACK                             | C               | 2500    
8     | alioth                              | Rust            | 396     
9     | civics_cdf_validator                | Python          | 41      
10    | osv-scanner-action                  | Python          | 103     
11    | skia                                | C++             | 11000   
12    | filament                            | C++             | 21000   
13    | gvisor                              | Go              | 20000   
14    | flutter-mediapipe                   | Dart            | 295     
15    | adk-python                          | Python          | 22000   
16    | jetpack-camera-app                  | Kotlin          | 347     
17    | three-live                          | TypeScript      | 309     
18    | perfetto                            | C++             | 6800    
19    | osv.dev                             | Go              | 3100    
20    | s2a-go                              | Go              | 29      
21    | android-cuttlefish                  | C++             | 750     
22    | budoux                              | Python          | 1800    
23    | chromium-policy-vulnfeed            | Go              | 14      
24    | adk-docs                            | Shell           | 1500    
25    | earthengine-catalog                 | Jsonnet         | 147     
26    | tpu-sync                            | C++             | 169     
27    | eclipsa-studio                      | Dart            | 6       
28    | xls                                 | C++             | 2000    
29    | peregrine                           | C++             | 6       
30    | orbax                               | Python          | 540     
31    | angle                               | C++             | 4100    
32    | open-sztp                           | Go              | 14      
33    | zerocopy                            | Rust            | 2600    
34    | filament-assets                     | Wolfram Language | 5       
35    | qwix                                | Python          | 143     
36    | ios-webkit-debug-proxy              | C               | 6200    
37    | boringssl                           | C++             | 2300    
38    | guava                               | Java            | 52000   
39    | truestreet                          | Go              | 45      
40    | GoogleSignIn-iOS                    | Objective-C     | 759     
41    | GTMAppAuth                          | Swift           | 451     
42    | adk-js                              | TypeScript      | 1500    
43    | elephant-goldfish-model             | Python          | 17000   
44    | earthengine-api                     | JavaScript      | 3500    
45    | oss-fuzz                            | Shell           | 13000   
46    | p4-infra                            | C++             | 8       
47    | highway                             | C++             | 6000    
48    | nearby                              | C++             | 991     
49    | moodle-on-gcp                       | HTML            | 74      
50    | koladata                            | C++             | 36      
51    | saferpickle                         | Python          | 28      
52    | adk-kotlin                          | Kotlin          | 306     
53    | compute-virtual-ethernet-dpdk       | C               | 14      
54    | betosim                             | Rust            | 8       
55    | adk-java                            | Java            | 1800    
56    | swiftshader                         | C++             | 2600    
57    | cybernetic-agent-governance-engine  | Python          | 46      
58    | quiche                              | C++             | 907     
59    | site-kit-wp                         | JavaScript      | 1400    
60    | libmotionphoto                      | C++             | 1       
61    | gemma.cpp                           | C++             | 7100    
62    | tensorstore                         | C++             | 1600    
63    | EarlGrey                            | Objective-C     | 5700    
64    | bughunters                          | None            | 331     
65    | stellar-engine                      | HCL             | 62      
66    | ground-android                      | Kotlin          | 298     
67    | device-infra                        | Java            | 86      
68    | goonami-scanner                     | Go              | 33      
69    | meridian                            | Python          | 1600    
70    | osv-scalibr                         | Go              | 658     
71    | mobly                               | Python          | 761     
72    | aarch64-esr-decoder                 | Rust            | 124     
73    | libhoth                             | C               | 22      
74    | clusterfuzz                         | Python          | 5600    
75    | j2objc                              | Java            | 6000    
76    | differential-privacy                | Go              | 3400    
77    | openhtf                             | Python          | 729     
78    | adk-go                              | Go              | 9000    
79    | GNM                                 | Python          | 1600    
80    | hdmitsuba                           | Python          | 90      
81    | metrax                              | Python          | 64      
82    | net_http                            | Python          | 31      
83    | inverting-proxy                     | Go              | 278     
84    | go-tpm-tools                        | C               | 312     
85    | nomulus                             | Java            | 1800    
86    | heir                                | MLIR            | 948     
87    | langfun                             | Python          | 920     
88    | dopamine                            | Jupyter Notebook | 11000   
89    | osv-scanner                         | Go              | 11000   
90    | skia-buildbot                       | Go              | 178     
