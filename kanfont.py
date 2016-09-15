#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
sys.path.append("LTsv")
from LTsv_printf  import *
from LTsv_file    import *
from LTsv_time    import *
#from LTsv_calc    import *
#from LTsv_joy     import *
#from LTsv_kbd     import *
from LTsv_gui     import *
from LTsv_glyph  import *

PSfont_ZW,PSfont_CW,PSchar_ZW,PSchar_CW=1024,624,1000,600
kanfont_ltsv,kanfont_config="",""
kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage="ぱ",25,0,0,0,"kanfont_grid25_199.png"
kanfont_refer,kanfont_refergrid="Noto Sans Japanese Regular",0
kanfont_referposX,kanfont_referposY,kanfont_referposS,kanfont_referposC=0,0,PSchar_ZW//2,"#E5E5E5"
kanfont_gridX,kanfont_gridY,kanfont_gridP,kanfont_gridQ,kanfont_catchP,kanfont_catchQ,kanfont_catchZ,kanfont_catchX,kanfont_catchY=0,0,-1,-1,-1,-1,-1,0,0
kanfont_layerclip=[]
kanfont_glyphcolorR,kanfont_glyphcolorL,kanfont_glyphcolorX,kanfont_glyphcolorG="#6E81D9","#6ED997","#D96ED3","#9F6C00"
kanfont_dicname,kanfont_svgname,kanfont_fontwidths,kanfont_autosave,kanfont_savetime="kanchar.tsv","kan5x5comic.svg","1024,824,624","off","@0h:@0n:@0s"
kanfont_fontname,kanfont_glyphtype={"活":"kan5x5","漫":"kan5x5comic","筆":"kan5x5brush"},"漫"
kanfont_max=0x2ffff  # if LTsv_GUI != "Tkinter" else 0xffff
kanfont_dictype_label,kanfont_dictype_entry=[None]*(len(LTsv_global_dictype())+1),[None]*(len(LTsv_global_dictype())+1)
LTsv_chrcode=chr if sys.version_info.major == 3 else unichr

pathadjustlen=0
def kanfont_pathadjustment(pathpos=None):
    global pathadjustlen
    pathadjustlen=len(LTsv_glyph_getnote(LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale)),draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    LTsv_widget_setnumber(kanfont_path_scale,pathadjustlen)
    LTsv_scale_adjustment(kanfont_path_scale,widget_s=0,widget_e=pathadjustlen)
    LTsv_widget_setnumber(kanfont_path_scale,pathadjustlen if pathpos == None else min(max(pathpos,0),pathadjustlen))
    LTsv_widget_showhide(kanfont_path_scale,True)

def kanfont_code(pathpos=None):
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    kanfont_seek=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    LTsv_widget_settext(kanfont_code_label,hex(LTsv_widget_getnumber(kanfont_code_scale)).replace("0x","U+"))
    kanfont_pathadjustment(pathpos)
    LTsv_glyphpath(kanfont_seek)
    kanfont_glyph_draw()
    LTsv_widget_disableenable(kanfont_copy_button,True if kanfont_seek != LTsv_widget_gettext(kanfont_clipboard)[:1] else False); LTsv_widget_showhide(kanfont_copy_button,True)
    kanfont_pathsel_shell()
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_global_kandic(),kanfont_seek)
    for dictype_cnt,dictype_split in enumerate(LTsv_global_dictype()):
        LTsv_kbdentry_settext(kanfont_dictype_canvas[dictype_cnt],widget_t=LTsv_pickdatalabel(LTsv_glyph_kanline,dictype_split))
    LTsv_widget_settext(kanfont_svg_button,"save:{0}({1})".format(kanfont_svgname,kanfont_fontname[kanfont_glyphtype if kanfont_glyphtype in LTsv_global_glyphtype() else LTsv_global_glyphtype()[kanfont_gothic]]))

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
    kbdentrycode=ord(kbdentry[:1])
    LTsv_widget_setnumber(kanfont_code_scale,int(kbdentrycode))
    kanfont_code()

def kanfont_codekbd_paste(window_objvoid=None,window_objptr=None):
    clippaste=LTsv_widget_gettext(kanfont_clipboard)[:1]
    LTsv_glyph_kbdfind(clippaste)
    kanfont_codekbd(clippaste)
    LTsv_glyph_kbddelete(kanfont_kbd_canvas); LTsv_glyph_kbddraw(kanfont_kbd_canvas,0,2); LTsv_draw_queue()

def kanfont_codekbd_copy(window_objvoid=None,window_objptr=None):
    LTsv_widget_settext(kanfont_clipboard,LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale)))
    LTsv_widget_disableenable(kanfont_copy_button,True if kanfont_seek != LTsv_widget_gettext(kanfont_clipboard)[:1] else False); LTsv_widget_showhide(kanfont_copy_button,True)

def kanfont_pathsel_shell(window_objvoid=None,window_objptr=None):
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    LTsv_widget_disableenable(kanfont_layerX_button,True if kanfont_catchZ < pathadjustlen else False); LTsv_widget_showhide(kanfont_layerX_button,True)
    LTsv_widget_disableenable(kanfont_layerC_button,True if kanfont_catchZ < pathadjustlen else False); LTsv_widget_showhide(kanfont_layerC_button,True)
    LTsv_widget_disableenable(kanfont_layerV_button,True if kanfont_layerclip != [] else False); LTsv_widget_showhide(kanfont_layerV_button,True)
    LTsv_widget_disableenable(kanfont_layerU_button,True if kanfont_catchZ < pathadjustlen-1 else False); LTsv_widget_showhide(kanfont_layerU_button,True)
    LTsv_widget_disableenable(kanfont_layerD_button,True if 0 < kanfont_catchZ < pathadjustlen else False); LTsv_widget_showhide(kanfont_layerD_button,True)
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
    kanfont_glyph_draw()

def debug_gothic_shell(radioNumber):
    def debug_gothic_kernel(window_objvoid=None,window_objptr=None):
        global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
        if kanfont_gothic != radioNumber:
            kanfont_gothic=radioNumber
            kanfont_code()
    return debug_gothic_kernel

def kanfont_refer_shell(window_objvoid=None,window_objptr=None):
    global kanfont_refer,kanfont_refergrid
    kanfont_refergrid=LTsv_widget_getnumber(kanfont_refer_check)
    kanfont_glyph_draw()

def kanfont_layerX_shell(window_objvoid=None,window_objptr=None):
    global kanfont_layerclip
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_pointsrotation(LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    if kanfont_catchZ < len(glyphnote):
        kanfont_layerclip=glyphnote[kanfont_catchZ]
        del glyphnote[kanfont_catchZ]
    else:
         kanfont_layerclip=[]
    LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_code(kanfont_catchZ)

def kanfont_layerC_shell(window_objvoid=None,window_objptr=None):
    global kanfont_layerclip
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_pointsrotation(LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    if kanfont_catchZ < len(glyphnote):
        kanfont_layerclip=glyphnote[kanfont_catchZ]
    else:
         kanfont_layerclip=[]
    LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_code(kanfont_catchZ)

def kanfont_layerV_shell(window_objvoid=None,window_objptr=None):
    global kanfont_layerclip
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_pointsrotation(LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    glyphnote=glyphnote
    if kanfont_catchZ < len(glyphnote):
        if kanfont_layerclip != []:
            glyphnote[kanfont_catchZ]=kanfont_layerclip
    else:
        glyphnote.append(kanfont_layerclip)
    LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_code(kanfont_catchZ)

def kanfont_layerU_shell(window_objvoid=None,window_objptr=None):
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_pointsrotation(LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    if kanfont_catchZ < len(glyphnote)-1:
        glyphnote[kanfont_catchZ],glyphnote[kanfont_catchZ+1]=glyphnote[kanfont_catchZ+1],glyphnote[kanfont_catchZ]
    LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_code(kanfont_catchZ+1)

def kanfont_layerD_shell(window_objvoid=None,window_objptr=None):
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_pointsrotation(LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    if 0 < kanfont_catchZ < len(glyphnote):
        glyphnote[kanfont_catchZ-1],glyphnote[kanfont_catchZ]=glyphnote[kanfont_catchZ],glyphnote[kanfont_catchZ-1]
    LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_code(kanfont_catchZ-1)

def kanfont_glyph_grid():
    global kanfont_gridX,kanfont_gridY,kanfont_gridP,kanfont_gridQ,kanfont_catchP,kanfont_catchQ,kanfont_catchZ,kanfont_catchX,kanfont_catchY
    kanfont_mouseX,kanfont_mouseY=min(max(LTsv_global_canvasmotionX(),0),PSchar_ZW//2),min(max(LTsv_global_canvasmotionY(),0),PSchar_ZW//2)
    kanfont_gridX,kanfont_gridY=kanfont_mouseX,kanfont_mouseY
    if kanfont_gridinner:
        kanfont_gridX=(kanfont_gridX//kanfont_fontgrid)*kanfont_fontgrid if kanfont_gridX//(kanfont_fontgrid//2)%2 == 0 else (kanfont_gridX//kanfont_fontgrid+1)*kanfont_fontgrid-1
        kanfont_gridY=(kanfont_gridY//kanfont_fontgrid)*kanfont_fontgrid if kanfont_gridY//(kanfont_fontgrid//2)%2 == 0 else (kanfont_gridY//kanfont_fontgrid+1)*kanfont_fontgrid-1
    else:
        kanfont_gridX,kanfont_gridY=(kanfont_gridX+(kanfont_fontgrid//2))//kanfont_fontgrid*kanfont_fontgrid,(kanfont_gridY+(kanfont_fontgrid//2))//kanfont_fontgrid*kanfont_fontgrid
    glyphentrychar=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    kanfont_gridP,kanfont_gridQ=LTsv_draw_glyphmouse(draw_t=glyphentrychar,draw_x=0,draw_y=0,path_z=LTsv_widget_getnumber(kanfont_path_scale),grid_x=kanfont_gridX,grid_y=kanfont_gridY,mouse_x=kanfont_mouseX,mouse_y=kanfont_mouseY,draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic])

kanfont_gridview=False
def kanfont_glyph_draw():
    glyphentrychar=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    LTsv_draw_selcanvas(kanfont_glyph_canvas)
    LTsv_draw_delete()
    if kanfont_gridview:
        LTsv_draw_picture(kanfont_gridimage,0,0)
        if kanfont_refergrid:
            LTsv_draw_color(kanfont_referposC); LTsv_draw_font(draw_f=kanfont_font_grid); LTsv_draw_text(draw_t=glyphentrychar,draw_x=kanfont_referposX,draw_y=kanfont_referposY);
        LTsv_draw_color(kanfont_glyphcolorG); LTsv_draw_glyphsfill(draw_t="X{0:3}Y{1:3}".format(kanfont_gridX,kanfont_gridY),draw_x=kanfont_gridX,draw_y=kanfont_gridY,draw_f=10,draw_g="漫")
        LTsv_draw_glyphclock(draw_t=glyphentrychar,draw_x=0,draw_y=0,draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic],color_R=kanfont_glyphcolorR,color_L=kanfont_glyphcolorL,color_X=kanfont_glyphcolorX)
    else:
        LTsv_draw_glyphclockfill(draw_t=glyphentrychar,draw_x=0,draw_y=0,draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic],color_R=kanfont_glyphcolorR,color_L=kanfont_glyphcolorL,color_X=kanfont_glyphcolorX)
        LTsv_draw_glypwide(draw_t=glyphentrychar,draw_x=0,draw_y=0,draw_s=0,draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic],color_W=kanfont_glyphcolorG)
    LTsv_draw_glyphcursor(draw_t=glyphentrychar,draw_x=0,draw_y=0,path_z=LTsv_widget_getnumber(kanfont_path_scale),draw_s=kanfont_lineseg,grid_p=kanfont_gridP,grid_q=kanfont_gridQ,draw_f=LTsv_PSchar_ZW//2,draw_g=LTsv_global_glyphtype()[kanfont_gothic],color_R=kanfont_glyphcolorR,color_L=kanfont_glyphcolorL,color_X=kanfont_glyphcolorX)
    LTsv_draw_queue()

def kanfont_glyph_mousepress(window_objvoid=None,window_objptr=None):
    global kanfont_gridX,kanfont_gridY,kanfont_gridP,kanfont_gridQ,kanfont_catchP,kanfont_catchQ,kanfont_catchZ,kanfont_catchX,kanfont_catchY
    kanfont_glyph_grid()
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    kanfont_catchX,kanfont_catchY=-1,-1
    if kanfont_catchZ >= len(glyphnote):
        glyphnote.append([kanfont_gridX*2,kanfont_gridY*2])
        LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
        kanfont_pathadjustment(kanfont_catchZ)
        kanfont_catchP=0
    else:
        if kanfont_gridP >= 0:
            kanfont_catchP=kanfont_gridP
            kanfont_catchX,kanfont_catchY=kanfont_gridX,kanfont_gridY
        else:
            if kanfont_gridQ >= 0:
                if kanfont_lineseg:
                    kanfont_catchQ=(kanfont_gridQ+1+len(glyphnote[kanfont_catchZ])//2)%(len(glyphnote[kanfont_catchZ])//2)
                    glyphnote[kanfont_catchZ].insert(kanfont_catchQ*2,kanfont_gridY*2); glyphnote[kanfont_catchZ].insert(kanfont_catchQ*2,kanfont_gridX*2)
                    kanfont_catchP=kanfont_catchQ
            else:
                kanfont_catchP=len(glyphnote[kanfont_catchZ])//2
                glyphnote[kanfont_catchZ]+=[kanfont_gridX*2]; glyphnote[kanfont_catchZ]+=[kanfont_gridY*2]
                LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_glyph_draw()

def kanfont_glyph_mousemotion(window_objvoid=None,window_objptr=None):
    global kanfont_gridX,kanfont_gridY,kanfont_gridP,kanfont_gridQ,kanfont_catchP,kanfont_catchQ,kanfont_catchZ,kanfont_catchX,kanfont_catchY
    kanfont_glyph_grid()
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    if kanfont_catchP >= 0:
        glyphnote[kanfont_catchZ][kanfont_catchP*2],glyphnote[kanfont_catchZ][kanfont_catchP*2+1]=kanfont_gridX*2,kanfont_gridY*2
        LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    if kanfont_catchX != kanfont_gridX or kanfont_catchY != kanfont_gridY:
        kanfont_catchX,kanfont_catchY=-1,-1
    kanfont_glyph_draw()

def kanfont_glyph_mouserelease(window_objvoid=None,window_objptr=None):
    global kanfont_gridX,kanfont_gridY,kanfont_gridP,kanfont_gridQ,kanfont_catchP,kanfont_catchQ,kanfont_catchZ,kanfont_catchX,kanfont_catchY
    kanfont_glyph_grid()
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_catchZ=LTsv_widget_getnumber(kanfont_path_scale)
    if kanfont_catchP >= 0:
        if kanfont_catchX == kanfont_gridX and kanfont_catchY == kanfont_gridY:
            if len(glyphnote[kanfont_catchZ]) > 2:
                glyphnote[kanfont_catchZ].pop(kanfont_catchP*2); glyphnote[kanfont_catchZ].pop(kanfont_catchP*2)
                LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
            else:
                del glyphnote[kanfont_catchZ]
                LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
                kanfont_pathadjustment(kanfont_catchZ)
    kanfont_catchP,kanfont_catchQ,kanfont_catchZ=-1,-1,-1
    kanfont_glyph_draw()

def kanfont_glyph_mouseenter(window_objvoid=None,window_objptr=None):
    global kanfont_gridview
    global kanfont_gridX,kanfont_gridY,kanfont_gridP,kanfont_gridQ,kanfont_catchP,kanfont_catchQ,kanfont_catchZ,kanfont_catchX,kanfont_catchY
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_pointsrotation(LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_gridview=True
    kanfont_catchP,kanfont_catchQ,kanfont_catchZ=-1,-1,-1
    kanfont_glyph_draw()

def kanfont_glyph_mouseleave(window_objvoid=None,window_objptr=None):
    global kanfont_gridview
    glyphcode=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale))
    glyphnote=LTsv_glyph_pointsrotation(LTsv_glyph_getnote(glyphcode,draw_g=LTsv_global_glyphtype()[kanfont_gothic]))
    LTsv_glyph_points2path(draw_t=glyphcode,glyphnote=glyphnote,draw_g=LTsv_global_glyphtype()[kanfont_gothic])
    kanfont_gridview=False
    kanfont_code(LTsv_widget_getnumber(kanfont_path_scale))


def kanfont_kbd_mouseenter(window_objvoid=None,window_objptr=None):
    pass
#    LTsv_glyph_kbdfind(LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale)))

def kanfont_kbd_mousepress(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mousepress(kanfont_kbd_canvas,0,2)

def kanfont_kbd_mousemotion(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mousemotion(kanfont_kbd_canvas,0,2)

def kanfont_kbd_mouserelease(window_objvoid=None,window_objptr=None):
    LTsv_glyph_mouserelease(kanfont_kbd_canvas,0,2)

def kanfont_keypress(window_objvoid=None,window_objptr=None):
    canvasmotionZ=LTsv_global_canvasmotionZ()
    if canvasmotionZ in kanfont_dictype_canvas:
        canvasmotionZkbd=kanfont_dictype_canvas.index(canvasmotionZ)
        LTsv_glyph_typepress(kanfont_dictype_canvas[canvasmotionZkbd],kanfont_dictype_canvasW[canvasmotionZkbd]-LTsv_global_glyphkbdW(),kanfont_entry_H-LTsv_global_glyphkbdH())
    elif canvasmotionZ == kanfont_kbd_canvas:
        LTsv_glyph_typepress(kanfont_kbd_canvas,0,2)
    pass

def kanfont_keyrelease(window_objvoid=None,window_objptr=None):
    canvasmotionZ=LTsv_global_canvasmotionZ()
    if canvasmotionZ in kanfont_dictype_canvas:
        canvasmotionZkbd=kanfont_dictype_canvas.index(canvasmotionZ)
        LTsv_glyph_typerelease(kanfont_dictype_canvas[canvasmotionZkbd],kanfont_dictype_canvasW[canvasmotionZkbd]-LTsv_global_glyphkbdW(),kanfont_entry_H-LTsv_global_glyphkbdH())
    elif canvasmotionZ == kanfont_kbd_canvas:
        LTsv_glyph_typerelease(kanfont_kbd_canvas,0,2)
    pass

def kanfont_dictype_paste():
    clippaste=LTsv_widget_gettext(kanfont_clipboard)
    return clippaste.replace('\n',"").replace('\t',"")

def kanfont_dictype_copy(clippaste):
    LTsv_widget_settext(kanfont_clipboard,clippaste)

def kanfont_dictype_inputed_shell(dictype_cnt):
    def kanfont_dictype_kernel(LTsv_kbdentry_input):
        LTsv_kbdentry_edit=LTsv_kbdentry_input
        if LTsv_global_dictype()[dictype_cnt] == "幅":
            LTsv_kbdentry_wide=LTsv_intstr0x(LTsv_kbdentry_edit)
            LTsv_kbdentry_edit=str(LTsv_kbdentry_wide) if 0 < LTsv_kbdentry_wide < PSfont_ZW  else ""
        LTsv_glyph_text2path(draw_t=LTsv_chrcode(LTsv_widget_getnumber(kanfont_code_scale)),kanpath=LTsv_kbdentry_edit,draw_g=LTsv_global_dictype()[dictype_cnt])
        if LTsv_global_dictype()[dictype_cnt] in "{0}幅".format(LTsv_global_glyphtype()):
            kanfont_code()
        return LTsv_kbdentry_edit
    return kanfont_dictype_kernel

def kanfont_svgsave_shell(window_objvoid=None,window_objptr=None):
    LTsv_widget_disableenable(kanfont_svg_button,False)
    LTsv_widget_settext(kanfont_svg_button,"make:{0}".format(kanfont_svgname))
    LTsv_window_after(kanfont_window,event_b=kanfont_svgmake,event_i="kanfont_svgmake",event_w=10)

kanfont_glyphtypeswap={"活":"活漫筆","漫":"漫活筆","筆":"筆活漫"}
def kanfont_svgmake(window_objvoid=None,window_objptr=None):
    global kanfont_dicname,kanfont_svgname,kanfont_fontwidths,kanfont_autosave,kanfont_savetime
    global kanfont_fontname,kanfont_glyphtype
    kanchar=LTsv_global_kandic().rstrip('\n').split('\n')
    glyphtype=kanfont_glyphtype if kanfont_glyphtype in LTsv_global_glyphtype() else LTsv_global_glyphtype()[kanfont_gothic]
    if not glyphtype in kanfont_glyphtypeswap: glyphtype="活"
    kanfont_svgtext=(
      '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<svg\n'
      '  xmlns="http://www.w3.org/2000/svg" version="1.1"\n'
      '  xmlns:dc="http://purl.org/dc/elements/1.1/"\n'
      '  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n'
      '  xmlns:svg="http://www.w3.org/2000/svg">\n'
      '    <defs>\n'
    )
    for fontwidths in kanfont_fontwidths.split(','):
        kanfont_svgtext+=(
          '        <font id="{0}" horiz-adv-x="{2}">\n'
          '            <font-face font-family="{1}" units-per-em="{2}"/>\n'
          ''.format(kanfont_fontname[glyphtype] if fontwidths == str(PSfont_ZW) else "{0}_w{1}".format(kanfont_fontname[glyphtype],fontwidths),kanfont_fontname[glyphtype],fontwidths)
        )
        for kanline in kanchar:
            for typeswap in kanfont_glyphtypeswap[glyphtype]:
                kanpath=LTsv_pickdatalabel(kanline,typeswap); kanpath=kanpath if not "[" in kanpath else LTsv_glyphSVG5x(kanpath)
                if len(kanpath): break;
            if len(kanpath):
                kanwide=LTsv_pickdatalabel(kanline,"幅"); kanwide=kanwide if len(kanwide) else "1024"
                if kanwide == fontwidths:
                    kanglyphname=kanline[0:kanline.find('\t')]; kanglyphname=kanglyphname if not kanglyphname in '&"<>' else LTsv_utf2xml(kanglyphname)
                    kanfont_svgtext+=(
                      '            <glyph glyph-name="{0}" unicode="{0}" d="{1}" />\n'.format(kanglyphname,kanpath)
                    )
        kanfont_svgtext+=(
          '        </font>\n'
        )
    kanfont_svgtext+=(
      '    </defs>\n'
      '</svg>\n'
    )
    LTsv_saveplain(kanfont_dicname,LTsv_global_kandic())
    LTsv_saveplain(kanfont_svgname,kanfont_svgtext)
    LTsv_widget_settext(kanfont_svg_button,LTsv_getdaytimestr("savetime({0})".format("@0h:@0n:@0s")))
    LTsv_widget_disableenable(kanfont_svg_button,True)

def kanfont_configload():
    global kanfont_ltsv,kanfont_config
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    global kanfont_refer,kanfont_refergrid
    global kanfont_referposX,kanfont_referposY,kanfont_referposS,kanfont_referposC
    global kanfont_glyphcolorR,kanfont_glyphcolorL,kanfont_glyphcolorX,kanfont_glyphcolorG
    global kanfont_dicname,kanfont_svgname,kanfont_fontwidths,kanfont_autosave,kanfont_savetime
    global kanfont_fontname,kanfont_glyphtype
    kanfont_ltsv=LTsv_loadfile("kanfont.tsv")
    kanfont_config=LTsv_getpage(kanfont_ltsv,"kanfont")
    kanfont_seek=LTsv_readlinerest(kanfont_config,"seek",kanfont_seek); kanfont_seek=kanfont_seek[:1] if len(kanfont_seek) else "ぱ"
    kanfont_fontgrid=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"grid",str(kanfont_fontgrid))),10),100)
    kanfont_gridinner=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"inner",str(kanfont_gridinner))),0),1)
    kanfont_lineseg=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"lineseg",str(kanfont_lineseg))),0),1)
    kanfont_gothic=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"gothic",str(kanfont_gothic))),0),1)
    kanfont_gridimage=LTsv_readlinerest(kanfont_config,"gridimage",kanfont_gridimage)
    kanfont_refer=LTsv_readlinerest(kanfont_config,"refer",kanfont_refer)
    kanfont_refergrid=min(max(LTsv_intstr0x(LTsv_readlinerest(kanfont_config,"refergrid",str(kanfont_refergrid))),0),1)
    if LTsv_global_GUI() == LTsv_global_GTK2():
        kanfont_referposX_t,kanfont_referposY_t,kanfont_referposS_t,kanfont_referposC=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanfont_config,"referGTK"),"X","Y","S","C"));
    if LTsv_global_GUI() == LTsv_global_Tkinter():
        kanfont_referposX_t,kanfont_referposY_t,kanfont_referposS_t,kanfont_referposC=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanfont_config,"referTkinter"),"X","Y","S","C"));
    kanfont_referposX,kanfont_referposY,kanfont_referposS=LTsv_intstr0x(kanfont_referposX_t),LTsv_intstr0x(kanfont_referposY_t),LTsv_intstr0x(kanfont_referposS_t)
    kanfont_glyphcolorR,kanfont_glyphcolorL,kanfont_glyphcolorX,kanfont_glyphcolorG=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanfont_config,"glyphcolor"),"R","L","X","G"))
    kanfont_dicname=LTsv_readlinerest(kanfont_config,"dic_name",kanfont_dicname)
    kanfont_svgname=LTsv_readlinerest(kanfont_config,"svg_name",kanfont_svgname)
    kanfont_fontname["活"],kanfont_fontname["漫"],kanfont_fontname["筆"]=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(kanfont_config,"font_name"),"活","漫","筆"))
    kanfont_glyphtype=LTsv_readlinerest(kanfont_config,"font_glyphtype",kanfont_glyphtype)
    kanfont_fontwidths=LTsv_readlinerest(kanfont_config,"font_widths",kanfont_fontwidths)
    kanfont_autosave=LTsv_readlinerest(kanfont_config,"autosave",kanfont_autosave)
    kanfont_savetime=LTsv_readlinerest(kanfont_config,"savetime",kanfont_savetime)

def kanfont_configsave_exit(window_objvoid=None,window_objptr=None):
    global kanfont_ltsv,kanfont_config
    global kanfont_seek,kanfont_fontgrid,kanfont_gridinner,kanfont_lineseg,kanfont_gothic,kanfont_gridimage
    global kanfont_refer,kanfont_refergrid
    kanfont_ltsv=LTsv_loadfile("kanfont.tsv")
    kanfont_config=LTsv_pushlinerest(kanfont_config,"seek",kanfont_seek)
    kanfont_config=LTsv_pushlinerest(kanfont_config,"grid",str(kanfont_fontgrid))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"inner",str(kanfont_gridinner))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"lineseg",str(kanfont_lineseg))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"gothic",str(kanfont_gothic))
    kanfont_config=LTsv_pushlinerest(kanfont_config,"refergrid",str(kanfont_refergrid))
    kanfont_ltsv=LTsv_putpage(kanfont_ltsv,"kanfont",kanfont_config)
    LTsv_savefile("kanfont.tsv",kanfont_ltsv)
    LTsv_glyph_picklesave()
    if kanfont_autosave in ["1","TRUE","True","true","YES","Yes","yes","ON","On","on"]:
        kanfont_svgmake()
    LTsv_window_exit()

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_tsvpath="LTsv/LTsv_kbd.tsv",LTsv_initmouse=True)
    LTsv_glyph_kbdinit(LTsv_tsvpath="LTsv/LTsv_glyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
    kanfont_configload()
    kanfont_fontsize_entry=LTsv_global_glyphkbdH()//2-2;    kanfont_font_entry="{0},{1}".format(kanfont_fontname["漫"],kanfont_fontsize_entry); kanfont_label_WH=kanfont_fontsize_entry*2
    kanfont_fontsize_refer=LTsv_global_glyphkbdH()//2-2;    kanfont_font_refer="{0},{1}".format(kanfont_refer,kanfont_fontsize_refer)
    kanfont_fontsize_grid=kanfont_referposS;    kanfont_font_grid="{0},{1}".format(kanfont_refer,kanfont_fontsize_grid)
    kanfont_entry_H=LTsv_global_glyphkbdH()+2
    kanfont_canvas_WH=PSfont_ZW//2; kanfont_scale_W=LTsv_global_glyphkbdW(); kanfont_entry_W=1024-kanfont_scale_W-kanfont_canvas_WH-kanfont_label_WH; 
    kanfont_canvas_X=kanfont_scale_W; kanfont_label_X=kanfont_canvas_X+kanfont_canvas_WH; kanfont_entry_X=kanfont_label_X+kanfont_label_WH; kanfont_W=kanfont_entry_X+kanfont_entry_W
    kanfont_H=kanfont_canvas_WH+kanfont_label_WH*3; kanfont_scale_X,kanfont_scale_Y=0,kanfont_entry_H; kanfont_scale_H=kanfont_H-kanfont_scale_Y-kanfont_label_WH*3
    kanfont_window=LTsv_window_new(widget_t="kanfont",event_b=kanfont_configsave_exit,widget_w=kanfont_W,widget_h=kanfont_H,event_k=kanfont_keypress,event_y=kanfont_keyrelease)
    kanfont_kbd_canvas=LTsv_canvas_new(kanfont_window,widget_x=0,widget_y=0,widget_w=LTsv_global_glyphkbdW(),widget_h=kanfont_entry_H,
     event_p=kanfont_kbd_mousepress,event_m=kanfont_kbd_mousemotion,event_r=kanfont_kbd_mouserelease,event_e=kanfont_kbd_mouseenter,event_l=None,event_w=50)
    LTsv_glyph_tapcallback_shell(kanfont_kbd_canvas,kanfont_codekbd)
    kanfont_code_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_scale_X,widget_y=kanfont_scale_Y,widget_w=kanfont_scale_W,widget_h=kanfont_scale_H,widget_s=1,widget_e=kanfont_max,widget_a=1,event_b=kanfont_codescale_shell)
    kanfont_code_spin=LTsv_spin_new(kanfont_window,widget_x=kanfont_scale_X,widget_y=kanfont_scale_Y+kanfont_scale_H,widget_w=kanfont_scale_W,widget_h=kanfont_label_WH,widget_s=1,widget_e=kanfont_max,widget_a=1,widget_f=kanfont_font_entry,event_b=kanfont_codespin_shell)
    kanfont_code_label=LTsv_label_new(kanfont_window,widget_t="U+f080",widget_x=kanfont_scale_X,widget_y=kanfont_scale_Y+kanfont_scale_H+kanfont_label_WH*1,widget_w=kanfont_scale_W,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_copy_button=LTsv_button_new(kanfont_window,widget_t="cp",widget_x=kanfont_scale_X+kanfont_scale_W*0//2,widget_y=kanfont_scale_Y+kanfont_scale_H+kanfont_label_WH*2,widget_w=kanfont_scale_W//2,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_codekbd_copy)
    kanfont_paste_button=LTsv_button_new(kanfont_window,widget_t="‎pt",widget_x=kanfont_scale_X+kanfont_scale_W*1//2,widget_y=kanfont_scale_Y+kanfont_scale_H+kanfont_label_WH*2,widget_w=kanfont_scale_W//2,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_codekbd_paste)
    kanfont_glyph_canvas=LTsv_canvas_new(kanfont_window,widget_x=kanfont_canvas_X,widget_y=0,widget_w=kanfont_canvas_WH,widget_h=kanfont_canvas_WH,
     event_p=kanfont_glyph_mousepress,event_m=kanfont_glyph_mousemotion,event_r=kanfont_glyph_mouserelease,event_e=kanfont_glyph_mouseenter,event_l=kanfont_glyph_mouseleave,event_w=50)
    kanfont_gridimageOBJ=LTsv_draw_picture_load(kanfont_gridimage)
    kanfont_path_scale=LTsv_scale_new(kanfont_window,widget_x=kanfont_canvas_X,widget_y=kanfont_canvas_WH,widget_w=kanfont_canvas_WH*5//8,widget_h=kanfont_label_WH*2,widget_s=0,widget_e=9,widget_a=1,event_b=kanfont_pathsel_shell)
    kanfont_layerX_button=LTsv_button_new(kanfont_window,widget_t="cut",widget_x=kanfont_canvas_X+kanfont_canvas_WH*1//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*2,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_layerX_shell)
    kanfont_layerC_button=LTsv_button_new(kanfont_window,widget_t="copy",widget_x=kanfont_canvas_X+kanfont_canvas_WH*0//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*2,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_layerC_shell)
    kanfont_layerV_button=LTsv_button_new(kanfont_window,widget_t="paste",widget_x=kanfont_canvas_X+kanfont_canvas_WH*2//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*2,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_layerV_shell)
    kanfont_layerU_button=LTsv_button_new(kanfont_window,widget_t="up",widget_x=kanfont_canvas_X+kanfont_canvas_WH*3//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*2,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_layerU_shell)
    kanfont_layerD_button=LTsv_button_new(kanfont_window,widget_t="down",widget_x=kanfont_canvas_X+kanfont_canvas_WH*4//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*2,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_layerD_shell)
    kanfont_grid_label=LTsv_label_new(kanfont_window,widget_t="grid",widget_x=kanfont_canvas_X+kanfont_canvas_WH*5//8,widget_y=kanfont_canvas_WH,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry)
    kanfont_grid_spin=LTsv_spin_new(kanfont_window,widget_x=kanfont_canvas_X+kanfont_canvas_WH*5//8,widget_y=kanfont_canvas_WH+kanfont_label_WH,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_s=5,widget_e=PSchar_ZW//5,widget_a=1,widget_f=kanfont_font_entry,event_b=kanfont_grid_shell)
    kanfont_inner_check=LTsv_check_new(kanfont_window,widget_t="24",widget_x=kanfont_canvas_X+kanfont_canvas_WH*5//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*2,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_inner_shell)
    kanfont_seg_check=LTsv_check_new(kanfont_window,widget_t="seg",widget_x=kanfont_canvas_X+kanfont_canvas_WH*6//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*0,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_lineseg_shell)
    kanfont_refer_check=LTsv_check_new(kanfont_window,widget_t="ref",widget_x=kanfont_canvas_X+kanfont_canvas_WH*6//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*1,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_refer_shell)
    kanfont_gothic_radio=[None]*len(LTsv_global_glyphtype())
    for glyphtype_cnt,glyphtype_split in enumerate(LTsv_global_glyphtype()):
        kanfont_gothic_radio[glyphtype_cnt]=LTsv_radio_new(kanfont_window,widget_t=glyphtype_split,widget_x=kanfont_canvas_X+kanfont_canvas_WH*7//8,widget_y=kanfont_canvas_WH+kanfont_label_WH*glyphtype_cnt,widget_w=kanfont_canvas_WH*1//8,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=debug_gothic_shell(glyphtype_cnt))
    kanfont_dictype_canvas=[None]*len(LTsv_global_dictype())
    kanfont_dictype_canvasW=[None]*len(LTsv_global_dictype())
    for dictype_cnt,dictype_split in enumerate(LTsv_global_dictype()):
        kanfont_dictype_label[dictype_cnt]=LTsv_label_new(kanfont_window,widget_t=dictype_split,widget_x=kanfont_label_X,widget_y=dictype_cnt*kanfont_entry_H,widget_w=kanfont_label_WH,widget_h=kanfont_entry_H,widget_f=kanfont_font_entry)
        kanfont_dictype_canvasW[dictype_cnt]=kanfont_entry_W if dictype_split != "幅" else kanfont_entry_W*2//5
        kanfont_dictype_canvas[dictype_cnt]=LTsv_kbdentry_new(kanfont_window,event_b=kanfont_dictype_inputed_shell(dictype_cnt),clip_c=kanfont_dictype_copy,clip_v=kanfont_dictype_paste,clip_e=kanfont_dictype_inputed_shell(dictype_cnt),widget_x=kanfont_entry_X,widget_y=dictype_cnt*kanfont_entry_H,widget_w=kanfont_dictype_canvasW[dictype_cnt],widget_h=kanfont_entry_H,event_w=50)
    kanfont_clipboard=LTsv_clipboard_new(kanfont_window)
    kanfont_svg_button=LTsv_button_new(kanfont_window,widget_t="save:{0}({1})".format(kanfont_svgname,kanfont_fontname[LTsv_global_glyphtype()[kanfont_gothic]]),widget_x=kanfont_entry_X+kanfont_entry_W*2//5,widget_y=kanfont_H-kanfont_label_WH,widget_w=kanfont_entry_W*3//5,widget_h=kanfont_label_WH,widget_f=kanfont_font_entry,event_b=kanfont_svgsave_shell)
    LTsv_widget_showhide(kanfont_window,True)
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    kanfont_codekbd(kanfont_seek)
    LTsv_widget_setnumber(kanfont_grid_spin,kanfont_fontgrid); kanfont_grid_shell()
    LTsv_widget_setnumber(kanfont_inner_check,kanfont_gridinner)
    LTsv_widget_setnumber(kanfont_seg_check,kanfont_lineseg)
    LTsv_widget_setnumber(kanfont_gothic_radio[0],kanfont_gothic)
    LTsv_widget_setnumber(kanfont_refer_check,kanfont_refergrid)
    LTsv_glyph_kbddelete(kanfont_kbd_canvas); LTsv_glyph_kbddraw(kanfont_kbd_canvas,0,2); LTsv_draw_queue()
    LTsv_window_main(kanfont_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
print("")


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE

