#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
sys.path.append("LTsv")
import copy
from LTsv_printf import *
from LTsv_file   import *
from LTsv_time   import *
from LTsv_calc   import *
#from LTsv_joy    import *
from LTsv_kbd    import *
from LTsv_gui    import *

tinykbd_fontsize,tinykbd_fontspace,tinykbd_fonthalf=5,6,3
tinykbd_menusize,tinykbd_menuspace,tinykbd_menuhalf=10,12,6
tinykbd_W,tinykbd_H=24*4,24
tinykbd_inputSandS,tinykbd_inputNFER,tinykbd_inputXFER,tinykbd_inputKANA="Space","NFER","XFER","KANA"
tinykbd_keepSandS,tinykbd_keepNFER,tinykbd_keepXFER,tinykbd_keepKANA=0,0,0,0
tinykbd_irohamax=12*4; tinykbd_SandS,tinykbd_NFER,tinykbd_XFER,tinykbd_KANA,tinykbd_None=48,49,50,51,52
tinykbd_irohatype= ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","゛","゜","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
tinykbd_irohatypeN=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
tinykbd_irohatypeX=["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ","｜"]
tinykbd_choice=    ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
tinykbd_choiceN=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
tinykbd_choiceX=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","Ε","Ρ","Τ","Υ","Θ","Ι","Ο","Π","｀","プ","Α","Σ","Δ","Φ","Γ","Η","Ξ","Κ","Λ","代","鍵","ぬ","Ζ","Χ","Ψ","Ω","Β","Ν","Μ","熙","●","▲","■","￥","Σ"]
tinykbd_alphatype= ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
tinykbd_alphatypeN=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
tinykbd_alphatypeX=["Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω","●","▲","■"]
tinykbd_irohaalpha=tinykbd_irohatype+tinykbd_alphatype
tinykbd_irohaalphaN=tinykbd_irohatypeN+tinykbd_alphatypeN
tinykbd_irohaalphaX=tinykbd_irohatypeX+tinykbd_alphatypeX
tinykbd_dictype=    ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","漫","幅"]
tinykbd_map,tinykbd_char,tinykbd_pickle,tinykbd_word,tinykbd_zip="","","","",""
tinykbd_kanmapN,tinykbd_kanmapX,tinykbd_kanmapD={},{},{}
tinykbd_fontcolor,tinykbd_bgcolor,tinykbd_markcolor="black","#CFE6CF","red"
tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF=tinykbd_None,tinykbd_None,"000",{"000":"Tap","100":"Tap","010":"Swipe","001":"Flick"}
tinykbd_fontX,tinykbd_fontY,tinykbd_spaceX,tinykbd_spaceY=[0]*(tinykbd_None),[0]*(tinykbd_None),[0]*(tinykbd_None),[0]*(tinykbd_None)
tinykbd_fontchar=[""]*(tinykbd_None); tinykbd_fontchar[tinykbd_SandS],tinykbd_fontchar[tinykbd_NFER],tinykbd_fontchar[tinykbd_XFER],tinykbd_fontchar[tinykbd_KANA]=tinykbd_dictype[0],"Ｎ","Ｘ",tinykbd_irohatype[0]

def kanedit_tinykbd_new(kbdresize=1):
    global tinykbd_W,tinykbd_H
    global tinykbd_fontsize,tinykbd_fontspace,tinykbd_fonthalf
    global tinykbd_menusize,tinykbd_menuspace,tinykbd_menuhalf
    tinykbd_fontspace=6*kbdresize; tinykbd_fontsize,tinykbd_fonthalf=tinykbd_fontspace-1,tinykbd_fontspace//2
    tinykbd_menusize,tinykbd_menuspace,tinykbd_menuhalf=tinykbd_fontsize*2,tinykbd_fontspace*2,tinykbd_fonthalf*2
    tinykbd_H=tinykbd_fontspace*4; tinykbd_W=tinykbd_H*4
    global keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX
    global keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu
    global tinykbd_fontX,tinykbd_fontY,tinykbd_spaceX,tinykbd_spaceY
    global tinykbd_fontchar
    tinykbd_fontX[tinykbd_SandS],tinykbd_fontY[tinykbd_SandS]=1,tinykbd_menuspace+1
    tinykbd_fontX[tinykbd_NFER],tinykbd_fontY[tinykbd_NFER]=1,1
    tinykbd_fontX[tinykbd_XFER],tinykbd_fontY[tinykbd_XFER]=1+tinykbd_fontspace*12+tinykbd_menuspace,1
    tinykbd_fontX[tinykbd_KANA],tinykbd_fontY[tinykbd_KANA]=1+tinykbd_fontspace*12+tinykbd_menuspace,tinykbd_menuspace+1
    for kbd_xy in range(tinykbd_irohamax):
        tinykbd_fontX[kbd_xy],tinykbd_fontY[kbd_xy]=tinykbd_fontspace*(kbd_xy%12)+tinykbd_menuspace,tinykbd_fontspace*(kbd_xy//12)+1
        tinykbd_spaceX[kbd_xy],tinykbd_spaceY[kbd_xy]=tinykbd_fontX[kbd_xy]+tinykbd_fonthalf,tinykbd_fontY[kbd_xy]+tinykbd_fonthalf
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        tinykbd_spaceX[kbd_xy],tinykbd_spaceY[kbd_xy]=tinykbd_fontX[kbd_xy]+tinykbd_menuhalf,tinykbd_fontY[kbd_xy]+tinykbd_menuhalf

kanedit_window=None
kanedit_getkbdnames,kanedit_getkbdkanas,kanedit_inputkey="","",0
kanedit_W,kanedit_H,kanedit_RS=tinykbd_W,tinykbd_H,False
kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind="","","","",""
kanedit_texteditfilename,kanedit_textvalue="",""
kanedit_fontcolor,kanedit_bgcolor,kanedit_markcolor,kanedit_fontsize="black","#FFF3F5","red",10
kanmemo_textvalue,kanmemo_textleft,kanmemo_textright="",0,0
kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor="black","white","red"


def kanedit_redraw():
    LTsv_drawtk_selcanvas(kanedit_canvas); LTsv_drawtk_delete(kanedit_bgcolor)
    kanedit_editdraw(5,5)
    kanedit_memodraw(0,kanedit_H-tinykbd_fontsize)
    kanedit_kbddraw(kanedit_W-tinykbd_W,kanedit_H-tinykbd_H)
    if kanedit_inputkey:
        LTsv_widget_settext(kanedit_window,widget_t="kanedit:{0}".format(kanedit_getkbdnames.replace('\t',' ')))
    LTsv_drawtk_queue()

def kanedit_editdraw(edit_x,edit_y):
    LTsv_drawtk_color(kanedit_bgcolor); LTsv_drawtk_polygonfill(0,0,kanedit_W,0,kanedit_W,kanedit_H,0,kanedit_H)
    LTsv_drawtk_color(kanedit_fontcolor);
    textline_y=edit_y
    for kanedit_textline in kanedit_textvalue.split('\n'):
        kanedit_textline+='\n'
        LTsv_drawtk_glyphfill(kanedit_textline,draw_x=edit_x,draw_y=textline_y,draw_f=kanedit_fontsize,draw_w=1,draw_h=1,draw_LF=True,draw_HT=True,draw_SP=True)
        textline_y+=kanedit_fontsize+1
        if textline_y > kanedit_H:
            break

def kanedit_memodraw(memo_x,memo_y):
    global kanmemo_textvalue,kanmemo_textleft,kanmemo_textright
    global kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor
    LTsv_drawtk_bgcolor(kanmemo_bgcolor); LTsv_drawtk_color(kanmemo_bgcolor); 
    LTsv_drawtk_polygonfill(memo_x,memo_y,kanedit_W-tinykbd_W,memo_y,kanedit_W-tinykbd_W,kanedit_H,memo_x,kanedit_H)
    LTsv_drawtk_color(kanmemo_fontcolor); LTsv_drawtk_glyphfill(kanmemo_textvalue,draw_x=memo_x,draw_y=memo_y,draw_f=tinykbd_fontsize,draw_w=1,draw_h=1,draw_LF=True,draw_HT=True,draw_SP=True)

def kanedit_kbddraw(kbd_x,kbd_y):
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    LTsv_drawtk_bgcolor(tinykbd_bgcolor)
    LTsv_drawtk_color(tinykbd_bgcolor); LTsv_drawtk_polygonfill(kbd_x,kbd_y,kbd_x+tinykbd_W,kbd_y,kbd_x+tinykbd_W,kbd_y+tinykbd_H,kbd_x,kbd_y+tinykbd_H)
    LTsv_drawtk_color(tinykbd_fontcolor)
    for kbd_xy in range(tinykbd_irohamax):
        LTsv_drawtk_glyphfill(tinykbd_fontchar[kbd_xy],draw_x=kbd_x+tinykbd_fontX[kbd_xy],draw_y=kbd_y+tinykbd_fontY[kbd_xy],draw_f=tinykbd_fontsize)
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        LTsv_drawtk_glyphfill(tinykbd_fontchar[kbd_xy],draw_x=kbd_x+tinykbd_fontX[kbd_xy],draw_y=kbd_y+tinykbd_fontY[kbd_xy],draw_f=tinykbd_menusize)

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

def kanedit_tinykbd_select(choice):
    global tinykbd_fontchar
    if choice in tinykbd_irohaalphaN:
        choiceNX=tinykbd_irohaalpha[tinykbd_irohaalphaN.index(choice)]
        tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_kanmapN[choiceNX][0:tinykbd_irohamax]
    elif choice in tinykbd_irohaalphaX:
        choiceNX=tinykbd_irohaalpha[tinykbd_irohaalphaX.index(choice)]
        tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_kanmapX[choiceNX][0:tinykbd_irohamax]

def kanedit_tinykbd_selected(choice):
    global tinykbd_fontchar
    if choice in tinykbd_irohaalphaN:
        choiceNX=tinykbd_irohaalphaN.index(choice)
    elif choice in tinykbd_irohaalphaX:
        choiceNX=tinykbd_irohaalphaX.index(choice)
    return choiceNX

def kanedit_inputchar(inputchar):
    global kanedit_texteditfilename,kanedit_textvalue
    global kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind
    global kanmemo_textvalue,kanmemo_textleft,kanmemo_textright
    charbind=LTsv_readlinerest(kanedit_charbind,inputchar)
    if len(charbind):
        if charbind == "+:Enter":
            kanmemo_textvalue+='\n'
        if charbind == "T:Tab":
            kanmemo_textvalue+='\t'
        if charbind == "G:4Space":
            kanmemo_textvalue+='    '
        if charbind == "<:BS":
            kanmemo_textvalue=kanmemo_textvalue[:-1]
    else:
        kanmemo_textvalue+=inputchar

def kanedit_inputcharNX(choice,kbd_xy):
    global kanedit_texteditfilename,kanedit_textvalue
    if choice in tinykbd_irohaalphaN:
        kanedit_inputchar(tinykbd_kanmapN[tinykbd_irohaalpha[tinykbd_irohaalphaN.index(choice)]][kbd_xy])
    if choice in tinykbd_irohaalphaX:
        kanedit_inputchar(tinykbd_kanmapX[tinykbd_irohaalpha[tinykbd_irohaalphaX.index(choice)]][kbd_xy])

def kanedit_mousecursor():
    global tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF
    tinykbd_cursorMSbf=tinykbd_cursorMSaf; tinykbd_cursorMSaf=tinykbd_None
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    kbd_x,kbd_y=kanedit_W-tinykbd_W,kanedit_H-tinykbd_H
    for kbd_xy in range(tinykbd_irohamax):
        if abs(kbd_x+tinykbd_spaceX[kbd_xy]-mouseX) <= tinykbd_fonthalf and abs(kbd_y+tinykbd_spaceY[kbd_xy]-mouseY) <= tinykbd_fonthalf:
            tinykbd_cursorMSaf=kbd_xy
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        if abs(kbd_x+tinykbd_spaceX[kbd_xy]-mouseX) <= tinykbd_menuhalf and abs(kbd_y+tinykbd_spaceY[kbd_xy]-mouseY) <= tinykbd_menuhalf:
            tinykbd_cursorMSaf=kbd_xy
    return tinykbd_cursorMSaf

def kanedit_mousepress(window_objvoid=None,window_objptr=None):
    global tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF
    tinykbd_cursorMSaf=kanedit_mousecursor()
    LTsv_setkbddata(25,25); kanedit_getmouse=LTsv_getkbdlabels("MouseL\tMouseR\tMouseC")
    tinykbd_cursorLCR="Tap"
#    tinykbd_cursorLCR="{0}{1}{2}".format(LTsv_pickdatalabel(kanedit_getmouse,"MouseL"),LTsv_pickdatalabel(kanedit_getmouse,"MouseC"),LTsv_pickdatalabel(kanedit_getmouse,"MouseR"))
#    LTsv_libc_printf("kanedit_mousepress「{0}」「{1}」".format(tinykbd_cursorLCR,kanedit_getmouse))
#    if tinykbd_cursorLCR in tinykbd_cursorTSF:
#        tinykbd_cursorLCR=tinykbd_cursorTSF[tinykbd_cursorLCR]
#    if tinykbd_cursorLCR == "Swipe":
#        tinykbd_cursorLCR="SwipeN"
    if tinykbd_cursorMSaf == tinykbd_SandS:
        tinykbd_cursorLCR="Flick"
    if tinykbd_cursorMSaf == tinykbd_NFER:
        tinykbd_cursorLCR="SwipeN"
    if tinykbd_cursorMSaf == tinykbd_XFER:
        tinykbd_cursorLCR="SwipeX"
    if tinykbd_cursorMSaf == tinykbd_KANA:
        tinykbd_cursorLCR="SwipeK"
    if tinykbd_cursorLCR == "Tap":
        if tinykbd_cursorMSaf < tinykbd_None:
            if tinykbd_cursorMSaf < tinykbd_irohamax:
                kanedit_inputcharNX(tinykbd_fontchar[tinykbd_KANA],tinykbd_cursorMSaf)
    if tinykbd_cursorLCR == "SwipeN":
        tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohaalphaN[kanedit_tinykbd_selected(tinykbd_fontchar[tinykbd_KANA])]
        kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
    if tinykbd_cursorLCR == "SwipeX":
        tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohaalphaX[kanedit_tinykbd_selected(tinykbd_fontchar[tinykbd_KANA])]
        kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
    if tinykbd_cursorLCR == "SwipeK":
        if tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaN:
            tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_choiceN[0:tinykbd_irohamax]
        elif tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaX:
            tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_choiceX[0:tinykbd_irohamax]
    if tinykbd_cursorLCR == "Flick":
        for kbd_xy in range(tinykbd_irohamax):
            tinykbd_fontchar[kbd_xy]=LTsv_pickdatalabel(LTsv_readlinerest(tinykbd_char,tinykbd_fontchar[kbd_xy]),tinykbd_fontchar[tinykbd_SandS])
            tinykbd_fontchar[kbd_xy]=tinykbd_fontchar[kbd_xy][0:1]
    kanedit_redraw()

def kanedit_mousemotion(window_objvoid=None,window_objptr=None):
    tinykbd_cursorMSaf=kanedit_mousecursor()
    if tinykbd_cursorLCR == "SwipeN":
        if tinykbd_cursorMSaf < tinykbd_irohamax:
            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohatypeN[tinykbd_cursorMSaf]
        if tinykbd_cursorMSaf == tinykbd_SandS or tinykbd_cursorMSaf == tinykbd_KANA:
            tinykbd_fontchar[tinykbd_KANA]="σ"
        if tinykbd_cursorMSbf != tinykbd_cursorMSaf:
            kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
            kanedit_redraw()
    if tinykbd_cursorLCR == "SwipeX":
        if tinykbd_cursorMSaf < tinykbd_irohamax:
            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohatypeX[tinykbd_cursorMSaf]
        if tinykbd_cursorMSaf == tinykbd_SandS or tinykbd_cursorMSaf == tinykbd_KANA:
            tinykbd_fontchar[tinykbd_KANA]="Σ"
        if tinykbd_cursorMSbf != tinykbd_cursorMSaf:
            kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
            kanedit_redraw()

def kanedit_mouserelease(window_objvoid=None,window_objptr=None):
    global tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF
    tinykbd_cursorMSaf=kanedit_mousecursor()
    if tinykbd_cursorLCR == "SwipeK":
        if tinykbd_cursorMSaf < tinykbd_irohamax:
            if tinykbd_fontchar[tinykbd_cursorMSaf] in tinykbd_dictype:
                tinykbd_fontchar[tinykbd_SandS]=tinykbd_fontchar[tinykbd_cursorMSaf]
            else:
                tinykbd_fontchar[tinykbd_KANA]=tinykbd_fontchar[tinykbd_cursorMSaf]
        kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
    if tinykbd_cursorLCR == "Flick":
        kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
        if tinykbd_cursorMSaf < tinykbd_irohamax:
            kanedit_inputchar(LTsv_pickdatalabel(LTsv_readlinerest(tinykbd_char,tinykbd_fontchar[tinykbd_cursorMSaf]),tinykbd_fontchar[tinykbd_SandS]))
    tinykbd_cursorLCR=""
    kanedit_redraw()

def kanedit_keypress(window_objvoid=None,window_objptr=None):
    global kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind
    global kanedit_getkbdnames,kanedit_getkbdkanas,kanedit_inputkey
    global tinykbd_keepSandS,tinykbd_keepNFER,tinykbd_keepXFER,tinykbd_keepKANA
    LTsv_setkbddata(20,0)
    kanedit_getkbdnames,kanedit_getkbdkanas=LTsv_getkbdnames(),LTsv_getkbdkanas()
    keybind=LTsv_readlinerest(kanedit_keybind,kanedit_getkbdnames.rstrip('\t').replace('\t',' '))
    if len(keybind):
        kanedit_inputchar(keybind)
    else:
        if tinykbd_keepSandS == 0 and tinykbd_inputSandS in kanedit_getkbdnames:
            tinykbd_keepSandS=1
            for kbd_xy in range(tinykbd_irohamax):
                tinykbd_fontchar[kbd_xy]=LTsv_pickdatalabel(LTsv_readlinerest(tinykbd_char,tinykbd_fontchar[kbd_xy]),tinykbd_fontchar[tinykbd_SandS])
                tinykbd_fontchar[kbd_xy]=tinykbd_fontchar[kbd_xy][0:1]
        if tinykbd_keepNFER == 0 and tinykbd_inputNFER in kanedit_getkbdnames:
            tinykbd_keepNFER=1
            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohaalphaN[kanedit_tinykbd_selected(tinykbd_fontchar[tinykbd_KANA])]
            kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
        if tinykbd_keepXFER == 0 and tinykbd_inputXFER in kanedit_getkbdnames:
            tinykbd_keepXFER=1
            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohaalphaX[kanedit_tinykbd_selected(tinykbd_fontchar[tinykbd_KANA])]
            kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
        if tinykbd_keepKANA == 0 and tinykbd_inputKANA in kanedit_getkbdnames:
            tinykbd_keepKANA=1
            if tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaN:
                tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_choiceN[0:tinykbd_irohamax]
            elif tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaX:
                tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_choiceX[0:tinykbd_irohamax]
        for getkbdkanas in kanedit_getkbdkanas.split('\t'):
            if not tinykbd_keepKANA:
                if getkbdkanas in tinykbd_irohatype:
#                    kanedit_inputcharNX(tinykbd_fontchar[tinykbd_KANA],tinykbd_irohatype.index(getkbdkanas))
#kanedit_inputchar(inputchar)
                    kanedit_inputcharNX(tinykbd_fontchar[tinykbd_KANA],tinykbd_irohatype.index(getkbdkanas))
    kanedit_redraw()

def kanedit_keyrelease(window_objvoid=None,window_objptr=None):
    global kanedit_getkbdnames,kanedit_getkbdkanas,kanedit_inputkey
    global tinykbd_keepSandS,tinykbd_keepNFER,tinykbd_keepXFER,tinykbd_keepKANA
    if kanedit_getkbdnames == tinykbd_inputSandS:
        kanedit_inputcharNX(tinykbd_fontchar[tinykbd_KANA],tinykbd_SandS)
    LTsv_setkbddata(20,0)
    kanedit_getkbdnames=LTsv_getkbdnames()
    if not tinykbd_inputSandS in kanedit_getkbdnames:
        tinykbd_keepSandS=0
        kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
    if not tinykbd_inputNFER in kanedit_getkbdnames:
        tinykbd_keepNFER=0
    if not tinykbd_inputXFER in kanedit_getkbdnames:
        tinykbd_keepXFER=0
    if not tinykbd_inputKANA in kanedit_getkbdnames:
        tinykbd_keepKANA=0
    kanedit_redraw()

def kanedit_textload(filename):
    global kanedit_window
    global kanedit_texteditfilename,kanedit_textvalue
    kanedit_texteditfilename=filename
    LTsv_widget_settext(kanedit_window,widget_t="kanedit:{0}".format(kanedit_texteditfilename))
    kanedit_textvalue=LTsv_loadfile(kanedit_texteditfilename)

def kanedit_configload():
    global kanedit_W,kanedit_H,kanedit_RS
    global kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind
    global tinykbd_inputSandS,tinykbd_inputNFER,tinykbd_inputXFER,tinykbd_inputKANA
    global kanedit_getkbdnames,kanedit_getkbdkanas,kanedit_inputkey
    global kanedit_fontcolor,kanedit_bgcolor,kanedit_markcolor,kanedit_fontsize
    global tinykbd_map,tinykbd_char,tinykbd_pickle,tinykbd_word,tinykbd_zip
    global tinykbd_kanmapN,tinykbd_kanmapX,tinykbd_kanmapD
    global tinykbd_fontcolor,tinykbd_bgcolor,tinykbd_markcolor
    global tinykbd_fontchar
    global kanmemo_textvalue,kanmemo_textleft,kanmemo_textright
    global kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_tinykbd=LTsv_getpage(kanedit_ltsv,"tinykbd")
    kbd_resize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_tinykbd,"kbd_resize")),1),5)
    tinykbd_inputSandS=LTsv_readlinerest(kanedit_tinykbd,"input_SandS",tinykbd_inputSandS)
    tinykbd_inputNFER=LTsv_readlinerest(kanedit_tinykbd,"input_NFER",tinykbd_inputNFER)
    tinykbd_inputXFER=LTsv_readlinerest(kanedit_tinykbd,"input_XFER",tinykbd_inputXFER)
    tinykbd_inputKANA=LTsv_readlinerest(kanedit_tinykbd,"input_KANA",tinykbd_inputKANA)
    tinykbd_fontcolor,tinykbd_bgcolor,tinykbd_markcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_tinykbd,"kbd_colors"),"font","bg","mark"))
    tinykbd_map=LTsv_loadfile(LTsv_readlinerest(kanedit_tinykbd,"dic_mapname","kanmap.tsv"))
    for irohaalpha in tinykbd_irohaalpha:
        kbd_lineT=LTsv_readlinerest(tinykbd_map,irohaalpha)
        kbd_lineL=kbd_lineT.split('\t'); kbd_lineL=kbd_lineL+[" "]*(tinykbd_SandS*2-len(kbd_lineL))
        tinykbd_kanmapN[irohaalpha],tinykbd_kanmapX[irohaalpha]=kbd_lineL[0:tinykbd_SandS+1],kbd_lineL[tinykbd_SandS+1:tinykbd_SandS+1+tinykbd_SandS+1]
    kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
    tinykbd_fontchar[tinykbd_KANA]=LTsv_readlinerest(kanedit_tinykbd,"find_NXalpha",tinykbd_fontchar[tinykbd_KANA])
    tinykbd_fontchar[tinykbd_KANA]=tinykbd_fontchar[tinykbd_KANA] if tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaN or tinykbd_fontchar[tinykbd_KANA] in tinykbd_irohaalphaX else tinykbd_irohatype[0]
    tinykbd_fontchar[tinykbd_SandS]=LTsv_readlinerest(kanedit_tinykbd,"find_dic",tinykbd_fontchar[tinykbd_SandS])
    tinykbd_fontchar[tinykbd_SandS]=tinykbd_fontchar[tinykbd_SandS] if tinykbd_fontchar[tinykbd_SandS] in tinykbd_dictype else tinykbd_dictype[0]
    tinykbd_char=LTsv_loadfile(LTsv_readlinerest(kanedit_tinykbd,"dic_charname","kanchar.tsv"))
    tinykbd_pickle=LTsv_readlinerest(kanedit_tinykbd,"glyph_picklename","kanchar.tsv")
    LTsv_glyphOBJunpickle(tinykbd_pickle)

    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_tinykbd_new(kbd_resize)
    kanedit_resizeW,kanedit_resizeH=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"window_size"),"width","height"))
    kanedit_W,kanedit_H=min(max(LTsv_intstr0x(kanedit_resizeW),tinykbd_W),LTsv_screen_w(kanedit_window)),min(max(LTsv_intstr0x(kanedit_resizeH),tinykbd_H),LTsv_screen_h(kanedit_window))
    kanedit_inputkey=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"kbd_inputkey")),0),1)
    kanedit_fontcolor,kanedit_bgcolor,kanedit_markcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"edit_colors"),"font","bg","mark"))
    kanmemo_fontcolor,kanmemo_bgcolor,kanmemo_markcolor=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanedit_config,"memo_colors"),"font","bg","mark"))
    kanedit_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"font_size",str(kanedit_fontsize))),5),100)
    LTsv_glyphdicload(LTsv_readlinerest(kanedit_config,"dic_charname","kanchar.tsv"))
    tinykbd_word=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_wordname","kanword.tsv"))
    tinykbd_zip=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_zipname","kanzip.tsv"))
    kanedit_texteditfilename=LTsv_readlinerest(kanedit_config,"open_last","kanedit.txt")
    kanedit_textload(kanedit_texteditfilename)
    kanedit_keybind=LTsv_getpage(kanedit_ltsv,"keybind")
    kanedit_charbind=LTsv_getpage(kanedit_ltsv,"charbind")
    kanmemo_textvalue=LTsv_readlinerest(kanedit_config,"eval_entry")

def kanedit_exit_configsave(window_objvoid=None,window_objptr=None):
    global kanedit_ltsv,kanedit_config,kanedit_tinykbd,kanedit_keybind,kanedit_charbind
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_tinykbd=LTsv_getpage(kanedit_ltsv,"tinykbd")
    kanedit_tinykbd=LTsv_pushlinerest(kanedit_tinykbd,"find_NXalpha",tinykbd_fontchar[tinykbd_KANA])
    kanedit_tinykbd=LTsv_pushlinerest(kanedit_tinykbd,"find_dic",tinykbd_fontchar[tinykbd_SandS])
    kanedit_ltsv=LTsv_putpage(kanedit_ltsv,"tinykbd",kanedit_tinykbd)
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_config=LTsv_pushlinerest(kanedit_config,"open_last",kanedit_texteditfilename)
    kanedit_config=LTsv_pushlinerest(kanedit_config,"eval_entry",kanmemo_textvalue)
    kanedit_ltsv=LTsv_putpage(kanedit_ltsv,"kanedit",kanedit_config)
    LTsv_savefile("kanedit.tsv",kanedit_ltsv)
    LTsv_glyphOBJpickle(tinykbd_pickle)
    LTsv_window_exit()
kanedit_exit_configsave_cbk=LTsv_CALLBACLTYPE(kanedit_exit_configsave)


