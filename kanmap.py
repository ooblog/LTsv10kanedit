#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
import math
os.chdir(sys.path[0])
sys.path.append("LTsv")
from LTsv_printf  import *
from LTsv_file    import *
#from LTsv_time    import *
#from LTsv_calc    import *
#from LTsv_joy     import *
#from LTsv_kbd     import *
from LTsv_gui     import *
from LTsv_glyph  import *


LTsv_irohaalpha_count=0
def LTsv_kanmap_drawKBDZero():
    global LTsv_irohaalpha_count
    LTsv_widget_settext(kanmap_window,"kanmap:pickling kanmap.tsv")
    LTsv_draw_selcanvas(kanmap_canvas); LTsv_draw_delete(); LTsv_draw_queue();
    LTsv_glyph_kbddelete(kanmap_canvas)
    LTsv_glyph_kbddraw(kanmap_canvas,kanmap_kbdX,kanmap_kbdY); LTsv_draw_queue();
    LTsv_irohaalpha_count=0
    LTsv_window_after(kanmap_window,event_b=LTsv_kanmap_drawKBDCount,event_i="LTsv_kanmap_drawKBDCount",event_w=10)

def LTsv_kanmap_drawKBD(irohaalpha_count):
    LTsv_draw_selcanvas(kanmap_canvas); LTsv_draw_color("black"); LTsv_draw_bgcolor("white")
    kbd_x,kbd_y=LTsv_glyph_kbdNX[irohaalpha_count],LTsv_glyph_kbdNY[irohaalpha_count]
    LTsv_glyph_kbdchars[0:LTsv_glyph_irohamax]=LTsv_glyph_kanmapN[LTsv_global_irohaalpha()[irohaalpha_count]][0:LTsv_glyph_irohamax]; LTsv_glyph_kbdchars[LTsv_glyph_irohamax]=LTsv_global_irohaalphaN()[irohaalpha_count]
    for kbd_xy in range(LTsv_glyph_None):
        LTsv_draw_glyphskbd(draw_t=LTsv_glyph_kbdchars[kbd_xy],draw_x=kbd_x+LTsv_glyph_fontX[kbd_xy],draw_y=kbd_y+LTsv_glyph_fontY[kbd_xy],draw_f=LTsv_glyph_fontG[kbd_xy],draw_g=LTsv_glyph_kbdtype[kbd_xy])
    kbd_x,kbd_y=LTsv_glyph_kbdXX[irohaalpha_count],LTsv_glyph_kbdXY[irohaalpha_count]
    LTsv_glyph_kbdchars[0:LTsv_glyph_irohamax]=LTsv_glyph_kanmapX[LTsv_global_irohaalpha()[irohaalpha_count]][0:LTsv_glyph_irohamax]; LTsv_glyph_kbdchars[LTsv_glyph_irohamax]=LTsv_global_irohaalphaX()[irohaalpha_count]
    for kbd_xy in range(LTsv_glyph_None):
        LTsv_draw_glyphskbd(draw_t=LTsv_glyph_kbdchars[kbd_xy],draw_x=kbd_x+LTsv_glyph_fontX[kbd_xy],draw_y=kbd_y+LTsv_glyph_fontY[kbd_xy],draw_f=LTsv_glyph_fontG[kbd_xy],draw_g=LTsv_glyph_kbdtype[kbd_xy])

def LTsv_kanmap_drawKBDCount(window_objvoid=None,window_objptr=None):
    global LTsv_irohaalpha_count
    LTsv_kanmap_drawKBD(LTsv_irohaalpha_count); LTsv_draw_queue();
    LTsv_irohaalpha_count+=1
    if LTsv_irohaalpha_count < len(LTsv_global_irohaalpha()):
        LTsv_window_after(kanmap_window,event_b=LTsv_kanmap_drawKBDCount,event_i="LTsv_kanmap_drawKBDCount",event_w=10)
    else:
        LTsv_window_after(kanmap_window,event_b=LTsv_kanmap_drawDICZero,event_i="LTsv_kanmap_drawDICZero",event_w=10)

LTsv_kansplits_count=0
def LTsv_kanmap_drawDICZero(window_objvoid=None,window_objptr=None):
    LTsv_widget_settext(kanmap_window,"kanmap:pickling LTsv/kanchar.tsv")
    LTsv_draw_selcanvas(kanmap_canvas); LTsv_draw_color("black"); LTsv_draw_bgcolor("black")
    LTsv_draw_polygonfill(LTsv_glyph_kbdF//2,LTsv_glyph_dicY-LTsv_glyph_kbdF//2,kanmap_canvasW-LTsv_glyph_kbdF//2,LTsv_glyph_dicY-LTsv_glyph_kbdF//2,kanmap_canvasW-LTsv_glyph_kbdF//2,LTsv_glyph_dicY-LTsv_glyph_kbdF//2-1,LTsv_glyph_kbdF//2,LTsv_glyph_dicY-LTsv_glyph_kbdF//2-1)
    LTsv_draw_queue()
    LTsv_window_after(kanmap_window,event_b=LTsv_kanmap_drawDICCount,event_i="LTsv_kanmap_drawDICCount",event_w=10)

def LTsv_kanmap_drawDIC(kansplits_count):
    LTsv_draw_selcanvas(kanmap_canvas); LTsv_draw_color("black"); LTsv_draw_bgcolor("white")
    dicY=LTsv_glyph_dicY+LTsv_glyph_kbdF*kansplits_count//kanmap_kansplits_linelen
    for kbd_xy in range(min(kanmap_kansplits_linelen,len(LTsv_kansplits)-kansplits_count)):
        LTsv_draw_glyphskbd(draw_t=LTsv_kansplits[kansplits_count+kbd_xy][0:1],draw_x=kbd_xy*LTsv_glyph_kbdF,draw_y=dicY)

def LTsv_kanmap_drawDICCount(window_objvoid=None,window_objptr=None):
    global LTsv_kansplits_count
    LTsv_kanmap_drawDIC(LTsv_kansplits_count); LTsv_draw_queue();
    LTsv_kansplits_count+=kanmap_kansplits_linelen
    if LTsv_kansplits_count < len(LTsv_kansplits):
        LTsv_window_after(kanmap_window,event_b=LTsv_kanmap_drawDICCount,event_i="LTsv_kanmap_drawDICCount",event_w=10)
    else:
        LTsv_widget_settext(kanmap_window,"kanmap")

LTsv_mapcursorBF,LTsv_mapcursorAF=0,0
def LTsv_kanmap_cursor():
    global LTsv_mapcursorBF,LTsv_mapcursorAF
    LTsv_draw_selcanvas(kanmap_canvas)
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()

def LTsv_kanmap_mousepress(window_objvoid=None,window_objptr=None):
    if LTsv_glyph_mousepress(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        LTsv_kanmap_cursor()

def LTsv_kanmap_mousemotion(window_objvoid=None,window_objptr=None):
    global LTsv_mapcursorBF,LTsv_mapcursorAF
    if LTsv_glyph_mousemotion(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        LTsv_kanmap_cursor()
#        if LTsv_glyph_dicY

def LTsv_kanmap_mouserelease(window_objvoid=None,window_objptr=None):
    if LTsv_glyph_mouserelease(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        LTsv_kanmap_cursor()

def kanmap_configsave_exit(window_objvoid=None,window_objptr=None):
    LTsv_glyph_picklesave()
    LTsv_draw_canvas_save(kanmap_canvas,"kanmap.png")
    LTsv_window_exit()


LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_tsvpath="LTsv/LTsv_kbd.tsv",LTsv_initmouse=True)
    LTsv_glyph_kbdinit(LTsv_tsvpath="LTsv/LTsv_glyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    LTsv_glyph_kanmapN,LTsv_glyph_kanmapX=LTsv_global_kanmapN(),LTsv_global_kanmapX()
    LTsv_glyph_irohamax=len(LTsv_global_irohatype())
    LTsv_glyph_None=LTsv_glyph_irohamax+1
    LTsv_glyph_kbdchars=[""]*(LTsv_glyph_None)
    LTsv_glyph_kbdF=6*LTsv_glyph_kbdsize; LTsv_glyph_kbdH=LTsv_glyph_kbdF*4; LTsv_glyph_kbdW=LTsv_glyph_kbdF*12
    LTsv_glyph_kbdG,LTsv_glyph_kbdC=LTsv_glyph_kbdF-1,LTsv_glyph_kbdF//2
    LTsv_glyph_fontX,LTsv_glyph_fontY,LTsv_glyph_fontG,LTsv_glyph_mouseX,LTsv_glyph_mouseY,LTsv_glyph_mouseC=[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None),[0]*(LTsv_glyph_None)
    for kbd_xy in range(LTsv_glyph_irohamax):
        LTsv_glyph_fontX[kbd_xy],LTsv_glyph_fontY[kbd_xy],LTsv_glyph_fontG[kbd_xy]=LTsv_glyph_kbdF*(kbd_xy%12),LTsv_glyph_kbdF*(kbd_xy//12)+LTsv_glyph_kbdF*2,LTsv_glyph_kbdG
    LTsv_glyph_fontX[LTsv_glyph_irohamax],LTsv_glyph_fontY[LTsv_glyph_irohamax],LTsv_glyph_fontG[LTsv_glyph_irohamax]=LTsv_glyph_kbdG=1+LTsv_glyph_kbdF*0,1,LTsv_glyph_kbdG*2
    LTsv_glyph_kbdtype=tuple(["活" if t < LTsv_glyph_irohamax else "漫" for t in range(LTsv_glyph_None)])
    kanmap_kbdNH=LTsv_glyph_kbdH+LTsv_glyph_kbdF*2
    kanmap_NH=kanmap_kbdNH*(4+2)
    LTsv_glyph_kbdNX,LTsv_glyph_kbdNY=[0]*len(LTsv_global_irohaalpha()),[0]*len(LTsv_global_irohaalpha())
    LTsv_glyph_kbdXX,LTsv_glyph_kbdXY=[0]*len(LTsv_global_irohaalpha()),[0]*len(LTsv_global_irohaalpha())
    for map_xy in range(len(LTsv_global_irohaalpha())):
        if map_xy < len(LTsv_global_irohaalpha())-3:
            LTsv_glyph_kbdNX[map_xy],LTsv_glyph_kbdNY[map_xy]=map_xy%12*LTsv_glyph_kbdW,map_xy//12*kanmap_kbdNH
            LTsv_glyph_kbdXX[map_xy],LTsv_glyph_kbdXY[map_xy]=map_xy%12*LTsv_glyph_kbdW,map_xy//12*kanmap_kbdNH+kanmap_NH
        else:
            LTsv_glyph_kbdNX[map_xy],LTsv_glyph_kbdNY[map_xy]=LTsv_glyph_kbdW*12,(map_xy%12+0)*kanmap_kbdNH
            LTsv_glyph_kbdXX[map_xy],LTsv_glyph_kbdXY[map_xy]=LTsv_glyph_kbdW*12,(map_xy%12+3)*kanmap_kbdNH+kanmap_NH
    LTsv_glyph_dicY=kanmap_NH*2+LTsv_glyph_kbdF
    kanmap_canvasW,kanmap_canvasH=LTsv_glyph_kbdF*int(math.ceil(1000/LTsv_glyph_kbdF)),LTsv_glyph_dicY
    kanmap_kansplits_linelen=kanmap_canvasW//LTsv_glyph_kbdF
    LTsv_glyph_kandic=LTsv_global_kandic(); LTsv_kansplits=LTsv_glyph_kandic.rstrip('\n').split('\n')
    LTsv_kansplits_len=len(LTsv_kansplits)//kanmap_kansplits_linelen
    kanmap_canvasH=kanmap_canvasH+LTsv_kansplits_len*LTsv_glyph_kbdF
    kanmap_kbdX,kanmap_kbdY=kanmap_canvasW-LTsv_global_glyphkbdW()-LTsv_glyph_kbdF,kanmap_NH-kanmap_kbdNH//2
    kanmapW,kanmapH=kanmap_canvasW,kanmap_canvasH
    kanmap_window=LTsv_window_new(widget_t="kanmap",event_b=kanmap_configsave_exit,widget_w=kanmapW,widget_h=kanmapH,event_k=None,event_y=None)
    kanmap_canvas=LTsv_canvas_new(kanmap_window,widget_x=0,widget_y=0,widget_w=kanmap_canvasW,widget_h=kanmap_canvasH,
     event_p=LTsv_kanmap_mousepress,event_m=LTsv_kanmap_mousemotion,event_r=LTsv_kanmap_mouserelease,event_e=None,event_l=None,event_w=50)
    LTsv_widget_showhide(kanmap_window,True)
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    LTsv_kanmap_drawKBDZero()
    LTsv_window_main(kanmap_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
