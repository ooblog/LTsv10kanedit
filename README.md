# 「LTsv10kanedit(tsvtool10)」は「L:Tsv」の読み書きを中心としたモジュール群です。

html版ドキュメント整備中。「[https://ooblog.github.io/LTsv10kanedit/](https://ooblog.github.io/LTsv10kanedit/ "「LTsv10kanedit(tsvtool10)」は「L:Tsv」の読み書きを中心としたモジュール群です。")」


## 「kanedit」は「LTsv10kanedit&#40;tsvtool10&#41;」を用いた漢直テキストエディタの予定です。

![kanedit_512x384](docs/kanedit_512x384.png "kanedit")  
NFER,XFERキーによる鍵盤切替＆KANAキーによる字引入力で漢字を直接入力します。  
※エディタ「kanedit」は現在１行テキストの「電卓」だけ動いてます&#40;開発中&#41;。テキストファイルの編集などはまだ実装してません。  

「kanedit」の詳細は「[docs/kanedit.txt](https://github.com/ooblog/LTsv10kanedit/blob/master/docs/kanedit.txt "「kanedit」は「LTsv10kanedit(tsvtool10)」を用いた漢直テキストエディタの予定です。")&#40;[kanedit.html](https://ooblog.github.io/LTsv10kanedit/kanedit.html "「kanedit」は「LTsv10kanedit(tsvtool10)」を用いた漢直テキストエディタの予定です。")&#41;」を参考。  


## 「kanfont」は「LTsv10kanedit&#40;tsvtool10&#41;」を用いたフォントエディタ(グリフエディタ)です。

![kanfont_512x384](docs/kanfont_512x384.png "kanfont")  
「[LTsv/kanchar.tsv](LTsv/kanchar.tsv "LTsv/kanchar.tsv")」から「kan5x5.svg」を生成して「[FontForge](http://fontforge.github.io/ja/ "FontForge")」などで変換してフォント「kan5x5comic.ttf」も作成できますが、  
「kanedit」は「[LTsv/kanchar.tsv](LTsv/kanchar.tsv "LTsv/kanchar.tsv")」を直に読み込む事でグリフを描画します。これにより「Tkinter」で表示できないCP932&#40;いわゆるシフトJIS、BMP基本多言語面0xffff範囲&#41;外の文字を扱えます。  

「kanfont」の詳細は「[docs/kanfont.txt](https://github.com/ooblog/LTsv10kanedit/blob/master/docs/kanfont.txt "「kanfont」は「LTsv10kanedit(tsvtool10)」を用いたフォントエディタ(グリフエディタ)です。")&#40;[kanfont.html](https://ooblog.github.io/LTsv10kanedit/kanfont.html "「kanfont」は「LTsv10kanedit(tsvtool10)」を用いたフォントエディタ(グリフエディタ)です。")&#41;」を参考。  


## 「kanzip」は「LTsv10kanedit&#40;tsvtool10&#41;」を用いた郵便番号ダウンローダーです。

![kanzip_512x384](docs/kanzip_512x384.png "kanzip")  
「[〒郵便番号](http://www.post.japanpost.jp/zipcode/dl/readme.html "郵便番号データの説明 - 日本郵便")」からzipをダウンロードして郵便番号辞書「kanzip.tsv」を作成します。  

「kanzip」の詳細は「[docs/kanzip.txt](https://github.com/ooblog/LTsv10kanedit/blob/master/docs/kanzip.txt "「kanzip」は「LTsv10kanedit(tsvtool10)」を用いた郵便番号ダウンローダーです。")&#40;[kanzip.html](https://ooblog.github.io/LTsv10kanedit/kanzip.html "「kanzip」は「LTsv10kanedit(tsvtool10)」を用いた郵便番号ダウンローダーです。")&#41;」を参考。  


## 「kanmap」は「LTsv10kanedit&#40;tsvtool10&#41;」を用いたグリフ進捗ビュアーです。

![kanmap_512x384](docs/kanmap_512x384.png "kanmap")  
「kan5x5comic」グリフ作成の進捗状況が確認できます。編集機能は準備中です。  

「kanmap」の詳細は「[docs/kanmap.txt](https://github.com/ooblog/LTsv10kanedit/blob/master/docs/kanmap.txt "「kanmap」は「LTsv10kanedit(tsvtool10)」を用いたグリフ進捗ビュアーです。")&#40;[kanmap.html](https://ooblog.github.io/LTsv10kanedit/kanmap.html "「kanmap」は「LTsv10kanedit(tsvtool10)」を用いたグリフ進捗ビュアーです。")&#41;」を参考。  


## 「LTsv_doc」は「LTsv10kanedit&#40;tsvtool10&#41;」を用いたドキュメントジェネレーターです。

![LTsv_doc_512x384](docs/LTsv_doc_512x384.png "LTsv_doc")  
モジュール解説文書「[docs/LTsv10.txt](https://github.com/ooblog/LTsv10kanedit/blob/master/docs/LTsv10.txt "「<？LTsv>」は「L:Tsv」の読み書きを中心としたモジュール群です。")&#40;[index.html](https://ooblog.github.io/LTsv10kanedit/index.html "「<？LTsv>」は「L:Tsv」の読み書きを中心としたモジュール群です。")&#41;」等は「[LTsv/LTsv_doc.py](LTsv/LTsv_doc.py "LTsv/LTsv_doc.py")」を使って「[docs/kanedit_etc.tsv](docs/kanedit_etc.tsv "docs/kanedit_etc.tsv")」から生成されてます。  

「LTsv_doc」の詳細は「[docs/LTsv_doc.txt](https://github.com/ooblog/LTsv10kanedit/blob/master/docs/LTsv_doc.txt "「LTsv_doc」は「LTsv10kanedit(tsvtool10)」を用いたドキュメントジェネレーターです。")&#40;[LTsv_doc.html](https://ooblog.github.io/LTsv10kanedit/LTsv_doc.html "「LTsv_doc」は「LTsv10kanedit(tsvtool10)」を用いたドキュメントジェネレーターです。")&#41;」を参考。  


## 次期バージョン「TSF1KEV」の叩き台として「kanedit.vim」試作中。

![KEV_512x384](docs/KEV_512x384.png "KEV")  
Vimでは「NEFR&#40;無変換&#41;」「XFER&#40;変換&#41;」キーを使えないので「Space」を用いて鍵盤変更&#40;imap&#41;します。  
ひらがなカタカナの操作は同じ鍵盤を連続選択する事でシフト入力だったカタカナを直接入力に交換。再度選択でひらがな帰ってきます。  
挿入モードとノーマルモードの往復も「Space」二回連続で可能なので「Esc」や「Ctrl+&#91;」より操作が簡単。  
「NEFR」「XFER」以外にも48鍵目「￥」鍵盤が入力できない&#40;「ろ」と「￥」が両方とも「&#92;」と入力される&#41;ので仕様変更。  
スクリプトが生成するmapはだいたい以下のイメージ。  

       <Space><Space>   a
    i  <Space><Space>   <Esc>
    i  <S-Space><S-Space> <C-V><Space>
       <Plug>(KEVimap_ぬ) * :call KEVimap('ぬ')<CR>
       <Plug>(KEVimap_ふ) * :call KEVimap('ふ')<CR>
       <Plug>(KEVimap_あ) * :call KEVimap('あ')<CR>
       <Plug>(KEVimap_ヌ) * :call KEVimap('ヌ')<CR>
       <Plug>(KEVimap_フ) * :call KEVimap('フ')<CR>
       <Plug>(KEVimap_ア) * :call KEVimap('ア')<CR>
    i  <Space>1      <C-O><Plug>(KEVimap_ぬ)
    i  <Space>2      <C-O><Plug>(KEVimap_ふ)
    i  <Space>3      <C-O><Plug>(KEVimap_あ)
    i  <S-Space>!    <C-O><Plug>(KEVimap_ヌ)
    i  <S-Space>"    <C-O><Plug>(KEVimap_フ)
    i  <S-Space>#    <C-O><Plug>(KEVimap_ア)
    i  1           * <C-V>U0000306c
    i  2           * <C-V>U00003075
    i  3           * <C-V>U00003042
    i  !           * <C-V>U000030cc
    i  "           * <C-V>U000030d5
    i  #           * <C-V>U000030a2

Vimの件とは別に「[TSF1KEV](https://github.com/ooblog/TSF1KEV "ooblog/TSF1KEV: プログラミング言語「TSF_Tab-Separated-Forth」開発予定。")」という新データフォーマットというか新言語開発の予定があります。  
既存の「L&#58;Tsv」と互換性がないので注意。移行ツールは準備する予定。  

「KEV」の詳細は「[docs/KEV.txt](https://github.com/ooblog/LTsv10kanedit/blob/master/docs/KEV.txt "「KEV」はVimスクリプトでできてる漢字直接入力です。")&#40;[KEV.html](https://ooblog.github.io/LTsv10kanedit/KEV.html "「KEV」はVimスクリプトでできてる漢字直接入力です。")&#41;」を参考。  


## 動作環境。

「Tahrpup6.0.5,Python2.7.6,vim.gtk7.4.52」および「Wine1.7.18,Python3.4.4,gvim8.0.134」で開発しています。  


## ライセンス・著作権など。

Copyright (c) 2016 ooblog  
License: MIT  
[https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE](LICENSE "https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE")  

