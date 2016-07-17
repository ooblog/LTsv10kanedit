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


kanfont_ltsv,kanfont_config="",""
kanfont_chartype=["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","幅"]
kanfont_chartype_label,kanfont_chartype_entry=[None]*len(kanfont_chartype),[None]*len(kanfont_chartype)
kanfont_dicname,kanfont_mapname,kanfont_svgname,kanfont_fontname,kanfont_fontwidths="kanchar.tsv","kanmap.tsv","kanfont.svg","kantray5x5comic","1024,624"
kanfont_fontgrid,kanfont_fontinner,kanfont_gridimage=25,0,"/mnt/sdb1/github/LTsv9kantray/kanfont_grid25_199.png"
kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half="□","","","","",1024
kanfont_dic,kanfont_alpha="名","α"
kanfont_getkbdstr,kanfont_cursorLCR="MouseL:0\tMouseC:0\tMouseR:0",""
kanfont_setfind=True
kantray_kanchar=""
keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM=0,0,0,0,-1,False
LTsv_keyboard_irohamax,LTsv_keyboard_alphapos,LTsv_keyboard_guidepos,LTsv_keyboard_dicinppos,LTsv_keyboard_dicselpos=48,49,50,51,52

kanfont_gridimageOBJ=None
kanfont_gridxy=[[0]*(6*5*2*2),[0]*(5*5*2),[0]*(6*6*2)]
for gridy in range(6):
    for gridx in range(5):
        kanfont_gridxypos=(gridy*5+gridx)*4
        kanfont_gridxy[0][kanfont_gridxypos+0],kanfont_gridxy[0][kanfont_gridxypos+1]=gridx*100+50,gridy*100
        kanfont_gridxy[0][kanfont_gridxypos+2],kanfont_gridxy[0][kanfont_gridxypos+3]=gridy*100,gridx*100+50
for gridy in range(5):
    for gridx in range(5):
        kanfont_gridxypos=(gridy*5+gridx)*2
        kanfont_gridxy[1][kanfont_gridxypos+0],kanfont_gridxy[1][kanfont_gridxypos+1]=gridx*100+50,gridy*100+50
for gridy in range(6):
    for gridx in range(6):
        kanfont_gridxypos=(gridy*6+gridx)*2
        kanfont_gridxy[2][kanfont_gridxypos+0],kanfont_gridxy[2][kanfont_gridxypos+1]=gridx*100,gridy*100

def kanfont_entry_shell(window_objvoid=None,window_objptr=None):
    global kanfont_setfind
    global kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half
    global kanfont_chartype_label,kanfont_chartype_entry
    kanfont_entry=LTsv_widget_gettext(kanfont_char_entry)
    if len(LTsv_widget_gettext(kanfont_char_entry)) > 2:
        LTsv_widget_settext(kanfont_char_entry,widget_t=LTsv_widget_gettext(kanfont_char_entry)[0]); kanfont_entry=LTsv_widget_gettext(kanfont_char_entry)
    if len(kanfont_entry) == 1:
        LTsv_widget_setnumber(kanfont_char_scale,ord(LTsv_widget_gettext(kanfont_char_entry)))
        LTsv_widget_setnumber(kanfont_char_spin,ord(LTsv_widget_gettext(kanfont_char_entry)))
    kanfont_char=LTsv_widget_gettext(kanfont_char_entry)
    kanfont_kanline=LTsv_readlinerest(kantray_kanchar,kanfont_char)
    if len(kanfont_kanline):
        for chartype_cnt,chartype_split in enumerate(kanfont_chartype):
            kanfont_kandata=LTsv_pickdatalabel(kanfont_kanline,chartype_split)
            LTsv_widget_settext(kanfont_chartype_entry[chartype_cnt],widget_t=kanfont_kandata)
        kanfont_path=LTsv_pickdatalabel(kanfont_kanline,"活")
        kanfont_wide=LTsv_pickdatalabel(kanfont_kanline,"幅")
        kanfont_half=LTsv_intstr0x(kanfont_wide) if len(kanfont_wide) > 0 else PSfont_ZW
    else:
        for chartype_cnt,chartype_split in enumerate(kanfont_chartype):
            LTsv_widget_settext(kanfont_chartype_entry[chartype_cnt],widget_t="")
        kanfont_path=""
        kanfont_wide=""
        kanfont_half=PSfont_ZW
    kanfont_glyphnote=kanfont_glyphpath2note(glyphpath=kanfont_path)
    if kanfont_setfind:
        if kanfont_setchar != kanfont_char:
            LTsv_keyboard_find(kantray_kbdcanvas,find_t=kanfont_char,find_max=kanfont_max)
    else:
        kanfont_setfind=True
    return

def kanfont_entry_setchar(kanfont_charcode):
    global kantray_kanchar
    kanfont_char=chr(kanfont_charcode) if sys.version_info.major >= 3 else unichr(kanfont_charcode)
    if LTsv_widget_gettext(kanfont_char_entry) != kanfont_char:
        LTsv_widget_settext(kanfont_char_entry,widget_t=kanfont_char)
        kanfont_entry_shell()
    return

def kanfont_spin_shell(window_objvoid=None,window_objptr=None):
    if LTsv_widget_getnumber(kanfont_char_scale) != LTsv_widget_getnumber(kanfont_char_spin):
        LTsv_widget_setnumber(kanfont_char_scale,LTsv_widget_getnumber(kanfont_char_spin))
        kanfont_entry_setchar(LTsv_widget_getnumber(kanfont_char_spin))
        kanfont_5x5draw()
    return

def kanfont_scale_shell(window_objvoid=None,window_objptr=None):
    if LTsv_widget_getnumber(kanfont_char_spin) != LTsv_widget_getnumber(kanfont_char_scale):
        LTsv_widget_setnumber(kanfont_char_spin,LTsv_widget_getnumber(kanfont_char_scale))
        kanfont_entry_setchar(LTsv_widget_getnumber(kanfont_char_scale))
        LTsv_widget_settext(kanfont_char_label,hex(LTsv_widget_getnumber(kanfont_char_scale)))
        kanfont_5x5draw()
    return

def LTsv_entry_diccolumn_shell(LTsv_windowPAGENAME,LTsv_called=None):
    def LTsv_entry_diccolumn_kernel(window_objvoid=None,window_objptr=None):
        global kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half
        global kanfont_char,kanfont_kanline,kanfont_half,kanfont_path,kantray_kanchar
        global kanfont_chartype_label,kanfont_chartype_entry
        global kantray_kanchar
        if kanfont_chartype[LTsv_called] == "幅":
            kanfont_wide=LTsv_widget_gettext(kanfont_chartype_entry[LTsv_called])
            kanfont_half=LTsv_intstr0x(kanfont_wide) if len(kanfont_wide) > 0 else PSfont_ZW
            if kanfont_half < 0 or PSfont_ZW < kanfont_half or str(kanfont_half) != kanfont_wide:
                kanfont_half=min(max(kanfont_half,0),PSfont_ZW); LTsv_widget_settext(kanfont_chartype_entry[LTsv_called],str(kanfont_half))
        kanfont_kanline=LTsv_setdatalabel(kanfont_kanline,kanfont_chartype[LTsv_called],LTsv_widget_gettext(kanfont_chartype_entry[LTsv_called]))
        kantray_kanchar=LTsv_pushlinerest(kantray_kanchar,kanfont_char,kanfont_kanline); LTsv_keyboard_dic(kandic=kantray_kanchar)
        if kanfont_chartype[LTsv_called] == "活":
            pass
        kanfont_path=LTsv_pickdatalabel(kanfont_kanline,"活")
        kanfont_glyphnote=kanfont_glyphpath2note(glyphpath=kanfont_path)
        return
    return LTsv_entry_diccolumn_kernel

def kanfont_mapexchange_shell(window_objvoid=None,window_objptr=None):
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    cursor_iroha=keyboard_irohatype[keyboard_cursorIR] if keyboard_cursorIR < LTsv_keyboard_irohamax else keyboard_alphatype[keyboard_cursorAF]
    if keyboard_cursorNX:
        keyboard_kanmapN[cursor_iroha][keyboard_cursorOLD]=LTsv_widget_gettext(kanfont_exchange_entry)
        LTsv_keyboard_map(kanmapN=keyboard_kanmapN)
    else:
        keyboard_kanmapX[cursor_iroha][keyboard_cursorOLD]=LTsv_widget_gettext(kanfont_exchange_entry)
        LTsv_keyboard_map(kanmapX=keyboard_kanmapX)
    LTsv_keyboard_find(kantray_kbdcanvas)
    LTsv_widget_settext(kanfont_exchange_entry,"")
    return

def kanfont_dicsave_shell(window_objvoid=None,window_objptr=None):
    global kantray_kanchar
    LTsv_widget_disableenable(kanfont_dic_button,False)
    kantray_kanchar=LTsv_keyboard_dic()
    LTsv_saveplain(kanfont_dicname,kantray_kanchar)
    LTsv_widget_disableenable(kanfont_dic_button,True)
    return

def kanfont_mapsave_shell(window_objvoid=None,window_objptr=None):
    LTsv_widget_disableenable(kanfont_map_button,False)
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    keyboard_kanmapT=""
    for kanfont_guide in keyboard_irohatype+keyboard_alphatype:
        keyboard_kanmapT+="{0}\t{1}\t{2}\n".format(kanfont_guide,"\t".join(keyboard_kanmapN[kanfont_guide]),"\t".join(keyboard_kanmapX[kanfont_guide]))
    LTsv_widget_disableenable(kanfont_map_button,True)
    LTsv_saveplain(kanfont_mapname,keyboard_kanmapT)
    return

def kanfont_svgsave_shell(window_objvoid=None,window_objptr=None):
    global kantray_kanchar
    LTsv_widget_disableenable(kanfont_svg_button,False)
    kantray_kancharL=kantray_kanchar.rstrip('\n').split('\n')
    kanfont_svg=(
      '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
      '<svg\n'
      '  xmlns="http://www.w3.org/2000/svg" version="1.1"\n'
      '  xmlns:dc="http://purl.org/dc/elements/1.1/"\n'
      '  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n'
      '  xmlns:svg="http://www.w3.org/2000/svg">\n'
      '    <defs>\n'
    )
    for fontwidths in kanfont_fontwidths.split('\t'):
        kanfont_svg+=(
          '        <font id="{0}" horiz-adv-x="{2}">\n'
          '            <font-face font-family="{1}" units-per-em="{2}"/>\n'
          ''.format(kanfont_fontname if fontwidths == "1024" else "{0}_w{1}".format(kanfont_fontname,fontwidths),kanfont_fontname,fontwidths)
        )
        for kanlineL in kantray_kancharL:
            kanfont_path=LTsv_pickdatalabel(kanlineL,"活")
            if len(kanfont_path):
                kanfont_wide=LTsv_pickdatalabel(kanlineL,"幅")
                kanfont_wide=kanfont_wide if len(kanfont_wide) else "1024"
                if kanfont_wide == fontwidths:
                    kanfont_glyphname=kanlineL[0:kanlineL.find('\t')]
                    kanfont_glyphname=kanfont_glyphname if not kanfont_glyphname in '&"<>' else LTsv_utf2xml(kanfont_glyphname)
                    kanfont_svg+=(
                      '            <glyph glyph-name="{0}" unicode="{0}" d="{1}" />\n'.format(kanfont_glyphname,kanfont_path)
                    )
        kanfont_svg+=(
          '        </font>\n'
        )
    kanfont_svg+=(
      '    </defs>\n'
      '</svg>\n'
    )
    LTsv_saveplain(kanfont_svgname,kanfont_svg)
    LTsv_widget_disableenable(kanfont_svg_button,True)
    return

def kanfont_getkey():
    global kanfont_getkbdstr,kanfont_cursorLCR
    LTsv_setkbddata(25,0); kanfont_getkbdstr=LTsv_getkbdlabels("MouseL\tMouseR\tMouseC")
    return kanfont_getkbdstr

def kanfont_setkey(setkey=None,setfind=True):
    global kanfont_setchar,kanfont_setfind
    kanfont_setchar=setkey
    kanfont_setfind=setfind
    if setkey != None:
        keyboard_bmp=setkey[0] if len(setkey) > 0 else " "
        if LTsv_GUI == "Tkinter":
            keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
            keyboard_bmp=keyboard_bmp if ord(keyboard_bmp) < 65535 else keyboard_tofu
        LTsv_widget_setnumber(kanfont_char_scale,ord(keyboard_bmp))

def kanfont_glyphnoteadjustment(glyphnote=""):
    LTsv_widget_setnumber(kanfont_path_scale,len(glyphnote))
    LTsv_scale_adjustment(kanfont_path_scale,widget_s=0,widget_e=len(glyphnote))
    LTsv_widget_setnumber(kanfont_path_scale,len(glyphnote))
    LTsv_widget_showhide(kanfont_path_scale,True)

def kanfont_glyphpath2note(glyphpath=""):
    global kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half
    glyphnote=[]
    glyphpathZ=glyphpath.strip(' ').replace('Z','z').rstrip('z').split('z') if len(glyphpath) else []
    for glyphline in glyphpathZ:
        glyphdata=glyphline.split(' '); glyphpointlist=[]
        for glyphpoint in glyphdata:
            if glyphpoint.count(',') != 1: continue;
            glyphpoints=glyphpoint.strip(' ').split(',')
            glyphpointlist+=[int(glyphpoints[0])//2 if glyphpoints[0].isdigit() else 0]
            glyphpointlist+=[(PSchar_ZW-int(glyphpoints[1]))//2 if glyphpoints[1].isdigit() else 0]
        glyphnote.append(glyphpointlist)
    kanfont_glyphnoteadjustment(glyphnote=glyphnote)
    return glyphnote

def kanfont_fontdraw(callback_void=None,callback_ptr=None):
    global kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half
    global keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM
    keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX=LTsv_keyboard_iroha_guide()
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    LTsv_drawtk_selcanvas(kanfont_canvas)
    LTsv_drawtk_delete("white")
    LTsv_drawtk_color(draw_c="#9F6C00"); gridx=kanfont_half//2
    if keyboard_gridM:
        if kanfont_gridimageOBJ:
            LTsv_drawtk_picture(kanfont_gridimage,0,0)
        else:
            for gridxy in range(3):
                LTsv_drawtk_circles(gridxy*2+1,*tuple(kanfont_gridxy[gridxy]))
    for gridy in range(11):
        LTsv_drawtk_squares(7,*(gridx,gridy*50))
    LTsv_drawtk_squares(7,*(gridx,PSchar_ZW//2+8))
    if keyboard_gridM:
        LTsv_drawtk_font(kanfont_font_grid)
        LTsv_drawtk_text(draw_t="X{0:3}Y{1:3}".format(keyboard_gridX,keyboard_gridY),draw_x=keyboard_gridX,draw_y=keyboard_gridY)
    glyphlayer=LTsv_widget_getnumber(kanfont_path_scale)
    for glyphpointlist_count,glyphpointlist in enumerate(kanfont_glyphnote):
        glyphclockwise=LTsv_clockwise(*tuple(glyphpointlist))
        LTsv_drawtk_color(draw_c="#6E81D9" if glyphclockwise > 0 else "#6ED997" if glyphclockwise < 0 else "#D96ED3")
        LTsv_drawtk_polygon(*tuple(glyphpointlist))
        if glyphlayer == glyphpointlist_count:
            LTsv_drawtk_circlesfill(10,*tuple(glyphpointlist))
            if 0 <= keyboard_gridZ*2 < len(glyphpointlist):
                LTsv_drawtk_squaresfill(10,*tuple(glyphpointlist[keyboard_gridZ*2:keyboard_gridZ*2+2]))
    LTsv_drawtk_queue()
    LTsv_widget_disableenable(kanfont_exchange_button,True if keyboard_cursorOLD < LTsv_keyboard_alphapos and len(LTsv_widget_gettext(kanfont_exchange_entry)) > 0 else False)
    LTsv_window_after(kanfont_window,event_b=kanfont_fontdraw,event_i="kanfont_fontdraw",event_w=50)

def kanfont_grid_shell(window_objvoid=None,window_objptr=None):
    global kanfont_fontgrid,kanfont_fontinner,kanfont_gridimage
    kanfont_fontgrid=LTsv_widget_getnumber(kanfont_grid_spin)
    LTsv_widget_settext(kanfont_inner_check,str(kanfont_fontgrid-1))

def kanfont_gridinner_shell(window_objvoid=None,window_objptr=None):
    global kanfont_fontgrid,kanfont_fontinner,kanfont_gridimage
    kanfont_fontinner=LTsv_widget_getnumber(kanfont_inner_check)

def kanfont_canvas_grid():
    global keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM
    keyboard_mouseX,keyboard_mouseY=min(max(LTsv_global_canvasmotionX(),0),PSchar_ZW//2),min(max(LTsv_global_canvasmotionY(),0),PSchar_ZW//2)
    if kanfont_fontinner:
        keyboard_gridX=(keyboard_mouseX//kanfont_fontgrid)*kanfont_fontgrid if keyboard_mouseX//(kanfont_fontgrid//2) % 2 == 0 else (keyboard_mouseX//kanfont_fontgrid+1)*kanfont_fontgrid-1
        keyboard_gridY=(keyboard_mouseY//kanfont_fontgrid)*kanfont_fontgrid if keyboard_mouseY//(kanfont_fontgrid//2) % 2 == 0 else (keyboard_mouseY//kanfont_fontgrid+1)*kanfont_fontgrid-1
    else:
        keyboard_gridX,keyboard_gridY=(keyboard_mouseX+(kanfont_fontgrid//2))//kanfont_fontgrid*kanfont_fontgrid,(keyboard_mouseY+(kanfont_fontgrid//2))//kanfont_fontgrid*kanfont_fontgrid

def kanfont_canvas_enter(callback_void=None,callback_ptr=None):
    global kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half
    global keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM
    keyboard_gridM=True
    keyboard_mouseX,keyboard_mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    keyboard_gridX,keyboard_gridY=(keyboard_mouseX+12)//25*25,(keyboard_mouseY+12)//25*25
    LTsv_widget_disableenable(kanfont_chartype_entry[kanfont_chartype.index("活")],False)
    LTsv_widget_disableenable(kanfont_char_entry,False); LTsv_widget_disableenable(kanfont_char_scale,False); LTsv_widget_disableenable(kanfont_char_spin,False)

def kanfont_canvas_press(callback_void=None,callback_ptr=None):
    global kanfont_getkbdstr,kanfont_cursorLCR
    global kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half
    global keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM
    kanfont_canvas_grid()
    glyphlayer=LTsv_widget_getnumber(kanfont_path_scale)
    LTsv_setkbddata(25,25); kanfont_getkbdstr=LTsv_getkbdlabels("MouseL\tMouseR\tMouseC")
    kanfont_cursorLCR="{0}{1}{2}".format(LTsv_pickdatalabel(kanfont_getkbdstr,"MouseL"),LTsv_pickdatalabel(kanfont_getkbdstr,"MouseC"),LTsv_pickdatalabel(kanfont_getkbdstr,"MouseR"))
    if kanfont_cursorLCR == "100" or kanfont_cursorLCR == "000":
        if glyphlayer < len(kanfont_glyphnote):
            if keyboard_gridZ < len(kanfont_glyphnote[glyphlayer])//2:
                kanfont_cursorLCR="reMove"
#                keyboard_removeX,keyboard_removeY=keyboard_gridX,keyboard_gridY
                kanfont_glyphlayer=kanfont_glyphnote[glyphlayer]
                keyboard_removeX,keyboard_removeY=kanfont_glyphlayer[keyboard_gridZ*2],kanfont_glyphlayer[keyboard_gridZ*2+1]
            else:
                 kanfont_glyphnote[glyphlayer]+=[keyboard_gridX]; kanfont_glyphnote[glyphlayer]+=[keyboard_gridY]
        else:
            kanfont_glyphnote.append([keyboard_gridX,keyboard_gridY])
            LTsv_scale_adjustment(kanfont_path_scale,widget_s=0,widget_e=len(kanfont_glyphnote))
            LTsv_widget_showhide(kanfont_path_scale,True)
    elif kanfont_cursorLCR == "001":
        if glyphlayer < len(kanfont_glyphnote):
            if keyboard_gridZ < len(kanfont_glyphnote[glyphlayer])//2:
                 kanfont_cursorLCR="Move"
            else:
                 kanfont_glyphnote[glyphlayer]+=[keyboard_gridX]; kanfont_glyphnote[glyphlayer]+=[keyboard_gridY]
        else:
            kanfont_glyphnote.append([keyboard_gridX,keyboard_gridY])
            LTsv_scale_adjustment(kanfont_path_scale,widget_s=0,widget_e=len(kanfont_glyphnote))
            LTsv_widget_showhide(kanfont_path_scale,True)
    elif kanfont_cursorLCR == "010":
        if glyphlayer < len(kanfont_glyphnote):
            if len(kanfont_glyphnote[glyphlayer]) > 2:
                if keyboard_gridZ < len(kanfont_glyphnote[glyphlayer])//2:
                    kanfont_glyphnote[glyphlayer].pop(keyboard_gridZ*2)
                    kanfont_glyphnote[glyphlayer].pop(keyboard_gridZ*2)
                else:
                    kanfont_glyphnote[glyphlayer].pop()
                    kanfont_glyphnote[glyphlayer].pop()
            else:
                del kanfont_glyphnote[glyphlayer]
                LTsv_scale_adjustment(kanfont_path_scale,widget_s=0,widget_e=len(kanfont_glyphnote))
                LTsv_widget_showhide(kanfont_path_scale,True)

def kanfont_canvas_motion(callback_void=None,callback_ptr=None):
    global kanfont_getkbdstr,kanfont_cursorLCR
    global keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM
    kanfont_canvas_grid()
    glyphlayer=LTsv_widget_getnumber(kanfont_path_scale)
    if glyphlayer < len( kanfont_glyphnote):
        kanfont_glyphlayer=kanfont_glyphnote[glyphlayer]
        if kanfont_cursorLCR == "Move" or kanfont_cursorLCR == "reMove":
            kanfont_glyphlayer[keyboard_gridZ*2],kanfont_glyphlayer[keyboard_gridZ*2+1]=keyboard_gridX,keyboard_gridY
            kanfont_glyphnote[glyphlayer]=kanfont_glyphlayer
            if keyboard_removeX != keyboard_gridX or keyboard_removeY != keyboard_gridY:
                 keyboard_removeX,keyboard_removeY=-1,-1
        else:
            keyboard_gridZ=len(kanfont_glyphlayer)//2
            for glyphpoints in range(len(kanfont_glyphlayer)//2):
#                if kanfont_glyphlayer[glyphpoints*2] == keyboard_gridX and kanfont_glyphlayer[glyphpoints*2+1] == keyboard_gridY:
                if abs(kanfont_glyphlayer[glyphpoints*2]-keyboard_gridX) < kanfont_fontgrid//2 and abs(kanfont_glyphlayer[glyphpoints*2+1]-keyboard_gridY) < kanfont_fontgrid //2:
                    keyboard_gridZ=glyphpoints

def kanfont_canvas_release(callback_void=None,callback_ptr=None):
    global kanfont_getkbdstr,kanfont_cursorLCR
    global keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM
    kanfont_canvas_grid()
    glyphlayer=LTsv_widget_getnumber(kanfont_path_scale)
    if kanfont_cursorLCR == "reMove":
        if keyboard_removeX == keyboard_gridX and keyboard_removeY == keyboard_gridY:
            if len(kanfont_glyphnote[glyphlayer]) > 2:
                if keyboard_gridZ < len(kanfont_glyphnote[glyphlayer])//2:
                    kanfont_glyphnote[glyphlayer].pop(keyboard_gridZ*2)
                    kanfont_glyphnote[glyphlayer].pop(keyboard_gridZ*2)
            else:
                del kanfont_glyphnote[glyphlayer]
                LTsv_scale_adjustment(kanfont_path_scale,widget_s=0,widget_e=len(kanfont_glyphnote))
                LTsv_widget_showhide(kanfont_path_scale,True)
    kanfont_cursorLCR=""

def kanfont_canvas_leave(callback_void=None,callback_ptr=None):
    global kantray_kanchar
    global kanfont_char,kanfont_setchar,kanfont_kanline,kanfont_path,kanfont_glyphnote,kanfont_half
    global keyboard_gridX,keyboard_gridY,keyboard_removeX,keyboard_removeY,keyboard_gridZ,keyboard_gridM
    kanfont_canvas_grid()
    glyphlayer=LTsv_widget_getnumber(kanfont_path_scale)
    keyboard_gridM=False
    kanfont_path=""
    for glyphpoints in kanfont_glyphnote:
        glyphpointlist=""
        for draw_xy_count in range(len(glyphpoints)//2):
            glyphpointlist+="{0},{1} ".format(glyphpoints[draw_xy_count*2]*2,PSchar_ZW-glyphpoints[draw_xy_count*2+1]*2)
        kanfont_path+="M {0}z ".format(glyphpointlist)
    kanfont_path=kanfont_path.rstrip(' ')
    LTsv_widget_settext(kanfont_chartype_entry[kanfont_chartype.index("活")],widget_t=kanfont_path)
    kanfont_kanline=LTsv_setdatalabel(kanfont_kanline,kanfont_chartype[kanfont_chartype.index("活")],LTsv_widget_gettext(kanfont_chartype_entry[kanfont_chartype.index("活")]))
    kantray_kanchar=LTsv_pushlinerest(kantray_kanchar,kanfont_char,kanfont_kanline); LTsv_keyboard_dic(kandic=kantray_kanchar)
    LTsv_widget_disableenable(kanfont_chartype_entry[kanfont_chartype.index("活")],True)
    LTsv_widget_disableenable(kanfont_char_entry,True); LTsv_widget_disableenable(kanfont_char_scale,True); LTsv_widget_disableenable(kanfont_char_spin,True)
    kanfont_5x5draw()

def kanfont_5x5draw():
    LTsv_drawtk_selcanvas(kanfont_5x5)
    LTsv_drawtk_delete("white"); LTsv_drawtk_color("black")
    LTsv_glyphdicread(kantray_kanchar); LTsv_drawtk_glyphpath(kanfont_char)
    LTsv_drawtk_glyphfill(kanfont_char,draw_x=5,draw_y=5,draw_f=5,draw_w=1,draw_h=1)
    LTsv_drawtk_glyphfill(kanfont_char,draw_x=10,draw_y=10,draw_f=10,draw_w=1,draw_h=1)
    LTsv_drawtk_glyphfill(kanfont_char,draw_x=20,draw_y=20,draw_f=20,draw_w=1,draw_h=1)
    LTsv_drawtk_queue()

def kanfont_configload():
    global kanfont_ltsv,kanfont_config
    global kanfont_char,kanfont_dic,kanfont_alpha
    global kanfont_dicname,kanfont_mapname,kanfont_svgname,kanfont_fontname,kanfont_fontwidths
    global kanfont_fontgrid,kanfont_fontinner,kanfont_gridimage
    kanfont_ltsv=LTsv_loadfile("kanfont.tsv")
    kanfont_config=LTsv_getpage(kanfont_ltsv,"kanfont")
    kanfont_alpha=LTsv_readlinerest(kanfont_config,"find_alpha",kanfont_alpha)
    kanfont_dic=LTsv_readlinerest(kanfont_config,"find_dic",kanfont_dic)
    kanfont_char=LTsv_readlinerest(kanfont_config,"find_char",kanfont_char)
    kanfont_svgname=LTsv_readlinerest(kanfont_config,"svg_name",kanfont_svgname)
    kanfont_fontname=LTsv_readlinerest(kanfont_config,"font_name",kanfont_fontname)
    kanfont_fontwidths=LTsv_readlinerest(kanfont_config,"font_widths",kanfont_fontwidths)
    kanfont_fontgrid=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"font_grid")),10),100)
    kanfont_fontinner=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"font_gridinner")),0),1)
    kanfont_gridimage=LTsv_readlinerest(kanfont_config,"gridimage",kanfont_gridimage)
    LTsv_kbdltsv=LTsv_loadfile("LTsv_kbd.tsv")
    keyboard_mapdic_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_mapdic")
    kanfont_mapname=LTsv_readlinerest(keyboard_mapdic_page,"mapname",kanfont_mapname)
    kanfont_dicname=LTsv_readlinerest(keyboard_mapdic_page,"dicname",kanfont_dicname)

def kanfont_exit_configsave(window_objvoid=None,window_objptr=None):
    global kanfont_ltsv,kanfont_config
    global kanfont_char,kanfont_dic,kanfont_alpha
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    kanfont_alpha,kanfont_dic=keyboard_alphatype[keyboard_cursorAF],keyboard_cursorDIC
    kanfont_ltsv=LTsv_loadfile("kanfont.tsv")
    kanfont_config=LTsv_pushlinerest(kanfont_config,"find_alpha",kanfont_alpha)
    kanfont_config=LTsv_pushlinerest(kanfont_config,"find_dic",kanfont_dic)
    kanfont_config=LTsv_pushlinerest(kanfont_config,"find_char",kanfont_char)
    kanfont_config=LTsv_pushlinerest(kanfont_config,"font_grid",str(kanfont_fontgrid))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"font_gridinner",str(kanfont_fontinner))
    kanfont_ltsv=LTsv_putpage(kanfont_ltsv,"kanfont",kanfont_config)
    LTsv_savefile("kanfont.tsv",kanfont_ltsv)
    LTsv_window_exit()
kanfont_exit_configsave_cbk=LTsv_CALLBACLTYPE(kanfont_exit_configsave)

LTsv_GUI=LTsv_guiinit()
kanfont_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_initmouse=False); kantray_kanchar=LTsv_keyboard_dic()
    kanfont_configload()
    kanfont_fontsize_entry=10;    kanfont_font_entry="{0},{1}".format(kanfont_fontname,kanfont_fontsize_entry); kanfont_label_WH=kanfont_fontsize_entry*2
    kanfont_fontsize_scale=40;    kanfont_font_scale="{0},{1}".format(kanfont_fontname,kanfont_fontsize_scale); kanfont_scale_WH=kanfont_fontsize_scale*2
    kanfont_fontsize_keyboard=12; kanfont_font_keyboard="{0},{1}".format(kanfont_fontname,kanfont_fontsize_keyboard)
    kanfont_fontsize_grid=8;      kanfont_font_grid="{0},{1}".format(kanfont_fontname,kanfont_fontsize_grid)
    PSfont_ZW,PSfont_CW,PSchar_ZW,PSchar_CW=1024,624,1000,600
    kanfont_scale_W,kanfont_entry_W=kanfont_scale_WH,400; kanfont_canvas_WH=PSfont_ZW//2
    kanfont_canvas_X=kanfont_scale_W; kanfont_label_X=kanfont_canvas_X+kanfont_canvas_WH; kanfont_entry_X=kanfont_label_X+kanfont_label_WH; kanfont_W=kanfont_entry_X+kanfont_entry_W
    kanfont_H=kanfont_canvas_WH; kanfont_scale_H=kanfont_H-kanfont_scale_WH-kanfont_label_WH-kanfont_label_WH; kanfont_scale_X,kanfont_scale_Y=0,kanfont_scale_WH
    kantray_kbdcanvasWH=LTsv_keyboard_size(12); kantray_kbdcanvasW,kantray_kbdcanvasH=LTsv_intstr0x(LTsv_pickdatanum(kantray_kbdcanvasWH,0)),LTsv_intstr0x(LTsv_pickdatanum(kantray_kbdcanvasWH,1))
    kanfont_button_W,kanfont_button_H=kanfont_W-kanfont_label_X-kanfont_label_WH-kantray_kbdcanvasW-kanfont_label_WH,kantray_kbdcanvasH//3
    kanfont_half=PSfont_ZW
    kanfont_window=LTsv_window_new(widget_t="kanfont",event_b=kanfont_exit_configsave,widget_w=kanfont_W,widget_h=kanfont_H)
    kanfont_canvas=LTsv_canvas_new(kanfont_window,widget_x=kanfont_canvas_X,widget_y=0,widget_w=kanfont_canvas_WH,widget_h=kanfont_canvas_WH,
     event_p=kanfont_canvas_press,event_r=kanfont_canvas_release,event_e=kanfont_canvas_enter,event_m=kanfont_canvas_motion,event_l=kanfont_canvas_leave,event_w=50)
    kanfont_gridimageOBJ=LTsv_draw_picture_load(kanfont_gridimage)
    kanfont_char_entry=LTsv_entry_new(kanfont_window,widget_t="",widget_x=0,widget_y=0,widget_w=kanfont_scale_WH,widget_h=kanfont_scale_WH,widget_f=kanfont_font_scale,event_b=kanfont_entry_shell)
    kanfont_char_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_scale_X,widget_y=kanfont_scale_Y,widget_w=kanfont_scale_W,widget_h=kanfont_scale_H,widget_s=1,widget_e=kanfont_max,widget_a=1,event_b=kanfont_scale_shell)
    kanfont_char_spin=LTsv_spin_new(kanfont_window,widget_x=0,widget_y=kanfont_scale_Y+kanfont_scale_H,widget_w=kanfont_scale_WH,widget_h=kanfont_label_WH,widget_s=1,widget_e=kanfont_max,widget_a=1,widget_f=kanfont_font_entry,event_b=kanfont_spin_shell)
    kanfont_char_label=LTsv_label_new(kanfont_window,widget_t="0xf080",widget_x=0,widget_y=kanfont_scale_Y+kanfont_scale_H+kanfont_label_WH,widget_w=kanfont_scale_WH,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    for chartype_cnt,chartype_split in enumerate(kanfont_chartype):
        if chartype_split in "活":
            kanfont_chartype_label[chartype_cnt]=LTsv_label_new(kanfont_window,widget_t=chartype_split,widget_x=kanfont_label_X,widget_y=chartype_cnt*kanfont_label_WH,widget_w=kanfont_label_WH,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
            kanfont_entry_diccolumn_callback=LTsv_entry_diccolumn_shell(LTsv_widget_newUUID(True),LTsv_called=chartype_cnt)
            kanfont_chartype_entry[chartype_cnt]=LTsv_entry_new(kanfont_window,widget_n=False,widget_t=chartype_split,widget_x=kanfont_entry_X,widget_y=chartype_cnt*kanfont_label_WH,widget_w=kanfont_entry_W*3//4,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_entry_diccolumn_callback)
        elif chartype_split == "幅":
            kanfont_chartype_label[chartype_cnt]=LTsv_label_new(kanfont_window,widget_t=chartype_split,widget_x=kanfont_label_X+kanfont_entry_W*3//4+kanfont_label_WH,widget_y=chartype_cnt*kanfont_label_WH-kanfont_label_WH,widget_w=kanfont_label_WH,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
            kanfont_entry_diccolumn_callback=LTsv_entry_diccolumn_shell(LTsv_widget_newUUID(True),LTsv_called=chartype_cnt)
            kanfont_chartype_entry[chartype_cnt]=LTsv_entry_new(kanfont_window,widget_n=False,widget_t=chartype_split,widget_x=kanfont_entry_X+kanfont_entry_W*3//4+kanfont_label_WH,widget_y=chartype_cnt*kanfont_label_WH-kanfont_label_WH,widget_w=kanfont_entry_W*1//4-kanfont_label_WH,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_entry_diccolumn_callback)
        else:
            kanfont_chartype_label[chartype_cnt]=LTsv_label_new(kanfont_window,widget_t=chartype_split,widget_x=kanfont_label_X,widget_y=chartype_cnt*kanfont_label_WH,widget_w=kanfont_label_WH,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
            kanfont_entry_diccolumn_callback=LTsv_entry_diccolumn_shell(LTsv_widget_newUUID(True),LTsv_called=chartype_cnt)
            kanfont_chartype_entry[chartype_cnt]=LTsv_entry_new(kanfont_window,widget_n=False,widget_t=chartype_split,widget_x=kanfont_entry_X,widget_y=chartype_cnt*kanfont_label_WH,widget_w=kanfont_entry_W,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_entry_diccolumn_callback)
    kantray_kbdcanvas=LTsv_keyboard_new(kanfont_window,widget_x=kanfont_W-kantray_kbdcanvasW,widget_y=kanfont_H-kantray_kbdcanvasH,keyboard_getkey=kanfont_getkey,keyboard_setkey=kanfont_setkey,widget_f=kanfont_font_keyboard)
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_font,LTsv_drawtk_color,LTsv_drawtk_text,LTsv_drawtk_picture=LTsv_drawGTK_selcanvas,LTsv_drawGTK_font,LTsv_drawGTK_color,LTsv_drawGTK_text,LTsv_drawGTK_picture
        LTsv_drawtk_squares,LTsv_drawtk_squaresfill,LTsv_drawtk_circles,LTsv_drawtk_circlesfill=LTsv_drawGTK_squares,LTsv_drawGTK_squaresfill,LTsv_drawGTK_circles,LTsv_drawGTK_circlesfill
        LTsv_drawtk_polygon,LTsv_drawtk_polygonfill=LTsv_drawGTK_polygon,LTsv_drawGTK_polygonfill
        LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_delete,LTsv_drawGTK_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_glyphpath=LTsv_drawGTK_glyph,LTsv_drawGTK_glyphfill,LTsv_glyphpath_outer
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_font,LTsv_drawtk_color,LTsv_drawtk_text,LTsv_drawtk_picture=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_font,LTsv_drawTkinter_color,LTsv_drawTkinter_text,LTsv_drawTkinter_picture
        LTsv_drawtk_squares,LTsv_drawtk_squaresfill,LTsv_drawtk_circles,LTsv_drawtk_circlesfill=LTsv_drawTkinter_squares,LTsv_drawTkinter_squaresfill,LTsv_drawTkinter_circles,LTsv_drawTkinter_circlesfill
        LTsv_drawtk_polygon,LTsv_drawtk_polygonfill=LTsv_drawTkinter_polygon,LTsv_drawTkinter_polygonfill
        LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_glyphpath=LTsv_drawTkinter_glyph,LTsv_drawTkinter_glyphfill,LTsv_glyphpath
    kanfont_5x5=LTsv_canvas_new(kanfont_window,widget_x=kanfont_entry_X-kanfont_label_WH//2,widget_y=(len(kanfont_chartype)-1)*kanfont_label_WH,widget_w=kanfont_entry_W//8,widget_h=kanfont_entry_W//8)
    kanfont_path_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_entry_X+kanfont_entry_W//8,widget_y=(len(kanfont_chartype)-1)*kanfont_label_WH,widget_w=kanfont_entry_W*4//8,widget_h=kanfont_label_WH*2,widget_s=0,widget_e=9,widget_a=1)
    kanfont_grid_label=LTsv_label_new(kanfont_window,widget_t="grid",widget_x=kanfont_entry_X+kanfont_entry_W*5//8,widget_y=(len(kanfont_chartype)-1)*kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_grid_spin=LTsv_spin_new(kanfont_window,widget_x=kanfont_entry_X+kanfont_entry_W*5//8,widget_y=(len(kanfont_chartype)-1)*kanfont_label_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_s=5,widget_e=PSchar_ZW//5,widget_a=1,widget_f=kanfont_font_entry,event_b=kanfont_grid_shell)
    kanfont_inner_label=LTsv_label_new(kanfont_window,widget_t="inner",widget_x=kanfont_entry_X+kanfont_entry_W*6//8,widget_y=(len(kanfont_chartype)-1)*kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_inner_check=LTsv_check_new(kanfont_window,widget_t="24",widget_x=kanfont_entry_X+kanfont_entry_W*6//8,widget_y=(len(kanfont_chartype)-1)*kanfont_label_WH+kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_gridinner_shell)
    kanfont_dic_button=LTsv_button_new(kanfont_window,widget_t=kanfont_dicname,widget_x=kanfont_entry_X,widget_y=kanfont_H-kantray_kbdcanvasH//3*3,widget_w=kanfont_button_W,widget_h=kanfont_button_H,widget_f=kanfont_font_entry,event_b=kanfont_dicsave_shell)
    kanfont_map_button=LTsv_button_new(kanfont_window,widget_t=kanfont_mapname,widget_x=kanfont_entry_X,widget_y=kanfont_H-kantray_kbdcanvasH//3*2,widget_w=kanfont_button_W,widget_h=kanfont_button_H,widget_f=kanfont_font_entry,event_b=kanfont_mapsave_shell)
    kanfont_svg_button=LTsv_button_new(kanfont_window,widget_t=kanfont_svgname,widget_x=kanfont_entry_X,widget_y=kanfont_H-kantray_kbdcanvasH//3*1,widget_w=kanfont_button_W,widget_h=kanfont_button_H,widget_f=kanfont_font_entry,event_b=kanfont_svgsave_shell)
    kanfont_exchange_entry=LTsv_entry_new(kanfont_window,widget_t="",widget_x=kanfont_W-kanfont_entry_W*1//8,widget_y=kanfont_H-kantray_kbdcanvasH-kanfont_label_WH*2,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_exchange_button=LTsv_button_new(kanfont_window,widget_t="↓",widget_x=kanfont_W-kanfont_entry_W*1//8,widget_y=kanfont_H-kantray_kbdcanvasH-kanfont_label_WH,widget_w=kanfont_entry_W*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_mapexchange_shell)
    LTsv_widget_showhide(kanfont_window,True)
    LTsv_keyboard_find(kantray_kbdcanvas,find_t=kanfont_char,find_max=kanfont_max,dic_t=kanfont_dic,alpha_t=kanfont_alpha)
    LTsv_widget_setnumber(kanfont_char_spin,ord(kanfont_char))
    LTsv_widget_setnumber(kanfont_grid_spin,kanfont_fontgrid)
    LTsv_widget_setnumber(kanfont_inner_check,kanfont_fontinner)
    if LTsv_GUI == "Tkinter":
        kanfont_entry_setchar(ord(kanfont_char))
    kanfont_fontdraw()
    kanfont_5x5draw()
    LTsv_window_main(kanfont_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE

