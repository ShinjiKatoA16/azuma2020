# さくひんをつくって github にいれてみましょう

- git (version かんりのプログラム) をインストール Q:\04_python\01_開発環境 (https://gitforwindows.org/ からダウンロードしても OK)
- github に User ID をさくせい. github.com で signup  (UserID Password をわすれないようにメモ)
- なにをつくるかきめる (tkinter のプログラム、AOJ/AtCoder のプログラム、Socket アプリ、HomePage, etc)
- github で Repository のさくせい (tkinter ならば tkinter_sample などわかりやすいなまえ) Readme.md にないようをかく


## git コマンドのつかいかた

GUI の Client Application もあるけど、うごきを りかいするために コマンドの つかいかたを おぼえましょう

### Status, commit のりれきのかくにん

- `git status`
- `git log`

### Local Repository さくせい

- `git clone https://github.com/user_name/repository_name` さいしょの1回だけじっこう。github の repository とおなじものを local PC につくる (URL は github の repository のページから Copy & Paste するとまちがいがすくない)

### Local のへんこうを github にはんえい

- Local PC の directory で file のへんしゅう・ついか
- `git add ファイル名`  または  `git add --ALL`
- `git commit -m "コメント"`
- `git push`

### github のへんこうを Local にはんえい

- `git pull`
