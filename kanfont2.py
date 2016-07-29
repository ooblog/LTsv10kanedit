#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
sys.path.append("LTsv")
from LTsv_printf import *
from LTsv_file   import *
#from LTsv_time   import *
#from LTsv_calc   import *
#from LTsv_joy    import *
from LTsv_kbd    import *
from LTsv_gui    import *

tinykbd_dictype=    ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","漫","幅"]
PSfont_ZW,PSfont_CW,PSchar_ZW,PSchar_CW=1024,624,1000,600
kanfont_ltsv,kanfont_config="",""
kanfont_dicname,kanfont_mapname,kanfont_svgname,kanfont_fontname,kanfont_fontwidths="kanchar.tsv","kanmap.tsv","kanfont.svg","kantray5x5comic","1024,624"
kanfont_fontgrid,kanfont_fontinner,kanfont_gridimage=25,0,"kanfont_grid25_199.png"
kanfont_max=0x2ffff  # if LTsv_GUI != "Tkinter" else 0xffff
kanfont_dictype_label,kanfont_dictype_entry=[None]*(len(tinykbd_dictype)+1),[None]*(len(tinykbd_dictype)+1)

def kanfont_codespin_shell(window_objvoid=None,window_objptr=None):
    if LTsv_widget_getnumber(kanfont_code_scale) != LTsv_widget_getnumber(kanfont_code_spin):
        LTsv_widget_setnumber(kanfont_code_scale,LTsv_widget_getnumber(kanfont_code_spin))
    return

def kanfont_codescale_shell(window_objvoid=None,window_objptr=None):
    if LTsv_widget_getnumber(kanfont_code_spin) != LTsv_widget_getnumber(kanfont_code_scale):
        LTsv_widget_setnumber(kanfont_code_spin,LTsv_widget_getnumber(kanfont_code_scale))
        LTsv_widget_settext(kanfont_code_label,hex(LTsv_widget_getnumber(kanfont_code_scale)))
    return

def kanfont_configload():
    global kanfont_ltsv,kanfont_config
    global kanfont_fontgrid,kanfont_fontinner,kanfont_gridimage
    kanfont_ltsv=LTsv_loadfile("kanfont.tsv")
    kanfont_config=LTsv_getpage(kanfont_ltsv,"kanfont")
    kanfont_gridimage=LTsv_readlinerest(kanfont_config,"gridimage",kanfont_gridimage)

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    kanfont_configload()
    kanfont_fontsize_entry=10;    kanfont_font_entry="{0},{1}".format(kanfont_fontname,kanfont_fontsize_entry); kanfont_label_WH=kanfont_fontsize_entry*2
    kanfont_fontsize_scale=40;    kanfont_font_scale="{0},{1}".format(kanfont_fontname,kanfont_fontsize_scale); kanfont_scale_WH=kanfont_fontsize_scale*2
    kanfont_fontsize_keyboard=12; kanfont_font_keyboard="{0},{1}".format(kanfont_fontname,kanfont_fontsize_keyboard)
    kanfont_fontsize_grid=8;      kanfont_font_grid="{0},{1}".format(kanfont_fontname,kanfont_fontsize_grid)
    kanfont_scale_W,kanfont_entry_W=kanfont_scale_WH,400; kanfont_canvas_WH=PSfont_ZW//2
    kanfont_canvas_X=kanfont_scale_W; kanfont_label_X=kanfont_canvas_X+kanfont_canvas_WH; kanfont_entry_X=kanfont_label_X+kanfont_label_WH; kanfont_W=kanfont_entry_X+kanfont_entry_W
    kanfont_H=kanfont_canvas_WH+kanfont_label_WH*2; kanfont_scale_H=kanfont_H-kanfont_scale_WH-kanfont_label_WH-kanfont_label_WH; kanfont_scale_X,kanfont_scale_Y=0,kanfont_scale_WH
    kanfont_window=LTsv_window_new(widget_t="kanfont",event_b=LTsv_window_exit,widget_w=kanfont_W,widget_h=kanfont_H)
#    kanfont_char_entry=LTsv_entry_new(kanfont_window,widget_t="",widget_x=0,widget_y=0,widget_w=kanfont_scale_WH,widget_h=kanfont_scale_WH,widget_f=kanfont_font_scale,event_b=None)
    kanfont_code_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_scale_X,widget_y=kanfont_scale_Y,widget_w=kanfont_scale_W,widget_h=kanfont_scale_H,widget_s=1,widget_e=kanfont_max,widget_a=1,event_b=None)
    kanfont_code_spin=LTsv_spin_new(kanfont_window,widget_x=0,widget_y=kanfont_scale_Y+kanfont_scale_H,widget_w=kanfont_scale_WH,widget_h=kanfont_label_WH,widget_s=1,widget_e=kanfont_max,widget_a=1,widget_f=kanfont_font_entry,event_b=None)
    kanfont_code_label=LTsv_label_new(kanfont_window,widget_t="0xf080",widget_x=0,widget_y=kanfont_scale_Y+kanfont_scale_H+kanfont_label_WH,widget_w=kanfont_scale_WH,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_glyph_canvas=LTsv_canvas_new(kanfont_window,widget_x=kanfont_canvas_X,widget_y=0,widget_w=kanfont_canvas_WH,widget_h=kanfont_canvas_WH)
    kanfont_gridimageOBJ=LTsv_draw_picture_load(kanfont_gridimage)
    kanfont_path_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_canvas_X,widget_y=kanfont_canvas_WH,widget_w=kanfont_canvas_WH-kanfont_entry_W*4//8,widget_h=kanfont_label_WH*2,widget_s=0,widget_e=9,widget_a=1)
    kanfont_grid_label=LTsv_label_new(kanfont_window,widget_t="grid",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*4//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_grid_spin=LTsv_spin_new(kanfont_window,widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*4//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_s=5,widget_e=PSchar_ZW//5,widget_a=1,widget_f=kanfont_font_entry,event_b=None)
    kanfont_inner_label=LTsv_label_new(kanfont_window,widget_t="inner",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*3//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_inner_check=LTsv_check_new(kanfont_window,widget_t="24",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*3//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=None)
    kanfont_seg_label=LTsv_label_new(kanfont_window,widget_t="line",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*2//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_seg_check=LTsv_check_new(kanfont_window,widget_t="seg",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*2//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=None)
    kanfont_gothic_radio=LTsv_radio_new(kanfont_window,widget_t="活",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*1//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=None)
    kanfont_comic_radio=LTsv_radio_new(kanfont_window,widget_t="漫",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*1//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=None)
    LTsv_widget_newUUID()
    for dictype_cnt,dictype_split in enumerate(tinykbd_dictype):
        kanfont_dictype_label[dictype_cnt]=LTsv_radio_new(kanfont_window,widget_t=dictype_split,widget_x=kanfont_label_X,widget_y=dictype_cnt*kanfont_label_WH,widget_w=kanfont_label_WH*2,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    dictype_cnt,dictype_split=len(tinykbd_dictype),"code"
    kanfont_dictype_label[dictype_cnt]=LTsv_radio_new(kanfont_window,widget_t=dictype_split,widget_x=kanfont_scale_X,widget_y=0,widget_w=kanfont_scale_W,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    LTsv_widget_showhide(kanfont_window,True)
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_font,LTsv_drawtk_color,LTsv_drawtk_text,LTsv_drawtk_picture=LTsv_drawGTK_selcanvas,LTsv_drawGTK_font,LTsv_drawGTK_color,LTsv_drawGTK_text,LTsv_drawGTK_picture
        LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_delete,LTsv_drawGTK_queue
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_font,LTsv_drawtk_color,LTsv_drawtk_text,LTsv_drawtk_picture=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_font,LTsv_drawTkinter_color,LTsv_drawTkinter_text,LTsv_drawTkinter_picture
        LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
    LTsv_drawtk_selcanvas(kanfont_glyph_canvas)
    LTsv_drawtk_picture(kanfont_gridimage,0,0)
    LTsv_drawtk_queue()
    LTsv_window_main(kanfont_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE

