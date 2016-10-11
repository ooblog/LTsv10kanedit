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

def LTsv_kanmap_drawline(kanmap_linecount):
    LTsv_draw_selcanvas(kanmap_canvas); LTsv_draw_color("black"); LTsv_draw_bgcolor("white")
    drawline_y=kanmap_linecount*LTsv_glyph_kbdF
    for map_xy in range(kanmap_charsW):
        LTsv_draw_glyphskbd(draw_t=kanmap_chars[kanmap_linecount][map_xy][0:1],draw_x=map_xy*LTsv_glyph_kbdF,draw_y=drawline_y)
    LTsv_draw_queue()

kanmap_linecount=0
def kanmap_KBDstart():
    LTsv_widget_settext(kanmap_window,"kanmap:pickling kanmap.tsv")
    for map_xy in range(len(LTsv_global_irohaalpha())):
        map_x,map_y=kanmap_irohaalphaNX[map_xy]//LTsv_glyph_kbdF+2,kanmap_irohaalphaNY[map_xy]//LTsv_glyph_kbdF-2
        for kbd_xy in range(len(LTsv_global_irohatype())):
            kbd_x,kbd_y=map_x+(kbd_xy%12),map_y+(kbd_xy//12)
            kanmap_chars[kbd_y][kbd_x]=LTsv_glyph_kanmapN[LTsv_global_irohaalpha()[map_xy]][kbd_xy]
        map_x,map_y=kanmap_irohaalphaXX[map_xy]//LTsv_glyph_kbdF+2,kanmap_irohaalphaXY[map_xy]//LTsv_glyph_kbdF-2
        for kbd_xy in range(len(LTsv_global_irohatype())):
            kbd_x,kbd_y=map_x+(kbd_xy%12),map_y+(kbd_xy//12)
            kanmap_chars[kbd_y][kbd_x]=LTsv_glyph_kanmapX[LTsv_global_irohaalpha()[map_xy]][kbd_xy]
    global kanmap_linecount
    kanmap_linecount=0
    LTsv_window_after(kanmap_window,event_b=kanmap_KBDcount,event_i="kanmap_KBDcount",event_w=10)

def kanmap_KBDcount(window_objvoid=None,window_objptr=None):
    global kanmap_linecount
    LTsv_kanmap_drawline(kanmap_linecount); kanmap_linecount+=1
    if kanmap_linecount < kanmap_charsH:
        LTsv_window_after(kanmap_window,event_b=kanmap_KBDcount,event_i="kanmap_KBDcount",event_w=10)
    else:
        kanmap_KBDfinishDICstart()

def kanmap_KBDfinishDICstart():
    for map_xy in range(len(LTsv_global_irohaalpha())):
        LTsv_draw_glyphskbd(draw_t=LTsv_global_irohaalphaN()[map_xy],draw_x=kanmap_irohaalphaNX[map_xy],draw_y=kanmap_irohaalphaNY[map_xy],draw_f=10,draw_g="漫")
        LTsv_draw_glyphskbd(draw_t=LTsv_global_irohaalphaX()[map_xy],draw_x=kanmap_irohaalphaXX[map_xy],draw_y=kanmap_irohaalphaXY[map_xy],draw_f=10,draw_g="漫")
    LTsv_draw_polygonfill(LTsv_glyph_kbdF//2,kanmap_dicY-LTsv_glyph_kbdF//2,kanmap_canvasW-LTsv_glyph_kbdF//2,kanmap_dicY-LTsv_glyph_kbdF//2,kanmap_canvasW-LTsv_glyph_kbdF//2,kanmap_dicY-LTsv_glyph_kbdF//2-1,LTsv_glyph_kbdF//2,kanmap_dicY-LTsv_glyph_kbdF//2-1)
    LTsv_draw_queue()
    LTsv_widget_settext(kanmap_window,"kanmap:pickling LTsv/kanchar.tsv")
    for dic_xy in range(kandic_charsH):
        for map_xy in range(kanmap_charsW):
            dicpos=dic_xy*kanmap_charsW+map_xy
            if dicpos >= len(kanmap_dicsplits): break;
            kanmap_chars[kanmap_charsY+dic_xy][map_xy]=kanmap_dicsplits[dicpos][0:1]
    global kanmap_linecount
    kanmap_linecount=kanmap_charsH+1
    LTsv_window_after(kanmap_window,event_b=kanmap_DICcount,event_i="kanmap_DICcount",event_w=10)

def kanmap_DICcount(window_objvoid=None,window_objptr=None):
    global kanmap_linecount
    LTsv_kanmap_drawline(kanmap_linecount); kanmap_linecount+=1
    if kanmap_linecount < kanmap_charsH+1+kandic_charsH:
        LTsv_window_after(kanmap_window,event_b=kanmap_DICcount,event_i="kanmap_DICcount",event_w=10)
    else:
        kanmap_DICfinish()

def kanmap_DICfinish():
    LTsv_widget_settext(kanmap_window,"kanmap")

def LTsv_kanmap_mousepress(window_objvoid=None,window_objptr=None):
    if LTsv_glyph_mousepress(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        pass

def LTsv_kanmap_mousemotion(window_objvoid=None,window_objptr=None):
    global LTsv_mapcursorBF,LTsv_mapcursorAF
    if LTsv_glyph_mousemotion(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        pass

def LTsv_kanmap_mouserelease(window_objvoid=None,window_objptr=None):
    if LTsv_glyph_mouserelease(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        pass

def kanmap_configsave_exit(window_objvoid=None,window_objptr=None):
    LTsv_glyph_picklesave()
    LTsv_draw_canvas_save(kanmap_canvas,"kanmap.png")
    LTsv_window_exit()


LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_tsvpath="LTsv/LTsv_kbd.tsv",LTsv_initmouse=True)
    LTsv_glyph_kbdinit(LTsv_tsvpath="LTsv/LTsv_glyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    LTsv_glyph_kanmapN,LTsv_glyph_kanmapX=LTsv_global_kanmapN(),LTsv_global_kanmapX()
    LTsv_glyph_kbdF=6*LTsv_glyph_kbdsize; LTsv_glyph_kbdW=LTsv_glyph_kbdF*(12+2); LTsv_glyph_kbdH=LTsv_glyph_kbdF*4
    kanmap_charsW,kanmap_charsH=LTsv_glyph_kbdW*12//LTsv_glyph_kbdF,LTsv_glyph_kbdH*(6*2+1)//LTsv_glyph_kbdF
    kanmap_charsY=kanmap_charsH+1; kanmap_dicY=kanmap_charsY*LTsv_glyph_kbdF
    LTsv_glyph_kandic=LTsv_global_kandic(); kanmap_dicsplits=LTsv_glyph_kandic.rstrip('\n').split('\n')
    kandic_charsH=len(kanmap_dicsplits)//kanmap_charsW
    kanmap_chars=[["" for x in range(kanmap_charsW)] for y in range(kanmap_charsH+1+kandic_charsH)]
#    print(kanmap_charsW,kanmap_charsH,kandic_charsH,kanmap_charsW*(kanmap_charsH+1+kandic_charsH))
    kanmap_canvasW,kanmap_canvasH=LTsv_glyph_kbdF*kanmap_charsW,LTsv_glyph_kbdF*(kanmap_charsH+1+kandic_charsH)
    kanmap_kbdX,kanmap_kbdY=LTsv_glyph_kbdW*5,LTsv_glyph_kbdH*6
    kanmap_irohaalphaNX,kanmap_irohaalphaNY=[0]*len(LTsv_global_irohaalpha()),[0]*len(LTsv_global_irohaalpha())
    kanmap_irohaalphaXX,kanmap_irohaalphaXY=[0]*len(LTsv_global_irohaalpha()),[0]*len(LTsv_global_irohaalpha())
    for map_xy in range(len(LTsv_global_irohaalpha())):
        if map_xy < len(LTsv_global_irohaalpha())-3:
            kanmap_irohaalphaNX[map_xy],kanmap_irohaalphaNY[map_xy]=LTsv_glyph_kbdW*(map_xy%12),LTsv_glyph_kbdH*(map_xy//12)+LTsv_glyph_kbdF*2
            kanmap_irohaalphaXX[map_xy],kanmap_irohaalphaXY[map_xy]=kanmap_irohaalphaNX[map_xy],kanmap_irohaalphaNY[map_xy]+LTsv_glyph_kbdH*7
        else:
            kanmap_irohaalphaNX[map_xy],kanmap_irohaalphaNY[map_xy]=LTsv_glyph_kbdW*(map_xy%12),LTsv_glyph_kbdH*(map_xy//12)+LTsv_glyph_kbdF*2
            kanmap_irohaalphaXX[map_xy],kanmap_irohaalphaXY[map_xy]=kanmap_irohaalphaNX[map_xy]+LTsv_glyph_kbdW*9,kanmap_irohaalphaNY[map_xy]+LTsv_glyph_kbdH*0
    kanmap_window=LTsv_window_new(widget_t="kanmap",event_b=kanmap_configsave_exit,widget_w=kanmap_canvasW,widget_h=kanmap_canvasH,event_k=None,event_y=None)
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
    LTsv_draw_selcanvas(kanmap_canvas); LTsv_draw_delete(); LTsv_draw_queue();
    LTsv_glyph_kbddelete(kanmap_canvas)
    LTsv_glyph_kbddraw(kanmap_canvas,kanmap_kbdX,kanmap_kbdY); LTsv_draw_queue();
    kanmap_KBDstart()
    LTsv_window_main(kanmap_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
