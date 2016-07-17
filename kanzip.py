#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
if sys.version_info.major == 2:
    import urllib
if sys.version_info.major == 3:
    import urllib.request
import math
sys.path.append("LTsv")
from LTsv_printf import *
from LTsv_file   import *
#from LTsv_time   import *
#from LTsv_calc   import *
#from LTsv_joy    import *
#from LTsv_kbd    import *
from LTsv_gui    import *

kanzip_kanzip_tsv="kanzip.tsv"
kanzip_workdir="./kanzip/"
kanzip_fontsize=10
kanzip_prefectureMAX=48
kanzip_prefectureCVID=kanzip_prefectureMAX
kanzip_font="{0},{1}".format("kantray5x5comic",kanzip_fontsize)
kanzip_DLlabel_W,kanzip_DLlabel_H=kanzip_fontsize*9,kanzip_fontsize*3;                     kanzip_DLlabel=[""]*(kanzip_prefectureMAX+2)
kanzip_DLbutton_W,kanzip_DLbutton_H=kanzip_fontsize*12,kanzip_DLlabel_H;                   kanzip_DLbutton=[""]*(kanzip_prefectureMAX+2)
kanzip_DLprogres_W,kanzip_DLprogres_H=kanzip_DLbutton_W-kanzip_DLlabel_W,kanzip_DLlabel_H; kanzip_DLprogres=[""]*(kanzip_prefectureMAX+2)
kanzip_DLbuzy={}; kanzip_DLconvert={}
kanzip_prefecture_W,kanzip_prefecture_H=max(kanzip_DLlabel_W,kanzip_DLbutton_W),kanzip_DLlabel_H+kanzip_DLbutton_H
kanzip_FXbutton_W,kanzip_FXbutton_H=kanzip_prefecture_W*8-kanzip_DLprogres_W,kanzip_DLbutton_H; kanzip_FXbutton=None
kanzip_window_W,kanzip_window_H=kanzip_prefecture_W*8,kanzip_prefecture_H*6+kanzip_FXbutton_H
kanzip_prefecturesKAN=["事業所","北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県",
                       "茨城県","栃木県","群馬県","埼玉県","千葉県","東京都","神奈川県","新潟県",
                       "富山県","石川県","福井県","山梨県","長野県","岐阜県","静岡県","愛知県",
                       "三重県","滋賀県","京都府","大阪府","兵庫県","奈良県","和歌山県","鳥取県",
                       "島根県","岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県",
                       "福岡県","佐賀県","長崎県","熊本県","大分県","宮崎県","鹿児島県","沖縄県","全国一括"]
kanzip_japanpostURL="http://www.post.japanpost.jp/zipcode/dl/"
kanzip_prefecturesNAME=["jigyosyo","01hokkai","02aomori","03iwate","04miyagi","05akita","06yamaga","07fukush",
                        "08ibarak","09tochig","10gumma","11saitam","12chiba","13tokyo","14kanaga","15niigat",
                        "16toyama","17ishika","18fukui","19yamana","20nagano","21gifu","22shizuo","23aichi",
                        "24mie","25shiga","26kyouto","27osaka","28hyogo","29nara","30wakaya","31tottor",
                        "32shiman","33okayam","34hirosh","35yamagu","36tokush","37kagawa","38ehime","39kochi",
                        "40fukuok","41saga","42nagasa","43kumamo","44oita","45miyaza","46kagosh","47okinaw","ken_all"]
kanzip_prefectureURL,kanzip_prefectureDL,kanzip_prefectureCSV,kanzip_prefectureTSV=[""]*(kanzip_prefectureMAX+1),[""]*(kanzip_prefectureMAX+1),[""]*(kanzip_prefectureMAX+1),[""]*(kanzip_prefectureMAX+1)
for ken in range(kanzip_prefectureMAX+1):
    kanzip_prefectureURL[ken]=kanzip_japanpostURL+"kogaki/zip/"+kanzip_prefecturesNAME[ken]+".zip"
    kanzip_prefectureDL[ken]=kanzip_workdir+kanzip_prefecturesNAME[ken]+".zip"
    kanzip_prefectureCSV[ken]=kanzip_workdir+kanzip_prefecturesNAME[ken]+".csv"
    kanzip_prefectureTSV[ken]=kanzip_workdir+kanzip_prefecturesNAME[ken]+".tsv"
