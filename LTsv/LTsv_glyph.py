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
from LTsv_gui    import *

LTsv_PSfont_ZW,LTsv_PSfont_CW,LTsv_PSchar_ZW,LTsv_PSchar_CW=1024,624,1000,600
LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide={},{},{}
LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide={},{},{}
LTsv_glyph_ltsvdir,LTsv_glyph_ltsvpath,LTsv_glyph_kandicname,LTsv_glyph_kanmapname,LTsv_glyph_kanpickleGTKname,LTsv_glyph_kanpickleTkintername="LTsv/","","kanchar.tsv","kanmap.tsv","kanpickleGTK.bin","kanpickleTkinter.bin"
LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanmap,LTsv_glyph_kanpickle="","","",{}
LTsv_glyph_irohatype= ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","゛","゜","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
LTsv_glyph_irohatypeN=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
LTsv_glyph_irohatypeX=["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ","｜"]
LTsv_glyph_alphatype= ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
LTsv_glyph_alphatypeN=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
LTsv_glyph_alphatypeX=["Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω","●","▲","■"]
LTsv_glyph_dictype=    ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","漫","幅"]
LTsv_glyph_choice=    ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
LTsv_glyph_choiceN=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
LTsv_glyph_choiceX=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","Ε","Ρ","Τ","Υ","Θ","Ι","Ο","Π","｀","プ","Α","Σ","Δ","Φ","Γ","Η","Ξ","Κ","Λ","代","鍵","ぬ","Ζ","Χ","Ψ","Ω","Β","Ν","Μ","熙","●","▲","■","￥","Σ"]
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
LTsv_glyph_kbdLCR=""
LTsv_glyph_kbdfontcolor,LTsv_glyph_kbdbgcolor="black","#CFE6CF"
LTsv_glyph_kbdsize=1
LTsv_chrcode=chr if sys.version_info.major == 3 else unichr
LTsv_draw_color,LTsv_draw_bgcolor=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI)
LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
LTsv_glyphSVG=None
def LTsv_glyph_kbdinit(ltsvpath="kanglyph.tsv",LTsv_glyph_kbddefsize=None):
    global LTsv_glyph_ltsvdir,LTsv_glyph_ltsvpath,LTsv_glyph_kandicname,LTsv_glyph_kanmapname,LTsv_glyph_kanpickleGTKname,LTsv_glyph_kanpickleTkintername
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide
    global LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide
    global LTsv_glyph_irohatype,LTsv_glyph_irohatypeN,LTsv_glyph_irohatypeX
    global LTsv_glyph_alphatype,LTsv_glyph_alphatypeN,LTsv_glyph_alphatypeX
    global LTsv_glyph_dictype
    global LTsv_glyph_choice,LTsv_glyph_choiceN,LTsv_glyph_choiceX
    global LTsv_glyph_irohaalpha,LTsv_glyph_irohaalphaN,LTsv_glyph_irohaalphaX
    global LTsv_glyph_kanmapN,LTsv_glyph_kanmapX
    global LTsv_glyph_kbdF,LTsv_glyph_kbdH,LTsv_glyph_kbdW,LTsv_glyph_kbdG,LTsv_glyph_kbdC
    global LTsv_glyph_fontX,LTsv_glyph_fontY,LTsv_glyph_fontG,LTsv_glyph_mouseX,LTsv_glyph_mouseY,LTsv_glyph_mouseC
    global LTsv_glyph_kbdchars
    global LTsv_glyph_kbdLCR
    global LTsv_glyph_kbdTAG,LTsv_glyph_kbdfontcolor,LTsv_glyph_kbdbgcolor
    global LTsv_draw_color,LTsv_draw_bgcolor
    global LTsv_glyph_kbdsize
    global LTsv_draw_polygon,LTsv_draw_polygonfill
    global LTsv_glyphSVG
    LTsv_glyph_ltsvdir=os.path.normpath(os.path.dirname(LTsv_glyph_ltsvpath))+"/"
    LTsv_glyph_ltsvpath=ltsvpath
    LTsv_glyph_ltsv=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_ltsvpath))
    LTsv_glyph_config=LTsv_getpage(LTsv_glyph_ltsv,"kanglyph")
    LTsv_glyph_kandicname=LTsv_readlinerest(LTsv_glyph_config,"dicname",LTsv_glyph_kandicname)
    LTsv_glyph_kandic=LTsv_loadfile(LTsv_glyph_kandicname)
    LTsv_glyph_kanmapname=LTsv_readlinerest(LTsv_glyph_config,"mapname",LTsv_glyph_kanmapname)
    LTsv_glyph_kanmap=LTsv_loadfile(LTsv_glyph_kanmapname)
    LTsv_draw_color,LTsv_draw_bgcolor=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_glyphSVG=LTsv_glyphSVG_shell(LTsv_GUI)
    if LTsv_global_GUI() == "GTK2":
        LTsv_glyph_kanpickleGTKname=LTsv_readlinerest(LTsv_glyph_config,"pickleGTKname",LTsv_glyph_kanpickleGTKname)
        if os.path.isfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpickleGTKname)):
            with open(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpickleGTKname),mode='rb') as pickle_fobj:
                LTsv_glyph_kanpickle=pickle.load(pickle_fobj)
            LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide,LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide=LTsv_glyph_kanpickle
    if LTsv_global_GUI() == "Tkinter":
        LTsv_glyph_kanpickleTkintername=LTsv_readlinerest(LTsv_glyph_config,"pickleTkintername",LTsv_glyph_kanpickleTkintername)
        if os.path.isfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpickleTkintername)):
            with open(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpickleTkintername),mode='rb') as pickle_fobj:
                LTsv_glyph_kanpickle=pickle.load(pickle_fobj)
            LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide,LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide=LTsv_glyph_kanpickle
    LTsv_glyph_irohatype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"irohatype",LTsv_tuple2tsv(LTsv_glyph_irohatype)))
    LTsv_glyph_irohatypeN=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"irohatypeN",LTsv_tuple2tsv(LTsv_glyph_irohatypeN)))
    LTsv_glyph_irohatypeX=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"irohatypeX",LTsv_tuple2tsv(LTsv_glyph_irohatypeX)))
    LTsv_glyph_alphatype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"alphatype",LTsv_tuple2tsv(LTsv_glyph_alphatype)))
    LTsv_glyph_alphatypeN=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"alphatypeN",LTsv_tuple2tsv(LTsv_glyph_alphatypeN)))
    LTsv_glyph_alphatypeX=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"alphatypeX",LTsv_tuple2tsv(LTsv_glyph_alphatypeX)))
    LTsv_glyph_dictype=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"dictype",LTsv_tuple2tsv(LTsv_glyph_dictype)))
    LTsv_glyph_choice=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"choice",LTsv_tuple2tsv(LTsv_glyph_choice)))
    LTsv_glyph_choiceN=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"choiceN",LTsv_tuple2tsv(LTsv_glyph_choiceN)))
    LTsv_glyph_choiceX=LTsv_tsv2list(LTsv_readlinerest(LTsv_glyph_config,"choiceX",LTsv_tuple2tsv(LTsv_glyph_choiceX)))
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
    LTsv_glyph_kbdselect('＠')

def LTsv_global_kandic():                              return LTsv_glyph_kandic
def LTsv_global_kanmap():                              return LTsv_glyph_kanmap
def LTsv_global_kanpickle():                          return LTsv_glyph_kanpickle
def LTsv_global_irohatype():                          return LTsv_glyph_irohatype
def LTsv_global_irohatypeN():                         return LTsv_glyph_irohatypeN
def LTsv_global_irohatypeX():                         return LTsv_glyph_irohatypeX
def LTsv_global_alphatype():                          return LTsv_glyph_alphatype
def LTsv_global_alphatypeN():                         return LTsv_glyph_alphatypeN
def LTsv_global_alphatypeX():                         return LTsv_glyph_alphatypeX
def LTsv_global_dictype():                             return LTsv_glyph_dictype
def LTsv_global_choice():                              return LTsv_glyph_choice
def LTsv_global_choiceN():                             return LTsv_glyph_choiceN
def LTsv_global_choiceX():                             return LTsv_glyph_choiceX
def LTsv_global_irohaalpha():                            return LTsv_glyph_irohaalpha
def LTsv_global_irohaalphaN():                           return LTsv_glyph_irohaalphaN
def LTsv_global_irohaalphaX():                           return LTsv_glyph_irohaalphaX
def LTsv_global_glyphkbdH():                           return LTsv_glyph_kbdH
def LTsv_global_glyphkbdW():                           return LTsv_glyph_kbdW
def LTsv_global_kbdcursorNone():                           return LTsv_glyph_None

def LTsv_glyphSVGGTK(LTsv_glyph_path):
    LTsv_glyph_pathZ=LTsv_glyph_path.strip(' ').replace('Z','z').rstrip('z').split('z') if len(LTsv_glyph_path) else []
    LTsv_glyphnote,LTsv_glyphclock=[],[]
    for LTsv_glyphline in LTsv_glyph_pathZ:
        LTsv_glyphdata=LTsv_glyphline.split(' '); LTsv_glyphpointlist=[]
        for LTsv_glyphpoint in LTsv_glyphdata:
            if LTsv_glyphpoint.count(',') != 1: continue;
            LTsv_glyphpoints=LTsv_glyphpoint.strip(' ').split(',')
#            LTsv_glyphpointlist+=[int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0]
#            LTsv_glyphpointlist+=[(LTsv_PSchar_ZW-int(LTsv_glyphpoints[1])) if LTsv_glyphpoints[1].isdigit() else 0]
            LTsv_glyphpoint98=int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0
            LTsv_glyphpoint98=LTsv_glyphpoint98 if LTsv_glyphpoint98 % 100 != 98 else LTsv_glyphpoint98+2
            LTsv_glyphpointlist+=[LTsv_glyphpoint98]
            LTsv_glyphpoint98=int(LTsv_glyphpoints[1]) if LTsv_glyphpoints[1].isdigit() else 0
            LTsv_glyphpoint98=LTsv_glyphpoint98 if LTsv_glyphpoint98 % 100 != 2 else LTsv_glyphpoint98-2
            LTsv_glyphpointlist+=[LTsv_PSchar_ZW-LTsv_glyphpoint98]
        LTsv_glyphnote.append(LTsv_glyphpointlist); LTsv_glyphclock.append(LTsv_clockwise(*tuple(LTsv_glyphpointlist)))
    return LTsv_glyphnote,LTsv_glyphclock

def LTsv_glyphSVGTkinter(LTsv_glyph_path):
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

def LTsv_glyphSVG_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_glyphSVGGTK
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_glyphSVGTkinter

def LTsv_glyphpath(glyphcode):
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide
    global LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
    LTsv_glyph_wide=LTsv_pickdatalabel(LTsv_glyph_kanline,"幅"); LTsv_glyph5x5_wide[glyphcode]=int(LTsv_glyph_wide) if len(LTsv_glyph_wide) else LTsv_PSfont_ZW
    LTsv_glyphcomic_wide[glyphcode]=LTsv_glyph5x5_wide[glyphcode]
    LTsv_glyph_path5x5=LTsv_pickdatalabel(LTsv_glyph_kanline,"活")
    LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]=LTsv_glyphSVG(LTsv_glyph_path5x5)
    LTsv_glyph_pathcomic=LTsv_pickdatalabel(LTsv_glyph_kanline,"漫")
    LTsv_glyphcomic_coord[glyphcode],LTsv_glyphcomic_clock[glyphcode]=LTsv_glyphSVG(LTsv_glyph_path5x5) if len(LTsv_glyph_pathcomic) else LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]

def LTsv_glyphfont_5x5(glyphcode):
    return LTsv_glyph5x5_coord[glyphcode],LTsv_glyph5x5_clock[glyphcode]

def LTsv_glyphfont_comic(glyphcode):
    return LTsv_glyphcomic_coord[glyphcode],LTsv_glyphcomic_clock[glyphcode]

def LTsv_glyphfont_shell(draw_g="活"):
    if draw_g == "活": return LTsv_glyphfont_5x5
    if draw_g == "漫": return LTsv_glyphfont_comic

def LTsv_draw_glyphs(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_g="活",draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide
    global LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide
    draw_xf,draw_yf=draw_x,draw_y
    draw_tf=draw_t if draw_LF == False else draw_tf.replace('\n',"")
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
        if not glyphcode in LTsv_glyph5x5_coord:
            LTsv_glyphpath(glyphcode)
        LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_draw_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_glyph5x5_wide[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_draw_glyphsfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_g="活",draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide
    global LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide
    draw_xf,draw_yf=draw_x,draw_y
    draw_tf=draw_t if draw_LF == False else draw_tf.replace('\n',"")
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
        if not glyphcode in LTsv_glyph5x5_coord:
            LTsv_glyphpath(glyphcode)
        LTsv_glyphnote,LTsv_clocknote=LTsv_glyphfont(glyphcode)
        for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
            if LTsv_clocknote[LTsv_glyphpointlist_count] > 0:
                 LTsv_draw_color(canvascolor)
            else:
                 LTsv_draw_color(canvasbgcolor)
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_draw_polygonfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_glyph5x5_wide[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w
    LTsv_draw_color(canvascolor); LTsv_draw_bgcolor(canvasbgcolor)

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

LTsv_glyph_tapcallback=None
def LTsv_glyph_tapcallback_shell(callback):
    global LTsv_glyph_tapcallback
    LTsv_glyph_tapcallback=callback

def LTsv_getdic(LTsv_text,LTsv_first,LTsv_label):
    LTsv_data=""
    LTsv_page='\n'+LTsv_text+'\n'
    LTsv_tagL='\n'+LTsv_first+'\t'; LTsv_posL=LTsv_page.find(LTsv_tagL)
    if 0 <= LTsv_posL:
        LTsv_rest='\t'+LTsv_page[LTsv_posL+len(LTsv_tagL):LTsv_page.find('\n',LTsv_posL+1)]+'\t'
        LTsv_tagR='\t'+LTsv_label+":"; LTsv_posR=LTsv_rest.find(LTsv_tagR)
        if 0 <= LTsv_posR:
            LTsv_data=LTsv_rest[LTsv_posR+len(LTsv_tagR):LTsv_rest.find('\t',LTsv_posR+1)]
    return LTsv_data

def LTsv_glyph_mousepress(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_kbdLCR
    LTsv_kbdcursor=LTsv_glyph_kbdcursor(kbd_canvas,kbd_x,kbd_y)
    if LTsv_kbdcursor < LTsv_glyph_None:
        LTsv_glyph_kbddelete(kbd_canvas,debug_kbdX,debug_kbdY)
        if LTsv_kbdcursor == LTsv_glyph_SandS:
            LTsv_glyph_kbdLCR="FlickS"
            LTsv_glyph_kbdchar_SandS=LTsv_glyph_kbdchars[LTsv_glyph_SandS]
#            for kbd_xy,kbd_c in enumerate(LTsv_glyph_kbdchars[:LTsv_glyph_irohamax]):
#                LTsv_glyph_kbdchars[kbd_xy]=LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,kbd_c),LTsv_glyph_kbdchar_SandS)[:1]
            LTsv_glyph_kbdchars[:LTsv_glyph_irohamax]=[LTsv_getdic(LTsv_glyph_kandic,kbd_c,LTsv_glyph_kbdchar_SandS)[:1] for kbd_c in LTsv_glyph_kbdchars[:LTsv_glyph_irohamax]]
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
            if LTsv_glyph_tapcallback != None:
                LTsv_glyph_tapcallback(LTsv_glyph_kbdchars[LTsv_kbdcursor])
        LTsv_glyph_kbddraw(debug_reversi_canvas,debug_kbdX,debug_kbdY)
        LTsv_draw_queue()

def LTsv_glyph_mousemotion(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_kbdLCR
    LTsv_kbdcursor=LTsv_glyph_kbdcursor(kbd_canvas,kbd_x,kbd_y)
    if LTsv_kbdcursor < LTsv_glyph_None:
        LTsv_glyph_kbddelete(kbd_canvas,debug_kbdX,debug_kbdY)
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
        LTsv_glyph_kbddraw(debug_reversi_canvas,debug_kbdX,debug_kbdY)
        LTsv_draw_queue()

def LTsv_glyph_mouserelease(kbd_canvas,kbd_x,kbd_y):
    global LTsv_glyph_kbdLCR
    LTsv_kbdcursor=LTsv_glyph_kbdcursor(kbd_canvas,kbd_x,kbd_y)
    if LTsv_kbdcursor < LTsv_glyph_None:
        LTsv_glyph_kbddelete(kbd_canvas,debug_kbdX,debug_kbdY)
        if LTsv_glyph_kbdLCR == "SwipeK":
            if LTsv_glyph_kbdchars[LTsv_kbdcursor] in LTsv_glyph_dictype:
                LTsv_glyph_kbdchars[LTsv_glyph_SandS]=LTsv_glyph_kbdchars[LTsv_kbdcursor]
            elif LTsv_glyph_kbdchars[LTsv_kbdcursor] in LTsv_glyph_irohaalphaN+LTsv_glyph_irohaalphaX:
                LTsv_glyph_kbdchars[LTsv_glyph_KANA]=LTsv_glyph_kbdchars[LTsv_kbdcursor]
            LTsv_glyph_kbdselect(LTsv_glyph_kbdchars[LTsv_glyph_KANA])
        elif LTsv_glyph_kbdLCR == "FlickS":
            LTsv_glyph_kbdselect(LTsv_glyph_kbdchars[LTsv_glyph_KANA])
            if LTsv_glyph_tapcallback != None:
                LTsv_glyph_tapcallback(LTsv_pickdatalabel(LTsv_readlinerest(LTsv_glyph_kandic,LTsv_glyph_kbdchars[LTsv_kbdcursor]),LTsv_glyph_kbdchars[LTsv_glyph_SandS]))
        LTsv_glyph_kbddraw(debug_reversi_canvas,debug_kbdX,debug_kbdY)
        LTsv_draw_queue()
    LTsv_glyph_kbdLCR=""

def LTsv_glyph_kbddelete(kbd_canvas,kbd_x,kbd_y):
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
        LTsv_draw_glyphsfill(draw_t=LTsv_glyph_kbdchars[kbd_xy],draw_x=kbd_x+LTsv_glyph_fontX[kbd_xy],draw_y=kbd_y+LTsv_glyph_fontY[kbd_xy],draw_f=LTsv_glyph_fontG[kbd_xy],draw_g="活")

def LTsv_glyph_picklesave():
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanpickle
    global LTsv_kanglyph5x5OBJ,LTsv_kanglyphcomicOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    LTsv_glyph_kanpickle=LTsv_glyph5x5_coord,LTsv_glyph5x5_clock,LTsv_glyph5x5_wide,LTsv_glyphcomic_coord,LTsv_glyphcomic_clock,LTsv_glyphcomic_wide
    if LTsv_global_GUI() == "GTK2":
        with open(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpickleGTKname),mode='wb') as pickle_fobj:
            pickle.dump(LTsv_glyph_kanpickle,pickle_fobj,protocol=2)
    if LTsv_global_GUI() == "Tkinter":
        with open(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanpickleTkintername),mode='wb') as pickle_fobj:
            pickle.dump(LTsv_glyph_kanpickle,pickle_fobj,protocol=2)
    


LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ={},{},{}
def LTsv9_glyphdicload(dicname="kanchar.tsv"):
    global LTsv_glyph_kandic
    LTsv_glyph_kandic=LTsv_loadfile(dicname) if os.path.isfile(dicname) else LTsv_keyboard_dic()

def LTsv9_glyphOBJpickle(filename="kanpickle.bin"):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    glyphOBJpickle=(LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ)
    with open(filename,mode='wb') as pickle_fobj:
        pickle.dump(glyphOBJpickle,pickle_fobj,protocol=2)

def LTsv9_glyphOBJunpickle(filename="kanpickle.bin"):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    if os.path.isfile(filename):
        with open(filename,mode='rb') as pickle_fobj:
            glyphOBJpickle=pickle.load(pickle_fobj)
        LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ=glyphOBJpickle

def LTsv9_glyphdicread(dictext):
    global LTsv_glyph_kandic
    LTsv_glyph_kandic=dictext

def LTsv9_glyphpath(glyphcode):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    global LTsv_glyph_kandic
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
    LTsv_glyph_path,LTsv_glyph_wide=LTsv_pickdatalabel(LTsv_glyph_kanline,"活"),LTsv_pickdatalabel(LTsv_glyph_kanline,"幅")
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
    LTsv_kanglyphOBJ[glyphcode]=LTsv_glyphnote
    LTsv_kanclockOBJ[glyphcode]=LTsv_glyphclock
    LTsv_kanwideOBJ[glyphcode]=int(LTsv_glyph_wide) if len(LTsv_glyph_wide) else LTsv_PSfont_ZW

def LTsv9_glyphpath_outer(glyphcode):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    global LTsv_glyph_kandic
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
    LTsv_glyph_path,LTsv_glyph_wide=LTsv_pickdatalabel(LTsv_glyph_kanline,"活"),LTsv_pickdatalabel(LTsv_glyph_kanline,"幅")
    LTsv_glyph_pathZ=LTsv_glyph_path.strip(' ').replace('Z','z').rstrip('z').split('z') if len(LTsv_glyph_path) else []
    LTsv_glyphnote,LTsv_glyphclock=[],[]
    for LTsv_glyphline in LTsv_glyph_pathZ:
        LTsv_glyphdata=LTsv_glyphline.split(' '); LTsv_glyphpointlist=[]
        for LTsv_glyphpoint in LTsv_glyphdata:
            if LTsv_glyphpoint.count(',') != 1: continue;
            LTsv_glyphpoints=LTsv_glyphpoint.strip(' ').split(',')
#            LTsv_glyphpointlist+=[int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0]
#            LTsv_glyphpointlist+=[(LTsv_PSchar_ZW-int(LTsv_glyphpoints[1])) if LTsv_glyphpoints[1].isdigit() else 0]
            LTsv_glyphpoint98=int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0
            LTsv_glyphpoint98=LTsv_glyphpoint98 if LTsv_glyphpoint98 % 100 != 98 else LTsv_glyphpoint98+2
            LTsv_glyphpointlist+=[LTsv_glyphpoint98]
            LTsv_glyphpoint98=int(LTsv_glyphpoints[1]) if LTsv_glyphpoints[1].isdigit() else 0
            LTsv_glyphpoint98=LTsv_glyphpoint98 if LTsv_glyphpoint98 % 100 != 2 else LTsv_glyphpoint98-2
            LTsv_glyphpointlist+=[LTsv_PSchar_ZW-LTsv_glyphpoint98]
        LTsv_glyphnote.append(LTsv_glyphpointlist); LTsv_glyphclock.append(LTsv_clockwise(*tuple(LTsv_glyphpointlist)))
    LTsv_kanglyphOBJ[glyphcode]=LTsv_glyphnote
    LTsv_kanclockOBJ[glyphcode]=LTsv_glyphclock
    LTsv_kanwideOBJ[glyphcode]=int(LTsv_glyph_wide) if len(LTsv_glyph_wide) else LTsv_PSfont_ZW

def LTsv9_drawGTK_glyph(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv9_glyphpath_outer(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_drawGTK_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv9_drawTkinter_glyph(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv9_glyphpath(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_drawTkinter_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv9_drawGTK_glyphfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv9_glyphpath_outer(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            if LTsv_kanclockOBJ[glyphcode][LTsv_glyphpointlist_count] > 0:
#                LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKcanvas_gccolor))
                LTsv_drawGTK_gcfcolor()
            else:
#                LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKfont_gccolor))
                LTsv_drawGTK_gcbcolor()
            LTsv_drawGTK_polygonfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv9_drawTkinter_glyphfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv9_glyphpath(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            if LTsv_kanclockOBJ[glyphcode][LTsv_glyphpointlist_count] > 0:
                LTsv_drawTkinter_polygonfill(*tuple(LTsv_glyphpointresize))
            else:
                LTsv_drawTkinter_fontfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def debug_mousepress(window_objvoid=None,window_objptr=None):
    keyboard_mouseX,keyboard_mouseY=min(max(LTsv_global_canvasmotionX(),0),debug_reversi_W),min(max(LTsv_global_canvasmotionY(),0),debug_reversi_H)
    if debug_milklidX[11] < keyboard_mouseX < debug_milklidX[99] and debug_milklidY[11] < keyboard_mouseY < debug_milklidY[99]:
        for xy in debug_milklid_range:
            if debug_milklidX[xy] < keyboard_mouseX < debug_milklidX[xy+1] and debug_milklidY[xy] < keyboard_mouseY < debug_milklidY[xy+10]:
                debug_milkAI_add(debug_reversi_key[xy])
    else:
        LTsv_glyph_mousepress(debug_reversi_canvas,debug_kbdX,debug_kbdY)

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
    LTsv_glyph_kbddelete(debug_reversi_canvas,debug_kbdX,debug_kbdY)
    LTsv_draw_selcanvas(debug_reversi_canvas)
    LTsv_draw_delete()
    LTsv_draw_color(debug_milklid_colordic["back"]); LTsv_draw_polygonfill(0,0,debug_reversi_W,0,debug_reversi_W,debug_reversi_H,0,debug_reversi_H)
    LTsv_draw_color(debug_milklid_colordic["green"]); LTsv_draw_polygonfill(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_font(debug_milkfont)
    LTsv_draw_bgcolor(debug_milklid_colordic["green"])
    for xy in debug_milklid_range:
        if debug_milklid_check(xy,debug_milklidBW) > 0:
            LTsv_draw_color(debug_milklid_colordic["next"])
            LTsv_draw_glyphs(draw_t=debug_reversi_key[xy],draw_x=debug_milklidX[xy]+debug_kbdH//8,draw_y=debug_milklidY[xy]+debug_kbdH//8,draw_f=debug_kbdH*2//3,draw_g="活")
        else:
            LTsv_draw_color(debug_milklid_colordic[debug_milklid_colorkey[debug_milkMAP[xy]]])
            LTsv_draw_glyphsfill(draw_t=debug_reversi_key[xy],draw_x=debug_milklidX[xy]+debug_kbdH//8,draw_y=debug_milklidY[xy]+debug_kbdH//8,draw_f=debug_kbdH*2//3,draw_g="活")
    LTsv_draw_color(debug_milklid_colordic["line"])
    LTsv_draw_polygon(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_polygon(debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_squaresfill(6,debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_bgcolor(debug_milklid_colordic["back"])
    for bw in range(2):
        milklidcount=0
        for xy in debug_milklid_range:
            milklidcount=milklidcount+1 if debug_milkMAP[xy] == debug_milklidBWswitch[bw] else milklidcount
        LTsv_draw_glyphsfill(draw_t="{0}\n{1:02}\n\n{2}".format(debug_milklidBWstone[debug_milklidBWswitch[bw]],milklidcount,debug_milklidBWwaitname[debug_milklidBWwait[debug_milklidBWswitch[bw]]]),draw_x=debug_milklidBWstatusX[debug_milklidBWswitch[bw]],draw_y=debug_milklidY[20],draw_f=debug_kbdH//2,draw_g="活")
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

def debug_configsave(window_objvoid=None,window_objptr=None):
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
        LTsv_glyph_kbdinit(ltsvpath="kanglyph.tsv")
        debug_kbdH=25
        debug_milklid_W,debug_milklid_H=debug_kbdH,debug_kbdH
        debug_milkfont="kantray5x5comic,{0}".format(debug_kbdH//2)
        debug_entryfont="kantray5x5comic,{0}".format(debug_kbdH//4)
        debug_buttonfont="kantray5x5comic,5".format(5)
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
        debug_reversi_window=LTsv_window_new(widget_t="reversi",event_b=debug_configsave,widget_w=debug_reversi_W,widget_h=debug_reversi_H+debug_milklid_H//2,event_z=None)
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
        LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
        LTsv_glyph_tapcallback_shell(debug_milkAI_add)
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
