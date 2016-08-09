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
LTsv_glyph_kandic=""
#def LTsv_glyph_init(dicname="kanglyph.tsv"):
#    pass
#    LTsv_tsvdir=os.path.normpath(os.path.dirname(LTsv_tsvpath))+"/"
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

def debug_milklid_draw():
    LTsv_draw_selcanvas(debug_reversi_canvas)
    LTsv_draw_delete("#E1E1E1")
    LTsv_draw_color("#76DC76")
    LTsv_draw_polygonfill(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_color("black"); LTsv_draw_font(debug_font)
    for i in range(debug_milklidLen):
#        LTsv_draw_text(draw_t=debug_reversi_key[i],draw_x=debug_milklidX[i],draw_y=debug_milklidY[i])
#        LTsv_draw_text(draw_t="{0:3}".format(debug_milkAI[i]),draw_x=debug_milklidX[i],draw_y=debug_milklidY[i]+debug_kbdH//2)
        LTsv_draw_text(draw_t=debug_reversi_key[i],draw_x=debug_milklidX[i]+debug_kbdH//8,draw_y=debug_milklidY[i]+debug_kbdH//8)
    LTsv_draw_polygon(debug_milklidX[11],debug_milklidY[11],debug_milklidX[19],debug_milklidY[19],debug_milklidX[99],debug_milklidY[99],debug_milklidX[91],debug_milklidY[91])
    LTsv_draw_polygon(debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_squaresfill(6,debug_milklidX[33],debug_milklidY[33],debug_milklidX[37],debug_milklidY[37],debug_milklidX[77],debug_milklidY[77],debug_milklidX[73],debug_milklidY[73])
    LTsv_draw_queue()

def debug_milkAI_reset():
    global debug_milkAI
    debug_milkAI=list(range(100))
    random.shuffle(debug_milkAI)
    for i in [11,18,81,88]: debug_milkAI[i]+=900;
    for i in [13,16,31,38,61,68,83,86]: debug_milkAI[i]+=800;
    for i in [33,36,63,66]: debug_milkAI[i]+=700;
    for i in [34,35,43,46,53,56,64,65]: debug_milkAI[i]+=600;
    for i in [14,15,41,48,51,58,84,85]: debug_milkAI[i]+=500;
    for i in [23,26,32,37,62,67,73,76]: debug_milkAI[i]+=400;
    for i in [24,25,42,47,52,57,74,75]: debug_milkAI[i]+=300;
    for i in [12,17,21,28,71,78,82,87]: debug_milkAI[i]+=200;
    for i in [22,27,72,77]: debug_milkAI[i]+=100;

if __name__=="__main__":
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
    if len(LTsv_GUI) > 0:
        import random
        debug_kbd_size=1
        debug_kbdH=6*4*debug_kbd_size
#        debug_milklid_W,debug_milklid_H=debug_kbdH,debug_kbdH; debug_font="kantray5x5comic,{0}".format(debug_kbdH//4)
        debug_milklid_W,debug_milklid_H=debug_kbdH,debug_kbdH; debug_font="kantray5x5comic,{0}".format(debug_kbdH//2)
        debug_reversi_X,debug_reversi_Y,debug_reversi_W,debug_reversi_H=debug_milklid_W*1,debug_milklid_H*1,debug_milklid_W*(2+8+2),debug_milklid_H*(2+8+2)
        debug_milklidLen=(10*10)
        debug_milklidX,debug_milklidY,debug_milkAI=[0]*debug_milklidLen,[0]*debug_milklidLen,[0]*debug_milklidLen
        for i in range(debug_milklidLen):
            debug_milklidX[i],debug_milklidY[i]=debug_reversi_X+debug_milklid_W*(i%(1+8+1)),debug_reversi_Y+debug_milklid_H*(i//(1+8+1))
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
        debug_reversi_window=LTsv_window_new(widget_t="reversi",event_b=LTsv_window_exit,widget_w=debug_reversi_W,widget_h=debug_reversi_H,event_z=None)
        debug_reversi_canvas=LTsv_canvas_new(debug_reversi_window,widget_x=0,widget_y=0,widget_w=debug_reversi_W,widget_h=debug_reversi_H,
         event_p=None,event_r=None,event_m=None,event_w=50)
        LTsv_widget_showhide(debug_reversi_window,True)
        LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
        LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
        LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
        LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
        LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
        LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
        debug_milkAI_reset()
        debug_milklid_draw()
        LTsv_window_main(debug_reversi_window)
    else:
        LTsv_libc_printf("GUIの設定に失敗しました。")
    print("")
    print("__main__",LTsv_file_ver())

# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
