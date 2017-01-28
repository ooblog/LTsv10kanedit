set encoding=utf-8
scriptencoding utf-8
let s:kev_scriptdir = expand('<sfile>:p:h')

"「KanEditVim」の初期化初期設定(imap等含む)。
function! KEVsetup()
    let s:kankbd_menuid = 10000
    let s:kankbd_HJKL = 'σ'
    let s:kankbd_dictype = ["英","名","音","訓","送","異","俗","簡","繁","越","地","顔","鍵","代","逆","非","照","熙","難","活","漫","筆","幅"]
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
    let s:kankbd_inputkanas = s:kankbd_inputkanaN + s:kankbd_inputkanaX + ["　"]
    let s:kankbd_kanamap = {}
    let s:kankbd_ESCmap = {}
    :for s:inputkey in range(len(s:kankbd_inputkeys))
        let s:kankbd_kanamap[s:kankbd_inputkeys[s:inputkey]] = s:kankbd_inputkanas[s:inputkey]
        let s:kankbd_ESCmap[s:kankbd_inputkeys[s:inputkey]] = get(s:kankbd_inputESCs,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputkeys[s:inputkey])
    :endfor
    let s:kankbd_kanmapNX = {"　":["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ", "た","て","い","す","か","ん","な","に","ら","せ",'゛','゜', "ち","と","し","は","き","く","ま","の","り","れ","け","む", "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ",
\                                   "名","音","訓","送","異","俗","簡","繁","越","地","逆","非", "英","顔","ε","ρ","τ","υ","θ","ι","ο","π","゛","゜", "α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ", "ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□"]}
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
    let s:kankbd_kanmapfilepath = s:KEVfilereadable(s:kev_scriptdir . "/kanmap.tsf",s:kev_scriptdir . "/kanmap.tsv")
    :if s:kankbd_kanmapfilepath != ""
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
    let s:kankbd_kancharfilepath = s:KEVfilereadable(s:kev_scriptdir . "/kanchar.tsf",s:kev_scriptdir . "/kanchar.tsv")
    :if s:kankbd_kancharfilepath != ""
        :for s:kanlinetsv in readfile(s:kankbd_kancharfilepath)
            let s:kanlinelist = split(s:kanlinetsv,"\t")
            :if len(s:kanlinelist) > 0 && s:kanlinelist[0] != ''
                let s:kankbd_kancharDIC[s:kanlinelist[0]] = s:kanlinetsv
            :endif
        :endfor
    :endif
    let s:kankbd_kbdkana = "ぬ"
    let s:kankbd_kbddic = "" 
    execute "noremap <Plug>(KEVhelp) :call KEVhelp()<Enter>"
    execute "noremap <Plug>(KEVexit) :call KEVexit()<Enter>"
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".01 漢直.ヘルプ(KEV\\.txt) <Plug>(KEVhelp)"
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".09 漢直.-sep_help- :"
    call KEVfindmenu(' ')
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".19 漢直.-sep_find- :"
    call KEValphamenu("鍵盤")
    call KEVkanamenu("ひらがな")
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".29 漢直.-sep_dakuon- :"
    call KEVdicmenu(' ')
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".39 漢直.-sep_kana- :"
    call KEVdakuonmenu('N')
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".49 漢直.-sep_exitdic- :"
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".50 漢直.履歴からファイルを開く <Plug>(KEVfiler)"
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".59 漢直.-sep_filer- :"
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".99 漢直.漢直中断(「call\\ KEVsetup()」で再開) <Plug>(KEVexit)"
    map <silent> <Space><Space> a
    vmap <silent> <Space><Space> <Esc>
    imap <silent> <Space><Space> <Esc>
    imap <silent> <S-Space><S-Space> <C-V><Space>
    imap <silent> <S-Space><Space> <C-V>　
    imap <silent> <Space><S-Space> <C-V><Tab>
    :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
        let s:kankbd_inputhyphen = s:kankbd_ESCmap[s:kankbd_inputkeys[s:inputkey]]
        execute "noremap <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ") :call KEVimap('" . s:kankbd_inputkanas[s:inputkey] . "')<Enter>"
        execute "imap <silent> <Space>" . s:kankbd_inputhyphen . " <C-o><Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")"
        execute "imap <silent> <S-Space>" . s:kankbd_inputhyphen . " <C-o><Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")"
        execute "map <silent> <Space>" . s:kankbd_inputhyphen . " <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")i"
        execute "map <silent> <S-Space>" . s:kankbd_inputhyphen . " <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")i"
    :endfor
    execute "noremap <Plug>(KEVimap_HJKL) :call KEVimap('HJKL')<Enter>"
    map <silent> <Space><Del> <Plug>(KEVimap_HJKL)i
    imap <silent> <Space><Del> <C-o><Plug>(KEVimap_HJKL)
    execute "noremap <Plug>(KEVfiler) :call KEVfiler()<Enter>"
    let s:kankbd_inputsigma = {'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Tab>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<C-o><Plug>(KEVfiler)",'':"<Nop>",
\                              '':"<esc>ggVG",'':"<C-o>:w<Enter>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Left>",'':"<Down>",'':"<Up>",'':"<Right>",'':"<BS>",'':"<Del>",'':"<Enter>",
\                              '':"<C-o>u",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Nop>",'':"<Home>",'':"<End>",'':"<PageUp>",'':"<PageDown>"}
    :for [s:sigmakey,s:sigmavalue] in items(s:kankbd_inputsigma)
        execute "imap  " . s:sigmakey . " " . s:sigmavalue
    :endfor
    call KEVimap('')
endfunction

"辞書等の存在チェック。漢字配列「<？https/kanmap.tsv>」と単漢字辞書「<？https/kanchar.tsv>」は「<？https/kanedit.vim>」と同じフォルダに。	LTsv版と互換性持たせるため「.tsf」と「.tsv」の両ファイルの有無を調べる。
function! s:KEVfilereadable(TSFfilepath,TSVfilepath)
    let s:kankbd_filepath = ""
    :if filereadable(a:TSFfilepath)
        let s:kankbd_filepath = a:TSFfilepath
    :endif
    :if filereadable(a:TSVfilepath)
        let s:kankbd_filepath = a:TSVfilepath
    :endif
    return s:kankbd_filepath
endfunction

"「[Space],[1(ぬ)〜&#92;(ろ)]」等のコマンド入力で鍵盤(imap等)変更。「[Space],[Enter]」「[Space],[Tab]」で一文字検索モード。
function! KEVimap(kankbd_kbdchar)
    :if a:kankbd_kbdchar == 'HJKL'
        call KEVfindmenu(' ')
        call KEVdakuonmenu(' ')
        call KEValphamenu("鍵盤")
        :if s:kankbd_kbdkana == s:kankbd_HJKL
            call KEVkanamenu('')
        :else
            call KEVkanamenu("ひらがな")
        :endif
        let s:kankbd_kbdkana = s:kankbd_HJKL
        call KEVdicmenu(' ')
    :elseif a:kankbd_kbdchar == 'findF'
        call KEVfindmenu('/')
    :elseif a:kankbd_kbdchar == 'findB'
        call KEVfindmenu('?')
    :elseif a:kankbd_kbdchar == 'NUPU'
        call KEVdakuonmenu('')
    :elseif a:kankbd_kbdchar == 'hirakana'
        call KEVkanamenu('')
    :elseif a:kankbd_kbdchar == 'alpha'
        call KEValphamenu('')
    :else
        let s:kankbd_kbdchar = get(s:kankbd_choicemap,a:kankbd_kbdchar,'ぬ')
        :if count(s:kankbd_dictype,s:kankbd_kbdchar)
            if s:kankbd_kbddic != s:kankbd_kbdchar
                call KEVdicmenu(s:kankbd_kbdchar)
            :else
                call KEVdicmenu(' ')
            :endif
        :else
            :if s:kankbd_kbdkana == s:kankbd_kbdchar
                :if a:kankbd_kbdchar != ''
                    call KEVkanamenu('')
                :else
                    call KEVkanamenu("ひらがな")
                :endif
            :endif
            let s:kankbd_kbdkana = s:kankbd_kbdchar
        :endif
    :endif
    call KEVdicmenu('')
    :if exists("s:kankbd_irohamenuname")
        execute "iunmenu <silent> " s:kankbd_irohamenuname
    :endif
    let s:kankbd_irohamenuname = (s:kankbd_findAF == 0 ? '' : (s:kankbd_findAF > 0 ? '/' : '?'))
    let s:kankbd_irohamenuname = s:kankbd_irohamenuname . "[" . (s:kankbd_kanaAF ? s:kankbd_irohatypeX[index(s:kankbd_irohatype,s:kankbd_kbdkana)] : s:kankbd_irohatypeN[index(s:kankbd_irohatype,s:kankbd_kbdkana)])
    let s:kankbd_inputimap = s:kankbd_kanmapNX[s:kankbd_kbdkana] + []
    :if s:kankbd_kanaAF
        let s:kankbd_inputimap = s:kankbd_inputimap[47:94] + s:kankbd_inputimap[0:46] 
    :endif
    :if count(s:kankbd_dictype,s:kankbd_kbddic) > 0
        let s:kankbd_irohamenuname = s:kankbd_irohamenuname . ":" . s:kankbd_kbddic
        :for s:mapkey in range(len(s:kankbd_inputimap))
            let s:kanlinetsv = get(s:kankbd_kancharDIC,s:kankbd_inputimap[s:mapkey],'') . "\t"
            let s:kanposL = stridx(s:kanlinetsv,"\t" . s:kankbd_kbddic . ":")
            :if 0 < s:kanposL
                let s:kanposL = stridx(s:kanlinetsv,":",s:kanposL)+1
                let s:kanposR = stridx(s:kanlinetsv,"\t",s:kanposL)
                let s:kankbd_inputimap[s:mapkey] = strpart(s:kanlinetsv,s:kanposL,s:kanposR-s:kanposL)
            :elseif s:kankbd_kbddic == "照"
                let s:kankbd_inputimap[s:mapkey] = printf("&#%d;",char2nr(s:kankbd_inputimap[s:mapkey]))
            :else
                let s:kankbd_inputimap[s:mapkey] = ''
            :endif
            :if len(s:kankbd_inputimap[s:mapkey]) == 0
                let s:kankbd_inputimap[s:mapkey] = ' '
            :endif
        :endfor
    :endif
    let s:kankbd_irohamenuname = s:kankbd_irohamenuname . "]"
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
        let s:kankbd_menuhyphen = s:kankbd_inputimap[s:inputkey] != '-' ? escape(s:kankbd_inputimap[s:inputkey],s:kankbd_menuESCs) : "-　"
        let s:kankbd_inputhyphen = get(s:kankbd_ESCmap,s:kankbd_inputkeys[s:inputkey],s:kankbd_inputimap[s:inputkey])
        :if s:kankbd_findAF == 0
            execute "imap <silent> " . s:kankbd_inputhyphen . " " . s:kankbd_unicode
            execute "imenu <silent> " . s:kankbd_menuid . "." . (s:inputkey+1) . " " . s:kankbd_irohamenuname. "." . s:kankbd_menuhyphen . " " . s:kankbd_unicode
        :else
            if s:kankbd_findAF > 0
                execute "imap <silent> " . s:kankbd_inputhyphen . " <C-o>/" . s:kankbd_unicode . "<Enter>"
                execute "imenu <silent> " . s:kankbd_menuid . "." . (s:inputkey+1) . " " . s:kankbd_irohamenuname. "." . s:kankbd_menuhyphen . " <C-o>/" . s:kankbd_unicode . "<Enter>"
            :else
                execute "imap <silent> " . s:kankbd_inputhyphen . " <C-o>?" . s:kankbd_unicode . "<Enter>"
                execute "imenu <silent> " . s:kankbd_menuid . "." . (s:inputkey+1) . " " . s:kankbd_irohamenuname. "." . s:kankbd_menuhyphen . " <C-o>?" . s:kankbd_unicode . "<Enter>"
            :endif
        :endif
    :endfor
endfunction

"ヘルプファイル「KEV.txt」読込。
function! KEVhelp()
    let s:kankbd_kanhelpfilepath = s:KEVfilereadable(s:kev_scriptdir . "/KEV.txt",s:kev_scriptdir . "/../docs/KEV.txt")
    :if filereadable(s:kankbd_kanhelpfilepath)
        execute "enew"
        execute "e " . s:kankbd_kanhelpfilepath . " | :se ro"
    :endif
endfunction

"「一文字検索モード」の設定。漢直検索。
function! KEVfindmenu(kankbd_menuoption)
    :if exists("s:kankbd_findFmenuname")
        execute "aunmenu <silent> 漢直." . s:kankbd_findFmenuname
        execute "aunmenu <silent> 漢直." . s:kankbd_findBmenuname
    :else
        execute "noremap <Plug>(KEVimap_findF) :call KEVimap('findF')<Enter>"
        map <silent> <Space><Enter> <Plug>(KEVimap_findF)i
        imap <silent> <Space><Enter> <C-o><Plug>(KEVimap_findF)
        execute "noremap <Plug>(KEVimap_findB) :call KEVimap('findB')<Enter>"
        map <silent> <Space><Tab> <Plug>(KEVimap_findB)i
        imap <silent> <Space><Tab> <C-o><Plug>(KEVimap_findB)
        let s:kankbd_findAF = 0 | let s:kankbd_findBF = s:kankbd_findAF
    :endif
    :if a:kankbd_menuoption == '/'
        let s:kankbd_findAF = 1
        let s:kankbd_findAF = (s:kankbd_findBF == s:kankbd_findAF) ? 0 : 1
    :elseif a:kankbd_menuoption == '?'
        let s:kankbd_findAF = -1
        let s:kankbd_findAF = (s:kankbd_findBF == s:kankbd_findAF) ? 0 : -1
    :elseif a:kankbd_menuoption == ' '
        let s:kankbd_findAF = 0
    :else
        let s:kankbd_findAF = !s:kankbd_findAF
    :endif
    let s:kankbd_findBF = s:kankbd_findAF
    let s:kankbd_findFmenuname = "一文字検索モード(/前方)" . (s:kankbd_findAF > 0 ? "✓" : "")
    let s:kankbd_findBmenuname = "一文字検索モード(?後方)" . (s:kankbd_findAF < 0 ? "✓" : "")
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".10 漢直." . s:kankbd_findFmenuname . " <Plug>(KEVimap_findF)"
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".11 漢直." . s:kankbd_findBmenuname . " <Plug>(KEVimap_findB)"
endfunction

"「カナ前衛モード」の設定。「ひらがな」と「カタカナ」を並び替える。
function! KEVkanamenu(kankbd_menuoption)
    :if exists("s:kankbd_kanamenuname")
        execute "aunmenu <silent> 漢直." . s:kankbd_kanamenuname
    :else
        execute "noremap <Plug>(KEVimap_hirakana) :call KEVimap('hirakana')<Enter>"
        let s:kankbd_kanaAF = 0
    :endif
    :if a:kankbd_menuoption == "ひらがな"
        let s:kankbd_kanaAF = 0
    :elseif a:kankbd_menuoption == "カタカナ"
        let s:kankbd_kanaAF = !0
    :else
        let s:kankbd_kanaAF = !s:kankbd_kanaAF
    :endif
    let s:kankbd_kanamenuname = "カナ前衛モード([Shift]使わずにカナ)" . (s:kankbd_kanaAF ? "✓" : "")
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".20 漢直." . s:kankbd_kanamenuname . " <Plug>(KEVimap_hirakana)"
endfunction

"「辞書前衛モード」の設定。「鍵盤」と「辞書」を並び替える。
function! KEValphamenu(kankbd_menuoption)
    :if exists("s:kankbd_alphamenuname")
        execute "aunmenu <silent> 漢直." . s:kankbd_alphamenuname
    :else
        execute "noremap <Plug>(KEVimap_alpha) :call KEVimap('alpha')<Enter>"
        map <silent> <Space><BS> <Plug>(KEVimap_alpha)i
        imap <silent> <Space><BS> <C-o><Plug>(KEVimap_alpha)
        let s:kankbd_dicAF = 0
        let s:kankbd_choicemap = {}
    :endif
    :if exists("s:kankbd_alphadicmenuname")
        execute "iunmenu <silent> " s:kankbd_alphadicmenuname
        execute "nunmenu <silent> " . s:kankbd_alphadicmenuname
    :endif
    :if a:kankbd_menuoption == "鍵盤"
        let s:kankbd_dicAF = 0
    :elseif a:kankbd_menuoption == "辞書"
        let s:kankbd_dicAF = !0
    :else
        let s:kankbd_dicAF = !s:kankbd_dicAF
    :endif
    :if s:kankbd_dicAF == 0
        let s:kankbd_alphadicmenuname = "鍵盤"
        let s:kankbd_inputchoice = s:kankbd_kanmapNX['　']
    :else
        let s:kankbd_alphadicmenuname = "辞書"
        let s:kankbd_inputchoice = s:kankbd_kanmapNX['　'][47:94] + s:kankbd_kanmapNX['　'][0:46]
    :endif
    :for s:inputkey in range(len(s:kankbd_inputkeys)-1)
        let s:kankbd_menuhyphen = "[" . escape(s:kankbd_inputkeys[s:inputkey],s:kankbd_menuESCs) . "(" . s:kankbd_inputchoice[s:inputkey] . ")]"
        execute "imenu  <silent> " . (s:kankbd_menuid+1) . "." . (s:inputkey+1) . " " . s:kankbd_alphadicmenuname . "." . s:kankbd_menuhyphen . " <C-o><Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")"
        execute "nmenu  <silent> " . (s:kankbd_menuid+1) . "." . (s:inputkey+1) . " " . s:kankbd_alphadicmenuname . "." . s:kankbd_menuhyphen . " <Plug>(KEVimap_" . s:kankbd_inputkanas[s:inputkey] . ")i"
        let s:kankbd_choicemap[s:kankbd_inputkanas[s:inputkey]] = s:kankbd_inputchoice[s:inputkey]
    :endfor
    let s:kankbd_alphamenuname = "辞書前衛モード([Shift]で鍵盤)" . (s:kankbd_dicAF ? "✓" : "")
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".25 漢直." . s:kankbd_alphamenuname . " <Plug>(KEVimap_alpha)"
endfunction

