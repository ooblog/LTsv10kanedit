#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
sys.path.append("LTsv")
import copy
from LTsv_printf  import *
from LTsv_file    import *
from LTsv_time    import *
from LTsv_calc    import *
#from LTsv_joy     import *
from LTsv_kbd     import *
from LTsv_gui     import *
from LTsv_glyph  import *

kanedit_window=None
kanedit_getkbdnames,kanedit_getkbdkanas,kanedit_inputkey="","",0
kanedit_W,kanedit_H,kanedit_RS=LTsv_global_glyphkbdW(),LTsv_global_glyphkbdH(),False
kanedit_ltsv,kanedit_config="",""
kanedit_texteditfilename,kanedit_textvalue="",""
kanedit_fontcolor,kanedit_bgcolor,kanedit_markcolor,kanedit_fontsize="black","#FFF3F5","red",10
kanmemo_textvalue,kanmemo_textleft,kanmemo_textright="",0,0
kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor="black","white","red"


def kanedit_redraw():
    LTsv_glyph_kbddelete(kanedit_canvas)
    LTsv_draw_selcanvas(kanedit_canvas)
    LTsv_draw_delete(kanedit_bgcolor)
    kanedit_editdraw(5,5)
    kanedit_memodraw(0,kanedit_H-LTsv_global_glyphkbdF())
    LTsv_glyph_kbddraw(kanedit_canvas,kanedit_W-LTsv_global_glyphkbdW(),kanedit_H-LTsv_global_glyphkbdH())
    if kanedit_inputkey:
        LTsv_widget_settext(kanedit_window,widget_t="kanedit:{0}".format(kanedit_getkbdnames.replace('\t',' ')))
    LTsv_draw_queue()

def kanedit_editdraw(edit_x,edit_y):
    LTsv_draw_color(kanedit_bgcolor); LTsv_draw_polygonfill(0,0,kanedit_W,0,kanedit_W,kanedit_H,0,kanedit_H)
    LTsv_draw_color(kanedit_fontcolor);
    textline_y=edit_y
    for kanedit_textline in kanedit_textvalue.split('\n'):
        kanedit_textline+='\n'
        LTsv_draw_glyphsfill(draw_t=kanedit_textline,draw_x=edit_x,draw_y=textline_y,draw_f=kanedit_fontsize,draw_w=1,draw_h=1,draw_g="漫",draw_LF=False,draw_HT=False,draw_SP=False)
        textline_y+=kanedit_fontsize+1
        if textline_y > kanedit_H:
            break

def kanedit_memodraw(memo_x,memo_y):
    global kanmemo_textvalue,kanmemo_textleft,kanmemo_textright
    global kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor
    LTsv_draw_bgcolor(kanmemo_bgcolor); LTsv_draw_color(kanmemo_bgcolor); 
    LTsv_draw_polygonfill(memo_x,memo_y,kanedit_W-LTsv_global_glyphkbdW(),memo_y,kanedit_W-LTsv_global_glyphkbdW(),kanedit_H,memo_x,kanedit_H)
    LTsv_draw_color(kanmemo_fontcolor)
#    LTsv_draw_glyphsfill(draw_t=kanmemo_textvalue,draw_x=memo_x,draw_y=memo_y,draw_f=LTsv_global_glyphkbdF(),draw_w=1,draw_h=1,draw_g="漫",draw_LF=True,draw_HT=True,draw_SP=True)

def kanedit_resizeredraw(window_objvoid=None,window_objptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    window_w,window_h=LTsv_window_wh(kanedit_window)
    if kanedit_W!=window_w or kanedit_H!=window_h:
        kanedit_W,kanedit_H=window_w,window_h
        kanedit_redraw()
        LTsv_window_after(kanedit_window,event_b=kanedit_resizeredraw,event_i="kanedit_resizeredraw",event_w=50)
    else:
        kanedit_W,kanedit_H=window_w,window_h
        kanedit_RS=False

def kanedit_resize(callback_void=None,callback_ptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    if kanedit_RS == False:
        kanedit_RS=True
        kanedit_resizeredraw()

def kanedit_mousepress(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mousepress(kanedit_canvas,kanedit_W-LTsv_global_glyphkbdW(),kanedit_H-LTsv_global_glyphkbdH())

def kanedit_mousemotion(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mousemotion(kanedit_canvas,kanedit_W-LTsv_global_glyphkbdW(),kanedit_H-LTsv_global_glyphkbdH())

def kanedit_mouserelease(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mouserelease(kanedit_canvas,kanedit_W-LTsv_global_glyphkbdW(),kanedit_H-LTsv_global_glyphkbdH())

def kanedit_keypress(window_objvoid=None,window_objptr=None):
    LTsv_setkbddata(20,0)
    kanedit_getkbdnames,kanedit_getkbdkanas=LTsv_getkbdnames(),LTsv_getkbdkanas()
    keybind=LTsv_readlinerest(kanedit_keybind,kanedit_getkbdnames.rstrip('\t').replace('\t',' '))
    if len(keybind):
        pass
#        kanedit_inputchar(keybind)
    else:
        pass
#        if tinykbd_keepSandS == 0 and tinykbd_inputSandS in kanedit_getkbdnames:
#            tinykbd_keepSandS=1
#            for kbd_xy in range(tinykbd_irohamax):
#                tinykbd_fontchar[kbd_xy]=LTsv_pickdatalabel(LTsv_readlinerest(tinykbd_char,tinykbd_fontchar[kbd_xy]),tinykbd_fontchar[tinykbd_SandS])
#                tinykbd_fontchar[kbd_xy]=tinykbd_fontchar[kbd_xy][0:1]
#        if tinykbd_keepNFER == 0 and tinykbd_inputNFER in kanedit_getkbdnames:
#            tinykbd_keepNFER=1
#            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohaalphaN[kanedit_tinykbd_selected(tinykbd_fontchar[tinykbd_KANA])]
#            kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
#        if tinykbd_keepXFER == 0 and tinykbd_inputXFER in kanedit_getkbdnames:
#            tinykbd_keepXFER=1
#            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohaalphaX[kanedit_tinykbd_selected(tinykbd_fontchar[tinykbd_KANA])]
#            kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
#        if tinykbd_keepKANA == 0 and tinykbd_inputKANA in kanedit_getkbdnames:
#            tinykbd_keepKANA=1
#            if tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaN:
#                tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_choiceN[0:tinykbd_irohamax]
#            elif tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaX:
#                tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_choiceX[0:tinykbd_irohamax]
#        for getkbdkanas in kanedit_getkbdkanas.split('\t'):
#            if not tinykbd_keepKANA:
#                if getkbdkanas in tinykbd_irohatype:
#                    kanedit_inputcharNX(tinykbd_fontchar[tinykbd_KANA],tinykbd_irohatype.index(getkbdkanas))
#kanedit_inputchar(inputchar)
#                    kanedit_inputcharNX(tinykbd_fontchar[tinykbd_KANA],tinykbd_irohatype.index(getkbdkanas))
#    kanedit_redraw()

def kanedit_keyrelease(window_objvoid=None,window_objptr=None):
    pass
#    global kanedit_getkbdnames,kanedit_getkbdkanas,kanedit_inputkey
#    global tinykbd_keepSandS,tinykbd_keepNFER,tinykbd_keepXFER,tinykbd_keepKANA
#    if kanedit_getkbdnames == tinykbd_inputSandS:
#        kanedit_inputcharNX(tinykbd_fontchar[tinykbd_KANA],tinykbd_SandS)
#    LTsv_setkbddata(20,0)
#    kanedit_getkbdnames=LTsv_getkbdnames()
#    if not tinykbd_inputSandS in kanedit_getkbdnames:
#        tinykbd_keepSandS=0
#        kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
#    if not tinykbd_inputNFER in kanedit_getkbdnames:
#        tinykbd_keepNFER=0
#    if not tinykbd_inputXFER in kanedit_getkbdnames:
#        tinykbd_keepXFER=0
#    if not tinykbd_inputKANA in kanedit_getkbdnames:
#        tinykbd_keepKANA=0
#    kanedit_redraw()

def kanedit_textload(filename):
    global kanedit_window
    global kanedit_texteditfilename,kanedit_textvalue
    kanedit_texteditfilename=filename
    LTsv_widget_settext(kanedit_window,widget_t="kanedit:{0}".format(kanedit_texteditfilename))
    kanedit_textvalue=LTsv_loadfile(kanedit_texteditfilename)

def kanedit_configload():
    global kanedit_W,kanedit_H,kanedit_RS
    global kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_resizeW,kanedit_resizeH=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"window_size"),"width","height"))
    kanedit_W,kanedit_H=min(max(LTsv_intstr0x(kanedit_resizeW),LTsv_global_glyphkbdW()),LTsv_screen_w(kanedit_window)),min(max(LTsv_intstr0x(kanedit_resizeH),LTsv_global_glyphkbdH()),LTsv_screen_h(kanedit_window))


#    global kanedit_W,kanedit_H,kanedit_RS
#    global kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind
#    global tinykbd_inputSandS,tinykbd_inputNFER,tinykbd_inputXFER,tinykbd_inputKANA
#    global kanedit_getkbdnames,kanedit_getkbdkanas,kanedit_inputkey
#    global kanedit_fontcolor,kanedit_bgcolor,kanedit_markcolor,kanedit_fontsize
#    global tinykbd_map,tinykbd_char,tinykbd_pickle,tinykbd_word,tinykbd_zip
#    global tinykbd_kanmapN,tinykbd_kanmapX,tinykbd_kanmapD
#    global tinykbd_fontcolor,tinykbd_bgcolor,tinykbd_markcolor
#    global tinykbd_fontchar
#    global kanmemo_textvalue,kanmemo_textleft,kanmemo_textright
#    global kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor
#    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
#    kanedit_tinykbd=LTsv_getpage(kanedit_ltsv,"tinykbd")
#    kbd_resize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_tinykbd,"kbd_resize")),1),5)
#    tinykbd_inputSandS=LTsv_readlinerest(kanedit_tinykbd,"input_SandS",tinykbd_inputSandS)
#    tinykbd_inputNFER=LTsv_readlinerest(kanedit_tinykbd,"input_NFER",tinykbd_inputNFER)
#    tinykbd_inputXFER=LTsv_readlinerest(kanedit_tinykbd,"input_XFER",tinykbd_inputXFER)
#    tinykbd_inputKANA=LTsv_readlinerest(kanedit_tinykbd,"input_KANA",tinykbd_inputKANA)
#    tinykbd_fontcolor,tinykbd_bgcolor,tinykbd_markcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_tinykbd,"kbd_colors"),"font","bg","mark"))
#    tinykbd_map=LTsv_loadfile(LTsv_readlinerest(kanedit_tinykbd,"dic_mapname","kanmap.tsv"))
#    for irohaalpha in tinykbd_irohaalpha:
#        kbd_lineT=LTsv_readlinerest(tinykbd_map,irohaalpha)
#        kbd_lineL=kbd_lineT.split('\t'); kbd_lineL=kbd_lineL+[" "]*(tinykbd_SandS*2-len(kbd_lineL))
#        tinykbd_kanmapN[irohaalpha],tinykbd_kanmapX[irohaalpha]=kbd_lineL[0:tinykbd_SandS+1],kbd_lineL[tinykbd_SandS+1:tinykbd_SandS+1+tinykbd_SandS+1]
#    kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
#    tinykbd_fontchar[tinykbd_KANA]=LTsv_readlinerest(kanedit_tinykbd,"find_NXalpha",tinykbd_fontchar[tinykbd_KANA])
#    tinykbd_fontchar[tinykbd_KANA]=tinykbd_fontchar[tinykbd_KANA] if tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaN or tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaX else tinykbd_irohatype[0]
#    tinykbd_fontchar[tinykbd_SandS]=LTsv_readlinerest(kanedit_tinykbd,"find_dic",tinykbd_fontchar[tinykbd_SandS])
##    tinykbd_fontchar[tinykbd_SandS]=tinykbd_fontchar[tinykbd_SandS] if tinykbd_fontchar[tinykbd_SandS] in tinykbd_dictype else tinykbd_dictype[0]
#    tinykbd_char=LTsv_loadfile(LTsv_readlinerest(kanedit_tinykbd,"dic_charname","kanchar.tsv"))
#    tinykbd_pickle=LTsv_readlinerest(kanedit_tinykbd,"glyph_picklename","kanchar.tsv")
#    LTsv9_glyphOBJunpickle(tinykbd_pickle)
#    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
#    kanedit_tinykbd_new(kbd_resize)
#    kanedit_resizeW,kanedit_resizeH=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"window_size"),"width","height"))
#    kanedit_W,kanedit_H=min(max(LTsv_intstr0x(kanedit_resizeW),tinykbd_W),LTsv_screen_w(kanedit_window)),min(max(LTsv_intstr0x(kanedit_resizeH),tinykbd_H),LTsv_screen_h(kanedit_window))
#    kanedit_inputkey=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"kbd_inputkey")),0),1)
#    kanedit_fontcolor,kanedit_bgcolor,kanedit_markcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"edit_colors"),"font","bg","mark"))
#    kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"memo_colors"),"font","bg","mark"))
#    kanedit_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"font_size",str(kanedit_fontsize))),5),100)
#    LTsv9_glyphdicload(LTsv_readlinerest(kanedit_config,"dic_charname","kanchar.tsv"))
#    tinykbd_word=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_wordname","kanword.tsv"))
#    tinykbd_zip=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_zipname","kanzip.tsv"))
#    kanedit_texteditfilename=LTsv_readlinerest(kanedit_config,"open_last","kanedit.txt")
#    kanedit_textload(kanedit_texteditfilename)
#    kanedit_keybind=LTsv_getpage(kanedit_ltsv,"keybind")
#    kanedit_charbind=LTsv_getpage(kanedit_ltsv,"charbind")
#    kanmemo_textvalue=LTsv_readlinerest(kanedit_config,"eval_entry")

def kanedit_exit_configsave(window_objvoid=None,window_objptr=None):
    global kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind
#    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
#    kanedit_tinykbd=LTsv_getpage(kanedit_ltsv,"tinykbd")
#    kanedit_tinykbd=LTsv_pushlinerest(kanedit_tinykbd,"find_NXalpha",tinykbd_fontchar[tinykbd_KANA])
#    kanedit_tinykbd=LTsv_pushlinerest(kanedit_tinykbd,"find_dic",tinykbd_fontchar[tinykbd_SandS])
#    kanedit_ltsv=LTsv_putpage(kanedit_ltsv,"tinykbd",kanedit_tinykbd)
#    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
#    kanedit_config=LTsv_pushlinerest(kanedit_config,"open_last",kanedit_texteditfilename)
#    kanedit_config=LTsv_pushlinerest(kanedit_config,"eval_entry",kanmemo_textvalue)
#    kanedit_ltsv=LTsv_putpage(kanedit_ltsv,"kanedit",kanedit_config)
#    LTsv_savefile("kanedit.tsv",kanedit_ltsv)
#    LTsv9_glyphOBJpickle(tinykbd_pickle)
#    LTsv_glyph_picklesave()
    LTsv_window_exit()
kanedit_exit_configsave_cbk=LTsv_CALLBACLTYPE(kanedit_exit_configsave)


LTsv_GUI=LTsv_guiinit()
#kantray_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff :「kanedit」non limit!
if len(LTsv_GUI) > 0:
    LTsv_glyph_kbdinit(ltsvpath="LTsv/kanglyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    kanedit_window=LTsv_window_new(widget_t="kanedit",event_b=kanedit_exit_configsave,widget_w=kanedit_W,widget_h=kanedit_H,event_z=kanedit_resize,event_k=kanedit_keypress,event_y=kanedit_keyrelease)
    kanedit_configload()
    LTsv_window_resize(kanedit_window,kanedit_W,kanedit_H)
    kanedit_canvas=LTsv_canvas_new(kanedit_window,widget_x=0,widget_y=0,widget_w=LTsv_screen_w(kanedit_window),widget_h=LTsv_screen_h(kanedit_window),
     event_p=kanedit_mousepress,event_r=kanedit_mouserelease,event_m=kanedit_mousemotion,event_w=50)
    kanedit_clipboard=LTsv_clipboard_new(kanedit_window)
    LTsv_widget_showhide(kanedit_window,True)
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    kanedit_resize()
    kanedit_redraw()
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
