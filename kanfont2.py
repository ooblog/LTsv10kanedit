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

PSfont_ZW,PSfont_CW,PSchar_ZW,PSchar_CW=1024,624,1000,600
kanfont_ltsv,kanfont_config="",""
kanfont_dicname,kanfont_mapname,kanfont_fontname,kanfont_fontwidths="kanchar.tsv","kanmap.tsv","kantray5x5comic","1024,624"
kanfont_svgname=["kanfont5x5.svg","kanfontcomic.svg"]
kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage="ぱ",25,0,0,0,"kanfont_grid25_199.png"
kanfont_glyphcolorR,kanfont_glyphcolorL,kanfont_glyphcolorX="#6E81D9","#6ED997","#D96ED3"
kanfont_max=0x2ffff  # if LTsv_GUI != "Tkinter" else 0xffff
kanfont_dictype_label,kanfont_dictype_entry=[None]*(len(LTsv_global_dictype())+1),[None]*(len(LTsv_global_dictype())+1)
LTsv_chrcode=chr if sys.version_info.major == 3 else unichr

pathadjustlen=0
def kanfont_pathadjustment():
    global pathadjustlen
    pathadjustlen=len(LTsv_glyph_note(LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale)),draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    LTsv_widget_setnumber(kanfont_path_scale,pathadjustlen)
    LTsv_scale_adjustment(kanfont_path_scale,widget_s=0,widget_e=pathadjustlen)
    LTsv_widget_setnumber(kanfont_path_scale,pathadjustlen)
    LTsv_widget_showhide(kanfont_path_scale,True)

def kanfont_code():
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    kanfont_seek=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    LTsv_widget_settext(kanfont_code_label,hex(LTsv_widget_getnumber(kanfont_code_scale)).replace("0x","U+"))
    kanfont_pathadjustment()
    LTsv_glyphpath(kanfont_seek)
    kanfont_glyph_draw()

def kanfont_codespin_shell(window_objvoid=None,window_objptr=None):
    if LTsv_widget_getnumber(kanfont_code_scale) != LTsv_widget_getnumber(kanfont_code_spin):
        LTsv_widget_setnumber(kanfont_code_scale,LTsv_widget_getnumber(kanfont_code_spin))
        kanfont_code()
    return

def kanfont_codescale_shell(window_objvoid=None,window_objptr=None):
    if LTsv_widget_getnumber(kanfont_code_spin) != LTsv_widget_getnumber(kanfont_code_scale):
        LTsv_widget_setnumber(kanfont_code_spin,LTsv_widget_getnumber(kanfont_code_scale))
        kanfont_code()
    return

def kanfont_codekbd(kbdentry):
    kbdentrycode=ord(kbdentry[0])
    LTsv_widget_setnumber(kanfont_code_scale,int(kbdentrycode))

def kanfont_pathsel_shell(window_objvoid=None,window_objptr=None):
    kanfont_glyph_draw()

def kanfont_grid_shell(window_objvoid=None,window_objptr=None):
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    kanfont_fontgrid=LTsv_widget_getnumber(kanfont_grid_spin)
    LTsv_widget_settext(kanfont_inner_check,str(kanfont_fontgrid-1))

def kanfont_inner_shell(window_objvoid=None,window_objptr=None):
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    kanfont_gridinner=LTsv_widget_getnumber(kanfont_inner_check)

def kanfont_lineseg_shell(window_objvoid=None,window_objptr=None):
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    kanfont_lineseg=LTsv_widget_getnumber(kanfont_seg_check)

def debug_gothic_shell(radioNumber):
    def debug_gothic_kernel(window_objvoid=None,window_objptr=None):
        global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
        if kanfont_gothic != radioNumber:
            kanfont_gothic=radioNumber
            kanfont_code()
    return debug_gothic_kernel

kanfont_gridview=False
def kanfont_glyph_draw():
    LTsv_draw_selcanvas(kanfont_glyph_canvas)
    LTsv_draw_delete()
    glyphentrychar=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    if kanfont_gridview:
        LTsv_draw_picture(kanfont_gridimage,0,0)
        LTsv_draw_glyphclock(draw_t=glyphentrychar,draw_x=0,draw_y=0,draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic],color_R=kanfont_glyphcolorR,color_L=kanfont_glyphcolorL,color_X=kanfont_glyphcolorX)
    else:
        LTsv_draw_glyphclockfill(draw_t=glyphentrychar,draw_x=0,draw_y=0,draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic],color_R=kanfont_glyphcolorR,color_L=kanfont_glyphcolorL,color_X=kanfont_glyphcolorX)
    LTsv_draw_glyphedit(draw_t=glyphentrychar,draw_x=0,draw_y=0,draw_z=LTsv_widget_getnumber(kanfont_path_scale),draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic],color_R=kanfont_glyphcolorR,color_L=kanfont_glyphcolorL,color_X=kanfont_glyphcolorX)
    LTsv_draw_queue()

def kanfont_glyph_mousepress(window_objvoid=None,window_objptr=None):
    kanfont_glyph_draw()

def kanfont_glyph_mousemotion(window_objvoid=None,window_objptr=None):
    kanfont_glyph_draw()

def kanfont_glyph_mouserelease(window_objvoid=None,window_objptr=None):
    kanfont_glyph_draw()

def kanfont_glyph_mouseenter(window_objvoid=None,window_objptr=None):
    global kanfont_gridview
    kanfont_gridview=True
    kanfont_glyph_draw()

def kanfont_glyph_mouseleave(window_objvoid=None,window_objptr=None):
    global kanfont_gridview
    kanfont_gridview=False
    kanfont_glyph_draw()

def kanfont_kbd_mousepress(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mousepress(kanfont_kbd_canvas,0,0)

def kanfont_kbd_mousemotion(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mousemotion(kanfont_kbd_canvas,0,0)

def kanfont_kbd_mouserelease(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mouserelease(kanfont_kbd_canvas,0,0)

def kanfont_configload():
    global kanfont_ltsv,kanfont_config
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    global kanfont_glyphcolorR,kanfont_glyphcolorL,kanfont_glyphcolorX
    kanfont_ltsv=LTsv_loadfile("kanfont2.tsv")
    kanfont_config=LTsv_getpage(kanfont_ltsv,"kanfont")
    kanfont_seek=LTsv_readlinerest(kanfont_config,"seek",kanfont_seek)[:1]
    kanfont_fontgrid=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"grid",str(kanfont_fontgrid))),10),100)
    kanfont_gridinner=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"inner",str(kanfont_gridinner))),0),1)
    kanfont_lineseg=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"lineseg",str(kanfont_lineseg))),0),1)
    kanfont_gothic=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"gothic",str(kanfont_gothic))),0),1)
    kanfont_gridimage=LTsv_readlinerest(kanfont_config,"gridimage",kanfont_gridimage)
    kanfont_glyphcolorR,kanfont_glyphcolorL,kanfont_glyphcolorX=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanfont_config,"glyphcolor"),"R","L","X"))

