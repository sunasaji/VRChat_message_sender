# はじめに
VRChatのフレンドになった日時とユーザ名をテキストに書き出すツールです。VRChat moderation APIを使っています。全てのフレンド名は取り出せない場合があるのでご留意ください。またミュート/アンミュート操作をした場合、その日時が出力されます。

[English](https://github.com/sunasaji/VRChat_Friend_History/blob/master/README.md) | Japanese

# 使い方
1. リリース [release](https://github.com/sunasaji/VRChat_Friend_History/releases) からZIP をダウンロードして解凍するか Python3.7.x を入れてソースをダウンロードします。

2. `credential.json` を開き `USERNAME` を自分の VRChat ユーザ名に置き換え, `PASSWORD` を自分の VRChat パスワードに置き換えます。

3. `VRChat_Friend_History.exe` またはPythonスクリプトを実行します。

4. `VRChat_Friend_History.txt` が生成されるので開きます。

# 出力例
```
2018-05-11T17:53:08.648Z 1人目のフレンドさんのユーザ名
2018-05-11T18:24:14.295Z 2人目のフレンドさんのユーザ名
```

# 自分でビルドする場合

1. Python3.7.x をインストールする
2. `pip install requests` を実行
3. `pip install pyinstaller` を実行
4. `pyinstaller VRChat_Friend_History.py --onefile --noconsole` を実行
5. dist フォルダに exe が生成される

# ライセンス
MIT License です。[LICENSE](https://github.com/sunasaji/VRChat_Friend_History/blob/master/LICENSE) ファイルを見てください。
