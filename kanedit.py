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

kanedit_window=None
kanedit_getkbdnames,kanedit_getkbdkanas="",""
kanedit_W,kanedit_H,kanedit_RS=LTsv_global_glyphkbdW(),LTsv_global_glyphkbdH(),False
kanedit_ltsv,kanedit_config="",""
kanedit_texteditfilename,kanedit_textvalue="",""
kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize="black","#FFF9FA",10
kanmemo_fontcolor,kanmemo_bgcolorr,kanmemo_fontsize="black","FFFFF3",LTsv_global_glyphkbdH()//2

def kanedit_resizeredraw(window_objvoid=None,window_objptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    window_w,window_h=LTsv_window_wh(kanedit_window)
    if kanedit_W!=window_w or kanedit_H!=window_h:
        kanedit_W,kanedit_H=window_w,window_h
        LTsv_editcanvas_kbdXY(kanedit_canvas,kbd_x=kanedit_W-LTsv_global_glyphkbdW(),kbd_y=kanedit_H-LTsv_global_glyphkbdH())
        LTsv_window_after(kanedit_canvas,event_b=kanedit_resizeredraw,event_i="kanedit_resizeredraw",event_w=50)
    else:
        kanedit_W,kanedit_H=window_w,window_h
        kanedit_RS=False

def kanedit_resize(callback_void=None,callback_ptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    if kanedit_RS == False:
        kanedit_RS=True
        kanedit_resizeredraw()

def kanfont_memo_copy(clippaste):
    LTsv_widget_settext(kanedit_clipboard,clippaste)

def kanedit_memo_paste():
    clippaste=LTsv_widget_gettext(kanedit_clipboard)
    return clippaste

def kanfont_memo_eval(calc_value):
    calc_V=LTsv_evaltext(calc_value)
    return calc_V

def kanedit_keypress(window_objvoid=None,window_objptr=None):
    LTsv_glyph_typepress(kanedit_canvas,kanedit_W-LTsv_global_glyphkbdW(),kanedit_H-LTsv_global_glyphkbdH())

def kanedit_keyrelease(window_objvoid=None,window_objptr=None):
    LTsv_glyph_typerelease(kanedit_canvas,kanedit_W-LTsv_global_glyphkbdW(),kanedit_H-LTsv_global_glyphkbdH())

def kanedit_filedialog_open():
    print("kanedit_filedialog_open")
    LTsv_widget_showhide(kanedit_filedialog,True)

def kanedit_filedialog_response(window_objvoid=None,window_objptr=None):
    kanedit_textload(LTsv_widget_geturi(kanedit_filedialog))
    LTsv_widget_showhide(kanedit_filedialog,False)
    kanedit_resize(); kanedit_resizeredraw()

def kanedit_textload(filename):
    global kanedit_window
    global kanedit_texteditfilename,kanedit_textvalue
    kanedit_texteditfilename=filename
    LTsv_widget_settext(kanedit_window,widget_t="kanedit:{0}".format(kanedit_texteditfilename))
    kanedit_textvalue=LTsv_loadfile(kanedit_texteditfilename)
    LTsv_widget_settext(kanedit_canvas,widget_t=kanedit_textvalue)

def kanedit_configload():
    global kanedit_W,kanedit_H,kanedit_RS
    global kanedit_ltsv,kanedit_config
    global kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize
    global kanmemo_fontcolor,kanmemo_bgcolorr,kanmemo_fontsize
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_resizeW,kanedit_resizeH=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"window_size"),"width","height"))
    kanedit_W,kanedit_H=min(max(LTsv_intstr0x(kanedit_resizeW),LTsv_global_glyphkbdW()),LTsv_screen_w(kanedit_window)),min(max(LTsv_intstr0x(kanedit_resizeH),LTsv_global_glyphkbdH()),LTsv_screen_h(kanedit_window))
    kanedit_fontcolor,kanedit_bgcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"edit_colors"),"font","bg"))
    kanedit_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"edit_fontsize",str(kanedit_fontsize))),5),100)
    kanedit_texteditfilename=LTsv_readlinerest(kanedit_config,"edit_last","kanedit.txt")
    kanedit_textload(kanedit_texteditfilename)
    kanmemo_fontcolor,kanmemo_bgcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"memo_colors"),"font","bg"))
    kanmemo_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"memo_fontsize",str(kanedit_fontsize))),5),100)
    LTsv_editcanvas_color(kanedit_canvas,UF=kanmemo_fontcolor,UB=kanmemo_bgcolor,TF=kanedit_fontcolor,TB=kanedit_bgcolor)
    LTsv_editcanvas_fontsize(kanedit_canvas,US=kanmemo_fontsize,TS=kanedit_fontsize)
    LTsv_widget_seturi(kanedit_canvas,LTsv_readlinerest(kanedit_config,"memo_entry"))

def kanedit_exit_configsave(window_objvoid=None,window_objptr=None):
    global kanedit_ltsv,kanedit_config
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_config=LTsv_pushlinerest(kanedit_config,"edit_last",kanedit_texteditfilename)
    kanedit_config=LTsv_pushlinerest(kanedit_config,"memo_entry",LTsv_widget_geturi(kanedit_canvas))
    kanedit_config=LTsv_pushlinerest(kanedit_config,"window_size","width:{0}\theight:{1}".format(kanedit_W,kanedit_H))
    kanedit_ltsv=LTsv_putpage(kanedit_ltsv,"kanedit",kanedit_config)
    LTsv_savefile("kanedit.tsv",kanedit_ltsv)
    LTsv_glyph_picklesave()
    LTsv_window_exit()
kanedit_exit_configsave_cbk=LTsv_CALLBACLTYPE(kanedit_exit_configsave)

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_tsvpath="LTsv/LTsv_kbd.tsv",LTsv_initmouse=True)
    LTsv_glyph_kbdinit(LTsv_tsvpath="LTsv/LTsv_glyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    kanedit_window=LTsv_window_new(widget_t="kanedit",event_b=kanedit_exit_configsave,widget_w=kanedit_W,widget_h=kanedit_H,event_z=kanedit_resize,event_k=kanedit_keypress,event_y=kanedit_keyrelease)
    kanedit_canvas=LTsv_editcanvas_new(kanedit_window,kbd_k=kanfont_memo_eval,clip_c=kanfont_memo_copy,clip_v=kanedit_memo_paste,clip_o=kanedit_filedialog_open,widget_x=0,widget_y=0,widget_w=LTsv_screen_w(kanedit_window),widget_h=LTsv_screen_h(kanedit_window),event_w=50)
    kanedit_configload()
    LTsv_window_resize(kanedit_window,kanedit_W,kanedit_H)
    kanedit_clipboard=LTsv_clipboard_new(kanedit_window)
    kanedit_filedialog=LTsv_filedialog_new(kanedit_window,widget_t="File Open",dialog_t=0,event_b=kanedit_filedialog_response)
    LTsv_widget_showhide(kanedit_window,True)
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    LTsv_editcanvas_kbdXY(kanedit_canvas,kbd_x=kanedit_W-LTsv_global_glyphkbdW(),kbd_y=kanedit_H-LTsv_global_glyphkbdH())
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