LTsv_GUI=LTsv_guiinit()
#kantray_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff :「kanedit」non limit!
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_initmouse=True)
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_selcanvas,LTsv_drawGTK_delete,LTsv_drawGTK_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color,LTsv_drawtk_bgcolor=LTsv_drawGTK_glyph,LTsv_drawGTK_glyphfill,LTsv_drawGTK_color,LTsv_drawGTK_bgcolor
        LTsv_drawtk_polygonfill,LTsv_drawtk_picture=LTsv_drawGTK_polygonfill,LTsv_drawGTK_picture
        LTsv_drawtk_font,LTsv_drawtk_text=LTsv_drawGTK_font,LTsv_drawGTK_text
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color,LTsv_drawtk_bgcolor=LTsv_drawTkinter_glyph,LTsv_drawTkinter_glyphfill,LTsv_drawTkinter_color,LTsv_drawTkinter_bgcolor
        LTsv_drawtk_polygonfill,LTsv_drawtk_picture=LTsv_drawTkinter_polygonfill,LTsv_drawTkinter_picture
        LTsv_drawtk_font,LTsv_drawtk_text=LTsv_drawTkinter_font,LTsv_drawTkinter_text
    kanedit_window=LTsv_window_new(widget_t="kanedit",event_b=kanedit_exit_configsave,widget_w=kanedit_W,widget_h=kanedit_H,event_z=kanedit_resize,event_k=kanedit_keypress,event_y=kanedit_keyrelease)
    kanedit_configload()
    LTsv_window_resize(kanedit_window,kanedit_W,kanedit_H)
    kanedit_canvas=LTsv_canvas_new(kanedit_window,widget_x=0,widget_y=0,widget_w=LTsv_screen_w(kanedit_window),widget_h=LTsv_screen_h(kanedit_window),
     event_p=kanedit_mousepress,event_r=kanedit_mouserelease,event_m=kanedit_mousemotion,event_w=50)
    kanedit_clipboard=LTsv_clipboard_new(kanedit_window)
    LTsv_widget_showhide(kanedit_window,True)
    kanedit_resize()
    kanedit_redraw()
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
