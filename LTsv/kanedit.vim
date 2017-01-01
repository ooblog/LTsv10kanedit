set encoding=utf-8
scriptencoding utf-8
let s:kankbd_scriptdir = expand('<sfile>:p:h')

"「kanedit」の初期化(imap等含む)。「kanmap.tsv」と「kanchar.tsv」は「kanedit.vim」と同じフォルダに。
function! s:KanEditSetup()
    let s:kankbd_kanmapfilepath = s:kankbd_scriptdir . "/kanmap.tsv"
    let s:kankbd_kanmapNX = {}
    :if filereadable(s:kankbd_kanmapfilepath)
        :for s:kanlinetsv in readfile(s:kankbd_kanmapfilepath)
            let s:kanlinelist = split(s:kanlinetsv,"\t")
            let s:kankbd_kanmapNX[s:kanlinelist[0]] = s:kanlinelist[1:47] + s:kanlinelist[-48:-2]
        :endfor
    :endif
    let s:kankbd_kancharfilepath = s:kankbd_scriptdir . "/kanchar.tsv"
    let s:kankbd_menuid = 10000
    let s:kankbd_dictype = ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","漫","筆","幅"]
    let s:kankbd_irohaype = ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ",'゛','゜',"ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
    let s:kankbd_irohaype += ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
    let s:kankbd_irohaypeN = ["1(ぬ)","2(ふ)","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
    let s:kankbd_irohaypeN += ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
    let s:kankbd_irohaypeX = ["1(ヌ)","2(フ)","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ","｜"]
    let s:kankbd_irohaypeX += ["Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω","●","▲","■"]
    let s:kankbd_inputkeys = ['1','2','3','4','5','6','7','8','9','0','-','^', 'q','w','e','r','t','y','u','i','o','p','@','[', 'a','s','d','f','g','h','j','k','l',';',':',']', 'z','x','c','v','b','n','m',',','.','/','\']
    let s:kankbd_inputkeys += ['!','"','#','$','%','&',"'",'(',')','~','=','|', 'Q','W','E','R','T','Y','U','I','O','P','`','{', 'A','S','D','F','G','H','J','K','L','+','*','}', 'Z','X','C','V','B','N','M','<','>','?','_',"\t",' ']
    let s:kankbd_inputESCs = {"\t":"<Tab>",' ':"<Space>",'<':"<lt>",'\':"<Bslash>",'|':"<Bar>"}
    let s:kankbd_inputkanaN = ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ", "た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ", "ち","と","し","は","き","く","ま","の","り","れ","け","む", "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ"]
    let s:kankbd_inputkanaX = ["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ", "タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ", "チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム", "ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ"]
    let s:kankbd_inputkanas = s:kankbd_inputkanaN + s:kankbd_inputkanaX + ["￥","　"]
    let s:kankbd_inputchoice =  ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ", "た","て","い","す","か","ん","な","に","ら","せ",'゛','゜', "ち","と","し","は","き","く","ま","の","り","れ","け","む", "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ"]
    let s:kankbd_inputchoice +=  ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非", "英","顔","ε","ρ","τ","υ","θ","ι","ο","π","゛","゜", "α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ", "ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","　"]
    let s:kankbd_kanamap = {}
    let s:kankbd_choicemap = {}
    let s:kankbd_ESCmap = {}
    :for s:inputkey in range(len(s:kankbd_inputkeys))
        let s:kankbd_kanamap[s:kankbd_inputkeys[s:inputkey]] = s:kankbd_inputkanas[s:inputkey]
        let s:kankbd_choicemap[s:kankbd_inputkanas[s:inputkey]] = s:kankbd_inputchoice[s:inputkey]
        let s:kankbd_ESCmap[s:kankbd_inputkeys[s:inputkey]] = get(s:kankbd_inputESCs,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputkeys[s:inputkey])
    :endfor
    :if !exists("s:kankbd_menuname")
        let s:kankbd_kbdkana = "ぬ" 
        let s:kankbd_kbdkanaNX = 1
        let s:kankbd_kbddic = "英" 
        let s:kankbd_choiceAF = ""
        let s:kankbd_choiceBF = s:kankbd_choiceAF
        let s:kankbd_inputimap = s:kankbd_inputkanaN + s:kankbd_inputkanaX
        :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
            execute "imenu  <silent> " . (s:kankbd_menuid+1) . "." . (s:inputkey+1) . " 鍵盤." . s:kankbd_inputchoice[s:inputkey] . " <C-o><Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ")"
            execute "nmenu  <silent> " . (s:kankbd_menuid+1) . "." . (s:inputkey+1) . " 鍵盤." . s:kankbd_inputchoice[s:inputkey] . " <Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ")i"
        :endfor
    :else
        let s:kankbd_kbdkanaNX = !s:kankbd_kbdkanaNX
    :endif
    map <silent> <Space><Space> i
    imap <silent> <Space><Space> <Esc>
    imap <silent> <S-Space><S-Space> <C-V><Space>
    imap <silent> <S-Space><Space> <C-V>　
    map <silent> <Space><Enter> <Plug>(kanedit_ト)i
    imap <silent> <Space><Enter> <C-o><Plug>(kanedit_ト)
    :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
        let s:kankbd_inputhyphen = get(s:kankbd_ESCmap,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputkanas[s:inputkey])
        execute "noremap <Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ") :call KanEdit('" . s:kankbd_inputkanas[s:inputkey] . "')<Enter>"
        execute "imap <silent> <Space>" . s:kankbd_inputhyphen . " <C-o><Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ")"
        execute "imap <silent> <S-Space>" . s:kankbd_inputhyphen . " <C-o><Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ")"
        execute "map <silent> <Space>" . s:kankbd_inputhyphen . " <Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ")i"
        execute "map <silent> <S-Space>" . s:kankbd_inputhyphen . " <Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ")i"
    :endfor
    let s:kankbd_inputsigma = {"":"<Left>","":"<Down>","":"<Up>","":"<Right>","":"<BS>","":"<Home>","":"<End>","":"<PageUp>","":"<PageDown>","":"<Enter>"}
    :for [s:sigmakey,s:sigmavalue] in items(s:kankbd_inputsigma)
        execute "imap <silent> " . s:sigmakey . " " . s:sigmavalue
    :endfor
    call KanEdit("ぬ")
endfunction

"「[Space][ぬ〜ろTab]」のコマンド入力でこの関数が呼ばれ鍵盤変更。
"kankbd_inputkeys→kankbd_inputkanas(kankbd_kanamap)→kankbd_inputchoice(kankbd_choicemap)とカナ名挟むことで入力キーと鍵盤変更コマンドとを抽象化(疎結合化)。
function! KanEdit(kankbd_kbdchar)
    :if exists("s:kankbd_menuname")
        execute "iunmenu " s:kankbd_menuname
    :endif
    let s:kankbd_choiceAF = s:kankbd_choicemap[a:kankbd_kbdchar]
    :if s:kankbd_choiceBF == s:kankbd_choiceAF
        let s:kankbd_kbdkanaNX = !s:kankbd_kbdkanaNX
    :endif
    :if count(s:kankbd_dictype,s:kankbd_choiceAF)
        let s:kankbd_kbddic = s:kankbd_choiceAF
    :else
        let s:kankbd_kbdkana = s:kankbd_choiceAF
    :endif
    let s:kankbd_inputimap = s:kankbd_kanmapNX[s:kankbd_kbdkana]
    :if s:kankbd_kbdkanaNX
        let s:kankbd_menuname = "[" . s:kankbd_irohaypeN[index(s:kankbd_irohaype,s:kankbd_kbdkana)]
    :else
        let s:kankbd_menuname = "[" . s:kankbd_irohaypeX[index(s:kankbd_irohaype,s:kankbd_kbdkana)]
        let s:kankbd_inputimap = s:kankbd_inputimap[47:-1] + s:kankbd_inputimap[0:48] 
    :endif
    :if count(s:kankbd_dictype,s:kankbd_choiceAF)
        let s:kankbd_menuname = s:kankbd_menuname . ":" . s:kankbd_kbddic
        :for s:mapkey in range(len(s:kankbd_inputimap))
            let s:kankbd_inputimap[s:mapkey] = s:kankbd_inputimap[s:mapkey]
        :endfor
    :endif
    let s:kankbd_menuname = s:kankbd_menuname . "]"
    echon s:kankbd_menuname 
    :for s:inputkey in range(len(s:kankbd_inputkeys)-2)
        let s:kankbd_menuhyphen = get(s:kankbd_ESCmap,s:kankbd_inputimap[s:inputkey],s:kankbd_inputimap[s:inputkey])
        let s:kankbd_inputhyphen = get(s:kankbd_ESCmap,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputimap[s:inputkey])
        execute "imap <silent> " . s:kankbd_inputhyphen . " " . s:kankbd_menuhyphen
        execute "imenu " . s:kankbd_menuid . "." . (s:inputkey+1) . " " . s:kankbd_menuname. ".\\" . (s:kankbd_menuhyphen == '-' ? "[-]" : s:kankbd_menuhyphen) . " " . s:kankbd_menuhyphen
    :endfor
    let s:kankbd_choiceBF = s:kankbd_choiceAF
endfunction

"「:call KanExit()」でメニューとimapをクリア。
function! KanExit()
    :if exists("s:kankbd_menuname")
        unmap <silent> <Space><Space>
        iunmap <silent> <Space><Space>
        iunmap <silent> <S-Space><S-Space>
        iunmap <silent> <S-Space><Space>
        unmap <silent> <Space><Enter>
        iunmap <silent> <Space><Enter>
        :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
            let s:kankbd_inputhyphen = get(s:kankbd_ESCmap,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputkanas[s:inputkey])
            execute "noremap <Plug>(kanedit_" . s:kankbd_inputkanas[s:inputkey] . ") :call KanEdit('" . s:kankbd_inputkanas[s:inputkey] . "')<Enter>"
            execute "iunmap <silent> <Space>" . s:kankbd_inputhyphen
            execute "iunmap <silent> <S-Space>" . s:kankbd_inputhyphen
            execute "unmap <silent> <Space>" . s:kankbd_inputhyphen
            execute "unmap <silent> <S-Space>" . s:kankbd_inputhyphen
        :endfor
        :for [s:sigmakey,s:sigmavalue] in items(s:kankbd_inputsigma)
            execute "iunmap <silent> " . s:sigmakey
        :endfor
        execute "iunmenu <silent> " s:kankbd_menuname
        execute "iunmenu <silent> 鍵盤"
        execute "nunmenu <silent> 鍵盤"
    :endif
    unlet! s:kankbd_menuname
endfunction

call s:KanEditSetup()
finish

"# Copyright (c) 2016 ooblog
"# License: MIT
"# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE


