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

PSfont_ZW,PSfont_CW,PSchar_ZW,PSchar_CW=1024,624,1000,600
kanfont_ltsv,kanfont_config="",""
tinykbd_dictype=    ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","漫","幅"]
kanfont_dicname,kanfont_mapname,kanfont_svgname,kanfont_fontname,kanfont_fontwidths="kanchar.tsv","kanmap.tsv","kanfont.svg","kantray5x5comic","1024,624"

def kanfont_configload():
    global kanfont_ltsv,kanfont_config

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    kanfont_configload()
    kanfont_fontsize_entry=10;    kanfont_font_entry="{0},{1}".format(kanfont_fontname,kanfont_fontsize_entry); kanfont_label_WH=kanfont_fontsize_entry*2
    kanfont_fontsize_scale=40;    kanfont_font_scale="{0},{1}".format(kanfont_fontname,kanfont_fontsize_scale); kanfont_scale_WH=kanfont_fontsize_scale*2
    kanfont_fontsize_keyboard=12; kanfont_font_keyboard="{0},{1}".format(kanfont_fontname,kanfont_fontsize_keyboard)
    kanfont_fontsize_grid=8;      kanfont_font_grid="{0},{1}".format(kanfont_fontname,kanfont_fontsize_grid)
    kanfont_scale_W,kanfont_entry_W=kanfont_scale_WH,400; kanfont_canvas_WH=PSfont_ZW//2
    kanfont_canvas_X=kanfont_scale_W; kanfont_label_X=kanfont_canvas_X+kanfont_canvas_WH; kanfont_entry_X=kanfont_label_X+kanfont_label_WH; kanfont_W=kanfont_entry_X+kanfont_entry_W
    kanfont_H=kanfont_canvas_WH; kanfont_scale_H=kanfont_H-kanfont_scale_WH-kanfont_label_WH-kanfont_label_WH; kanfont_scale_X,kanfont_scale_Y=0,kanfont_scale_WH
    kanfont_window=LTsv_window_new(widget_t="kanfont",event_b=LTsv_window_exit,widget_w=kanfont_W,widget_h=kanfont_H)
    LTsv_widget_showhide(kanfont_window,True)
    LTsv_window_main(kanfont_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE

