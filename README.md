# 「LTsv10kanedit(tsvtool10)」は「L:Tsv」の読み書きを中心としたモジュール群と漢字エディタ「kanedit」のPythonによる実装の予定です。

## 「kanedit」は漢直エディタです&#40;開発中&#41;。NFER,XFER,KANAキーを用いて鍵盤を切り替える事で漢字の直接入力を目指してます。

![kanedit_512](icon_cap/kanedit_512.png "kanedit")  
前作「[https://github.com/ooblog/LTsv9kantray](https://github.com/ooblog/LTsv9kantray "LTsv9kantray")」のキーフックの代わりに漢直専用エディタ「kanedit」の開発中です。  
「kanedit」で用いる漢直キーボードをなるだけ簡単な方法で他のソフトにも搭載できるようにというのが「LTsv10kanedit」のコンセプトになります。  
※エディタ「kanedit」は現在１行テキストの箇所だけ動いてます。テキストファイルの編集などはまだ実装してません。  

「kanedit」の詳細は「[kanedit.txt](kanedit.txt "kanedit.txt")」を参考。  


## 「kanfont」は単漢字辞書「kanchar.tsv」を編集するソフトです。辞書の項目にはフォント「kan5x5cmic」のグリフデザインも含まれます。

![kanfont_512](icon_cap/kanfont_512.png "kanfont")  
「[kanchar.tsv](kanchar.tsv "kanchar.tsv")」から「kan5x5.svg」を生成して、「[FontForge](http://fontforge.github.io/ja/ "FontForge")」で変換してもらう事でフォントが作成できます。
FontForgeの導入が困難なWindowsの場合、「kan5x5comic.woff&#40;準備中&#41;」を「[WOFFコンバータ](http://opentype.jp/woffconv.htm "WOFFコンバータ")」でTTFに変換してください。  

「kanedit」の詳細は「[kanfont.txt](kanfont.txt "kanfont.txt")」を参考。  


## 「kanzip」は郵便番号辞書「kanzip.tsv」を作成するソフトです&#40;「kanzip.tsv」は同梱してません&#41;。

![kanzip_512](icon_cap/kanzip_512.png "kanzip")  
「[〒郵便番号](http://www.post.japanpost.jp/zipcode/dl/readme.html "郵便番号データの説明 - 日本郵便")」からzipをダウンロードして郵便番号辞書「kanzip.tsv」を作成します。  

「kanzip」の詳細は「[kanzip.txt](kanzip.txt "kanzip.txt")」を参考。  


## 「kanmap」は漢字配列「kanmap.tsv」を編集する…事はまだできませんが「kan5x5comic」を「kanpickle.bin」にある程度積み込む事ができます。

![kanmap_512](icon_cap/kanmap_512.png "kanmap")  
「[kanmap.tsv](kanmap.tsv "kanmap.tsv")」から「kanpickle.bin」と「kanmap.png」を生成します&#40;PNGの生成はGTKのみ&#41;。  

「kanmap」の詳細は「[kanmap.txt](kanmap.txt "kanmap.txt")」を参考。  


## 「L&#58;Tsv」は上記のようなソフトが作れるモジュール群です。

「L&#58;Tsv」の詳細は「[LTsv/LTsv.txt](LTsv/LTsv.txt "LTsv.txt")」を参考。  
ドキュメントは整理中につき「kantray」の話題が混在しています。  


## 動作環境。

Python 2.7.6&#40;Tahrpup6.0.5)およびPython3.4.4&#40;Wine1.7.18&#41;で動作を確認しています。  


## ライセンス・著作権など。

Copyright (c) 2016 ooblog  
License: MIT  
[https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE](https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE "https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE")  
