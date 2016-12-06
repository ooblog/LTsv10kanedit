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
        LTsv_global_canvasTAG(TkinterTAG="kanmap{0:04}{1:04}".format(map_xy,kanmap_linecount))
        LTsv_draw_glyphskbd(draw_t=kanmap_chars[kanmap_linecount][map_xy][:1],draw_x=map_xy*LTsv_glyph_kbdF,draw_y=drawline_y)
    LTsv_draw_queue()

kanmap_drawwait=20
kanmap_linecount=0
kanmap_linefix=False
def kanmap_KBDstart(drawwait):
    global kanmap_drawwait
    kanmap_drawwait=min(max(drawwait,5),1000)
    LTsv_widget_settext(kanmap_window,"kanmap:pickling kanmap.tsv")
    for map_xy in range(len(LTsv_global_irohaalpha())):
        map_x,map_y=kanmap_irohaalphaNX[map_xy]//LTsv_glyph_kbdF,kanmap_irohaalphaNY[map_xy]//LTsv_glyph_kbdF-2
        for kbd_xy in range(len(LTsv_global_irohatype())):
            kbd_x,kbd_y=map_x+(kbd_xy%12),map_y+(kbd_xy//12)
            kanmap_chars[kbd_y][kbd_x]=LTsv_glyph_kanmapN[LTsv_global_irohaalpha()[map_xy]][kbd_xy]
        map_x,map_y=kanmap_irohaalphaXX[map_xy]//LTsv_glyph_kbdF,kanmap_irohaalphaXY[map_xy]//LTsv_glyph_kbdF-2
        for kbd_xy in range(len(LTsv_global_irohatype())):
            kbd_x,kbd_y=map_x+(kbd_xy%12),map_y+(kbd_xy//12)
            kanmap_chars[kbd_y][kbd_x]=LTsv_glyph_kanmapX[LTsv_global_irohaalpha()[map_xy]][kbd_xy]
    global kanmap_linecount
    kanmap_linecount=0
    LTsv_window_after(kanmap_window,event_b=kanmap_KBDcount,event_i="kanmap_KBDcount",event_w=kanmap_drawwait)

def kanmap_KBDcount(window_objvoid=None,window_objptr=None):
    global kanmap_linecount
    LTsv_kanmap_drawline(kanmap_linecount); kanmap_linecount+=1
    if kanmap_linecount < kanmap_charsH:
        LTsv_window_after(kanmap_window,event_b=kanmap_KBDcount,event_i="kanmap_KBDcount",event_w=kanmap_drawwait)
    else:
        kanmap_KBDfinishDICstart()

def kanmap_checkboxdraw():
    for map_xy in range(len(kanmap_checkboxL)):
        draw_x,draw_y=kanmap_checkboxX[map_xy],kanmap_checkboxY[map_xy]
        LTsv_draw_color("white"); LTsv_draw_bgcolor("white")
        LTsv_draw_glyphsfill(draw_t=kanmap_checkboxT[map_xy][1],draw_x=draw_x+LTsv_glyph_kbdF,draw_y=draw_y+LTsv_glyph_kbdF,draw_f=10,draw_g="漫")
        LTsv_draw_color("black"); LTsv_draw_bgcolor("white")
        LTsv_draw_glyphsfill(draw_t=kanmap_checkboxT[map_xy][kanmap_checkboxC[map_xy]],draw_x=draw_x+LTsv_glyph_kbdF,draw_y=draw_y+LTsv_glyph_kbdF,draw_f=10,draw_g="漫")
        LTsv_draw_color("gray"); LTsv_draw_bgcolor("gray")
        LTsv_draw_polygon(*tuple([draw_x,draw_y,draw_x+LTsv_glyph_kbdW-1,draw_y,draw_x+LTsv_glyph_kbdW-1,draw_y+LTsv_glyph_kbdH-1,draw_x,draw_y+LTsv_glyph_kbdH-1]))
    draw_x,draw_y=LTsv_glyph_kbdW*6,LTsv_glyph_kbdH*6
    LTsv_draw_color("black"); LTsv_draw_bgcolor("white")
    LTsv_draw_glyphsfill(draw_t="find",draw_x=draw_x+LTsv_glyph_kbdF*3,draw_y=draw_y+LTsv_glyph_kbdF,draw_f=10,draw_g="漫")
    LTsv_draw_color("gray"); LTsv_draw_bgcolor("gray")
    LTsv_draw_polygon(*tuple([draw_x+LTsv_glyph_kbdF*2,draw_y,draw_x+LTsv_glyph_kbdW-1,draw_y,draw_x+LTsv_glyph_kbdW-1,draw_y+LTsv_glyph_kbdH-1,draw_x+LTsv_glyph_kbdF*2,draw_y+LTsv_glyph_kbdH-1]))
    LTsv_draw_queue()

def kanmap_KBDfinishDICstart():
    for map_xy in range(len(LTsv_global_irohaalpha())):
        LTsv_draw_glyphskbd(draw_t=LTsv_global_irohaalphaN()[map_xy],draw_x=kanmap_irohaalphaNX[map_xy]-LTsv_glyph_kbdF*2,draw_y=kanmap_irohaalphaNY[map_xy],draw_f=10,draw_g="漫")
        LTsv_draw_glyphskbd(draw_t=LTsv_global_irohaalphaX()[map_xy],draw_x=kanmap_irohaalphaXX[map_xy]-LTsv_glyph_kbdF*2,draw_y=kanmap_irohaalphaXY[map_xy],draw_f=10,draw_g="漫")
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
    LTsv_window_after(kanmap_window,event_b=kanmap_DICcount,event_i="kanmap_DICcount",event_w=kanmap_drawwait)

def kanmap_DICcount(window_objvoid=None,window_objptr=None):
    global kanmap_linecount
    LTsv_kanmap_drawline(kanmap_linecount); kanmap_linecount+=1
    if kanmap_linecount < kandic_charsdicH:
        LTsv_window_after(kanmap_window,event_b=kanmap_DICcount,event_i="kanmap_DICcount",event_w=kanmap_drawwait)
    else:
        kanmap_DICfinish()

def kanmap_DICfinish():
    global kanmap_linefix
    LTsv_widget_settext(kanmap_window,"kanmap")
    kanmap_checkboxdraw()
    kanmap_linefix=True

kanmap_cursorAX,kanmap_cursorAY=0,0; kanmap_cursorBX,kanmap_cursorBY=kanmap_cursorAX,kanmap_cursorAY
kanmap_cursorMX,kanmap_cursorMY=0,0; kanmap_cursorDX,kanmap_cursorDY=0,0;
def LTsv_kanmap_mousecursorXY():
    global kanmap_cursorAX,kanmap_cursorAY,kanmap_cursorBX,kanmap_cursorBY
    kanmap_cursorBX,kanmap_cursorBY=kanmap_cursorAX,kanmap_cursorAY
    LTsv_draw_selcanvas(kanmap_canvas)
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    kanmap_cursorAX,kanmap_cursorAY=min(max(mouseX//LTsv_glyph_kbdF,0),kanmap_charsW),min(max(mouseY//LTsv_glyph_kbdF,0),kandic_charsdicH)

def LTsv_kanmap_mousecursordraw(cursorAX,cursorAY,cursorBX,cursorBY):
    if len(kanmap_chars[cursorBY][cursorBX]) > 0:
        if LTsv_GUI == LTsv_GUI_GTK2:
            LTsv_draw_color("white"); LTsv_draw_bgcolor("white")
            draw_x,draw_y=cursorBX*LTsv_glyph_kbdF,cursorBY*LTsv_glyph_kbdF
            LTsv_draw_polygonfill(*tuple([draw_x,draw_y,draw_x+LTsv_glyph_kbdF,draw_y,draw_x+LTsv_glyph_kbdF,draw_y+LTsv_glyph_kbdF,draw_x,draw_y+LTsv_glyph_kbdF]))
        elif LTsv_GUI == LTsv_GUI_Tkinter:
            LTsv_deleteTAG("kanmap{0:04}{1:04}".format(cursorBX,cursorBY))
        if ( cursorBX == kanmap_cursorMX and cursorBY == kanmap_cursorMY ) or ( cursorBX == kanmap_cursorDX and cursorBY == kanmap_cursorDY ):
            LTsv_draw_color("IndianRed"); LTsv_draw_bgcolor("IndianRed")
            LTsv_draw_polygonfill(*tuple([draw_x,draw_y,draw_x+LTsv_glyph_kbdF,draw_y,draw_x+LTsv_glyph_kbdF,draw_y+LTsv_glyph_kbdF,draw_x,draw_y+LTsv_glyph_kbdF]))
            LTsv_draw_color("white"); LTsv_draw_bgcolor("IndianRed")
            LTsv_draw_glyphskbd(draw_t=kanmap_chars[cursorBY][cursorBX][:1],draw_x=cursorBX*LTsv_glyph_kbdF,draw_y=cursorBY*LTsv_glyph_kbdF)
        else:
            LTsv_draw_color("black"); LTsv_draw_bgcolor("white")
            LTsv_draw_glyphskbd(draw_t=kanmap_chars[cursorBY][cursorBX][:1],draw_x=cursorBX*LTsv_glyph_kbdF,draw_y=cursorBY*LTsv_glyph_kbdF)
    if len(kanmap_chars[cursorAY][cursorAX]) > 0:
        LTsv_global_canvasTAG(TkinterTAG="kanmap{0:04}{1:04}".format(cursorAX,cursorAY))
        draw_x,draw_y=cursorAX*LTsv_glyph_kbdF,cursorAY*LTsv_glyph_kbdF
        LTsv_draw_color("black"); LTsv_draw_bgcolor("black")
        LTsv_draw_polygonfill(*tuple([draw_x,draw_y,draw_x+LTsv_glyph_kbdF,draw_y,draw_x+LTsv_glyph_kbdF,draw_y+LTsv_glyph_kbdF,draw_x,draw_y+LTsv_glyph_kbdF]))
        LTsv_draw_color("white"); LTsv_draw_bgcolor("white")
        LTsv_draw_glyphskbd(draw_t=kanmap_chars[cursorAY][cursorAX][:1],draw_x=cursorAX*LTsv_glyph_kbdF,draw_y=cursorAY*LTsv_glyph_kbdF)
    LTsv_draw_queue()

def LTsv_kanmap_mousepress(window_objvoid=None,window_objptr=None):
    if LTsv_glyph_mousepress(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        if kanmap_linefix:
            LTsv_kanmap_mousecursorXY()
            LTsv_kanmap_mousecursordraw(kanmap_cursorAX,kanmap_cursorAY,kanmap_cursorBX,kanmap_cursorBY)

def LTsv_kanmap_mousemotion(window_objvoid=None,window_objptr=None):
    if LTsv_glyph_mousemotion(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        LTsv_kanmap_mousecursorXY()
        if kanmap_linefix == True and (kanmap_cursorBX != kanmap_cursorAX or kanmap_cursorBY != kanmap_cursorAY):
            LTsv_kanmap_mousecursordraw(kanmap_cursorAX,kanmap_cursorAY,kanmap_cursorBX,kanmap_cursorBY)

def LTsv_kanmap_mouserelease(window_objvoid=None,window_objptr=None):
    global kanmap_cursorMX,kanmap_cursorMY,kanmap_cursorDX,kanmap_cursorDY
    global kanmap_chars
    if LTsv_glyph_mouserelease(kanmap_canvas,kanmap_kbdX,kanmap_kbdY) == LTsv_global_kbdcursorNone():
        if kanmap_linefix:
            LTsv_kanmap_mousecursorXY()
            LTsv_kanmap_mousecursordraw(kanmap_cursorAX,kanmap_cursorAY,kanmap_cursorBX,kanmap_cursorBY)
            check_x,check_y=(kanmap_cursorAX*LTsv_glyph_kbdF)//LTsv_glyph_kbdW,(kanmap_cursorAY*LTsv_glyph_kbdF)//LTsv_glyph_kbdH
            if len(kanmap_chars[kanmap_cursorAY][kanmap_cursorAX]) > 0:
                LTsv_widget_settext(kanmap_clipboard,kanmap_chars[kanmap_cursorAY][kanmap_cursorAX][:1])
                if kanmap_cursorAY < kanmap_charsH:
                    cursorMX,cursorMY=kanmap_cursorMX,kanmap_cursorMY
                    kanmap_cursorMX,kanmap_cursorMY=kanmap_cursorAX,kanmap_cursorAY
                    LTsv_kanmap_mousecursordraw(kanmap_cursorMX,kanmap_cursorMY,cursorMX,cursorMY)
                    if kanmap_checkboxC[kanmap_checkboxN["swap"]] != 0:
                        if len(kanmap_chars[kanmap_cursorMY][kanmap_cursorMX]) > 0 and len(kanmap_chars[cursorMY][cursorMX]) > 0:
                            kanmap_chars[kanmap_cursorMY][kanmap_cursorMX],kanmap_chars[cursorMY][cursorMX]=kanmap_chars[cursorMY][cursorMX],kanmap_chars[kanmap_cursorMY][kanmap_cursorMX]
                            LTsv_kanmap_mousecursordraw(kanmap_cursorMX,kanmap_cursorMY,cursorMX,cursorMY)
                            kanmap_cursorMX,kanmap_cursorMY=0,0
                            LTsv_kanmap_mousecursordraw(kanmap_cursorMX,kanmap_cursorMY,cursorMX,cursorMY)
                if kanmap_cursorAY >= kanmap_charsH:
                    cursorDX,cursorDY=kanmap_cursorDX,kanmap_cursorDY
                    kanmap_cursorDX,kanmap_cursorDY=kanmap_cursorAX,kanmap_cursorAY
                    LTsv_kanmap_mousecursordraw(kanmap_cursorDX,kanmap_cursorDY,cursorDX,cursorDY)
                    if kanmap_checkboxC[kanmap_checkboxN["rewrite"]] != 0:
                        if len(kanmap_chars[kanmap_cursorMY][kanmap_cursorMX]) > 0 and len(kanmap_chars[kanmap_cursorDY][kanmap_cursorDX]) > 0:
                            kanmap_chars[kanmap_cursorMY][kanmap_cursorMX]=kanmap_chars[kanmap_cursorDY][kanmap_cursorDX]
                            LTsv_kanmap_mousecursordraw(kanmap_cursorDX,kanmap_cursorDY,kanmap_cursorMX,kanmap_cursorMY)
            else:
                if ( check_x in kanmap_checkboxL ) and check_y == 6:
                    for map_xy in kanmap_checkboxL:
                        if map_xy == check_x:
                            kanmap_checkboxC[kanmap_checkboxL.index(map_xy)]=1 if kanmap_checkboxC[kanmap_checkboxL.index(map_xy)] == 0 else 0
                        else:
                            kanmap_checkboxC[kanmap_checkboxL.index(map_xy)]=0
                    kanmap_checkboxdraw()
                if check_x ==6 and check_y == 6:
                    LTsv_kanmap_find()

def LTsv_kanmap_keypress(window_objvoid=None,window_objptr=None):
    LTsv_kanmap_kbdinput(LTsv_glyph_calctypelimited(kanmap_canvas,kanmap_kbdX,kanmap_kbdY))

def LTsv_kanmap_keyrelease(window_objvoid=None,window_objptr=None):
    LTsv_kanmap_keypress()

def LTsv_kanmap_kbdinput(kbdinput):
    kanmap_clipfind=kbdinput[:1]
    LTsv_widget_settext(kanmap_clipboard,kanmap_clipfind)
    if kanmap_checkboxC[kanmap_checkboxN["kbdfind"]] != 0:
        LTsv_kanmap_find()

def LTsv_kanmap_find():
    global kanmap_cursorMX,kanmap_cursorMY,kanmap_cursorDX,kanmap_cursorDY
    kanmap_clipfind=LTsv_widget_gettext(kanmap_clipboard)[:1]
    if len(kanmap_clipfind) > 0:
        cursorDX,cursorDY=kanmap_cursorDX,kanmap_cursorDY; cursorMX,cursorMY=kanmap_cursorMX,kanmap_cursorMY
        kanmap_cursorMX,kanmap_cursorMY=0,0; kanmap_cursorDX,kanmap_cursorDY=0,0;
        for drawline_y in range(kandic_charsdicH):
            if kanmap_clipfind in kanmap_chars[drawline_y]:
                if drawline_y < kanmap_charsH:
                    if kanmap_cursorMX == 0:
                        kanmap_cursorMX,kanmap_cursorMY=kanmap_chars[drawline_y].index(kanmap_clipfind),drawline_y
                        LTsv_kanmap_mousecursordraw(kanmap_cursorMX,kanmap_cursorMY,cursorMX,cursorMY)
                        LTsv_kanmap_mousecursordraw(kanmap_cursorAX,kanmap_cursorAY,kanmap_cursorMX,kanmap_cursorMY)
                if drawline_y > kanmap_charsH:
                    if kanmap_cursorDY == 0:
                        kanmap_cursorDX,kanmap_cursorDY=kanmap_chars[drawline_y].index(kanmap_clipfind),drawline_y
                        LTsv_kanmap_mousecursordraw(kanmap_cursorDX,kanmap_cursorDY,cursorDX,cursorDY)
                        LTsv_kanmap_mousecursordraw(kanmap_cursorAX,kanmap_cursorAY,kanmap_cursorDX,kanmap_cursorDY)
        LTsv_glyph_kbdfind(kanmap_clipfind)
        LTsv_glyph_kbddelete(kanmap_canvas); LTsv_glyph_kbddraw(kanmap_canvas,kanmap_kbdX,kanmap_kbdY); LTsv_draw_queue();

def kanmap_configsave_exit(window_objvoid=None,window_objptr=None):
    LTsv_glyph_picklesave()
    LTsv_draw_canvas_save(kanmap_canvas,"kanmap.png")
    if kanmap_checkboxC[kanmap_checkboxN["update"]] != 0:
        pass
    LTsv_window_exit()
#LTsv_global_kanmappath():                         return os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kanmapname)
#LTsv_global_kandicpath():                         return os.path.normpath(LTsv_glyph_ltsvdir+LTsv_glyph_kandicname)

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_tsvpath="LTsv/LTsv_kbd.tsv",LTsv_initmouse=True)
    LTsv_glyph_kbdinit(LTsv_tsvpath="LTsv/LTsv_glyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    LTsv_glyph_kanmapN,LTsv_glyph_kanmapX=LTsv_global_kanmapN(),LTsv_global_kanmapX()
    LTsv_glyph_kbdF=6*LTsv_glyph_kbdsize; LTsv_glyph_kbdW=LTsv_glyph_kbdF*(12+2); LTsv_glyph_kbdH=LTsv_glyph_kbdF*4
    kanmap_charsW,kanmap_charsH=LTsv_glyph_kbdW*12//LTsv_glyph_kbdF,LTsv_glyph_kbdH*(6*2+1)//LTsv_glyph_kbdF
    kanmap_charsY=kanmap_charsH+1; kanmap_dicY=kanmap_charsY*LTsv_glyph_kbdF
    LTsv_glyph_kandic=LTsv_global_kandic(); kanmap_dicsplits=LTsv_glyph_kandic.rstrip('\n').split('\n')
    kandic_charsH=int(math.ceil(len(kanmap_dicsplits)/kanmap_charsW))
    kandic_charsdicH=kanmap_charsH+1+kandic_charsH
    kanmap_chars=[["" for x in range(kanmap_charsW)] for y in range(kandic_charsdicH)]
#    print(kanmap_charsW,kanmap_charsH,kandic_charsH,kanmap_charsW*(kandic_charsdicH))
    kanmap_canvasW,kanmap_canvasH=LTsv_glyph_kbdF*kanmap_charsW,LTsv_glyph_kbdF*(kandic_charsdicH)
    kanmap_kbdX,kanmap_kbdY=LTsv_glyph_kbdW*5,LTsv_glyph_kbdH*6
    kanmap_irohaalphaNX,kanmap_irohaalphaNY=[0]*len(LTsv_global_irohaalpha()),[0]*len(LTsv_global_irohaalpha())
    kanmap_irohaalphaXX,kanmap_irohaalphaXY=[0]*len(LTsv_global_irohaalpha()),[0]*len(LTsv_global_irohaalpha())
    for map_xy in range(len(LTsv_global_irohaalpha())):
        if map_xy < len(LTsv_global_irohaalpha())-3:
            kanmap_irohaalphaNX[map_xy],kanmap_irohaalphaNY[map_xy]=LTsv_glyph_kbdW*(map_xy%12)+LTsv_glyph_kbdF*2,LTsv_glyph_kbdH*(map_xy//12)+LTsv_glyph_kbdF*2
            kanmap_irohaalphaXX[map_xy],kanmap_irohaalphaXY[map_xy]=kanmap_irohaalphaNX[map_xy],kanmap_irohaalphaNY[map_xy]+LTsv_glyph_kbdH*7
        else:
            kanmap_irohaalphaNX[map_xy],kanmap_irohaalphaNY[map_xy]=LTsv_glyph_kbdW*(map_xy%12)+LTsv_glyph_kbdF*2,LTsv_glyph_kbdH*(map_xy//12)+LTsv_glyph_kbdF*2
            kanmap_irohaalphaXX[map_xy],kanmap_irohaalphaXY[map_xy]=kanmap_irohaalphaNX[map_xy]+LTsv_glyph_kbdW*9,kanmap_irohaalphaNY[map_xy]+LTsv_glyph_kbdH*0
    kanmap_checkboxL=[3,4,7,8]; kanmap_checkboxT=[["update☐","update☑"],["kbdfind☐","kbdfind☑"],["rewrite☐","rewrite☑"],["swap☐","swap☑"]]; kanmap_checkboxN={"update":0,"kbdfind":1,"rewrite":2,"swap":3}
    kanmap_checkboxX,kanmap_checkboxY,kanmap_checkboxC=[0]*len(kanmap_checkboxL),[0]*len(kanmap_checkboxL),[0]*len(kanmap_checkboxL)
    kanmap_checkboxC[kanmap_checkboxN["kbdfind"]]=1
    for map_xy in range(len(kanmap_checkboxL)):
        kanmap_checkboxX[map_xy],kanmap_checkboxY[map_xy]=kanmap_checkboxL[map_xy]*LTsv_glyph_kbdW,LTsv_glyph_kbdH*6
    kanmap_window=LTsv_window_new(widget_t="kanmap",event_b=kanmap_configsave_exit,widget_w=kanmap_canvasW,widget_h=kanmap_canvasH,event_k=LTsv_kanmap_keypress,event_y=LTsv_kanmap_keyrelease)
    kanmap_canvas=LTsv_canvas_new(kanmap_window,widget_x=0,widget_y=0,widget_w=kanmap_canvasW,widget_h=kanmap_canvasH,
     event_p=LTsv_kanmap_mousepress,event_m=LTsv_kanmap_mousemotion,event_r=LTsv_kanmap_mouserelease,event_e=None,event_l=None,event_w=50)
    kanmap_clipboard=LTsv_clipboard_new(kanmap_window)
    LTsv_widget_showhide(kanmap_window,True)
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    LTsv_deleteTAG=LTsv_draw_deleteTAG_shell(LTsv_GUI)
    LTsv_glyph_tapcallback_shell(kanmap_canvas,LTsv_kanmap_kbdinput)
    LTsv_draw_selcanvas(kanmap_canvas); LTsv_draw_delete(); LTsv_draw_queue();
    LTsv_glyph_kbddelete(kanmap_canvas); LTsv_glyph_kbddraw(kanmap_canvas,kanmap_kbdX,kanmap_kbdY); LTsv_draw_queue();
    kanmap_KBDstart(5 if os.path.isfile(LTsv_global_picklepath()) else 50)
    LTsv_window_main(kanmap_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
