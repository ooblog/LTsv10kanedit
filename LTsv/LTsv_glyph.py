#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
import math
try:
   import cPickle as pickle
except:
   import pickle
from LTsv_file    import *
from LTsv_printf import *
from LTsv_time    import *
from LTsv_calc    import *
#from LTsv_joy     import *
#from LTsv_kbd     import *
from LTsv_gui    import *

LTsv_PSfont_ZW,LTsv_PSfont_CW,LTsv_PSchar_ZW,LTsv_PSchar_CW=1024,624,1000,600
LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide={},{},{}
LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide={},{},{}
LTsv_glyphbrush_coord,LTsv_glyphbrush_clock,LTsv_glyphbrush_wide={},{},{}
LTsv_glyph_ltsvdir,LTsv_glyph_ltsvpath,LTsv_glyph_kandicname,LTsv_glyph_kanmapname,LTsv_glyph_kanpicklename="LTsv/","","kanchar.tsv","kanmap.tsv","kanpickle.bin"
LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanmap,LTsv_glyph_kanpickle="","","",{}
LTsv_glyph_irohatype= ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","゛","゜","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
LTsv_glyph_irohatypeN=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
LTsv_glyph_irohatypeX=["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ","｜"]
LTsv_glyph_alphatype= ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
LTsv_glyph_alphatypeN=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
LTsv_glyph_alphatypeX=["Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω","●","▲","■"]
LTsv_glyph_dictype=    ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","漫","筆","幅"]
LTsv_glyph_glyphtype=  ["活","漫","筆"]
LTsv_glyph_choice=    ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
LTsv_glyph_choiceN=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
LTsv_glyph_choiceX=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","Ε","Ρ","Τ","Υ","Θ","Ι","Ο","Π","｀","プ","Α","Σ","Δ","Φ","Γ","Η","Ξ","Κ","Λ","代","鍵","ぬ","Ζ","Χ","Ψ","Ω","Β","Ν","Μ","熙","●","▲","■","￥","Σ"]
LTsv_glyph_evaltype= ["平","片","大","小","半","全","＼","￥","清","Ｈ","Ｍ","濁","Ｂ","Ｐ","今","⑩","⑯","⑧","⓪","照","探","〒","汎","算"]
LTsv_glyph_evalslash,LTsv_glyph_evaldakuon,LTsv_glyph_evalseion="￥","Ｐ","Ｈ"
LTsv_glyph_now,LTsv_glyph_overhour,LTsv_glyph_branch="年-月-日(週曜)時:分:秒",30,"@000y@0m@0dm@wdec@0h@0n@0s"
LTsv_glyph_worddicname,LTsv_glyph_zipdicname,LTsv_glyph_worddic,LTsv_glyph_zipdic="../kanword.tsv","../kanzip.tsv","",""
LTsv_glyph_irohaalpha=LTsv_glyph_irohatype+LTsv_glyph_alphatype
LTsv_glyph_irohaalphaN=LTsv_glyph_irohatypeN+LTsv_glyph_alphatypeN
LTsv_glyph_irohaalphaX=LTsv_glyph_irohatypeX+LTsv_glyph_alphatypeX
LTsv_glyph_kanmapN,LTsv_glyph_kanmapX={},{}
LTsv_glyph_irohamax=12*4; LTsv_glyph_SandS,LTsv_glyph_NFER,LTsv_glyph_XFER,LTsv_glyph_KANA,LTsv_glyph_None=48,49,50,51,52
LTsv_glyph_kbdTAG="kanglyphkbd"
LTsv_glyph_kbdF=6; LTsv_glyph_kbdH=LTsv_glyph_kbdF*4; LTsv_glyph_kbdW=LTsv_glyph_kbdH*4;
LTsv_glyph_kbdG,LTsv_glyph_kbdC=LTsv_glyph_kbdF-1,LTsv_glyph_kbdF//2
LTsv_glyph_fontX,LTsv_glyph_fontY,LTsv_glyph_fontG,LTsv_glyph_mouseX,LTsv_glyph_mouseY,LTsv_glyph_mouseC=[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None)
LTsv_glyph_kbdchars=[""]*(LTsv_glyph_None); LTsv_glyph_kbdchars[LTsv_glyph_SandS],LTsv_glyph_kbdchars[LTsv_glyph_NFER],LTsv_glyph_kbdchars[LTsv_glyph_XFER],LTsv_glyph_kbdchars[LTsv_glyph_KANA]=LTsv_glyph_dictype[0],"Ｎ","Ｘ",LTsv_glyph_irohatype[0]
LTsv_glyph_kbdtype=tuple(["活" if t < LTsv_glyph_SandS else "漫" for t in range(LTsv_glyph_None)])
LTsv_glyph_kbdLCR=[""]
LTsv_glyph_NXKS,LTsv_glyph_kbdSpace,LTsv_glyph_kbdNFER,LTsv_glyph_kbdXFER,LTsv_glyph_kbdKANA=LTsv_glyph_None,"Space","NFER","XFER","KANA"
LTsv_glyph_kbdfontcolor,LTsv_glyph_kbdbgcolor="black","#DAFFF0"
LTsv_glyph_kbdsize=1
LTsv_glyph_cursorsize=10
LTsv_chrcode=chr if sys.version_info.major == 3 else unichr
LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI)
LTsv_draw_color,LTsv_draw_bgcolor=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI)
LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
def LTsv_glyph_kbdinit(ltsvpath="kanglyph.tsv",LTsv_glyph_GUI="",LTsv_glyph_kbddefsize=None):
    global LTsv_glyph_ltsvdir,LTsv_glyph_ltsvpath,LTsv_glyph_kandicname,LTsv_glyph_kanmapname,LTsv_glyph_kanpicklename
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide
    global LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide
    global LTsv_glyphbrush_coord,LTsv_glyphbrush_clock,LTsv_glyphbrush_wide
    global LTsv_glyph_irohatype,LTsv_glyph_irohatypeN,LTsv_glyph_irohatypeX
    global LTsv_glyph_alphatype,LTsv_glyph_alphatypeN,LTsv_glyph_alphatypeX
    global LTsv_glyph_dictype,LTsv_glyph_glyphtype
    global LTsv_glyph_choice,LTsv_glyph_choiceN,LTsv_glyph_choiceX
    global LTsv_glyph_evaltype,LTsv_glyph_evalslash,LTsv_glyph_evaldakuon,LTsv_glyph_evalseion
    global LTsv_glyph_now,LTsv_glyph_overhour,LTsv_glyph_branch
    global LTsv_glyph_worddicname,LTsv_glyph_zipdicname,LTsv_glyph_worddic,LTsv_glyph_zipdic
    global LTsv_glyph_irohaalpha,LTsv_glyph_irohaalphaN,LTsv_glyph_irohaalphaX
    global LTsv_glyph_kanmapN,LTsv_glyph_kanmapX
    global LTsv_glyph_kbdF,LTsv_glyph_kbdH,LTsv_glyph_kbdW,LTsv_glyph_kbdG,LTsv_glyph_kbdC
    global LTsv_glyph_fontX,LTsv_glyph_fontY,LTsv_glyph_fontG,LTsv_glyph_mouseX,LTsv_glyph_mouseY,LTsv_glyph_mouseC
    global LTsv_glyph_kbdchars
    global LTsv_glyph_kbdTAG,LTsv_glyph_kbdfontcolor,LTsv_glyph_kbdbgcolor
    global LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue
    global LTsv_draw_color,LTsv_draw_bgcolor
    global LTsv_glyph_kbdsize
    global LTsv_draw_polygon,LTsv_draw_polygonfill
    global LTsv_draw_squares,LTsv_draw_squaresfill
    global LTsv_draw_circles,LTsv_draw_circlesfill
    global LTsv_draw_points
    LTsv_glyph_ltsvpath=ltsvpath
    LTsv_glyph_ltsv=LTsv_loadfile(LTsv_glyph_ltsvpath)
    LTsv_glyph_ltsvdir=os.path.normpath(os.path.dirname(LTsv_glyph_ltsvpath))+"/"
    LTsv_glyph_config=LTsv_getpage(LTsv_glyph_ltsv,"kanglyph")
    LTsv_glyph_kandicname=LTsv_readlinerest(LTsv_glyph_config,"dicname",LTsv_glyph_kandicname)
    LTsv_glyph_kandic=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kandicname))
    LTsv_glyph_kanmapname=LTsv_readlinerest(LTsv_glyph_config,"mapname",LTsv_glyph_kanmapname)
    LTsv_glyph_kanmap=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanmapname))
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue=LTsv_draw_selcanvas_shell(LTsv_glyph_GUI),LTsv_draw_delete_shell(LTsv_glyph_GUI),LTsv_draw_queue_shell(LTsv_glyph_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor=LTsv_draw_color_shell(LTsv_glyph_GUI),LTsv_draw_bgcolor_shell(LTsv_glyph_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_glyph_GUI),LTsv_draw_polygonfill_shell(LTsv_glyph_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_glyph_GUI),LTsv_draw_squaresfill_shell(LTsv_glyph_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_glyph_GUI),LTsv_draw_circlesfill_shell(LTsv_glyph_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_glyph_GUI)
    LTsv_glyph_kanpicklename=LTsv_readlinerest(LTsv_glyph_config,"picklename",LTsv_glyph_kanpicklename)
    if os.path.isfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpicklename)):
        with open(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpicklename),mode='rb') as pickle_fobj:
            LTsv_glyph_kanpickle=pickle.load(pickle_fobj)
        LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide,LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide,LTsv_glyphbrush_coord,LTsv_glyphbrush_clock,LTsv_glyphbrush_wide=LTsv_glyph_kanpickle
    LTsv_glyph_irohatype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"irohatype",LTsv_tuple2tsv(LTsv_glyph_irohatype)))
    LTsv_glyph_irohatypeN=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"irohatypeN",LTsv_tuple2tsv(LTsv_glyph_irohatypeN)))
    LTsv_glyph_irohatypeX=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"irohatypeX",LTsv_tuple2tsv(LTsv_glyph_irohatypeX)))
    LTsv_glyph_alphatype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"alphatype",LTsv_tuple2tsv(LTsv_glyph_alphatype)))
    LTsv_glyph_alphatypeN=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"alphatypeN",LTsv_tuple2tsv(LTsv_glyph_alphatypeN)))
    LTsv_glyph_alphatypeX=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"alphatypeX",LTsv_tuple2tsv(LTsv_glyph_alphatypeX)))
    LTsv_glyph_dictype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"dictype",LTsv_tuple2tsv(LTsv_glyph_dictype)))
    LTsv_glyph_glyphtype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"glyphtype",LTsv_tuple2tsv(LTsv_glyph_glyphtype)))
    LTsv_glyph_choice=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"choice",LTsv_tuple2tsv(LTsv_glyph_choice)))
    LTsv_glyph_choiceN=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"choiceN",LTsv_tuple2tsv(LTsv_glyph_choiceN)))
    LTsv_glyph_choiceX=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"choiceX",LTsv_tuple2tsv(LTsv_glyph_choiceX)))
    LTsv_glyph_evaltype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"evaltype",LTsv_tuple2tsv(LTsv_glyph_evaltype)))
    LTsv_glyph_evalslash=LTsv_readlinerest(LTsv_glyph_config,"eval_slash",LTsv_glyph_evalslash)
    LTsv_glyph_evaldakuon=LTsv_readlinerest(LTsv_glyph_config,"eval_dakuon",LTsv_glyph_evaldakuon)
    LTsv_glyph_evalseion=LTsv_readlinerest(LTsv_glyph_config,"eval_seion",LTsv_glyph_evalseion)
    LTsv_glyph_now=LTsv_readlinerest(LTsv_glyph_config,"eval_now",LTsv_glyph_now)
    LTsv_glyph_overhour=min(max(LTsv_intstr0x(LTsv_readlinerest(LTsv_glyph_config,"font_size",str(LTsv_glyph_overhour))),24),48)
    LTsv_glyph_branch=LTsv_readlinerest(LTsv_glyph_config,"eval_branch",LTsv_glyph_branch)
    LTsv_glyph_worddicname=LTsv_readlinerest(LTsv_glyph_config,"eval_worddicname",LTsv_glyph_worddicname)
    LTsv_glyph_zipdicname=LTsv_readlinerest(LTsv_glyph_config,"eval_zipdicname",LTsv_glyph_zipdicname)
    LTsv_glyph_irohaalpha=LTsv_glyph_irohatype+LTsv_glyph_alphatype
    LTsv_glyph_irohaalphaN=LTsv_glyph_irohatypeN+LTsv_glyph_alphatypeN
    LTsv_glyph_irohaalphaX=LTsv_glyph_irohatypeX+LTsv_glyph_alphatypeX
    for irohaalpha in LTsv_glyph_irohaalpha:
        kbd_lineT=LTsv_readlinerest(LTsv_glyph_kanmap,irohaalpha)
        kbd_lineL=kbd_lineT.split('\t'); kbd_lineL=kbd_lineL+[" "]*(LTsv_glyph_SandS*2-len(kbd_lineL))
        LTsv_glyph_kanmapN[irohaalpha],LTsv_glyph_kanmapX[irohaalpha]=kbd_lineL[0:LTsv_glyph_SandS+1],kbd_lineL[LTsv_glyph_SandS+1:LTsv_glyph_SandS+1+LTsv_glyph_SandS+1]
    LTsv_glyph_kbdTAG=LTsv_readlinerest(LTsv_glyph_config,"kbdTAG",LTsv_glyph_kbdTAG)
    LTsv_glyph_kbdfontcolor=LTsv_readlinerest(LTsv_glyph_config,"fontcolor",LTsv_glyph_kbdfontcolor)
    LTsv_glyph_kbdbgcolor=LTsv_readlinerest(LTsv_glyph_config,"bgcolor",LTsv_glyph_kbdbgcolor)
    LTsv_glyph_kbdsize=LTsv_intstr0x(LTsv_readlinerest(LTsv_glyph_config,"kbddefsize",str(LTsv_glyph_kbdsize))) if LTsv_glyph_kbddefsize == None else LTsv_glyph_kbddefsize
    LTsv_glyph_kbdF=6*LTsv_glyph_kbdsize; LTsv_glyph_kbdH=LTsv_glyph_kbdF*4; LTsv_glyph_kbdW=LTsv_glyph_kbdH*4;
    LTsv_glyph_kbdG,LTsv_glyph_kbdC=LTsv_glyph_kbdF-1,LTsv_glyph_kbdF//2
    for kbd_xy in range(LTsv_glyph_irohamax):
        LTsv_glyph_fontX[kbd_xy],LTsv_glyph_fontY[kbd_xy]=LTsv_glyph_kbdF*(kbd_xy%12)+LTsv_glyph_kbdF*2,LTsv_glyph_kbdF*(kbd_xy//12)
        LTsv_glyph_kbdchars[kbd_xy]=LTsv_glyph_irohatype[kbd_xy]
    LTsv_glyph_fontX[LTsv_glyph_SandS],LTsv_glyph_fontY[LTsv_glyph_SandS]=1+LTsv_glyph_kbdF*14,1+LTsv_glyph_kbdF*2
    LTsv_glyph_fontX[LTsv_glyph_NFER],LTsv_glyph_fontY[LTsv_glyph_NFER]=1+LTsv_glyph_kbdF*0,1+LTsv_glyph_kbdF*0
    LTsv_glyph_fontX[LTsv_glyph_XFER],LTsv_glyph_fontY[LTsv_glyph_XFER]=1+LTsv_glyph_kbdF*14,1+LTsv_glyph_kbdF*0
    LTsv_glyph_fontX[LTsv_glyph_KANA],LTsv_glyph_fontY[LTsv_glyph_KANA]=1+LTsv_glyph_kbdF*0,1+LTsv_glyph_kbdF*2
    for kbd_xy in range(LTsv_glyph_None):
        kbdC=LTsv_glyph_kbdC if kbd_xy < LTsv_glyph_SandS else LTsv_glyph_kbdC*2
        kbdG=LTsv_glyph_kbdG if kbd_xy < LTsv_glyph_SandS else LTsv_glyph_kbdG*2
        LTsv_glyph_mouseX[kbd_xy],LTsv_glyph_mouseY[kbd_xy],LTsv_glyph_mouseC[kbd_xy],LTsv_glyph_fontG[kbd_xy]=LTsv_glyph_fontX[kbd_xy]+kbdC,LTsv_glyph_fontY[kbd_xy]+kbdC,kbdC,kbdG
    LTsv_glyph_kbdchars[LTsv_glyph_KANA]=LTsv_readlinerest(LTsv_glyph_config,"last_alpha",LTsv_glyph_kbdchars[LTsv_glyph_KANA])[:1]
    LTsv_glyph_kbdchars[LTsv_glyph_SandS]=LTsv_readlinerest(LTsv_glyph_config,"last_dic",LTsv_glyph_kbdchars[LTsv_glyph_SandS])[:1]
    LTsv_glyph_kbdselect(LTsv_glyph_kbdchars[LTsv_glyph_KANA])

#def LTsv_global_kandic():                              return LTsv_glyph_kandic
def LTsv_global_kandic(new_kandic=None):
    global LTsv_glyph_kandic
    LTsv_glyph_kandic=LTsv_glyph_kandic if new_kandic == None else new_kandic
    return LTsv_glyph_kandic
def LTsv_global_kanmap():                              return LTsv_glyph_kanmap
def LTsv_global_kanpickle():                          return LTsv_glyph_kanpickle
def LTsv_global_irohatype():                          return LTsv_glyph_irohatype
def LTsv_global_irohatypeN():                         return LTsv_glyph_irohatypeN
def LTsv_global_irohatypeX():                         return LTsv_glyph_irohatypeX
def LTsv_global_alphatype():                          return LTsv_glyph_alphatype
def LTsv_global_alphatypeN():                         return LTsv_glyph_alphatypeN
def LTsv_global_alphatypeX():                         return LTsv_glyph_alphatypeX
def LTsv_global_dictype():                             return LTsv_glyph_dictype
def LTsv_global_glyphtype():                          return LTsv_glyph_glyphtype
def LTsv_global_choice():                              return LTsv_glyph_choice
def LTsv_global_choiceN():                             return LTsv_glyph_choiceN
def LTsv_global_choiceX():                             return LTsv_glyph_choiceX
def LTsv_global_evaltype():                             return LTsv_glyph_evaltype
def LTsv_global_irohaalpha():                            return LTsv_glyph_irohaalpha
def LTsv_global_irohaalphaN():                           return LTsv_glyph_irohaalphaN
def LTsv_global_irohaalphaX():                           return LTsv_glyph_irohaalphaX
def LTsv_global_kbdchars():                          return LTsv_glyph_kbdchars
def LTsv_global_glyphkbdH():                           return LTsv_glyph_kbdH
def LTsv_global_glyphkbdW():                           return LTsv_glyph_kbdW
def LTsv_global_glyphkbdF():                           return LTsv_glyph_kbdF
def LTsv_global_kbdcursorNone():                           return LTsv_glyph_None

def LTsv_glyphSVG(LTsv_glyph_path):
    LTsv_glyph_pathZ=LTsv_glyph_path.strip(' ').replace('Z','z').rstrip('z').split('z') if len(LTsv_glyph_path) else []
    LTsv_glyphnote,LTsv_glyphclock=[],[]
    for LTsv_glyphline in LTsv_glyph_pathZ:
        LTsv_glyphdata=LTsv_glyphline.split(' '); LTsv_glyphpointlist=[]
        for LTsv_glyphpoint in LTsv_glyphdata:
            if LTsv_glyphpoint.count(',') != 1: continue;
            LTsv_glyphpoints=LTsv_glyphpoint.strip(' ').split(',')
            LTsv_glyphpointlist+=[int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0]
            LTsv_glyphpointlist+=[(LTsv_PSchar_ZW-int(LTsv_glyphpoints[1])) if LTsv_glyphpoints[1].isdigit() else 0]
        LTsv_glyphnote.append(LTsv_glyphpointlist); LTsv_glyphclock.append(LTsv_clockwise(*tuple(LTsv_glyphpointlist)))
    return LTsv_glyphnote,LTsv_glyphclock

def LTsv_glyphpath(glyphcode):
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide
    global LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide
    global LTsv_glyphbrush_coord,LTsv_glyphbrush_clock,LTsv_glyphbrush_wide
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
    LTsv_glyph_wide=LTsv_pickdatalabel(LTsv_glyph_kanline,"幅"); LTsv_glyph5x5_wide[glyphcode]=int(LTsv_glyph_wide) if len(LTsv_glyph_wide) else LTsv_PSfont_ZW
    LTsv_glyphcomic_wide[glyphcode],LTsv_glyphbrush_wide[glyphcode]=LTsv_glyph5x5_wide[glyphcode],LTsv_glyph5x5_wide[glyphcode]
    LTsv_glyph_path5x5=LTsv_pickdatalabel(LTsv_glyph_kanline,"活")
    LTsv_glyph_pathcomic=LTsv_pickdatalabel(LTsv_glyph_kanline,"漫")
    LTsv_glyph_pathbrush=LTsv_pickdatalabel(LTsv_glyph_kanline,"筆")
    if len(LTsv_glyph_path5x5) > 0:
        LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]=LTsv_glyphSVG(LTsv_glyph_path5x5)
    elif len(LTsv_glyph_pathcomic) > 0:
        LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]=LTsv_glyphSVG(LTsv_glyph_pathcomic)
    else:
        LTsv_glyph5x5_coord[glyphcode],LTsv_glyphbrush_clock[glyphcode]=LTsv_glyphSVG(LTsv_glyph_pathbrush)
    if len(LTsv_glyph_pathcomic) > 0:
        LTsv_glyphcomic_coord[glyphcode],LTsv_glyphcomic_clock[glyphcode]=LTsv_glyphSVG(LTsv_glyph_pathcomic)
    else:
        LTsv_glyphcomic_coord[glyphcode],LTsv_glyphcomic_clock[glyphcode]=LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]
    if len(LTsv_glyph_pathbrush) > 0:
        LTsv_glyphbrush_coord[glyphcode],LTsv_glyphbrush_clock[glyphcode]=LTsv_glyphSVG(LTsv_glyph_pathbrush)
    else:
        LTsv_glyphbrush_coord[glyphcode],LTsv_glyphbrush_clock[glyphcode]=LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]

def LTsv_glyphfont_5x5(glyphcode):
    if not glyphcode in LTsv_glyph5x5_coord:
        LTsv_glyphpath(glyphcode)
    return LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]

def LTsv_glyphfont_comic(glyphcode):
    if not glyphcode in LTsv_glyphcomic_coord:
        LTsv_glyphpath(glyphcode)
    return LTsv_glyphcomic_coord[glyphcode],LTsv_glyphcomic_clock[glyphcode]

def LTsv_glyphfont_brush(glyphcode):
    if not glyphcode in LTsv_glyphbrush_coord:
        LTsv_glyphpath(glyphcode)
    return LTsv_glyphbrush_coord[glyphcode],LTsv_glyphbrush_clock[glyphcode]

def LTsv_glyphfont_shell(draw_g="活"):
    if draw_g == "活": return LTsv_glyphfont_5x5
    if draw_g == "漫": return LTsv_glyphfont_comic
    if draw_g == "筆": return LTsv_glyphfont_brush

def LTsv_draw_glyphs(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_g="活",draw_LF=False,draw_HT=False,draw_SP=False):
    draw_xf,draw_yf=draw_x,draw_y
    draw_tf=draw_t if draw_LF == False else draw_tf.replace('\n',"\uf0d3") #
    draw_tf=draw_tf if draw_HT == False else draw_tf.replace('\t',"")
    draw_tf=draw_tf if draw_SP == False else draw_tf.replace(' ',"")
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    for glyphcode in draw_t:
        if glyphcode in "\n\t":
            if glyphcode == '\n':
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
            if glyphcode == '\t':
                draw_xf=int(math.ceil(draw_xf/(draw_f*4))*(draw_f*4))+draw_w
            continue
        LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_draw_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_glyph5x5_wide[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_draw_glyphsfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_g="活",draw_LF=False,draw_HT=False,draw_SP=False):
    draw_xf,draw_yf=draw_x,draw_y
    draw_tf=draw_t if draw_LF == False else draw_tf.replace('\n',"\uf0d3") #
    draw_tf=draw_tf if draw_HT == False else draw_tf.replace('\t',"")
    draw_tf=draw_tf if draw_SP == False else draw_tf.replace(' ',"")
    canvascolor,canvasbgcolor=LTsv_global_canvascolor(),LTsv_global_canvasbgcolor()
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    for glyphcode in draw_t:
        if glyphcode in "\n\t":
            if glyphcode == '\n':
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
            if glyphcode == '\t':
                draw_xf=int(math.ceil(draw_xf/(draw_f*4))*(draw_f*4))+draw_w
            continue
        LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
        for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_draw_color(canvascolor if LTsv_clocknote[LTsv_glyphpointlist_count] > 0 else canvasbgcolor)
            LTsv_draw_polygonfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_glyph5x5_wide[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w
    LTsv_draw_bgcolor(canvasbgcolor); LTsv_draw_color(canvascolor); 

def LTsv_draw_glyphskbd(draw_t,draw_x=0,draw_y=0,draw_f=5,draw_g="活"):
    canvascolor,canvasbgcolor=LTsv_global_canvascolor(),LTsv_global_canvasbgcolor()
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    glyphcode=draw_t[:1]
    LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
    for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
        LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_y if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_x for odd,xy in enumerate(LTsv_glyphpointlist)]
        LTsv_draw_color(canvascolor if LTsv_clocknote[LTsv_glyphpointlist_count] > 0 else canvasbgcolor)
        LTsv_draw_polygonfill(*tuple(LTsv_glyphpointresize))
    LTsv_draw_bgcolor(canvasbgcolor); LTsv_draw_color(canvascolor); 

def LTsv_draw_glyphsentry(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_cL=0,draw_cR=0,draw_g="漫",draw_LF=False,draw_HT=False,draw_SP=False):
    draw_xf,draw_yf=draw_x,draw_y
    draw_tf=draw_t if draw_LF == False else draw_tf.replace('\n',"\uf0d3") #
    draw_tf=draw_tf if draw_HT == False else draw_tf.replace('\t',"")
    draw_tf=draw_tf if draw_SP == False else draw_tf.replace(' ',"")
    canvascolor,canvasbgcolor=LTsv_global_canvascolor(),LTsv_global_canvasbgcolor()
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    for draw_t_pos,glyphcode in enumerate(draw_t):
        if glyphcode in "\n\t":
            if glyphcode == '\n':
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
            if glyphcode == '\t':
                draw_xf=int(math.ceil(draw_xf/(draw_f*4))*(draw_f*4))+draw_w
            continue
        LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
        if draw_cL <= draw_t_pos <= draw_cR:
            LTsv_draw_color(canvascolor)
            for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
                LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
                LTsv_draw_polygon(*tuple(LTsv_glyphpointresize))
        else:
            for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
                LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
                LTsv_draw_color(canvascolor if LTsv_clocknote[LTsv_glyphpointlist_count] > 0 else canvasbgcolor)
                LTsv_draw_polygonfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_glyph5x5_wide[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w
    LTsv_draw_color(canvascolor); LTsv_draw_bgcolor(canvasbgcolor)

def LTsv_draw_glyphclock(draw_t="",draw_x=0,draw_y=0,draw_f=LTsv_PSchar_ZW//2,draw_g="活",color_R="#6E81D9",color_L="#6ED997",color_X="#D96ED3"):
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    glyphcode=draw_t[:1]
    LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
    for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
        glyphclock=LTsv_clocknote[LTsv_glyphpointlist_count]
        LTsv_draw_color(draw_c=color_R if glyphclock > 0 else color_L if glyphclock < 0 else color_X)
        LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_y if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_x for odd,xy in enumerate(LTsv_glyphpointlist)]
        LTsv_draw_polygon(*tuple(LTsv_glyphpointresize))

def LTsv_draw_glyphclockfill(draw_t="",draw_x=0,draw_y=0,draw_f=LTsv_PSchar_ZW//2,draw_g="活",color_R="#6E81D9",color_L="#6ED997",color_X="#D96ED3"):
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    glyphcode=draw_t[:1]
    LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
    for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
        glyphclock=LTsv_clocknote[LTsv_glyphpointlist_count]
        LTsv_draw_color(draw_c=color_R if glyphclock > 0 else color_L if glyphclock < 0 else color_X)
        LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_y if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_x for odd,xy in enumerate(LTsv_glyphpointlist)]
        LTsv_draw_polygonfill(*tuple(LTsv_glyphpointresize))

def LTsv_draw_glyphcursor(draw_t="",draw_x=0,draw_y=0,path_z=0,draw_s=0,grid_p=-1,grid_q=-1,draw_f=LTsv_PSchar_ZW//2,draw_g="活",color_R="#6E81D9",color_L="#6ED997",color_X="#D96ED3"):
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    glyphcode=draw_t[:1]
    LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
    for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
        if path_z != LTsv_glyphpointlist_count: continue;
        glyphclock=LTsv_clocknote[LTsv_glyphpointlist_count]
        LTsv_draw_color(draw_c=color_R if glyphclock > 0 else color_L if glyphclock < 0 else color_X)
        LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_y if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_x for odd,xy in enumerate(LTsv_glyphpointlist)]
        LTsv_draw_glyphsfill(draw_t=str(path_z),draw_x=LTsv_glyphpointresize[0]+LTsv_glyph_cursorsize,draw_y=LTsv_glyphpointresize[1]+LTsv_glyph_cursorsize,draw_f=LTsv_glyph_cursorsize,draw_g="漫")
        LTsv_glyphpointseg=[(xy+LTsv_glyphpointresize[(odd+2)%len(LTsv_glyphpointresize)])//2 for odd,xy in enumerate(LTsv_glyphpointresize)]
        grid_len=len(LTsv_glyphpointlist)//2
        for glyphpoints in range(grid_len):
            x,y=LTsv_glyphpointresize[glyphpoints*2],LTsv_glyphpointresize[glyphpoints*2+1]
            if grid_p == glyphpoints:
                LTsv_draw_squaresfill(LTsv_glyph_cursorsize,*tuple([x,y]))
            else:
                LTsv_draw_squares(LTsv_glyph_cursorsize,*tuple([x,y]))
            if draw_s != 0:
                x,y=LTsv_glyphpointseg[glyphpoints*2],LTsv_glyphpointseg[glyphpoints*2+1]
                if grid_q == glyphpoints:
                    LTsv_draw_circlesfill(LTsv_glyph_cursorsize-2,*tuple([x,y]))
                else:
                    LTsv_draw_circles(LTsv_glyph_cursorsize-2,*tuple([x,y]))

def LTsv_draw_glypwide(draw_t="",draw_x=0,draw_y=0,draw_s=0,draw_f=LTsv_PSchar_ZW//2,draw_g="活",color_W="#9F6C00"):
    LTsv_draw_color(color_W)
    glyphcode=draw_t[:1]
    wide=LTsv_glyph5x5_wide[glyphcode]//2
    LTsv_draw_squares(LTsv_glyph_cursorsize,*tuple([LTsv_PSchar_ZW//2//20*xy if xy%2 else wide for xy in range(20)]))

def LTsv_draw_glyphmouse(draw_t="",draw_x=0,draw_y=0,path_z=0,grid_x=LTsv_PSchar_ZW//2,grid_y=LTsv_PSchar_ZW//2,mouse_x=LTsv_PSchar_ZW//2,mouse_y=LTsv_PSchar_ZW//2,draw_f=LTsv_PSchar_ZW//2,draw_g="活"):
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    glyphcode=draw_t[:1]
    LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
    grid_p,grid_q=-1,-1
    for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
        if path_z != LTsv_glyphpointlist_count: continue;
        LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_y if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_x for odd,xy in enumerate(LTsv_glyphpointlist)]
        LTsv_glyphpointseg=[(xy+LTsv_glyphpointresize[(odd+2)%len(LTsv_glyphpointresize)])//2 for odd,xy in enumerate(LTsv_glyphpointresize)]
        grid_len=len(LTsv_glyphpointlist)//2
        for glyphpoints in range(grid_len):
            if abs(LTsv_glyphpointresize[glyphpoints*2]-grid_x) < LTsv_glyph_cursorsize//2 and abs(LTsv_glyphpointresize[glyphpoints*2+1]-grid_y) < LTsv_glyph_cursorsize//2:
                grid_p=glyphpoints
        if not grid_p >= 0:
            for glyphpoints in range(grid_len):
                if abs(LTsv_glyphpointseg[glyphpoints*2]-mouse_x) < LTsv_glyph_cursorsize//2 and abs(LTsv_glyphpointseg[glyphpoints*2+1]-mouse_y) < LTsv_glyph_cursorsize//2:
                    grid_q=glyphpoints
    return grid_p,grid_q

def LTsv_glyph_getnote(draw_t="",draw_g="活"):
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    glyphcode=draw_t[:1]
    LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
    return LTsv_glyphnote

def LTsv_glyph_pointsrotation(glyphnote=[]):
    for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(glyphnote):
        distance=[math.sqrt(LTsv_glyphpointlist[xy*2]**2+LTsv_glyphpointlist[xy*2+1]**2) for xy in range(len(LTsv_glyphpointlist)//2)]
        rotation=distance.index(min(distance))
        if rotation != 0:
            glyphnote[LTsv_glyphpointlist_count]=[LTsv_glyphpointlist[(odd+rotation*2)%len(LTsv_glyphpointlist)] for odd,xy in enumerate(LTsv_glyphpointlist)]
    return glyphnote

def LTsv_glyph_points2path(draw_t="",glyphnote=[],draw_g="活"):
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    LTsv_glyphfont=LTsv_glyphfont_shell(draw_g)
    glyphcode=draw_t[:1]
    LTsv_glyph_kanpath=""
    for glyphpoints in glyphnote:
        glyphpointlist=""
        for draw_xy_count in range(len(glyphpoints)//2):
            glyphpointlist+="{0},{1} ".format(glyphpoints[draw_xy_count*2],LTsv_PSchar_ZW-glyphpoints[draw_xy_count*2+1])
        LTsv_glyph_kanpath+="M {0}z ".format(glyphpointlist)
    LTsv_glyph_kanpath=LTsv_glyph_kanpath.rstrip(' ')
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
    if draw_g == "活":
        LTsv_glyph_kanline=LTsv_setdatalabel(LTsv_glyph_kanline,draw_g,LTsv_glyph_kanpath)
    else:
        LTsv_glyph_kanline=LTsv_setdatalabel(LTsv_glyph_kanline,draw_g,LTsv_glyph_kanpath if LTsv_pickdatalabel(LTsv_glyph_kanline,"活") != LTsv_glyph_kanpath else "")
    LTsv_glyph_kandic=LTsv_pushlinerest(LTsv_glyph_kandic,glyphcode,LTsv_glyph_kanline)
    LTsv_glyphpath(glyphcode)
    LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)

def LTsv_glyph_text2path(draw_t="",kanpath="",draw_g="俗"):
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    glyphcode=draw_t[:1]
    if LTsv_pickdic(LTsv_glyph_kandic,glyphcode,draw_g) != kanpath:
        LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
        LTsv_glyph_kanline=LTsv_setdatalabel(LTsv_glyph_kanline,draw_g,kanpath)
        LTsv_glyph_kanline=LTsv_sievetuplelabels(LTsv_glyph_kanline,*tuple(LTsv_glyph_dictype))
        LTsv_glyph_kandic=LTsv_pushlinerest(LTsv_glyph_kandic,glyphcode,LTsv_glyph_kanline)

def LTsv_glyph_kbdcursor(kbd_canvas,kbd_x,kbd_y):
    LTsv_draw_selcanvas(kbd_canvas,draw_g=LTsv_glyph_kbdTAG)
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    LTsv_kbdcursor=LTsv_glyph_None
    for kbd_xy in range(LTsv_glyph_None):
        if abs(kbd_x+LTsv_glyph_mouseX[kbd_xy]-mouseX) <= LTsv_glyph_mouseC[kbd_xy] and abs(kbd_y+LTsv_glyph_mouseY[kbd_xy]-mouseY) <= LTsv_glyph_mouseC[kbd_xy]:
            LTsv_kbdcursor=kbd_xy
    return  LTsv_kbdcursor

def LTsv_glyph_kbdselect(choice):
    global LTsv_glyph_kbdchars
    if choice in LTsv_glyph_irohaalphaN:
        choiceNX=LTsv_glyph_irohaalpha[LTsv_glyph_irohaalphaN.index(choice)]
        LTsv_glyph_kbdchars[0:LTsv_glyph_irohamax]=LTsv_glyph_kanmapN[choiceNX][0:LTsv_glyph_irohamax]
        LTsv_glyph_kbdchars[LTsv_glyph_KANA]=choice
    elif choice in LTsv_glyph_irohaalphaX:
        choiceNX=LTsv_glyph_irohaalpha[LTsv_glyph_irohaalphaX.index(choice)]
        LTsv_glyph_kbdchars[0:LTsv_glyph_irohamax]=LTsv_glyph_kanmapX[choiceNX][0:LTsv_glyph_irohamax]
        LTsv_glyph_kbdchars[LTsv_glyph_KANA]=choice

def LTsv_glyph_choiceNX(choice):
    if choice in LTsv_glyph_irohaalphaN:
        choiceNX=LTsv_glyph_irohaalphaN.index(choice)
    elif choice in LTsv_glyph_irohaalphaX:
        choiceNX=LTsv_glyph_irohaalphaX.index(choice)
    return choiceNX

def LTsv_glyph_kbdfind(find_t):
    find_existpos=-1
    for exist_index,exist_char in enumerate(find_t):
        for iroha_char in LTsv_glyph_irohaalpha:
            if exist_char in LTsv_glyph_kanmapN[iroha_char]:
#                print(exist_char,iroha_char,LTsv_glyph_irohaalpha.index(iroha_char),LTsv_glyph_irohaalphaN[LTsv_glyph_irohaalpha.index(iroha_char)])
                LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaN[LTsv_glyph_irohaalpha.index(iroha_char)])
                find_existpos=exist_index
            if exist_char in LTsv_glyph_kanmapX[iroha_char]:
#                print(exist_char,iroha_char,LTsv_glyph_irohaalpha.index(iroha_char),LTsv_glyph_irohaalphaX[LTsv_glyph_irohaalpha.index(iroha_char)])
                LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaX[LTsv_glyph_irohaalpha.index(iroha_char)])
                find_existpos=exist_index
            if find_existpos >= 0: break;
        if find_existpos >= 0: break;
    return find_existpos

LTsv_glyph_tapcallback={}
def LTsv_glyph_tapcallback_shell(kbd_canvas,callback):
    global LTsv_glyph_tapcallback
    LTsv_glyph_tapcallback[kbd_canvas]=callback

def LTsv_glyph_mousepress(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_kbdLCR
    LTsv_kbdcursor=LTsv_glyph_kbdcursor(kbd_canvas,kbd_x,kbd_y)
    if LTsv_kbdcursor < LTsv_glyph_None:
        LTsv_glyph_kbddelete(kbd_canvas)
        if LTsv_kbdcursor == LTsv_glyph_SandS:
            LTsv_glyph_kbdLCR="FlickS"
            LTsv_glyph_kbdchar_SandS=LTsv_glyph_kbdchars[LTsv_glyph_SandS]
#            for kbd_xy,kbd_c in enumerate(LTsv_glyph_kbdchars[:LTsv_glyph_irohamax]):
#                LTsv_glyph_kbdchars[kbd_xy]=LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,kbd_c),LTsv_glyph_kbdchar_SandS)[:1]
            LTsv_glyph_kbdchars[:LTsv_glyph_irohamax]=[LTsv_pickdic(LTsv_glyph_kandic,kbd_c,LTsv_glyph_kbdchar_SandS)[:1] for kbd_c in LTsv_glyph_kbdchars[:LTsv_glyph_irohamax]]
        elif LTsv_kbdcursor == LTsv_glyph_NFER:
            LTsv_glyph_kbdLCR="SwipeN"
            LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaN[LTsv_glyph_choiceNX(LTsv_glyph_kbdchars[LTsv_glyph_KANA])])
        elif LTsv_kbdcursor == LTsv_glyph_XFER:
            LTsv_glyph_kbdLCR="SwipeX"
            LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaX[LTsv_glyph_choiceNX(LTsv_glyph_kbdchars[LTsv_glyph_KANA])])
        elif LTsv_kbdcursor == LTsv_glyph_KANA:
            LTsv_glyph_kbdLCR="SwipeK"
            if LTsv_glyph_kbdchars[LTsv_glyph_KANA] in LTsv_glyph_irohaalphaN:
                LTsv_glyph_kbdchars[0:LTsv_glyph_irohamax]=LTsv_glyph_choiceN[0:LTsv_glyph_irohamax]
            elif LTsv_glyph_kbdchars[LTsv_glyph_KANA] in LTsv_glyph_irohaalphaX:
                LTsv_glyph_kbdchars[0:LTsv_glyph_irohamax]=LTsv_glyph_choiceX[0:LTsv_glyph_irohamax]
        else:
            LTsv_glyph_kbdLCR="Tap"
            if kbd_canvas in LTsv_glyph_tapcallback:
                if LTsv_glyph_tapcallback[kbd_canvas] != None:
                    LTsv_glyph_tapcallback[kbd_canvas](LTsv_glyph_kbdchars[LTsv_kbdcursor])
        LTsv_glyph_kbddraw(kbd_canvas,kbd_x,kbd_y)
        LTsv_draw_queue()
    return LTsv_kbdcursor

def LTsv_glyph_mousemotion(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_kbdLCR
    LTsv_kbdcursor=LTsv_glyph_kbdcursor(kbd_canvas,kbd_x,kbd_y)
    if LTsv_kbdcursor < LTsv_glyph_None:
        LTsv_glyph_kbddelete(kbd_canvas)
        if LTsv_glyph_kbdLCR == "SwipeN":
            if LTsv_kbdcursor < LTsv_glyph_SandS:
                LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaN[LTsv_kbdcursor])
            elif LTsv_kbdcursor == LTsv_glyph_XFER:
                LTsv_glyph_kbdLCR="SwipeX"
                LTsv_glyph_kbdselect('Σ')
            elif LTsv_kbdcursor != LTsv_glyph_NFER:
                LTsv_glyph_kbdselect('σ')
        elif LTsv_glyph_kbdLCR == "SwipeX":
            if LTsv_kbdcursor < LTsv_glyph_SandS:
                LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaX[LTsv_kbdcursor])
            elif LTsv_kbdcursor == LTsv_glyph_NFER:
                LTsv_glyph_kbdLCR="SwipeN"
                LTsv_glyph_kbdselect('σ')
            elif LTsv_kbdcursor != LTsv_glyph_XFER:
                LTsv_glyph_kbdselect('Σ')
        LTsv_glyph_kbddraw(kbd_canvas,kbd_x,kbd_y)
        LTsv_draw_queue()
    return LTsv_kbdcursor

def LTsv_glyph_mouserelease(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_kbdLCR
    LTsv_kbdcursor=LTsv_glyph_kbdcursor(kbd_canvas,kbd_x,kbd_y)
    if LTsv_kbdcursor < LTsv_glyph_None:
        LTsv_glyph_kbddelete(kbd_canvas)
        if LTsv_glyph_kbdLCR == "SwipeK":
            if LTsv_glyph_kbdchars[LTsv_kbdcursor] in LTsv_glyph_dictype:
                LTsv_glyph_kbdchars[LTsv_glyph_SandS]=LTsv_glyph_kbdchars[LTsv_kbdcursor]
            elif LTsv_glyph_kbdchars[LTsv_kbdcursor] in LTsv_glyph_irohaalphaN+LTsv_glyph_irohaalphaX:
                LTsv_glyph_kbdchars[LTsv_glyph_KANA]=LTsv_glyph_kbdchars[LTsv_kbdcursor]
            LTsv_glyph_kbdselect(LTsv_glyph_kbdchars[LTsv_glyph_KANA])
        elif LTsv_glyph_kbdLCR == "FlickS":
            LTsv_glyph_kbdselect(LTsv_glyph_kbdchars[LTsv_glyph_KANA])
            if LTsv_kbdcursor < LTsv_glyph_SandS:
                if kbd_canvas in LTsv_glyph_tapcallback:
                    if LTsv_glyph_tapcallback[kbd_canvas] != None:
                        LTsv_glyph_tapcallback[kbd_canvas](LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,LTsv_glyph_kbdchars[LTsv_kbdcursor]),LTsv_glyph_kbdchars[LTsv_glyph_SandS]))
        LTsv_glyph_kbddraw(kbd_canvas,kbd_x,kbd_y)
        LTsv_draw_queue()
    LTsv_glyph_kbdLCR=""
    return LTsv_kbdcursor

def LTsv_glyph_typepress(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_NXKS,LTsv_glyph_kbdSpace,LTsv_glyph_kbdNFER,LTsv_glyph_kbdXFER,LTsv_glyph_kbdKANA
    LTsv_setkbddata(20,0); glyphtype_getkbdnames,glyphtype_getkbdkanas=LTsv_getkbdnames(),LTsv_getkbdkanas()
    print(glyphtype_getkbdnames)
    LTsv_glyph_NXKS= \
     LTsv_glyph_SandS if LTsv_glyph_kbdSpace in glyphtype_getkbdnames else \
     LTsv_glyph_NFER if LTsv_glyph_kbdNFER in glyphtype_getkbdnames else \
     LTsv_glyph_XFER if LTsv_glyph_kbdXFER in glyphtype_getkbdnames else \
     LTsv_glyph_KANA if LTsv_glyph_kbdKANA in glyphtype_getkbdnames else LTsv_glyph_None
    if LTsv_glyph_NXKS == LTsv_glyph_NFER:
        LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaN[LTsv_glyph_choiceNX(LTsv_glyph_kbdchars[LTsv_glyph_KANA])])
        LTsv_glyph_kbddelete(kbd_canvas); LTsv_glyph_kbddraw(kbd_canvas,kbd_x,kbd_y); LTsv_draw_queue()
    if LTsv_glyph_NXKS == LTsv_glyph_XFER:
        LTsv_glyph_kbdselect(LTsv_glyph_irohaalphaX[LTsv_glyph_choiceNX(LTsv_glyph_kbdchars[LTsv_glyph_KANA])])
        LTsv_glyph_kbddelete(kbd_canvas); LTsv_glyph_kbddraw(kbd_canvas,kbd_x,kbd_y); LTsv_draw_queue()
    if kbd_canvas in LTsv_glyph_tapcallback:
        if LTsv_glyph_tapcallback[kbd_canvas] != None:
            if "Tab" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "BS" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "DEL" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "Enter" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "Left" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("")
            if "Down" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "Up" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "Right" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "Home" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "End" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "PgUp" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            if "PgDn" in glyphtype_getkbdnames: LTsv_glyph_tapcallback[kbd_canvas]("");
            for kbdkanas in glyphtype_getkbdkanas.split('\t') if len(glyphtype_getkbdkanas) > 0 else []:
                if kbdkanas in LTsv_glyph_irohatype:
                    LTsv_kbdcursor=LTsv_glyph_irohatype.index(kbdkanas)
                    if LTsv_glyph_NXKS == LTsv_glyph_None:
                        LTsv_glyph_tapcallback[kbd_canvas](LTsv_glyph_kbdchars[LTsv_kbdcursor])
                    elif LTsv_glyph_NXKS <= LTsv_glyph_SandS:
                        LTsv_glyph_NXKS == LTsv_kbdcursor
                    elif LTsv_glyph_NXKS == LTsv_glyph_NFER:
                        pass
                    elif LTsv_glyph_NXKS == LTsv_glyph_XFER:
                        pass
                    elif LTsv_glyph_NXKS == LTsv_glyph_KANA:
                        pass

def LTsv_glyph_typerelease(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_NXKS,LTsv_glyph_kbdSpace,LTsv_glyph_kbdNFER,LTsv_glyph_kbdXFER,LTsv_glyph_kbdKANA
    LTsv_setkbddata(20,0); glyphtype_getkbdnames,glyphtype_getkbdkanas=LTsv_getkbdnames(),LTsv_getkbdkanas()
    if LTsv_glyph_NXKS <= LTsv_glyph_SandS:
        if not LTsv_glyph_kbdSpace in glyphtype_getkbdnames:
            print("SandS",LTsv_glyph_NXKS,LTsv_glyph_SandS)
    LTsv_glyph_NXKS= \
     LTsv_glyph_SandS if LTsv_glyph_kbdSpace in glyphtype_getkbdnames else \
     LTsv_glyph_NFER if LTsv_glyph_kbdNFER in glyphtype_getkbdnames else \
     LTsv_glyph_XFER if LTsv_glyph_kbdXFER in glyphtype_getkbdnames else \
     LTsv_glyph_KANA if LTsv_glyph_kbdKANA in glyphtype_getkbdnames else LTsv_glyph_None

def LTsv_glyph_kbddelete(kbd_canvas):
    if LTsv_global_GUI() == "GTK2":
        pass
    if LTsv_global_GUI() == "Tkinter":
        LTsv_draw_selcanvas(kbd_canvas,draw_g=LTsv_glyph_kbdTAG)
        LTsv_draw_delete()

def LTsv_glyph_kbddraw(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_kbdchars
    LTsv_draw_selcanvas(kbd_canvas,draw_g=LTsv_glyph_kbdTAG)
    LTsv_draw_color(LTsv_glyph_kbdbgcolor)
    LTsv_draw_bgcolor(LTsv_glyph_kbdbgcolor)
    LTsv_draw_polygonfill(*tuple([kbd_x,kbd_y,kbd_x+LTsv_glyph_kbdW,kbd_y,kbd_x+LTsv_glyph_kbdW,kbd_y+LTsv_glyph_kbdH,kbd_x,kbd_y+LTsv_glyph_kbdH]))
    LTsv_draw_color(LTsv_glyph_kbdfontcolor)
    for kbd_xy in range(LTsv_glyph_None):
        LTsv_draw_glyphskbd(draw_t=LTsv_glyph_kbdchars[kbd_xy],draw_x=kbd_x+LTsv_glyph_fontX[kbd_xy],draw_y=kbd_y+LTsv_glyph_fontY[kbd_xy],draw_f=LTsv_glyph_fontG[kbd_xy],draw_g=LTsv_glyph_kbdtype[kbd_xy])

def LTsv_glyph_picklesave():
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_kanglyph5x5OBJ,LTsv_kanglyphcomicOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    LTsv_glyph_kanpickle=LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide,LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide,LTsv_glyphbrush_coord,LTsv_glyphbrush_clock,LTsv_glyphbrush_wide
    with open(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpicklename),mode='wb') as pickle_fobj:
        pickle.dump(LTsv_glyph_kanpickle,pickle_fobj,protocol=2)
    LTsv_glyph_ltsv=LTsv_loadfile(LTsv_glyph_ltsvpath)
    LTsv_glyph_config=LTsv_getpage(LTsv_glyph_ltsv,"kanglyph")
    LTsv_glyph_config=LTsv_pushlinerest(LTsv_glyph_config,"last_alpha",LTsv_glyph_kbdchars[LTsv_glyph_KANA])
    LTsv_glyph_config=LTsv_pushlinerest(LTsv_glyph_config,"last_dic",LTsv_glyph_kbdchars[LTsv_glyph_SandS])
    LTsv_glyph_ltsv=LTsv_putpage(LTsv_glyph_ltsv,"kanglyph",LTsv_glyph_config)
    LTsv_savefile(LTsv_glyph_ltsvpath,LTsv_glyph_ltsv)

LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text,LTsv_kbdentry_fontcolor,LTsv_kbdentry_cursorL,LTsv_kbdentry_cursorR={},{},{},{},{},{}
LTsv_clipentry_l,LTsv_clipentry_c,LTsv_clipentry_v,LTsv_clipentry_e={},{},{},{}
def LTsv_kbdentry_hjkl(entry_t="",entry_ch="",entry_cL=0,entry_cR=0,clip_c=None,clip_v=None,clip_e=None):
    entry_cL,entry_cR=min(max(0,entry_cL),len(entry_t)),min(max(0,entry_cR),len(entry_t))
    if entry_cR < entry_cL: entry_cL,entry_cR=entry_cR,entry_cL
    LTsv_hjkl_clippaste=""
    if entry_ch in "":
        if entry_ch in "":
            LTsv_hjkl_clippaste="\t"
        if entry_ch in "":
            LTsv_hjkl_clippaste="    "
        if entry_ch in "":
            LTsv_hjkl_clippaste=clip_v() if clip_v != None else ""
        if entry_ch in "":
            entry_t=entry_t[:entry_cL]+LTsv_hjkl_clippaste+entry_t[entry_cR:]
            entry_cR=entry_cL+len(LTsv_hjkl_clippaste)-1
        if entry_ch in "":
            if clip_c != None: clip_c(entry_t[entry_cL:entry_cR+1])
        if entry_ch in "":
            if 0 < entry_cL: entry_t=entry_t[:max(entry_cL-1,0)]+entry_t[entry_cL:];
        if entry_ch in "":
            entry_t=entry_t[:entry_cL]+entry_t[max(entry_cR+1,0):]
        if entry_ch in "":
            entry_cL=max(0,entry_cL-1) if not entry_ch in "" else 0
        if entry_ch in "":
            entry_cL=min(entry_cL+1,len(entry_t)); entry_cR=max(entry_cR,entry_cL)
        if entry_ch in "":
            entry_cR=min(entry_cR+1,len(entry_t)) if not entry_ch in "" else len(entry_t)
        if entry_ch in "":
            entry_cR=max(0,entry_cR-1); entry_cL=min(entry_cR,entry_cL)
        if entry_ch in "":
            entry_cR=entry_cL
        if entry_ch in "":
            entry_cL=entry_cR
    elif entry_ch == "":
        if clip_e != None:
            entry_t=clip_e(entry_t); entry_cL,entry_cR=len(entry_t),len(entry_t)
    else:
        entry_t=entry_t[:entry_cL]+entry_ch+entry_t[entry_cL:];  entry_cL+=1; entry_cR=entry_cL
    return entry_t,entry_cL,entry_cR

def LTsv_kbdentry_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,clip_c=None,clip_v=None,clip_e=None,widget_x=0,widget_y=0,widget_w=LTsv_glyph_kbdW,widget_h=LTsv_glyph_kbdH,event_w=50):
    global LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text,LTsv_kbdentry_fontcolor,LTsv_kbdentry_cursorL
    global LTsv_clipentry_c,LTsv_clipentry_v,LTsv_clipentry_e
    def kbdentry_input(kbdentry):
        LTsv_kbdentry_text[kbdentry_canvas],LTsv_kbdentry_cursorL[kbdentry_canvas],LTsv_kbdentry_cursorR[kbdentry_canvas]=LTsv_kbdentry_hjkl(entry_t=LTsv_kbdentry_text[kbdentry_canvas],entry_ch=kbdentry,entry_cL=LTsv_kbdentry_cursorL[kbdentry_canvas],entry_cR=LTsv_kbdentry_cursorR[kbdentry_canvas],clip_c=clip_c,clip_v=clip_v,clip_e=clip_e)
        LTsv_draw_selcanvas(kbdentry_canvas)
        LTsv_draw_delete()
        LTsv_draw_color(LTsv_kbdentry_fontcolor[kbdentry_canvas]); LTsv_draw_glyphsentry(draw_t=LTsv_kbdentry_text[kbdentry_canvas],draw_x=0,draw_y=LTsv_glyph_kbdH//4,draw_cL=LTsv_kbdentry_cursorL[kbdentry_canvas],draw_cR=LTsv_kbdentry_cursorR[kbdentry_canvas],draw_f=LTsv_glyph_kbdH//2,draw_g="漫")
        LTsv_glyph_kbddraw(kbdentry_canvas,LTsv_kbdentry_x[kbdentry_canvas],LTsv_kbdentry_y[kbdentry_canvas])
        LTsv_draw_queue()
    def kbdentry_press(window_objvoid=None,window_objptr=None):
        global LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text,LTsv_kbdentry_fontcolor,LTsv_kbdentry_cursorL
        LTsv_draw_selcanvas(kbdentry_canvas)
        LTsv_glyph_mousepress(kbdentry_canvas,LTsv_kbdentry_x[kbdentry_canvas],LTsv_kbdentry_y[kbdentry_canvas])
        LTsv_draw_queue()
    def kbdentry_release(window_objvoid=None,window_objptr=None):
        global LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text,LTsv_kbdentry_fontcolor,LTsv_kbdentry_cursorL
        LTsv_draw_selcanvas(kbdentry_canvas)
        LTsv_glyph_mouserelease(kbdentry_canvas,LTsv_kbdentry_x[kbdentry_canvas],LTsv_kbdentry_y[kbdentry_canvas])
        LTsv_draw_queue()
    def kbdentry_motion(window_objvoid=None,window_objptr=None):
        global LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text,LTsv_kbdentry_fontcolor,LTsv_kbdentry_cursorL
        LTsv_draw_selcanvas(kbdentry_canvas)
        LTsv_glyph_mousemotion(kbdentry_canvas,LTsv_kbdentry_x[kbdentry_canvas],LTsv_kbdentry_y[kbdentry_canvas])
        LTsv_draw_queue()
    def kbdentry_enter(window_objvoid=None,window_objptr=None):
        global LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text,LTsv_kbdentry_fontcolor,LTsv_kbdentry_cursorL
        LTsv_draw_selcanvas(kbdentry_canvas)
        LTsv_draw_delete()
        LTsv_draw_color(LTsv_kbdentry_fontcolor[kbdentry_canvas]); LTsv_draw_glyphsentry(draw_t=LTsv_kbdentry_text[kbdentry_canvas],draw_x=0,draw_y=LTsv_glyph_kbdH//4,draw_cL=LTsv_kbdentry_cursorL[kbdentry_canvas],draw_cR=LTsv_kbdentry_cursorR[kbdentry_canvas],draw_f=LTsv_glyph_kbdH//2,draw_g="漫")
        LTsv_glyph_kbddraw(kbdentry_canvas,LTsv_kbdentry_x[kbdentry_canvas],LTsv_kbdentry_y[kbdentry_canvas])
        LTsv_draw_queue()
    def kbdentry_leave(window_objvoid=None,window_objptr=None):
        global LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text
        if LTsv_clipentry_l[kbdentry_canvas] != None:
            LTsv_kbdentry_text[kbdentry_canvas]=LTsv_clipentry_l[kbdentry_canvas](LTsv_kbdentry_text[kbdentry_canvas])
        LTsv_glyph_kbddelete(kbdentry_canvas)
        LTsv_draw_selcanvas(kbdentry_canvas)
        LTsv_draw_delete()
        LTsv_draw_color(LTsv_kbdentry_fontcolor[kbdentry_canvas]); LTsv_draw_glyphsfill(draw_t=LTsv_kbdentry_text[kbdentry_canvas],draw_x=0,draw_y=LTsv_glyph_kbdH//4,draw_f=LTsv_glyph_kbdH//2,draw_g="漫")
        LTsv_draw_queue()
    kbdentry_canvas=LTsv_canvas_new(LTsv_windowPAGENAME,widget_n=widget_n,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h,
     event_p=kbdentry_press,event_r=kbdentry_release,event_m=kbdentry_motion,event_e=kbdentry_enter,event_l=kbdentry_leave,event_w=event_w)
    LTsv_kbdentry_fontcolor[kbdentry_canvas]=LTsv_global_canvascolor()
    LTsv_kbdentry_text[kbdentry_canvas]=""
    LTsv_kbdentry_cursorL[kbdentry_canvas]=len(LTsv_kbdentry_text[kbdentry_canvas]); LTsv_kbdentry_cursorR[kbdentry_canvas]=LTsv_kbdentry_cursorL[kbdentry_canvas]
    LTsv_kbdentry_x[kbdentry_canvas],LTsv_kbdentry_y[kbdentry_canvas]=widget_w-LTsv_glyph_kbdW,widget_h-LTsv_glyph_kbdH
    LTsv_clipentry_l[kbdentry_canvas],LTsv_clipentry_c[kbdentry_canvas],LTsv_clipentry_v[kbdentry_canvas],LTsv_clipentry_e[kbdentry_canvas]=event_b,clip_c,clip_v,clip_e
    LTsv_glyph_tapcallback_shell(kbdentry_canvas,kbdentry_input)
    LTsv_widgetLTSV=LTsv_global_widgetltsv()
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,kbdentry_canvas)
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,kbd_p=kbdentry_press,kbd_r=kbdentry_release,kbd_m=kbdentry_motion,kbd_e=kbdentry_enter,kbd_l=kbdentry_leave,kbd_i=kbdentry_input)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,kbdentry_canvas,LTsv_widgetPAGE)
    LTsv_global_widgetltsv(LTsv_widgetLTSV)
    return kbdentry_canvas

def LTsv_kbdentry_settext(kbdentry_canvas,widget_t=""):
    global LTsv_kbdentry_x,LTsv_kbdentry_y,LTsv_kbdentry_text
    LTsv_kbdentry_text[kbdentry_canvas]=widget_t
    LTsv_kbdentry_cursorL[kbdentry_canvas]=len(LTsv_kbdentry_text[kbdentry_canvas]); LTsv_kbdentry_cursorR[kbdentry_canvas]=LTsv_kbdentry_cursorL[kbdentry_canvas]
    LTsv_widgetLTSV=LTsv_global_widgetltsv()
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,kbdentry_canvas)
#    LTsv_widget_getobj(LTsv_widgetPAGE,"kbdentry_leave")()
    LTsv_glyph_kbddelete(kbdentry_canvas)
    LTsv_draw_selcanvas(kbdentry_canvas)
    LTsv_draw_delete()
    LTsv_draw_color(LTsv_kbdentry_fontcolor[kbdentry_canvas]); LTsv_draw_glyphsfill(draw_t=LTsv_kbdentry_text[kbdentry_canvas],draw_x=0,draw_y=LTsv_glyph_kbdH//4,draw_f=LTsv_glyph_kbdH//2,draw_g="漫")
    LTsv_draw_queue()
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,kbdentry_canvas,LTsv_widgetPAGE)
    LTsv_global_widgetltsv(LTsv_widgetLTSV)

def LTsv_kbdentry_gettext(kbdentry_canvas):
    return LTsv_kbdentry_text[kbdentry_canvas]

def LTsv_kbdentry_evaltext(calc_value=""):
    global LTsv_glyph_worddicname,LTsv_glyph_zipdicname,LTsv_glyph_worddic,LTsv_glyph_zipdic
    calc_V,calc_K,calc_Q,calc_A=calc_value,"","",""
    if len(calc_V) == 0:
        LTsv_glyph_kbdselect('Σ')
    elif calc_V.find('⇔') < 0:
        calc_V+='⇔'
    if calc_V.find('⇔') == 0:
        if calc_V[:2] == "⇔⇔":
            calc_Q=calc_V[0]
            calc_A=LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_Q),LTsv_glyph_kbdchars[LTsv_glyph_SandS])
            if len(calc_A) > 0:
                calc_K=LTsv_glyph_kbdchars[LTsv_glyph_SandS]
            else:
                calc_K,calc_A="照",""
        else:
            if len(calc_V) == 1:
                if len(LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_V[0]),LTsv_glyph_kbdchars[LTsv_glyph_SandS])) > 0:
                    calc_K,calc_Q=LTsv_glyph_kbdchars[LTsv_glyph_SandS],calc_V[0]
                else:
                    calc_K,calc_Q="照",calc_V[0]
            else:
                calc_K,calc_Q="算",""
    elif calc_V.find('⇔') == 1:
        calc_Q=calc_V[0]
        if len(calc_V) > 2:
            if calc_V[2] == ('⇔'):
                if calc_Q in LTsv_glyph_evaltype or calc_Q in LTsv_glyph_dictype:
                    calc_K=calc_Q
        if calc_K == "":
            calc_A=LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_Q),LTsv_glyph_kbdchars[LTsv_glyph_SandS])
            if len(calc_A) > 0:
                calc_K=LTsv_glyph_kbdchars[LTsv_glyph_SandS]
            else:
                calc_K,calc_A="照",""
        LTsv_glyph_kbdfind(calc_Q)
    elif calc_V.find('⇔') == 2:
        if calc_V[0] in LTsv_glyph_evaltype or calc_V[0] in LTsv_glyph_dictype:
            calc_K,calc_Q=calc_V[0],calc_V[1]
        else:
            calc_K,calc_Q="汎",calc_V[:2]
    else:
        if len(calc_V) > 0:
            calc_Q=calc_V[:calc_V.find('⇔')]
            if (calc_Q.startswith("&#") or calc_Q.startswith("&")) and calc_Q.endswith(";"):
                calc_K="照"
            elif calc_Q[0] in LTsv_glyph_evaltype:
                calc_K,calc_Q=calc_Q[0],calc_Q[1:]
            else:
                calc_K="汎"
    if calc_K == "全":
        calc_K="￥" if LTsv_glyph_evalslash == "￥" else "＼"
    if calc_K == "濁":
        calc_K="Ｐ" if LTsv_glyph_evaldakuon == "Ｐ" else "Ｂ"
    if calc_K == "清":
        calc_K="Ｈ" if LTsv_glyph_evalseion == "Ｈ" else "Ｍ"
    if calc_K in LTsv_glyph_dictype:
        calc_A=LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_Q),calc_K)
    elif calc_K == "平":
        calc_A=LTsv_kanare(calc_Q,"Kata2Hira")
    elif calc_K == "片":
        calc_A=LTsv_kanare(calc_Q,"Hira2Kata")
    elif calc_K == "大":
        calc_A=LTsv_kanare(calc_Q,"Alpha2BIG")
    elif calc_K == "小":
        calc_A=LTsv_kanare(calc_Q,"Alpha2SML")
    elif calc_K == "半":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2HanKaKe"); calc_A=LTsv_kanare(calc_A,"Alpha2HAN")
    elif calc_K == "＼":
        calc_A=LTsv_kanare(calc_Q,"Han2Kata");         calc_A=LTsv_kanare(calc_A,"Alpha2ZENBS")
    elif calc_K == "￥":
        calc_A=LTsv_kanare(calc_Q,"Han2Kata");         calc_A=LTsv_kanare(calc_A,"Alpha2ZENYen")
    elif calc_K == "Ｈ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2SeiH")
    elif calc_K == "Ｍ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2SeiM")
    elif calc_K == "Ｂ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2DakB")
    elif calc_K == "Ｐ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2DakP")
    elif calc_K == "⑩":
        calc_A=str(LTsv_intstr0x(calc_Q))
    elif calc_K == "⑯":
        calc_A=hex(LTsv_intstr0x(calc_Q.lstrip('0x').strip('$')))
    elif calc_K == "⑧":
        calc_A=LTsv_utf2ink(calc_Q)
    elif calc_K == "⓪":
        calc_A=LTsv_ink2utf(calc_Q)
    elif calc_K == "照":
        if (calc_Q.startswith("&#") or calc_Q.startswith("&")) and calc_Q.endswith(";"):
            calc_A=LTsv_xml2utf(calc_Q)
        else:
            calc_A=LTsv_utf2xml(calc_Q)
    elif calc_K == "探":
        for calc_F in calc_Q:
            calc_EX=""
            calc_EXdic=LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_F),'異')+ \
              LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_F),'簡')+ \
              LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_F),'繁')+ \
              LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,calc_F),'代')
            for calc_e in calc_EXdic:
                calc_EX=calc_EX if ord(calc_e) < 128 else calc_EX+calc_e
            if LTsv_glyph_kbdfind(calc_F) >= 0:
                calc_A=calc_F
                break
    elif calc_K == "今":
        LTsv_putdaytimenow(overhour=LTsv_glyph_overhour)
        calc_Q=calc_Q.replace("今",LTsv_glyph_now)
        calc_Q=calc_Q.replace("干","@yzj").replace("年","@000y").replace("月","@0m").replace("日","@0dm").replace("週","@0wnyi").replace("曜","@wdj").replace("時","@0h").replace("分","@0n").replace("秒","@0s")
        calc_Q=calc_Q.replace("版",LTsv_file_ver())
        calc_Q=calc_Q.replace("枝",LTsv_glyph_branch)
        calc_A=LTsv_getdaytimestr(calc_Q)
    elif calc_K == "〒":
        if len(LTsv_glyph_zipdic) == 0:
            LTsv_glyph_zipdic=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_zipdicname))
        calc_Q=LTsv_kanare(calc_Q,"HiraKana2HanKaKe"); calc_Q=LTsv_kanare(calc_Q,"Alpha2HAN")
        calc_Q=(calc_Q.replace('-','').replace('ｰ','')+'0'*7)[:7]
        calc_A=LTsv_readlinerest(LTsv_glyph_zipdic,calc_Q)
    elif calc_K == "汎":
        if len(LTsv_glyph_worddic) == 0:
            LTsv_glyph_worddic=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_worddicname))
        calc_A=LTsv_readlinerest(LTsv_glyph_worddic,calc_Q)
        if calc_A == "":
            calc_A=LTsv_readlinerest(LTsv_glyph_worddic,LTsv_kanare(calc_Q,"Kata2Hira"))
            calc_Q=LTsv_kanare(calc_Q,"Kata2Hira") if calc_A != "" else calc_Q
        if calc_A == "":
            calc_A=LTsv_readlinerest(LTsv_glyph_worddic,LTsv_kanare(calc_Q,"Hira2Kata"))
            calc_Q=LTsv_kanare(calc_Q,"Kata2Hira") if calc_A != "" else calc_Q
        if calc_A == "":
            calc_K="算"
    if calc_K == "算":
        calc_A=LTsv_calc(calc_Q)
    if calc_K != "":
        calc_V="{0}{1}⇔{2}".format(calc_K,calc_Q,calc_A)
    LTsv_libc_printf(calc_V)
    return calc_V

def debug_mousepress(window_objvoid=None,window_objptr=None):
    if LTsv_glyph_mousepress(debug_reversi_canvas,debug_kbdX,debug_kbdY) == LTsv_global_kbdcursorNone():
        keyboard_mouseX,keyboard_mouseY=min(max(LTsv_global_canvasmotionX(),0),debug_reversi_W),min(max(LTsv_global_canvasmotionY(),0),debug_reversi_H)
        if debug_milklidX[11] < keyboard_mouseX < debug_milklidX[99] and debug_milklidY[11] < keyboard_mouseY < debug_milklidY[99]:
            for xy in debug_milklid_range:
                if debug_milklidX[xy] < keyboard_mouseX < debug_milklidX[xy+1] and debug_milklidY[xy] < keyboard_mouseY < debug_milklidY[xy+10]:
                    debug_milkAI_add(debug_reversi_key[xy])

def debug_mousemotion(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mousemotion(debug_reversi_canvas,debug_kbdX,debug_kbdY)

def debug_mouserelease(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mouserelease(debug_reversi_canvas,debug_kbdX,debug_kbdY)

def debug_milklid_check(xy,bw):
    milkcount,milkcountall=0,0
    if debug_milkMAP[xy] == 0:
        for v in debug_milklidV:
            milkcount=0; oxy=xy+v
            while debug_milkMAP[oxy] == debug_milklidBWswitch[bw]:
                milkcount+=1; oxy+=v
            if debug_milkMAP[oxy] == bw:
                milkcountall+=milkcount
    return milkcountall

def debug_milklid_turn(xy,bw):
    for v in debug_milklidV:
        milklist=[]; oxy=xy+v
        while debug_milkMAP[oxy] == debug_milklidBWswitch[bw]:
            milklist.append(oxy); oxy+=v
        if debug_milkMAP[oxy] == bw:
            for t in milklist:
                debug_milkMAP[t]=bw
    debug_milkMAP[xy]=bw

def debug_milkAI_BS(window_objvoid=None,window_objptr=None):
    reversi_entry=LTsv_widget_gettext(debug_reversi_entry)
    reversi_entry=reversi_entry[:len(reversi_entry)-1] if len(reversi_entry) > 0 else ""
    LTsv_widget_settext(debug_reversi_entry,reversi_entry)
    debug_milkAI_entry()

def debug_milkAI_reset():
    global debug_milkAI,debug_milkMAP,debug_milklidBW,debug_milklidBWwait
    debug_milkAI=list(range(debug_milklidLen)); random.shuffle(debug_milkAI)
    for xy in [11,18,81,88]: debug_milkAI[xy]+=900;
    for xy in [13,16,31,38,61,68,83,86]: debug_milkAI[xy]+=800;
    for xy in [33,36,63,66]: debug_milkAI[xy]+=700;
    for xy in [34,35,43,46,53,56,64,65]: debug_milkAI[xy]+=600;
    for xy in [14,15,41,48,51,58,84,85]: debug_milkAI[xy]+=500;
    for xy in [23,26,32,37,62,67,73,76]: debug_milkAI[xy]+=400;
    for xy in [24,25,42,47,52,57,74,75]: debug_milkAI[xy]+=300;
    for xy in [12,17,21,28,71,78,82,87]: debug_milkAI[xy]+=200;
    for xy in [22,27,72,77]: debug_milkAI[xy]+=100;

debug_reversi_entrysavedata=""
def debug_milkAI_entry(window_objvoid=None,window_objptr=None):
    global debug_milkAI,debug_milkMAP,debug_milklidBW,debug_milklidBWwait
    global debug_reversi_entrysavedata
    reversi_entry=LTsv_widget_gettext(debug_reversi_entry)
    reversi_entry=reversi_entry[:60]
    if len(reversi_entry) == 0:
        debug_milkAI_reset()
    debug_milkMAP=[0 for xy in range(debug_milklidLen)]
    for xy in [45,54]: debug_milkMAP[xy]=debug_milklidBWswitch[0];
    for xy in [44,55]: debug_milkMAP[xy]=debug_milklidBWswitch[1];
    debug_milklidBW=debug_milklidBWswitch[0]
    for bw in range(2):
        debug_milklidBWwait[debug_milklidBWswitch[bw]]=1 if debug_milklidBWswitch[bw] == debug_milklidBW else 0
    for entrylen,entryxy in enumerate(reversi_entry):
        if entryxy in debug_reversi_key:
            if debug_milklid_check(debug_reversi_key.index(entryxy),debug_milklidBW) == 0:
                reversi_entry=reversi_entry[:entrylen]
                break
            debug_milklid_turn(debug_reversi_key.index(entryxy),debug_milklidBW)
            debug_milklidBW=debug_milklidBWswitch[debug_milklidBW]
            milkcounttotal=0
            for xy in debug_milklid_range:
                milkcounttotal+=debug_milklid_check(xy,debug_milklidBW)
            if milkcounttotal == 0:
                debug_milklidBW=debug_milklidBWswitch[debug_milklidBW]
                for bw in range(2):
                    debug_milklidBWwait[debug_milklidBWswitch[bw]]=1 if debug_milklidBWswitch[bw] == debug_milklidBW else 2
                milkcounttotal=0
                for xy in debug_milklid_range:
                    milkcounttotal+=debug_milklid_check(xy,debug_milklidBW)
                if milkcounttotal == 0:
                    debug_milklidBWwait[debug_milklidBW],debug_milklidBWwait[debug_milklidBWswitch[debug_milklidBW]]=3,4
            else:
                for bw in range(2):
                    debug_milklidBWwait[debug_milklidBWswitch[bw]]=1 if debug_milklidBWswitch[bw] == debug_milklidBW else 0
        else:
            reversi_entry=reversi_entry[:entrylen]
            break
    LTsv_widget_settext(debug_reversi_entry,reversi_entry)
    debug_reversi_entrysavedata=reversi_entry
    LTsv_glyph_kbddelete(debug_reversi_canvas)
    LTsv_draw_selcanvas(debug_reversi_canvas)
    LTsv_draw_delete()
    LTsv_draw_color(debug_milklid_colordic["back"]); LTsv_draw_polygonfill(0,0,debug_reversi_W,0,debug_reversi_W,debug_reversi_H,0,debug_reversi_H)
    LTsv_draw_color(debug_milklid_colordic["green"]); LTsv_draw_polygonfill(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_font(debug_milkfont)
    LTsv_draw_bgcolor(debug_milklid_colordic["green"])
    for xy in debug_milklid_range:
        if debug_milklid_check(xy,debug_milklidBW) > 0:
            LTsv_draw_color(debug_milklid_colordic["next"])
            LTsv_draw_glyphs(draw_t=debug_reversi_key[xy],draw_x=debug_milklidX[xy]+debug_kbdH//8,draw_y=debug_milklidY[xy]+debug_kbdH//8,draw_f=debug_kbdH*2//3,draw_g="漫")
        else:
            LTsv_draw_color(debug_milklid_colordic[debug_milklid_colorkey[debug_milkMAP[xy]]])
            LTsv_draw_glyphsfill(draw_t=debug_reversi_key[xy],draw_x=debug_milklidX[xy]+debug_kbdH//8,draw_y=debug_milklidY[xy]+debug_kbdH//8,draw_f=debug_kbdH*2//3,draw_g="漫")
    LTsv_draw_color(debug_milklid_colordic["line"])
    LTsv_draw_polygon(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_polygon(debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_squaresfill(6,debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_bgcolor(debug_milklid_colordic["back"])
    for bw in range(2):
        milklidcount=0
        for xy in debug_milklid_range:
            milklidcount=milklidcount+1 if debug_milkMAP[xy] == debug_milklidBWswitch[bw] else milklidcount
        LTsv_draw_glyphsfill(draw_t="{0}\n{1:02}\n\n{2}".format(debug_milklidBWstone[debug_milklidBWswitch[bw]],milklidcount,debug_milklidBWwaitname[debug_milklidBWwait[debug_milklidBWswitch[bw]]]),draw_x=debug_milklidBWstatusX[debug_milklidBWswitch[bw]],draw_y=debug_milklidY[20],draw_f=debug_kbdH//2,draw_g="漫")
    LTsv_glyph_kbddraw(debug_reversi_canvas,debug_kbdX,debug_kbdY)
    LTsv_draw_queue()

def debug_milkAI_Auto(window_objvoid=None,window_objptr=None):
    milklist=[0]
    for xy in debug_milklid_range:
        if debug_milklid_check(xy,debug_milklidBW) > 0:
            milklist.append(xy)
    milkAIdic={}
    for key in milklist:
        milkAIdic[str(key)]=debug_milkAI[key]
    milkAImax=max(milkAIdic.items(),key=lambda d:d[1])[0]
    debug_milkAI_add(debug_reversi_key[int(milkAImax)])

def debug_milkAI_add(addentry):
    addentrychar=addentry[:1]
    reversi_entry=LTsv_widget_gettext(debug_reversi_entry)
    milkcounttotal=0
    for xy in debug_milklid_range:
        milkcounttotal+=debug_milklid_check(xy,debug_milklidBW)
    if addentrychar == "\uf0d1": #
        debug_milkAI_BS(); return;
    if addentrychar == "\uf0d3": #
        debug_milkAI_Auto(); return;
    if milkcounttotal > 0:
        if addentrychar in debug_reversi_key and addentrychar != debug_reversi_key[0]:
            if debug_milklid_check(debug_reversi_key.index(addentrychar),debug_milklidBW) > 0:
                reversi_entry="{0}{1}".format(reversi_entry,addentrychar) if len(reversi_entry) < 60 else ""
    else:
        reversi_entry=""
    LTsv_widget_settext(debug_reversi_entry,reversi_entry)
    debug_milkAI_entry()

def debug_configload():
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    LTsv_glyph_ltsv=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_ltsvpath))
    debug_config=LTsv_getpage(LTsv_glyph_ltsv,"reversi")
    debug_reversi_entrysavedata=LTsv_readlinerest(debug_config,"entry")
    LTsv_widget_settext(debug_reversi_entry,debug_reversi_entrysavedata)

def debug_configsave_exit(window_objvoid=None,window_objptr=None):
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    LTsv_glyph_ltsv=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_ltsvpath))
    debug_config=LTsv_getpage(LTsv_glyph_ltsv,"reversi")
    debug_config=LTsv_pushlinerest(debug_config,"entry",debug_reversi_entrysavedata)
    LTsv_glyph_ltsv=LTsv_putpage(LTsv_glyph_ltsv,"reversi",debug_config)
    LTsv_savefile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_ltsvpath),LTsv_glyph_ltsv)
    LTsv_glyph_picklesave()
    LTsv_window_exit()

if __name__=="__main__":
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
    if len(LTsv_GUI) > 0:
        import random
        LTsv_glyph_kbdinit(ltsvpath="./kanglyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=None)
        debug_kbdH=25
        debug_milklid_W,debug_milklid_H=debug_kbdH,debug_kbdH
        debug_milkfont="kan5x5comic,{0}".format(debug_kbdH//2)
        debug_entryfont="kan5x5comic,{0}".format(debug_kbdH//4)
        debug_buttonfont="kan5x5comic,5".format(5)
        debug_reversi_X,debug_reversi_Y,debug_reversi_W,debug_reversi_H=debug_milklid_W*7,debug_milklid_H*1,debug_milklid_W*(2+20+2),debug_milklid_H*(2+8+2)
        debug_kbdX,debug_kbdY=debug_reversi_W-LTsv_global_glyphkbdW(),debug_reversi_H-LTsv_global_glyphkbdH()*3//2
        debug_milklidLen=(10*10)
        debug_milklidX,debug_milklidY,debug_milkAI,debug_milkMAP=[0]*debug_milklidLen,[0]*debug_milklidLen,[0]*debug_milklidLen,[0]*debug_milklidLen
        for xy in range(debug_milklidLen):
            debug_milklidX[xy],debug_milklidY[xy]=debug_reversi_X+debug_milklid_W*(xy%(1+8+1)),debug_reversi_Y+debug_milklid_H*(xy//(1+8+1))
        debug_reversi_key="　　　　　　　　　　" \
          "　ＡＢＣＤＥＦＧＨ　" \
          "　ＩＪＫＬＭＮＯＰ　" \
          "　ＱＲＳＴＵＶＷＸ　" \
          "　ＹＺ０１２３４５　" \
          "　６７８９＿．ａｂ　" \
          "　ｃｄｅｆｇｈｉｊ　" \
          "　ｋｌｍｎｏｐｑｒ　" \
          "　ｓｔｕｖｗｘｙｚ　" \
          "　　　　　　　　　　"
        debug_milklidV=[+1,+9,+10,+11,-1,-9,-10,-11]
        debug_milklidBWswitch=[1,2,1]
        debug_milklidBW=debug_milklidBWswitch[0]
        debug_milklidBWstone=["","●","○"]
        debug_milklidBWstatusX=[0,debug_milklidX[20]-debug_milklid_W,debug_milklidX[29]+debug_milklid_W]
        debug_milklidBWwait=[0,0,0]
        debug_milklidBWwaitname=["　\n　\n　\n　","Ｔ\nＵ\nＲ\nＮ","Ｐ\nＡ\nＳ\nＳ","Ｗ\nＩ\nＮ\n　","Ｌ\nＯ\nＳ\nＥ"]
        debug_milklid_range=[y*10+x for y in range(1,9) for x in range(1,9)]
        debug_milklid_colorkey=["green","black","white","back","line","nexr"]
        debug_milklid_colordic={"green":"#76DC76","black":"#4E4E4E","white":"#FFF5FD","back":"#F1F1F1","line":"#00918F","next":"#FFD7F3"}
        debug_reversi_window=LTsv_window_new(widget_t="reversi",event_b=debug_configsave_exit,widget_w=debug_reversi_W,widget_h=debug_reversi_H+debug_milklid_H//2,event_z=None)
        debug_reversi_back=LTsv_button_new(debug_reversi_window,widget_t="BS",widget_x=0,widget_y=debug_reversi_H,widget_w=debug_milklid_W*1,widget_h=debug_milklid_H//2,widget_f=debug_buttonfont,event_b=debug_milkAI_BS)
        debug_reversi_entry=LTsv_entry_new(debug_reversi_window,widget_t="",widget_x=debug_milklid_W*1,widget_y=debug_reversi_H,widget_w=debug_reversi_W-debug_milklid_W*3,widget_h=debug_milklid_H//2,widget_f=debug_entryfont,event_b=debug_milkAI_entry)
        debug_reversi_button=LTsv_button_new(debug_reversi_window,widget_t="Auto",widget_x=debug_reversi_W-debug_milklid_W*2,widget_y=debug_reversi_H,widget_w=debug_milklid_W*2,widget_h=debug_milklid_H//2,widget_f=debug_buttonfont,event_b=debug_milkAI_Auto)
        debug_reversi_canvas=LTsv_canvas_new(debug_reversi_window,widget_x=0,widget_y=0,widget_w=debug_reversi_W,widget_h=debug_reversi_H,
         event_p=debug_mousepress,event_m=debug_mousemotion,event_r=debug_mouserelease,event_w=50)
        LTsv_widget_showhide(debug_reversi_window,True)
        LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
        LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
        LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
        LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
        LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
        LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
        LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
        LTsv_glyph_tapcallback_shell(debug_reversi_canvas,debug_milkAI_add)
        debug_milkAI_reset()
        debug_configload()
        debug_milkAI_entry()
        LTsv_window_main(debug_reversi_window)
    else:
        LTsv_libc_printf("GUIの設定に失敗しました。")
    print("")
    print("__main__",LTsv_file_ver())

# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