def kanfont_configsave_exit(window_objvoid=None,window_objptr=None):
    global kanfont_ltsv,kanfont_config
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    kanfont_ltsv=LTsv_loadfile("kanfont2.tsv")
    kanfont_config=LTsv_pushlinerest(kanfont_config,"seek",kanfont_seek)
    kanfont_config=LTsv_pushlinerest(kanfont_config,"grid",str(kanfont_fontgrid))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"inner",str(kanfont_gridinner))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"lineseg",str(kanfont_lineseg))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"gothic",str(kanfont_gothic))
    kanfont_ltsv=LTsv_putpage(kanfont_ltsv,"kanfont",kanfont_config)
    LTsv_savefile("kanfont2.tsv",kanfont_ltsv)
    LTsv_glyph_picklesave()
    LTsv_window_exit()

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_glyph_kbdinit(ltsvpath="LTsv/kanglyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    kanfont_configload()
    kanfont_fontsize_entry=12;    kanfont_font_entry="{0},{1}".format(kanfont_fontname,kanfont_fontsize_entry); kanfont_label_WH=kanfont_fontsize_entry*2
    kanfont_fontsize_keyboard=12; kanfont_font_keyboard="{0},{1}".format(kanfont_fontname,kanfont_fontsize_keyboard)
    kanfont_fontsize_grid=8;      kanfont_font_grid="{0},{1}".format(kanfont_fontname,kanfont_fontsize_grid)
    kanfont_canvas_WH=PSfont_ZW//2; kanfont_scale_W=LTsv_global_glyphkbdW(); kanfont_entry_W=1024-kanfont_scale_W-kanfont_canvas_WH-kanfont_label_WH; 
    kanfont_canvas_X=kanfont_scale_W; kanfont_label_X=kanfont_canvas_X+kanfont_canvas_WH; kanfont_entry_X=kanfont_label_X+kanfont_label_WH; kanfont_W=kanfont_entry_X+kanfont_entry_W
    kanfont_savebutton_X=kanfont_entry_X-kanfont_label_WH//2
    kanfont_H=kanfont_canvas_WH+kanfont_label_WH*2; kanfont_scale_X,kanfont_scale_Y=0,LTsv_global_glyphkbdH(); kanfont_scale_H=kanfont_H-kanfont_scale_Y-kanfont_label_WH-kanfont_label_WH
    kanfont_window=LTsv_window_new(widget_t="kanfont",event_b=kanfont_configsave_exit,widget_w=kanfont_W,widget_h=kanfont_H)
    kanfont_kbd_canvas=LTsv_canvas_new(kanfont_window,widget_x=0,widget_y=0,widget_w=LTsv_global_glyphkbdW(),widget_h=LTsv_global_glyphkbdH(),
     event_p=kanfont_kbd_mousepress,event_m=kanfont_kbd_mousemotion,event_r=kanfont_kbd_mouserelease,event_w=50)
    LTsv_glyph_tapcallback_shell(kanfont_kbd_canvas,kanfont_codekbd)
    kanfont_code_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_scale_X,widget_y=kanfont_scale_Y,widget_w=kanfont_scale_W,widget_h=kanfont_scale_H,widget_s=1,widget_e=kanfont_max,widget_a=1,event_b=kanfont_codescale_shell)
    kanfont_code_spin=LTsv_spin_new(kanfont_window,widget_x=0,widget_y=kanfont_scale_Y+kanfont_scale_H,widget_w=kanfont_scale_W,widget_h=kanfont_label_WH,widget_s=1,widget_e=kanfont_max,widget_a=1,widget_f=kanfont_font_entry,event_b=kanfont_codespin_shell)
    kanfont_code_label=LTsv_label_new(kanfont_window,widget_t="U+f080",widget_x=0,widget_y=kanfont_scale_Y+kanfont_scale_H+kanfont_label_WH,widget_w=kanfont_scale_W,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_glyph_canvas=LTsv_canvas_new(kanfont_window,widget_x=kanfont_canvas_X,widget_y=0,widget_w=kanfont_canvas_WH,widget_h=kanfont_canvas_WH,
     event_p=kanfont_glyph_mousepress,event_m=kanfont_glyph_mousemotion,event_r=kanfont_glyph_mouserelease,event_e=kanfont_glyph_mouseenter,event_l=kanfont_glyph_mouseleave,event_w=50)
    kanfont_gridimageOBJ=LTsv_draw_picture_load(kanfont_gridimage)
    kanfont_path_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_canvas_X,widget_y=kanfont_canvas_WH,widget_w=kanfont_canvas_WH-kanfont_entry_W*4//8,widget_h=kanfont_label_WH*2,widget_s=0,widget_e=9,widget_a=1,event_b=kanfont_pathsel_shell)
    kanfont_grid_label=LTsv_label_new(kanfont_window,widget_t="grid",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*4//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_grid_spin=LTsv_spin_new(kanfont_window,widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*4//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_s=5,widget_e=PSchar_ZW//5,widget_a=1,widget_f=kanfont_font_entry,event_b=kanfont_grid_shell)
    kanfont_inner_label=LTsv_label_new(kanfont_window,widget_t="inner",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*3//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_inner_check=LTsv_check_new(kanfont_window,widget_t="24",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*3//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_inner_shell)
    kanfont_seg_label=LTsv_label_new(kanfont_window,widget_t="line",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*2//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_seg_check=LTsv_check_new(kanfont_window,widget_t="seg",widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*2//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_entry_W*5//32,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_lineseg_shell)
    kanfont_gothic_radio=[None]*len(LTsv_global_glyphtype())
    for glyphtype_cnt,glyphtype_split in enumerate(LTsv_global_glyphtype()):
        kanfont_gothic_radio[glyphtype_cnt]=LTsv_radio_new(kanfont_window,widget_t=glyphtype_split,widget_x=kanfont_canvas_X+kanfont_canvas_WH-kanfont_entry_W*3//32,widget_y=kanfont_canvas_WH+kanfont_label_WH*glyphtype_cnt,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=debug_gothic_shell(glyphtype_cnt))
    kanfont_svg_button=[None]*len(LTsv_global_glyphtype())
    for glyphtype_cnt,glyphtype_split in enumerate(LTsv_global_glyphtype()):
        kanfont_svg_button[glyphtype_cnt]=LTsv_button_new(kanfont_window,widget_t=kanfont_svgname[glyphtype_cnt],widget_x=kanfont_savebutton_X+kanfont_entry_W//2*0,widget_y=kanfont_H-kanfont_label_WH*(glyphtype_cnt+1),widget_w=kanfont_entry_W//2,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=None)
    for dictype_cnt,dictype_split in enumerate(LTsv_global_dictype()):
        kanfont_dictype_label[dictype_cnt]=LTsv_label_new(kanfont_window,widget_t=dictype_split,widget_x=kanfont_label_X,widget_y=dictype_cnt*kanfont_label_WH,widget_w=kanfont_label_WH,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    LTsv_widget_showhide(kanfont_window,True)
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    kanfont_codekbd(kanfont_seek)
    LTsv_widget_setnumber(kanfont_grid_spin,kanfont_fontgrid)
    LTsv_widget_setnumber(kanfont_inner_check,kanfont_gridinner)
    LTsv_widget_setnumber(kanfont_seg_check,kanfont_lineseg)
    LTsv_widget_setnumber(kanfont_gothic_radio[0],kanfont_gothic)
    LTsv_glyph_kbddelete(kanfont_kbd_canvas,0,0); LTsv_glyph_kbddraw(kanfont_kbd_canvas,0,0); LTsv_draw_queue()
    LTsv_window_main(kanfont_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE

