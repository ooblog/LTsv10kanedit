#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
try:
   import cPickle as pickle
except:
   import pickle
from LTsv_file    import *
from LTsv_printf import *
from LTsv_gui    import *

LTsv_PSfont_ZW,LTsv_PSfont_CW,LTsv_PSchar_ZW,LTsv_PSchar_CW=1024,624,1000,600
LTsv_glyph_ltsvdir,LTsv_glyph_kandicname,LTsv_glyph_kanmapname,LTsv_glyph_kanpicklename="LTsv/","kanchar.tsv","kanmap.tsv","kanpickle.bin"
LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanmap,LTsv_glyph_kanpickle="","","",""
LTsv_glyph_irohatype= ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","゛","゜","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
LTsv_glyph_irohatypeN=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
LTsv_glyph_irohatypeX=["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ","｜"]
LTsv_glyph_choice=    ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
LTsv_glyph_choiceN=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
LTsv_glyph_choiceX=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","Ε","Ρ","Τ","Υ","Θ","Ι","Ο","Π","｀","プ","Α","Σ","Δ","Φ","Γ","Η","Ξ","Κ","Λ","代","鍵","ぬ","Ζ","Χ","Ψ","Ω","Β","Ν","Μ","熙","●","▲","■","￥","Σ"]
LTsv_glyph_alphatype= ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
LTsv_glyph_alphatypeN=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
LTsv_glyph_alphatypeX=["Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω","●","▲","■"]
LTsv_glyph_dictype=    ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","漫","幅"]
def LTsv_glyph_init(LTsv_glyph_ltsvpath="kanglyph.tsv"):
    global LTsv_glyph_ltsvdir,LTsv_glyph_kandicname,LTsv_glyph_kanmapname,LTsv_glyph_kanpicklename
    global LTsv_glyph_ltsv,LTsv_glyph_kandic,LTsv_glyph_kanmap,LTsv_glyph_kanpickle
    LTsv_glyph_ltsvdir=os.path.normpath(os.path.dirname(LTsv_glyph_ltsvpath))+"/"
    LTsv_glyph_ltsv=LTsv_loadfile(os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_ltsvpath))
    LTsv_glyph_config=LTsv_getpage(LTsv_glyph_ltsv,"kanglyph")
    LTsv_glyph_kandicname=LTsv_readlinerest(LTsv_glyph_config,"dicname",LTsv_glyph_kandicname)
    LTsv_glyph_kanmapname=LTsv_readlinerest(LTsv_glyph_config,"mapname",LTsv_glyph_kanmapname)
    LTsv_glyph_kanpicklename=LTsv_readlinerest(LTsv_glyph_config,"picklename",LTsv_glyph_kanpicklename)

#    print("LTsv_glyph_kandicname",LTsv_glyph_kandicname)
##    print("LTsv_glyph_kanmapname",LTsv_glyph_kanmapname)
#    print("LTsv_glyph_kanpicklename",LTsv_glyph_kanpicklename)
#    print(LTsv_glyph_ltsv)
#    keyboard_kanmapT=LTsv_loadfile(os.path.normpath(LTsv_glyph_tsvdir+LTsv_glyph_kandicname)
#        keyboard_kanmapT=LTsv_loadfile(os.path.normpath(LTsv_tsvdir+LTsv_readlinerest(keyboard_mapdic_page,"mapname")))

def LTsv_glyphdicload(dicname="kanchar.tsv"):
    global LTsv_glyph_kandic
    LTsv_glyph_kandic=LTsv_loadfile(dicname) if os.path.isfile(dicname) else LTsv_keyboard_dic()

def LTsv_glyphOBJpickle(filename="kanpickle.bin"):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    glyphOBJpickle=(LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ)
    with open(filename,mode='wb') as pickle_fobj:
        pickle.dump(glyphOBJpickle,pickle_fobj,protocol=2)

def LTsv_glyphOBJunpickle(filename="kanpickle.bin"):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    if os.path.isfile(filename):
        with open(filename,mode='rb') as pickle_fobj:
            glyphOBJpickle=pickle.load(pickle_fobj)
        LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ=glyphOBJpickle

def LTsv_glyphdicread(dictext):
    global LTsv_glyph_kandic
    LTsv_glyph_kandic=dictext

def LTsv_glyphpath(glyphcode):
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

def LTsv_glyphpath_outer(glyphcode):
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

def LTsv_drawGTK_glyph(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
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
            LTsv_glyphpath_outer(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_drawGTK_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_drawTkinter_glyph(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
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
            LTsv_glyphpath(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_drawTkinter_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_drawGTK_glyphfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
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
            LTsv_glyphpath_outer(glyphcode)
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

def LTsv_drawTkinter_glyphfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
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
            LTsv_glyphpath(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            if LTsv_kanclockOBJ[glyphcode][LTsv_glyphpointlist_count] > 0:
                LTsv_drawTkinter_polygonfill(*tuple(LTsv_glyphpointresize))
            else:
                LTsv_drawTkinter_fontfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_kbddraw():
    pass

def debug_mousepress(window_objvoid=None,window_objptr=None):
    keyboard_mouseX,keyboard_mouseY=min(max(LTsv_global_canvasmotionX(),0),debug_reversi_W),min(max(LTsv_global_canvasmotionY(),0),debug_reversi_H)
    if debug_milklidX[11] < keyboard_mouseX < debug_milklidX[99] and debug_milklidY[11] < keyboard_mouseY < debug_milklidY[99]:
        for xy in debug_reversi_range:
            if debug_milklidX[xy] < keyboard_mouseX < debug_milklidX[xy+1] and debug_milklidY[xy] < keyboard_mouseY < debug_milklidY[xy+10]:
                debug_milkAI_add(debug_reversi_key[xy])
    else:
        pass

def debug_mousemotion(window_objvoid=None,window_objptr=None):
    pass

def debug_mouserelease(window_objvoid=None,window_objptr=None):
    pass

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

def debug_milklid_draw():
    LTsv_draw_selcanvas(debug_reversi_canvas)
    LTsv_draw_delete()
    LTsv_draw_color(debug_milklid_colordic["back"]); LTsv_draw_polygonfill(0,0,debug_reversi_W,0,debug_reversi_W,debug_reversi_H,0,debug_reversi_H)
    LTsv_draw_color(debug_milklid_colordic["green"]); LTsv_draw_polygonfill(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_font(debug_milkfont)
    for xy in debug_reversi_range:
        if debug_milklid_check(xy,debug_milklidBW) > 0:
            LTsv_draw_color(debug_milklid_colordic["next"])
        else:
            LTsv_draw_color(debug_milklid_colordic[debug_milklid_colorkey[debug_milkMAP[xy]]])
        LTsv_draw_text(draw_t=debug_reversi_key[xy],draw_x=debug_milklidX[xy]+debug_kbdH//8,draw_y=debug_milklidY[xy]+debug_kbdH//8)
    LTsv_draw_color(debug_milklid_colordic["line"])
    LTsv_draw_polygon(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_polygon(debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_squaresfill(6,debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_queue()

def debug_milkAI_reset():
    global debug_milkAI,debug_milkMAP,debug_milklidBW
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

def debug_milkMAP_reset():
    global debug_milkAI,debug_milkMAP,debug_milklidBW
    debug_milklidBW=debug_milklidBWswitch[0]
    debug_milkMAP=[0 for xy in range(debug_milklidLen)]
    for xy in [45,54]: debug_milkMAP[xy]=debug_milklidBWswitch[0];
    for xy in [44,55]: debug_milkMAP[xy]=debug_milklidBWswitch[1];

def debug_milkAI_entry(window_objvoid=None,window_objptr=None):
    global debug_milkAI,debug_milkMAP,debug_milklidBW
    reversi_entry=LTsv_widget_gettext(debug_reversi_entry)
    reversi_entry=reversi_entry[:60]
    if len(reversi_entry) == 0:
        debug_milkAI_reset()
    debug_milkMAP_reset()
    for entrylen,entryxy in enumerate(reversi_entry):
        if entryxy in debug_reversi_key and entryxy != debug_reversi_key[0]:
#            debug_milkMAP[debug_reversi_key.index(entryxy)]=debug_milklidBW
            debug_milklid_turn(debug_reversi_key.index(entryxy),debug_milklidBW)
            debug_milklidBW=debug_milklidBWswitch[debug_milklidBW]
        else:
            reversi_entry=reversi_entry[:entrylen]
            break
    LTsv_widget_settext(debug_reversi_entry,reversi_entry)
    debug_milklid_draw()

def debug_milkAI_BS(window_objvoid=None,window_objptr=None):
    reversi_entry=LTsv_widget_gettext(debug_reversi_entry)
    reversi_entry=reversi_entry[:len(reversi_entry)-1] if len(reversi_entry) > 0 else ""
    LTsv_widget_settext(debug_reversi_entry,reversi_entry)
    debug_milkAI_entry()

def debug_milkAI_add(addentry):
    reversi_entry=LTsv_widget_gettext(debug_reversi_entry)
    reversi_entry="{0}{1}".format(reversi_entry,addentry) if len(reversi_entry) < 60 else ""
    LTsv_widget_settext(debug_reversi_entry,reversi_entry)
    debug_milkAI_entry()

def debug_milkAI_Auto(window_objvoid=None,window_objptr=None):
    debug_milkAI_add("Ａ")

if __name__=="__main__":
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
    if len(LTsv_GUI) > 0:
        import random
        LTsv_glyph_init(LTsv_glyph_ltsvpath="kanglyph.tsv")
        debug_kbd_size=1
        debug_kbdH=6*4*debug_kbd_size
        debug_milklid_W,debug_milklid_H=debug_kbdH,debug_kbdH
        debug_milkfont="kantray5x5comic,{0}".format(debug_kbdH//2)
        debug_entryfont="kantray5x5comic,{0}".format(debug_kbdH//4)
        debug_buttonfont="kantray5x5comic,5".format(5)
        debug_reversi_X,debug_reversi_Y,debug_reversi_W,debug_reversi_H=debug_milklid_W*7,debug_milklid_H*1,debug_milklid_W*(2+20+2),debug_milklid_H*(2+8+2)
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
        debug_reversi_range=[y*10+x for y in range(1,9) for x in range(1,9)]
        debug_milklid_colorkey=["green","black","white","back","line","nexr"]
        debug_milklid_colordic={"green":"#76DC76","black":"#4E4E4E","white":"#FFF5FD","back":"#F3F3F3","line":"#4D4D4D","next":"#C0D2FF"}
        debug_reversi_window=LTsv_window_new(widget_t="reversi",event_b=LTsv_window_exit,widget_w=debug_reversi_W,widget_h=debug_reversi_H+debug_milklid_H//2,event_z=None)
        debug_reversi_entry=LTsv_entry_new(debug_reversi_window,widget_t="",widget_x=0,widget_y=debug_reversi_H,widget_w=debug_reversi_W-debug_milklid_W*3,widget_h=debug_milklid_H//2,widget_f=debug_entryfont,event_b=debug_milkAI_entry)
        debug_reversi_back=LTsv_button_new(debug_reversi_window,widget_t="BS",widget_x=debug_reversi_W-debug_milklid_W*3,widget_y=debug_reversi_H,widget_w=debug_milklid_W*1,widget_h=debug_milklid_H//2,widget_f=debug_buttonfont,event_b=debug_milkAI_BS)
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
        debug_milkAI_entry()
        LTsv_window_main(debug_reversi_window)
    else:
        LTsv_libc_printf("GUIの設定に失敗しました。")
    print("")
    print("__main__",LTsv_file_ver())

# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