"辞書の選択および解除。
function! KEVdicmenu(kankbd_menuoption)
    :if exists("s:kankbd_dicmenuname")
        execute "aunmenu <silent> 漢直." . s:kankbd_dicmenuname
    :else
        let s:kankbd_kbddic = ''
    :endif
"    let s:kankbd_kbddic = get(s:kankbd_dictype,a:kankbd_menuoption,'')   # get関数の値が無い場合の「''」が指定できない。
    :if count(s:kankbd_dictype,a:kankbd_menuoption)
        let s:kankbd_kbddic = a:kankbd_menuoption
    :elseif a:kankbd_menuoption == ''
        let s:kankbd_kbddic = s:kankbd_kbddic
    :else
        let s:kankbd_kbddic = ''
    :endif
    let s:kankbd_dicmenuname = "「" . s:kankbd_HJKL . "」鍵盤選択＆検索モード前衛モード解除" . ((s:kankbd_kbdkana == s:kankbd_HJKL && len(s:kankbd_kbddic) == 0 && s:kankbd_findAF == 0 && s:kankbd_kanaAF == 0 && s:kankbd_dicAF == 0)? "✓" : "")
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".30 漢直." . s:kankbd_dicmenuname . " <Plug>(KEVimap_HJKL)"
endfunction

"「[Shift]で濁音モード」の設定。「ヌ」鍵盤と「ぷ」鍵盤を入れ替える。
function! KEVdakuonmenu(kankbd_menuoption)
    :if exists("s:kankbd_dakuonmenuname")
        execute "aunmenu <silent> 漢直." . s:kankbd_dakuonmenuname
    :else
        execute "noremap <Plug>(KEVimap_NUPU) :call KEVimap('NUPU')<Enter>"
        map <silent> <S-Space><S-BS> <Plug>(KEVimap_NUPU)i
        map <silent> <Space><S-BS> <Plug>(KEVimap_NUPU)i
        map <silent> <S-Space><BS> <Plug>(KEVimap_NUPU)i
        imap <silent> <S-Space><S-BS> <C-o><Plug>(KEVimap_NUPU)
        imap <silent> <Space><S-BS> <C-o><Plug>(KEVimap_NUPU)
        imap <silent> <S-Space><BS> <C-o><Plug>(KEVimap_NUPU)
        let s:kankbd_kanmapNX_NU = s:kankbd_kanmapNX['ぬ']
        let s:kankbd_kanmapNX_PU = s:kankbd_kanmapNX['゜']
        let s:kankbd_dakuonAF = 0
    :endif
    :if count(["G","D","Z","J","B","P","V","C","X","Q"],a:kankbd_menuoption)
        let s:kankbd_dakuonAF = !0
    :elseif count(["A","I","U","E","O","K","S","T","N","H","F","M","Y","R","L","W"],a:kankbd_menuoption)
        let s:kankbd_dakuonAF = 0
    :else
        let s:kankbd_dakuonAF = !s:kankbd_dakuonAF
    :endif
    :if s:kankbd_dakuonAF
        let s:kankbd_irohatypeX[0] = "1(ゔ)" | let s:kankbd_irohatypeN[23] = "[(ヌ)" | let s:kankbd_irohatypeX[23] = "[(ヴ)"
        let s:kankbd_kanmapNX['ぬ'] = s:kankbd_kanmapNX_NU[0:46] + s:kankbd_kanmapNX_PU[0:46]
        let s:kankbd_kanmapNX['゜']  = s:kankbd_kanmapNX_NU[47:94] + s:kankbd_kanmapNX_PU[47:94]
    :else
        let s:kankbd_irohatypeX[0] = "1(ヌ)" | let s:kankbd_irohatypeN[23] = "[(ぷ)" | let s:kankbd_irohatypeX[23] = "[(プ)"
        let s:kankbd_kanmapNX['ぬ'] = s:kankbd_kanmapNX_NU
        let s:kankbd_kanmapNX['゜'] = s:kankbd_kanmapNX_PU
    :endif
    let s:kankbd_dakuonmenuname = "濁音モード(ヌ→ゔ)" . (s:kankbd_dakuonAF > 0 ? "✓" : "")
    execute "amenu  <silent> " . (s:kankbd_menuid+2) . ".40 漢直." . s:kankbd_dakuonmenuname . " <Plug>(KEVimap_NUPU)"
endfunction

"「σ」鍵盤で [o(ら)]が押された時に履歴などからファイルを開く簡易ファイラー。
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

"「KanEditVim」の終了。imap等マップ関連の撤去やメニューの撤去処理。
function! KEVexit()
    :if exists("s:kankbd_irohamenuname")
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
        unmap <silent> <Space><BS>
        iunmap <silent> <Space><BS>
        unmap <silent> <S-Space><S-BS>
        unmap <silent> <Space><S-BS>
        unmap <silent> <S-Space><BS>
        iunmap <silent> <S-Space><S-BS>
        iunmap <silent> <Space><S-BS>
        iunmap <silent> <S-Space><BS>
        unmap <silent> <Space><Del>
        iunmap <silent> <Space><Del>
        unmap <silent> <Space><Enter>
        iunmap <silent> <Space><Enter>
        unmap <silent> <Space><Tab>
        iunmap <silent> <Space><Tab>
        :for [s:sigmakey,s:sigmavalue] in items(s:kankbd_inputsigma)
            execute "iunmap <silent> " . s:sigmakey
        :endfor
        execute "iunmenu <silent> " s:kankbd_irohamenuname
        execute "iunmenu <silent> " . s:kankbd_alphamenuname
        execute "nunmenu <silent> " . s:kankbd_alphamenuname
        execute "aunmenu  <silent> " . "漢直"
    :endif
    unlet! s:kankbd_irohamenuname
    unlet! s:kankbd_findFmenuname
    unlet! s:kankbd_alphamenuname
    unlet! s:kankbd_kanamenuname
    unlet! s:kankbd_dicmenuname
    unlet! s:kankbd_dakuonmenuname
endfunction

call KEVsetup()
finish

"# Copyright (c) 2016 ooblog
"# License: MIT
"# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
