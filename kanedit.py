#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
sys.path.append("LTsv")
from LTsv_printf  import *
from LTsv_file    import *
#from LTsv_time    import *
#from LTsv_calc    import *
#from LTsv_joy     import *
from LTsv_kbd     import *
from LTsv_gui     import *
from LTsv_glyph  import *

kanedit_W,kanedit_H,kanedit_RS=LTsv_global_glyphkbdW(),LTsv_global_glyphkbdH(),False
kanedit_ltsv,kanedit_config="",""
kanedit_texteditfilename,kanedit_textvalue="",""
kanedit_cursorY=0
kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize,kanedit_fontstyle="black","#FFF9FA",10,"漫"

def kanedit_draw():
    LTsv_draw_selcanvas(kanedit_canvas); LTsv_draw_delete(); LTsv_glyph_calcdelete(kanedit_canvas)
    LTsv_draw_color(kanedit_bgcolor); LTsv_draw_polygonfill(0,0,kanedit_W,0,kanedit_W,kanedit_H,0,kanedit_H)
    kanedit_textsplit=kanedit_textvalue.split('\n')
    kanedit_lineY=0
    for kanedit_pos,kanedit_line in enumerate(kanedit_textsplit):
        if kanedit_pos == kanedit_cursorY:
            LTsv_glyph_calcresize(kanedit_canvas,calculatorY=kanedit_lineY,calculatorW=kanedit_W,calculatorT=kanedit_line,calculatorTX=None,calculatorTC=None)
            LTsv_glyph_calcdraw(kanedit_canvas)
            kanedit_lineY+=LTsv_global_glyphkbdH()+1  #kanedit_lineY+=24+1
            LTsv_draw_selcanvas(kanedit_canvas)
        else:
            LTsv_draw_color(kanedit_fontcolor); LTsv_draw_bgcolor(kanedit_bgcolor)
            LTsv_draw_glyphsfill(draw_t=kanedit_line,draw_x=0,draw_y=kanedit_lineY,draw_f=kanedit_fontsize,draw_g=kanedit_fontstyle)
            kanedit_lineY+=kanedit_fontsize
    LTsv_draw_queue()

def kanedit_resizeredraw(window_objvoid=None,window_objptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    window_w,window_h=LTsv_window_wh(kanedit_window)
    if kanedit_W!=window_w or kanedit_H!=window_h:
        kanedit_W,kanedit_H=window_w,window_h
        kanedit_draw()
        LTsv_window_after(kanedit_window,event_b=kanedit_resizeredraw,event_i="kanedit_resizeredraw",event_w=50)
    else:
        kanedit_W,kanedit_H=window_w,window_h
        kanedit_RS=False

def kanedit_resize(callback_void=None,callback_ptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    if kanedit_RS == False:
        kanedit_RS=True
        kanedit_resizeredraw()

def kanfont_memo_eval(calc_value):
    calc_V=LTsv_evaltext(calc_value)
    return calc_V

def kanedit_calculatormousepress(window_objvoid=None,window_objptr=None):
    if not LTsv_glyph_calcpress(kanedit_canvas):
        pass

def kanedit_calculatormousemotion(window_objvoid=None,window_objptr=None):
    if not LTsv_glyph_calcmotion(kanedit_canvas):
        pass

def kanedit_calculatormouserelease(window_objvoid=None,window_objptr=None):
    if not LTsv_glyph_calcrelease(kanedit_canvas):
        pass

def kanedit_calculatormouseleave(window_objvoid=None,window_objptr=None):
    global kanedit_texteditfilename,kanedit_textvalue,kanedit_cursorY
    kanedit_textsplit=kanedit_textvalue.split('\n')
    kanedit_textsplit[kanedit_cursorY]= LTsv_glyph_calcresize(kanedit_canvas)
    kanedit_textvalue="\n".join(kanedit_textsplit)
    LTsv_glyph_calcleave(kanedit_canvas)

def kanedit_calculatormouseenter(window_objvoid=None,window_objptr=None):
    LTsv_glyph_calcenter(kanedit_canvas)

def kanedit_calculatormouseinput(calculatormouseinput):
    kanedit_calculatoredit(LTsv_glyph_calcinput(kanedit_canvas,calculatormouseinput))

def kanedit_keypress(window_objvoid=None,window_objptr=None):
    kanedit_calculatoredit(LTsv_glyph_calctype(kanedit_canvas))

def kanedit_keyrelease(window_objvoid=None,window_objptr=None):
    kanedit_keypress()

def kanedit_calculatoredit(calculatormouseinput):
    global kanedit_texteditfilename,kanedit_textvalue,kanedit_cursorY
    if calculatormouseinput == "":
        LTsv_glyph_calcresize(kanedit_canvas,calculatorT=LTsv_evaltext(LTsv_glyph_calcresize(kanedit_canvas)))
    elif calculatormouseinput == "":
        LTsv_glyph_calcinput(kanedit_canvas,"\t")
    elif calculatormouseinput == "":
        LTsv_glyph_calcinput(kanedit_canvas,"    ")
    elif calculatormouseinput == "":
        LTsv_glyph_calcinput(kanedit_canvas," ")
    elif calculatormouseinput == "":
        LTsv_glyph_calcinput(kanedit_canvas,"　")
    elif calculatormouseinput == "":
        kanedit_cursorY=min(kanedit_cursorY+1,LTsv_readlinedeno(kanedit_textvalue))
        LTsv_glyph_calcresize(kanedit_canvas,calculatorY=kanedit_cursorY*10)
        kanedit_draw()
    elif calculatormouseinput == "":
        kanedit_cursorY=max(kanedit_cursorY-1,0)
        LTsv_glyph_calcresize(kanedit_canvas,calculatorY=kanedit_cursorY*10)
        kanedit_draw()
    elif calculatormouseinput == "":
        evaltext=LTsv_evaltext(LTsv_glyph_calcresize(kanedit_canvas))
        LTsv_glyph_calcresize(kanedit_canvas,calculatorT=evaltext)
    LTsv_glyph_calcinput(kanedit_canvas)

def kanedit_filedialog_open():
    print("kanedit_filedialog_open")
    LTsv_widget_showhide(kanedit_filedialog,True)

def kanedit_filedialog_response(window_objvoid=None,window_objptr=None):
    kanedit_textload(LTsv_widget_geturi(kanedit_filedialog))
    LTsv_widget_showhide(kanedit_filedialog,False)
    kanedit_resize(); kanedit_draw()

def kanedit_textload(filename):
    global kanedit_texteditfilename,kanedit_textvalue,kanedit_cursorY
    kanedit_texteditfilename=filename
    LTsv_widget_settext(kanedit_window,widget_t="kanedit:{0}".format(kanedit_texteditfilename))
    kanedit_textvalue=LTsv_loadfile(kanedit_texteditfilename)

def kanedit_configload():
    global kanedit_W,kanedit_H,kanedit_RS
    global kanedit_ltsv,kanedit_config
    global kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize,kanedit_fontstyle
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_resizeW,kanedit_resizeH=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"window_size"),"width","height"))
    kanedit_W,kanedit_H=min(max(LTsv_intstr0x(kanedit_resizeW),LTsv_global_glyphkbdW()),LTsv_screen_w(kanedit_window)),min(max(LTsv_intstr0x(kanedit_resizeH),LTsv_global_glyphkbdH()),LTsv_screen_h(kanedit_window))
    kanedit_fontcolor,kanedit_bgcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"edit_colors"),"font","bg"))
    kanedit_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"edit_fontsize",str(kanedit_fontsize))),5),100)
    kanedit_fontstyle=LTsv_readlinerest(kanedit_config,"edit_fontstyle",kanedit_fontstyle); kanedit_fontstyle=kanedit_fontstyle if kanedit_fontstyle in LTsv_global_glyphtype() else "漫"
    kanedit_texteditfilename=LTsv_readlinerest(kanedit_config,"edit_last","kanedit.txt")
    kanedit_textload(kanedit_texteditfilename)

def kanedit_exit_configsave(window_objvoid=None,window_objptr=None):
    global kanedit_ltsv,kanedit_config
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_config=LTsv_pushlinerest(kanedit_config,"window_size","width:{0}\theight:{1}".format(kanedit_W,kanedit_H))
    kanedit_config=LTsv_pushlinerest(kanedit_config,"edit_last",kanedit_texteditfilename)
    kanedit_ltsv=LTsv_putpage(kanedit_ltsv,"kanedit",kanedit_config)
    LTsv_savefile("kanedit.tsv",kanedit_ltsv)
#    LTsv_glyph_picklesave()
    LTsv_window_exit()
kanedit_exit_configsave_cbk=LTsv_CALLBACLTYPE(kanedit_exit_configsave)

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_tsvpath="LTsv/LTsv_kbd.tsv",LTsv_initmouse=True)
    LTsv_glyph_kbdinit(LTsv_tsvpath="LTsv/LTsv_glyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    kanedit_window=LTsv_window_new(widget_t="kanedit",event_b=kanedit_exit_configsave,widget_w=kanedit_W,widget_h=kanedit_H,event_z=kanedit_resize,event_k=kanedit_keypress,event_y=kanedit_keyrelease)
    kanedit_canvas=LTsv_canvas_new(kanedit_window,widget_x=0,widget_y=0,widget_w=LTsv_screen_w(kanedit_window),widget_h=LTsv_screen_h(kanedit_window),
     event_p=kanedit_calculatormousepress,event_m=kanedit_calculatormousemotion,event_r=kanedit_calculatormouserelease,event_e=kanedit_calculatormouseenter,event_l=kanedit_calculatormouseleave,event_w=50)
    kanedit_configload()
    LTsv_window_resize(kanedit_window,kanedit_W,kanedit_H)
    kanedit_clipboard=LTsv_clipboard_new(kanedit_window)
    kanedit_filedialog=LTsv_filedialog_new(kanedit_window,widget_t="File Open",dialog_t=0,event_b=kanedit_filedialog_response)
    LTsv_widget_showhide(kanedit_window,True)
    LTsv_glyph_calcsetup(kanedit_canvas,calculatorX=0,calculatorY=0,calculatorW=kanedit_W,calculatorH=LTsv_global_glyphkbdH(),calculatorC=kanedit_clipboard,calculatorB=kanedit_calculatormouseinput,calculatorT="debug_calculator")
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    kanedit_draw()
    LTsv_glyph_calcresize(kanedit_canvas); LTsv_glyph_calcleave(kanedit_canvas);
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