kanzip_prefectureURL[0]=kanzip_japanpostURL+"jigyosyo/zip/"+kanzip_prefecturesNAME[0]+".zip"
kanzip_prefecturedic=dict(zip(kanzip_prefecturesKAN,kanzip_prefectureURL))
if sys.version_info.major == 2:
    kanzip_prefectures_glyph={"事業所":unichr(12306),"北海道":unichr(61568),"青森県":unichr(61569),"岩手県":unichr(61570),"宮城県":unichr(61571),"秋田県":unichr(61572),"山形県":unichr(61573),"福島県":unichr(61574),
                              "茨城県":unichr(61575),"栃木県":unichr(61576),"群馬県":unichr(61577),"埼玉県":unichr(61578),"千葉県":unichr(61579),"東京都":unichr(61580),"神奈川県":unichr(61581),"新潟県":unichr(61582),
                              "富山県":unichr(61583),"石川県":unichr(61584),"福井県":unichr(61585),"山梨県":unichr(61586),"長野県":unichr(61587),"岐阜県":unichr(61588),"静岡県":unichr(61589),"愛知県":unichr(61590),
                              "三重県":unichr(61591),"滋賀県":unichr(61592),"京都府":unichr(61593),"大阪府":unichr(61594),"兵庫県":unichr(61595),"奈良県":unichr(61596),"和歌山県":unichr(61597),"鳥取県":unichr(61598),
                              "島根県":unichr(61599),"岡山県":unichr(61600),"広島県":unichr(61601),"山口県":unichr(61602),"徳島県":unichr(61603),"香川県":unichr(61604),"愛媛県":unichr(61605),"高知県":unichr(61606),
                              "福岡県":unichr(61607),"佐賀県":unichr(61608),"長崎県":unichr(61609),"熊本県":unichr(61610),"大分県":unichr(61611),"宮崎県":unichr(61612),"鹿児島県":unichr(61613),"沖縄県":unichr(61614),"全国一括":unichr(61615)}
if sys.version_info.major == 3:
    kanzip_prefectures_glyph={"事業所":chr(12306),"北海道":chr(61568),"青森県":chr(61569),"岩手県":chr(61570),"宮城県":chr(61571),"秋田県":chr(61572),"山形県":chr(61573),"福島県":chr(61574),
                              "茨城県":chr(61575),"栃木県":chr(61576),"群馬県":chr(61577),"埼玉県":chr(61578),"千葉県":chr(61579),"東京都":chr(61580),"神奈川県":chr(61581),"新潟県":chr(61582),
                              "富山県":chr(61583),"石川県":chr(61584),"福井県":chr(61585),"山梨県":chr(61586),"長野県":chr(61587),"岐阜県":chr(61588),"静岡県":chr(61589),"愛知県":chr(61590),
                              "三重県":chr(61591),"滋賀県":chr(61592),"京都府":chr(61593),"大阪府":chr(61594),"兵庫県":chr(61595),"奈良県":chr(61596),"和歌山県":chr(61597),"鳥取県":chr(61598),
                              "島根県":chr(61599),"岡山県":chr(61600),"広島県":chr(61601),"山口県":chr(61602),"徳島県":chr(61603),"香川県":chr(61604),"愛媛県":chr(61605),"高知県":chr(61606),
                              "福岡県":chr(61607),"佐賀県":chr(61608),"長崎県":chr(61609),"熊本県":chr(61610),"大分県":chr(61611),"宮崎県":chr(61612),"鹿児島県":chr(61613),"沖縄県":chr(61614),"全国一括":chr(61615)}

def kanzip_fileexist(window_objvoid=None,window_objptr=None):
    tsvcount=0
    for ken in range(kanzip_prefectureMAX):
        kanzip_buzyicon(ken,True)
        if os.path.isfile(kanzip_prefectureTSV[ken]):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],False)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken])
            tsvcount+=1
        elif os.path.isfile(kanzip_prefectureCSV[ken]):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],True)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken]+".tsv")
        elif os.path.isfile(kanzip_prefectureDL[ken]):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],True)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken]+".csv")
        else:
            LTsv_widget_disableenable(kanzip_DLbutton[ken],True)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken]+".zip")
    if tsvcount == kanzip_prefectureMAX and not os.path.isfile(kanzip_kanzip_tsv):
        LTsv_widget_disableenable(kanzip_DLbutton[kanzip_prefectureMAX],True)
    else:
        LTsv_widget_disableenable(kanzip_DLbutton[kanzip_prefectureMAX],False)
    kanzip_buzyicon(kanzip_prefectureMAX,True)
    LTsv_widget_showhide(kanzip_window,True)
    if os.path.isfile(kanzip_kanzip_tsv):
        LTsv_widget_settext(kanzip_window,widget_t="kanzip:completion:{0}".format(kanzip_kanzip_tsv))
    else:
        LTsv_widget_settext(kanzip_window,widget_t="kanzip")

def kanzip_buzyicon(kanzip_ken,kanzip_buzy):
    LTsv_drawtk_selcanvas(kanzip_DLprogres[kanzip_ken])
#    LTsv_draw_delete(kanzip_DLprogres[kanzip_ken])
    LTsv_drawtk_delete("white")
    if kanzip_buzy:
        LTsv_drawtk_color(draw_c="gray"); LTsv_drawtk_glyph(kanzip_prefectures_glyph[kanzip_prefecturesKAN[kanzip_ken]],draw_x=0,draw_y=0,draw_f=kanzip_DLlabel_H-1)
    else:
        for ken in range(kanzip_prefectureMAX+1):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],False)
        LTsv_drawtk_color(draw_c="gray"); LTsv_drawtk_glyphfill(kanzip_prefectures_glyph[kanzip_prefecturesKAN[kanzip_ken]],draw_x=0,draw_y=0,draw_f=kanzip_DLlabel_H-1)
        LTsv_drawtk_color(draw_c="black"); LTsv_drawtk_glyph(kanzip_prefectures_glyph[kanzip_prefecturesKAN[kanzip_ken]],draw_x=0,draw_y=0,draw_f=kanzip_DLlabel_H-1)
#    LTsv_draw_queue(kanzip_DLprogres[kanzip_ken])
    LTsv_drawtk_queue()
    LTsv_widget_showhide(kanzip_DLprogres[kanzip_ken],True)

def kanzip_DL_report(kanzip_DL_cnt=None,kanzip_DL_size=None,kanzip_DL_total=None):
    pass
#    LTsv_libc_printf("{0}({1}/{2})".format(kanzip_prefectureDL[kanzip_ken],min(kanzip_DL_cnt*kanzip_DL_size,kanzip_DL_total),kanzip_DL_total))

def kanzip_DL_shell(kanzip_ken):
    def kanzip_DL_convert(window_objvoid=None,window_objptr=None):
        kanzip_buzyicon(kanzip_ken,True)
        if os.path.isfile(kanzip_prefectureTSV[kanzip_ken]):
            pass
        elif os.path.isfile(kanzip_prefectureCSV[kanzip_ken]):
            kanzip_csv=LTsv_loadcp932file(kanzip_prefectureCSV[kanzip_ken]); kanzip_tsv=""
            kanzip_splits=kanzip_csv.strip('\n').split('\n')
            kantsv_splits=[]; kantsv_splitsfirst=[];
            if kanzip_prefecturesKAN[kanzip_ken] == "事業所":
                for kanzip_CV_cnt,kanzip_split in enumerate(kanzip_splits):
                    kanzip_csvsplits=kanzip_split.split(',')
                    kanzip_tsvfirst=kanzip_csvsplits[7].strip('"')
                    kanzip_tsvrest=kanzip_csvsplits[3].strip('"')+kanzip_csvsplits[4].strip('"')+kanzip_csvsplits[5].strip('"')+kanzip_csvsplits[6].strip('"')+"　"+kanzip_csvsplits[2].strip('"')
                    kantsv_splits.append(kanzip_tsvfirst+'\t'+kanzip_tsvrest+'\n')
            else:
                for kanzip_CV_cnt,kanzip_split in enumerate(kanzip_splits):
                    kanzip_csvsplits=kanzip_split.split(',')
                    kanzip_tsvfirst=kanzip_csvsplits[2].strip('"')
                    if kanzip_tsvfirst in kantsv_splitsfirst:
                        kanzip_tsvrestjoin=kantsv_splits[kantsv_splitsfirst.index(kanzip_tsvfirst)]
                        kanzip_tsvrest=kanzip_csvsplits[8].strip('"') if kanzip_csvsplits[7].strip('"') in kanzip_tsvrestjoin else kanzip_csvsplits[7].strip('"')+kanzip_csvsplits[8].strip('"')
                        kantsv_splits[kantsv_splitsfirst.index(kanzip_tsvfirst)]=kanzip_tsvrestjoin.strip('\n')+' '+kanzip_tsvrest+'\n'
                    else:
                        kantsv_splitsfirst.append(kanzip_tsvfirst)
                        kanzip_tsvrest=kanzip_csvsplits[6].strip('"')+kanzip_csvsplits[7].strip('"')+kanzip_csvsplits[8].strip('"')
                        kantsv_splits.append(kanzip_tsvfirst+'\t'+kanzip_tsvrest+'\n')
            kanzip_tsv="".join(kantsv_splits)
            LTsv_saveplain(kanzip_prefectureTSV[kanzip_ken],kanzip_tsv)
        elif os.path.isfile(kanzip_prefectureDL[kanzip_ken]):
            LTsv_zipload(kanzip_prefectureDL[kanzip_ken],kanzip_prefecturesNAME[kanzip_ken]+".csv",kanzip_prefectureCSV[kanzip_ken])
        else:
            LTsv_download(kanzip_prefectureURL[kanzip_ken],kanzip_prefectureDL[kanzip_ken],kanzip_DL_report)
        LTsv_window_after(kanzip_window,event_b=kanzip_fileexist,event_i="kanzip_fileexist",event_w=10)
    def kanzip_DL_buzy(window_objvoid=None,window_objptr=None):
        kanzip_buzyicon(kanzip_ken,False)
        if kanzip_ken < kanzip_prefectureMAX:
            if os.path.isfile(kanzip_prefectureTSV[kanzip_ken]):
                pass
            elif os.path.isfile(kanzip_prefectureCSV[kanzip_ken]):
                LTsv_widget_settext(kanzip_window,widget_t="kanzip:convert:{0}→{1}".format(kanzip_prefectureCSV[kanzip_ken],kanzip_prefectureTSV[kanzip_ken]))
            elif os.path.isfile(kanzip_prefectureDL[kanzip_ken]):
                LTsv_widget_settext(kanzip_window,widget_t="kanzip:unpack:{0}→{1}".format(kanzip_prefectureDL[kanzip_ken],kanzip_prefectureCSV[kanzip_ken]))
            else:
                LTsv_widget_settext(kanzip_window,widget_t="kanzip:DownLoad:{0}".format(kanzip_prefectureDL[kanzip_ken]))
            LTsv_window_after(kanzip_window,event_b=kanzip_DL_convert,event_i="kanzip_DL_convert",event_w=10)
        else:
            LTsv_widget_settext(kanzip_window,widget_t="kanzip:merge:{0}".format(kanzip_kanzip_tsv))
            LTsv_window_after(kanzip_window,event_b=kanzip_FX_merge,event_i="kanzip_FX_merge",event_w=10)
    return kanzip_DL_buzy,kanzip_DL_convert

def kanzip_FX_merge(window_objvoid=None,window_objptr=None):
    kanzip_tsv,kanzip_preTSV="",""
    for ken in range(kanzip_prefectureMAX):
        kanzip_preTSV=LTsv_loadfile(kanzip_prefectureTSV[ken])
        kanzip_tsv+=kanzip_preTSV
    LTsv_saveplain(kanzip_kanzip_tsv,kanzip_tsv)
    LTsv_window_after(kanzip_window,event_b=kanzip_fileexist,event_i="kanzip_fileexist",event_w=10)

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    from LTsv_kbd    import *
    LTsv_kbdinit()
    LTsv_glyphdicload("kanchar.tsv")
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_color,LTsv_drawtk_polygon,LTsv_drawtk_polygonfill=LTsv_drawGTK_selcanvas,LTsv_drawGTK_color,LTsv_drawGTK_polygon,LTsv_drawGTK_polygonfill
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_glyph,LTsv_drawGTK_glyphfill,LTsv_drawGTK_delete,LTsv_drawGTK_queue
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_color,LTsv_drawtk_polygon,LTsv_drawtk_polygonfill=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_color,LTsv_drawTkinter_polygon,LTsv_drawTkinter_polygonfill
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_glyph,LTsv_drawTkinter_glyphfill,LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
    kanzip_window=LTsv_window_new(widget_t="kanzip",event_b=LTsv_window_exit,widget_w=kanzip_window_W,widget_h=kanzip_window_H)
    if not os.path.isdir(kanzip_workdir): os.mkdir(kanzip_workdir)
    for ken in range(kanzip_prefectureMAX):
        prefecture_x,prefecture_y=kanzip_prefecture_W*(ken%8),kanzip_prefecture_H*(ken//8)
        kanzip_DLlabel[ken]=LTsv_label_new(kanzip_window,widget_t=kanzip_prefecturesKAN[ken],widget_x=prefecture_x,widget_y=prefecture_y,widget_w=kanzip_DLlabel_W,widget_h=kanzip_DLlabel_H,widget_f=kanzip_font)
        kanzip_DLbuzy[str(ken)],kanzip_DLconvert[str(ken)]=kanzip_DL_shell(ken)
        kanzip_DLbutton[ken]=LTsv_button_new(kanzip_window,event_b=kanzip_DLbuzy[str(ken)],widget_t=kanzip_prefecturesNAME[ken],widget_x=prefecture_x,widget_y=prefecture_y+kanzip_DLlabel_H,widget_w=kanzip_DLbutton_W,widget_h=kanzip_DLbutton_H,widget_f=kanzip_font)
        kanzip_DLprogres[ken]=LTsv_canvas_new(kanzip_window,widget_x=prefecture_x+kanzip_DLlabel_W,widget_y=prefecture_y,widget_w=kanzip_DLprogres_W,widget_h=kanzip_DLprogres_H)
    kanzip_DLbuzy[str(kanzip_prefectureMAX)],kanzip_DLconvert[str(kanzip_prefectureMAX)]=kanzip_DL_shell(kanzip_prefectureMAX)
    kanzip_DLbutton[kanzip_prefectureMAX]=LTsv_button_new(kanzip_window,event_b=kanzip_DLbuzy[str(kanzip_prefectureMAX)],widget_t="都道府県と事業所をダウンロード＆コンバートし終えてから[{0}]にマージ。".format(kanzip_kanzip_tsv),widget_x=0,widget_y=kanzip_prefecture_H*6,widget_w=kanzip_FXbutton_W,widget_h=kanzip_FXbutton_H,widget_f=kanzip_font)
    kanzip_DLprogres[kanzip_prefectureMAX]=LTsv_canvas_new(kanzip_window,widget_x=kanzip_window_W-kanzip_DLprogres_W,widget_y=kanzip_prefecture_H*6,widget_w=kanzip_DLprogres_W,widget_h=kanzip_DLprogres_H)
    LTsv_widget_showhide(kanzip_window,True)
    kanzip_fileexist()
    LTsv_window_main(kanzip_window)


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE

