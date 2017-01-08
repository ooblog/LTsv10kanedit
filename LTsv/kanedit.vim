set encoding=utf-8
scriptencoding utf-8
let s:kev_scriptdir = expand('<sfile>:p:h')

"「KanEditVim」の初期設定(imap等含む)。漢字配列「kanmap.tsv」と単漢字辞書「kanchar.tsv」は「kanedit.vim」と同じフォルダに。
function! KEVsetup()
    let s:kankbd_menuid = 10000
    let s:kankbd_HJKL = 'σ'
    let s:kankbd_dictype = ["英","名","音","訓","送","異","俗","簡","繁","越","地","顔","鍵","代","逆","非","熙","照","難","活","漫","筆","幅"]
    let s:kankbd_irohatype = ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ",'゛','゜',"ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ"]
    let s:kankbd_irohatype += ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
    let s:kankbd_irohatypeN = ["1(ぬ)","2(ふ)","3(あ)","4(う)","5(え)","6(お)","7(や)","8(ゆ)","9(よ)","0(わ)","-(ほ)","^(へ)","q(た)","s(て)","e(い)","r(す)","t(か)","y(ん)","u(な)","i(に)","o(ら)","p(せ)","@(＠)","[(ぷ)","a(ち)","s(と)","d(し)","f(は)","g(き)","h(く)","j(ま)","k(の)","l(り)",";(れ)",":(け)","](む)","z(つ)","x(さ)","c(そ)","v(ひ)","b(こ)","n(み)","m(も)",",(ね)","\\.(る)","/(め)","\\\\(ろ)"]
    let s:kankbd_irohatypeN += ["A(α)","B(β)","G(γ)","D(δ)","E(ε)","Z(ζ)","H(η)","U(θ)","I(ι)","K(κ)","L(λ)","M(μ)","N(ν)","J(ξ)","O(ο)","P(π)","R(ρ)","S(σ)","T(τ)","Y(υ)","F(φ)","X(χ)","C(ψ)","V(ω)",">(○)","?(△)","_(□)"]
    let s:kankbd_irohatypeX = ["1(ヌ)","2(フ)","3(ア)","4(ウ)","5(エ)","6(オ)","7(ヤ)","8(ユ)","9(ヨ)","0(ワ)","-(ホ)","^(ヘ)","q(タ)","w(テ)","e(イ)","r(ス)","t(カ)","y(ン)","u(ナ)","i(ニ)","o(ラ)","p(セ)","@(｀)","[(プ)","a(チ)","s(ト)","d(シ)","f(ハ)","g(キ)","h(ク)","j(マ)","k(ノ)","l(リ)",";(レ)",":(ケ)","](ム)","z(ツ)","x(サ)","c(ソ)","v(ヒ)","b(コ)","n(ミ)","m(モ)",".(ネ)","\\.(ル)","/(メ)","\\\\(ロ)"]
    let s:kankbd_irohatypeX += ["A(Α)","B(Β)","G(Γ)","D(Δ)","E(Ε)","Z(Ζ)","H(Η)","U(Θ)","I(Ι)","K(Κ)","L(Λ)","M(Μ)","N(Ν)","J(Ξ)","O(Ο)","P(Π)","R(Ρ)","S(Σ)","T(Τ)","Y(Υ)","F(Φ)","X(Χ)","C(Ψ)","V(Ω)",">(●)","?(▲)","_(■)"]
    let s:kankbd_inputkeys = ['1','2','3','4','5','6','7','8','9','0','-','^', 'q','w','e','r','t','y','u','i','o','p','@','[', 'a','s','d','f','g','h','j','k','l',';',':',']', 'z','x','c','v','b','n','m',',','.','/','\']
    let s:kankbd_inputkeys += ['!','"','#','$','%','&',"'",'(',')','~','=','|', 'Q','W','E','R','T','Y','U','I','O','P','`','{', 'A','S','D','F','G','H','J','K','L','+','*','}', 'Z','X','C','V','B','N','M','<','>','?','_',' ']
    let s:kankbd_inputESCs = {"\t":"<Tab>",' ':"<Space>",'<':"<lt>",'\':"<Bslash>",'|':"<Bar>"}
    let s:kankbd_menuESCs = "\t\\:|< >.-"
    let s:kankbd_inputkanaN = ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ", "た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ", "ち","と","し","は","き","く","ま","の","り","れ","け","む", "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ"]
    let s:kankbd_inputkanaX = ["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ", "タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ", "チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム", "ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ"]
    let s:kankbd_inputkanas = s:kankbd_inputkanaN + s:kankbd_inputkanaX + ["￥","　"]
    let s:kankbd_inputchoice =  ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ", "た","て","い","す","か","ん","な","に","ら","せ",'゛','゜', "ち","と","し","は","き","く","ま","の","り","れ","け","む", "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ"]
    let s:kankbd_inputchoice +=  ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非", "英","顔","ε","ρ","τ","υ","θ","ι","ο","π","゛","゜", "α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ", "ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","　"]
    let s:kankbd_kanamap = {}
    let s:kankbd_choicemap = {}
    let s:kankbd_ESCmap = {}
    :for s:inputkey in range(len(s:kankbd_inputkeys))
        let s:kankbd_kanamap[s:kankbd_inputkeys[s:inputkey]] = s:kankbd_inputkanas[s:inputkey]
        let s:kankbd_choicemap[s:kankbd_inputkanas[s:inputkey]] = s:kankbd_inputchoice[s:inputkey]
        let s:kankbd_ESCmap[s:kankbd_inputkeys[s:inputkey]] = get(s:kankbd_inputESCs,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputkeys[s:inputkey])
    :endfor
    let s:kankbd_kanmapNX = {}
    :for s:kanlinekey in s:kankbd_irohatype
        :if s:kanlinekey == "゛"
            let s:kankbd_kanmapNX[s:kanlinekey] = s:kankbd_inputkeys[:-1]
        :elseif s:kanlinekey == "λ"
            let s:kankbd_kanmapNX[s:kanlinekey] = s:kankbd_inputkeys[:-1]
            :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
                let s:kankbd_kanmapNX[s:kanlinekey][s:inputkey] = nr2char(char2nr(s:kankbd_kanmapNX[s:kanlinekey][s:inputkey])+0xfee0)
            :endfor
        :else
            let s:kankbd_kanmapNX[s:kanlinekey] = s:kankbd_inputkanas
        :endif
    :endfor
    :let s:kankbd_kanmapfilepath = s:kev_scriptdir . "/kanmap.tsv"
    :if filereadable(s:kankbd_kanmapfilepath)
        :for s:kanlinetsv in readfile(s:kankbd_kanmapfilepath)
            let s:kanlinelist = split(s:kanlinetsv,"\t")
            :if len(s:kanlinelist) >= 2
                let s:kankbd_kanmapNX[s:kanlinelist[0]] = s:kanlinelist[1:]
                :for s:inputkey in range(max([0,len(s:kankbd_inputkeys)-len(s:kanlinelist)]))
                    let s:kankbd_kanmapNX[s:kanlinelist[0]] = s:kankbd_kanmapNX[s:kanlinelist[0]] + [" "]
                :endfor
            :endif
        :endfor
    :endif
    let s:kankbd_kancharDIC = {}
    let s:kankbd_kancharfilepath = s:kev_scriptdir . "/kanchar.tsv"
    :if filereadable(s:kankbd_kancharfilepath)
        :for s:kanlinetsv in readfile(s:kankbd_kancharfilepath)
            let s:kanlinelist = split(s:kanlinetsv,"\t")
            :if len(s:kanlinelist) > 0 && s:kanlinelist[0] != ''
                let s:kankbd_kancharDIC[s:kanlinelist[0]] = s:kanlinetsv
            :endif
        :endfor
    :endif
    :if !exists("s:kankbd_menuname")
        let s:kankbd_kbdkanaNX = 1
        let s:kankbd_kbdkana = "ぬ"
        let s:kankbd_kbddic = "英" 
        let s:kankbd_choiceAF = "" | let s:kankbd_choiceBF = s:kankbd_choiceAF
        let s:kankbd_findAF = 0 | let s:kankbd_findBF = s:kankbd_findAF
        let s:kankbd_inputimap = s:kankbd_inputkanaN + s:kankbd_inputkanaX
        :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
            let s:kankbd_menuhyphen = "[" . escape(s:kankbd_inputkeys[s:inputkey],s:kankbd_menuESCs) . "(" . s:kankbd_inputchoice[s:inputkey] . ")]"
            execute "imenu  <silent> " . (s:kankbd_menuid+1) . "." . (s:inputkey+1) . " 鍵盤." . s:kankbd_menuhyphen . " <C-o><Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")"
            execute "nmenu  <silent> " . (s:kankbd_menuid+1) . "." . (s:inputkey+1) . " 鍵盤." . s:kankbd_menuhyphen . " <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")i"
        :endfor
    :else
        let s:kankbd_kbdkanaNX = !s:kankbd_kbdkanaNX
    :endif
    map <silent> <Space><Space> a
    vmap <silent> <Space><Space> <Esc>
    imap <silent> <Space><Space> <Esc>
    imap <silent> <S-Space><S-Space> <C-V><Space>
    imap <silent> <S-Space><Space> <C-V>　
    imap <silent> <Space><S-Space> <C-V>　
    :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
        let s:kankbd_inputhyphen = s:kankbd_ESCmap[s:kankbd_inputkeys[s:inputkey]]
        execute "noremap <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ") :call KEVimap('" . s:kankbd_inputkanas[s:inputkey] . "')<Enter>"
        execute "imap <silent> <Space>" . s:kankbd_inputhyphen . " <C-o><Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")"
        execute "imap <silent> <S-Space>" . s:kankbd_inputhyphen . " <C-o><Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")"
        execute "map <silent> <Space>" . s:kankbd_inputhyphen . " <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")i"
        execute "map <silent> <S-Space>" . s:kankbd_inputhyphen . " <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")i"
    :endfor
    execute "noremap <Plug>(KEVfiler) :call KEVfiler()<Enter>"
    execute "noremap <Plug>(KEVimap_HJKL) :call KEVimap('HJKL')<Enter>"
    map <silent> <Space><Enter> <Plug>(KEVimap_HJKL)i
    imap <silent> <Space><Enter> <C-o><Plug>(KEVimap_HJKL)
    let s:kankbd_inputsigma = {'':"<esc><C-Q>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Tab>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<C-o><Plug>(KEVfiler)",'':"<Nop>",
\                              '':"<esc>ggVG",'':"<C-o>:w<Enter>",'':"<Nop>",'':"<C-o>/あ<Enter>",'':"<Nop>",'':"<Left>",'':"<Down>",'':"<Up>",'':"<Right>",'':"<BS>",'':"<Right><BS>",'':"<Enter>",
\                              '':"<C-o>u",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Home>",'':"<End>",'':"<PageUp>",'':"<PageDown>"}
    :for [s:sigmakey,s:sigmavalue] in items(s:kankbd_inputsigma)
        execute "imap  " . s:sigmakey . " " . s:sigmavalue
    :endfor
    execute "noremap <Plug>(KEVimap_find) :call KEVimap('find')<Enter>"
    execute "noremap <Plug>(KEVimap_Find) :call KEVimap('Find')<Enter>"
    map <silent> <Space><Tab> <Plug>(KEVimap_find)i
    map <silent> <Space><S-Tab> <Plug>(KEVimap_Find)i
    map <silent> <S-Space><Tab> <Plug>(KEVimap_find)i
    map <silent> <S-Space><S-Tab> <Plug>(KEVimap_Find)i
    imap <silent> <Space><Tab> <C-o><Plug>(KEVimap_find)
    imap <silent> <Space><S-Tab> <C-o><Plug>(KEVimap_Find)
    imap <silent> <S-Space><Tab> <C-o><Plug>(KEVimap_find)
    imap <silent> <S-Space><S-Tab> <C-o><Plug>(KEVimap_Find)
    call KEVimap("ぬ")
endfunction

"「[Space][ぬ〜ろ]」等のコマンド入力で鍵盤(imap等)変更。「[Space][Tab]」で一文字検索モード。
function! KEVimap(kankbd_kbdchar)
    :if exists("s:kankbd_menuname")
        execute "iunmenu " s:kankbd_menuname
    :endif
    echo 
    :if a:kankbd_kbdchar == 'HJKL'
        let s:kankbd_choiceAF = s:kankbd_HJKL
        :if s:kankbd_choiceBF == s:kankbd_choiceAF
            let s:kankbd_kbdkanaNX = !s:kankbd_kbdkanaNX
        :else
            let s:kankbd_kbdkanaNX = 1
        :endif
        let s:kankbd_kbdkana = s:kankbd_choiceAF
        let s:kankbd_findAF = 0
    :elseif a:kankbd_kbdchar == 'find'
        let s:kankbd_findAF = 1
        let s:kankbd_findAF = (s:kankbd_findBF == s:kankbd_findAF) ? 0 : 1
        let s:kankbd_findBF = s:kankbd_findAF
    :elseif a:kankbd_kbdchar == 'Find'
        let s:kankbd_findAF = -1
        let s:kankbd_findAF = (s:kankbd_findBF == s:kankbd_findAF) ? 0 : -1
        let s:kankbd_findBF = s:kankbd_findAF
    :else
        let s:kankbd_choiceAF = get(s:kankbd_choicemap,a:kankbd_kbdchar,'ぬ')
        :if s:kankbd_choiceBF == s:kankbd_choiceAF
            let s:kankbd_kbdkanaNX = !s:kankbd_kbdkanaNX
        :endif
        :if count(s:kankbd_dictype,s:kankbd_choiceAF)
            let s:kankbd_kbddic = s:kankbd_choiceAF
        :else
            let s:kankbd_kbdkana = s:kankbd_choiceAF
        :endif
    :endif
    let s:kankbd_inputimap = s:kankbd_kanmapNX[s:kankbd_kbdkana]
    :if s:kankbd_kbdkanaNX
        let s:kankbd_menuname = "[" . s:kankbd_irohatypeN[index(s:kankbd_irohatype,s:kankbd_kbdkana)]
    :else
        let s:kankbd_menuname = "[" . s:kankbd_irohatypeX[index(s:kankbd_irohatype,s:kankbd_kbdkana)]
        let s:kankbd_inputimap = s:kankbd_inputimap[47:-1] + s:kankbd_inputimap[0:48] 
    :endif
    :if count(s:kankbd_dictype,s:kankbd_choiceAF)
        let s:kankbd_menuname = s:kankbd_menuname . ":" . s:kankbd_kbddic
        :for s:mapkey in range(len(s:kankbd_inputimap))
            let s:kanlinetsv = get(s:kankbd_kancharDIC,s:kankbd_inputimap[s:mapkey],'') . "\t"
            let s:kanposL = stridx(s:kanlinetsv,"\t" . s:kankbd_kbddic . ":")
            let s:kankbd_inputimap[s:mapkey] = ''
            :if 0 < s:kanposL
                let s:kanposL = stridx(s:kanlinetsv,":",s:kanposL)+1
                let s:kanposR = stridx(s:kanlinetsv,"\t",s:kanposL)
                let s:kankbd_inputimap[s:mapkey] = strpart(s:kanlinetsv,s:kanposL,s:kanposR-s:kanposL)
            :endif
            :if len(s:kankbd_inputimap[s:mapkey]) == 0
                let s:kankbd_inputimap[s:mapkey] = ' '
            :endif
        :endfor
    :endif
    let s:kankbd_menuname = s:kankbd_menuname . "]"
    :if s:kankbd_findAF != 0
        let s:kankbd_menuname = s:kankbd_menuname . (s:kankbd_findAF > 0 ? '+' : '-')
    :endif
    :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
        :if has_key(s:kankbd_inputsigma,s:kankbd_inputimap[s:inputkey])
            let s:kankbd_unicode = s:kankbd_inputimap[s:inputkey]
        :else
            let s:kankbd_unicodeL = [] | let s:kankbd_unicodeL = split(s:kankbd_inputimap[s:inputkey],'\zs')
            :for s:mapkey in range(len(s:kankbd_unicodeL))
                let s:kankbd_unicodeL[s:mapkey] = "<C-V>U" . printf("%08x",char2nr(s:kankbd_unicodeL[s:mapkey]))
            :endfor
            let s:kankbd_unicode = join(s:kankbd_unicodeL,'') 
        :endif
        let s:kankbd_menuhyphen = escape(s:kankbd_inputimap[s:inputkey],s:kankbd_menuESCs)
        let s:kankbd_inputhyphen = get(s:kankbd_ESCmap,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputimap[s:inputkey])
        :if s:kankbd_findAF == 0
            execute "imap <silent> " . s:kankbd_inputhyphen . " " . s:kankbd_unicode
            execute "imenu <silent> " . s:kankbd_menuid . "." . (s:inputkey+1) . " " . s:kankbd_menuname. "." . s:kankbd_menuhyphen . " " . s:kankbd_unicode
        :else
            if s:kankbd_findAF > 0
                execute "imap <silent> " . s:kankbd_inputhyphen . " <C-o>/" . s:kankbd_unicode . "<Enter>"
                execute "imenu <silent> " . s:kankbd_menuid . "." . (s:inputkey+1) . " " . s:kankbd_menuname. "." . s:kankbd_menuhyphen . " <C-o>/" . s:kankbd_unicode . "<Enter>"
            :else
                execute "imap <silent> " . s:kankbd_inputhyphen . " <C-o>?" . s:kankbd_unicode . "<Enter>"
                execute "imenu <silent> " . s:kankbd_menuid . "." . (s:inputkey+1) . " " . s:kankbd_menuname. "." . s:kankbd_menuhyphen . " <C-o>?" . s:kankbd_unicode . "<Enter>"
            :endif
        :endif
    :endfor
    let s:kankbd_choiceBF = s:kankbd_choiceAF
endfunction
"<C-o>/あ<Enter>

"「σ」鍵盤のOで履歴などからファイルを開く。
function! KEVfiler()
    cd $HOME
    let s:dirline = expand('%:p:h')
    execute "cd " . s:dirline
    let s:filelines = ["",s:dirline] + v:oldfiles
    let s:filelabels = ["ファイル履歴(01でフォルダ選択)※履歴はウィンドウの高さに合わせます。"]
    :for s:labelno in range(1,len(s:filelines)-2)
         let s:filelabels = s:filelabels + [ printf("%02d",s:labelno) . ":" . s:filelines[s:labelno] ]
    :endfor
    let s:filechoice = inputlist(s:filelabels[:max([1,min([&lines-2,len(s:filelabels)])])])
    :while 0 < s:filechoice && s:filechoice < len(s:filelines)
        echo "\n"
        :if isdirectory(s:filelines[s:filechoice])
            execute "cd " . s:filelines[s:filechoice]
            let s:dirline = getcwd()
        :elseif filereadable(s:filelines[s:filechoice])
            execute "enew"
            execute "e " . s:filelines[s:filechoice]
            :break
        :else
            echo "リーダブルではないファイルです「" . s:filelines[s:filechoice] . "」"
        :endif
        let s:filelines = ["",".."] + split(expand("./*"),"\n")
        let s:filelabels = ["「" . s:dirline . "」(01で親フォルダ選択)※ファイルクリックはズレるので注意。"]
        :for s:labelno in range(1,len(s:filelines)-1)
             let s:filelabels = s:filelabels + [ printf("%02d",s:labelno) . ":" . s:filelines[s:labelno] ]
        :endfor
        let s:filechoice = inputlist(s:filelabels)
    :endwhile
endfunction

"メニューとimapを消去。
function! KEVexit()
    :if exists("s:kankbd_menuname")
        unmap <silent> <Space><Space>
        iunmap <silent> <Space><Space>
        iunmap <silent> <S-Space><S-Space>
        iunmap <silent> <S-Space><Space>
        iunmap <silent> <Space><S-Space>
        :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
            let s:kankbd_inputhyphen = get(s:kankbd_ESCmap,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputkanas[s:inputkey])
            execute "noremap <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ") :call KEVimap('" . s:kankbd_inputkanas[s:inputkey] . "')<Enter>"
            execute "iunmap <silent> <Space>" . s:kankbd_inputhyphen
            execute "iunmap <silent> <S-Space>" . s:kankbd_inputhyphen
            execute "unmap <silent> <Space>" . s:kankbd_inputhyphen
            execute "unmap <silent> <S-Space>" . s:kankbd_inputhyphen
        :endfor
        unmap <silent> <Space><Enter>
        iunmap <silent> <Space><Enter>
        let s:kankbd_kbdkanaNX = 1
        :for [s:sigmakey,s:sigmavalue] in items(s:kankbd_inputsigma)
            execute "iunmap <silent> " . s:sigmakey
        :endfor
        execute "iunmenu <silent> " s:kankbd_menuname
        execute "iunmenu <silent> 鍵盤"
        execute "nunmenu <silent> 鍵盤"
    :endif
    unlet! s:kankbd_menuname
endfunction

call KEVsetup()
finish

"# Copyright (c) 2016 ooblog
"# License: MIT
"# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
