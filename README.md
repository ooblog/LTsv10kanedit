# 「LTsv10kanedit(tsvtool10)」は「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kantray」のPythonによる実装の予定です。

## 「kantray」→「kanedit」に移行計画。

![kanedit_512](icon_cap/kanedit_512.png "kanedit")  
キー入力割り込みはOSによっては動かないもしくは意図しない動きになる危険性があるので、「kantray」の代わりに漢直専用エディタ「kanedit」の開発をしています。  
旧「kantray」に関しては「[https://github.com/ooblog/LTsv9kantray](https://github.com/ooblog/LTsv9kantray "LTsv9kantray")」を参考。


## 「kanfont」は単漢字辞書&#91;kanchar.tsv&#93;を管理するソフトの予定です。辞書の項目にはフォントのグリフデザインも含まれます。

![kanfont_512](icon_cap/kanfont_512.png "kanfont")  
「kanfont.svg」を「kantray5x5comic.ttf」に変換するには「[FontForge](http://fontforge.github.io/ja/ "FontForge")」が別途必要です。  
FontForgeの導入が困難なWindowsの場合、「kantray5x5comic.woff」を「[WOFFコンバータ](http://opentype.jp/woffconv.htm "WOFFコンバータ")」でTTFに変換してください。  


## 「kanzip」は郵便番号辞書&#91;kanzip.tsv&#93;を作成するソフトの予定です。

![kanzip_512](icon_cap/kanzip_512.png "kanzip")  
「[〒郵便番号](http://www.post.japanpost.jp/zipcode/dl/readme.html "郵便番号データの説明 - 日本郵便")」からzipをダウンロードして郵便番号辞書「kanzip.tsv」を作成します。  


## 「LTsv」はアプリを作るためのモジュール群です。

モジュール群の仕様や日時フォーマット・電卓フォーマットの仕様とかは[LTsv/LTsv.txt](LTsv/LTsv.txt "LTsv.txt")の方に書いてます。  
「kanedit」「kanfont」「kanzip」の操作方法は[kanedit.txt](kanedit.txt "kanedit.txt")にて書く予定です。  
ドキュメントは整理中につき「kantray」で実装してた「kanedit」で未実装のキーボード漢直の話題が混在しています。  


## 動作環境。

Python 2.7.6&#40;Tahrpup6.0.5)およびPython3.4.4&#40;Wine1.7.18&#41;で動作を確認しています。  


## ライセンス・著作権など。

Copyright (c) 2016 ooblog  
License: MIT  
[https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE](https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE "https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE")  
