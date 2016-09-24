#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
import subprocess
import codecs
import ctypes
import struct
import uuid
import datetime
import math
from LTsv_file    import *
from LTsv_printf import *
LTsv_Tkinter=True
try:
    import tkinter as Tk
    import tkinter.scrolledtext as Tk_sc
    import tkinter.filedialog as Tk_fd
#    import messagebox as Tk_mb
except:
    LTsv_Tkinter=False
#if LTsv_Tkinter == False:
#    #http://shinobar.server-on.net/puppy/opt/tcl_tk-8.5.7-1-p4.sfs
#    if os.path.exists("/usr/lib/python3.4"):
#        sys.path.append("/usr/lib/python3.4")
#        try:
#            import tkinter as Tk
#            import tkinter.scrolledtext as Tk_sc
#            import tkinter.filedialog as Tk_fd
##            import messagebox as Tk_mb
#            LTsv_Tkinter=True
#        except:
#            LTsv_Tkinter=False
LTsv_libgtk,LTsv_libgdk,LTsv_libobj=None,None,None
LTsv_user32,LTsv_shell32,LTsv_kernel32,LTsv_gdi32=None,None,None,None
LTsv_GUI_ERROR,LTsv_GUI_GTK2,LTsv_GUI_Tkinter,LTsv_GUI_WinAPI="","GTK2","Tkinter","WinAPI"
LTsv_GUI,LTsv_Notify=LTsv_GUI_ERROR,LTsv_GUI_ERROR
#LTsv_CALLBACLTYPE=ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.POINTER(ctypes.c_ulong))
#LTsv_CALLBACLTYPE=ctypes.CFUNCTYPE(ctypes.c_bool,ctypes.c_void_p)
#LTsv_CALLBACLTYPE=ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int)
LTsv_CALLBACLTYPE=ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_void_p)
LTsv_widgetLTSV=LTsv_newfile("LTsv_gui",LTsv_default=None)
LTsv_widgetOBJ={}; LTsv_widgetOBJcount=0
LTsv_timerOBJ={}; LTsv_timer_cbk={}
LTsv_canvas_motion_X,LTsv_canvas_motion_Y,LTsv_canvas_motion_Z=0,0,""
canvas_EMLenter,canvas_EMLmotion,canvas_EMLleave={},{},{}
canvas_CBKenter,canvas_CBKmotion,canvas_CBKleave,canvas_CBKtimeout,canvas_CBKafter,LTsv_canvasCBKpagename={},{},{},{},{},{}
LTsv_pictureOBJ,LTsv_pictureW,LTsv_pictureH={},{},{}
LTsv_iconOBJ={}; LTsv_iconOBJnotify=[]
LTsv_popupmenuOBJ={}
LTsv_default_iconuri=""

def LTsv_guiCDLLver(LTsv_libname,LTsv_libvermin,LTsv_libvermax):
    LTsv_min,LTsv_max=(LTsv_libvermin,LTsv_libvermax) if LTsv_libvermin <= LTsv_libvermax else (LTsv_libvermax,LTsv_libvermin)
    if LTsv_min == LTsv_max:
        LTsv_max+=1
    LTsv_CDLL=None
    for LTsv_libver in range(LTsv_min,LTsv_max):
        LTsv_CDLL=ctypes.CDLL(LTsv_libname.replace('?',str(LTsv_libver)))
        if LTsv_CDLL != None:
            break
    return LTsv_CDLL

def LTsv_guiinit(LTsv_guistyle=LTsv_GUI_GTK2,LTsv_libvermin=0,LTsv_libvermax=0):
    global LTsv_GUI,LTsv_Notify,LTsv_default_iconuri
    global LTsv_libgtk,LTsv_libgdk,LTsv_libobj,LTsv_user32,LTsv_shell32,LTsv_kernel32,LTsv_gdi32
    LTsv_GUI=LTsv_guistyle
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_Notify=LTsv_GUI_GTK2; LTsv_default_iconuri="/usr/share/pixmaps/python.xpm"
        if sys.platform.startswith("linux"): #"/usr/lib/libgtk-x11-2.0.so.0"
            LTsv_libgtk=LTsv_guiCDLLver("libgtk-x11-2.0.so.?",LTsv_libvermin,LTsv_libvermax)
            LTsv_libgtk.gtk_range_get_value.restype=ctypes.c_double
            LTsv_libgdk=LTsv_guiCDLLver("libgdk-x11-2.0.so.?",LTsv_libvermin,LTsv_libvermax)
            LTsv_libobj=LTsv_guiCDLLver("libgobject-2.0.so.?",LTsv_libvermin,LTsv_libvermax)
            LTsv_libobj.g_timeout_add.restype=ctypes.c_uint
#        if sys.platform.startswith("cygwin"):
#            LTsv_libgtk=LTsv_guiCDLLver("cyggtk-x11-2.0-?.dll",0,10)
#            LTsv_libgdk=LTsv_guiCDLLver("cyggdk-x11-2.0-?.dll",0,10)
#            LTsv_libobj=LTsv_guiCDLLver("cyggobject-2.0-?.dll",0,10)
#        if sys.platform.startswith("darwin"):
#            LTsv_libgtk=ctypes.CDLL("/opt/local/lib/libgtk-x11-2.0.0.dylib")#"/Library/Frameworks/Gtk.framework/Libraries/libgtk-quartz-2.0.0.dylib"
#            LTsv_libgdk=ctypes.CDLL("/opt/local/lib/libgdk-x11-2.0.0.dylib")#"/Library/Frameworks/Gtk.framework/Libraries/libgdk-quartz-2.0.0.dylib"
#            LTsv_libobj=ctypes.CDLL("/opt/local/lib/libgobject-2.0.0.dylib")#"/Library/Frameworks/Glib.framework/Libraries/libgobject-2.0.0.dylib"
        if LTsv_libgtk == None or LTsv_libgdk == None or LTsv_libobj == None:
#            if sys.platform.startswith("win"):
#                LTsv_GUI=LTsv_GUI_WinAPI
            LTsv_GUI=LTsv_GUI_Tkinter
        else:
            LTsv_libgtk.gtk_init(0,0)
    if LTsv_GUI == LTsv_GUI_WinAPI or LTsv_GUI == LTsv_GUI_Tkinter:
        if sys.platform.startswith("win"):
            LTsv_Notify=LTsv_GUI_WinAPI; LTsv_default_iconuri=sys.executable
            LTsv_shell32=ctypes.windll.shell32
            LTsv_user32=ctypes.windll.user32
            LTsv_kernel32=ctypes.windll.kernel32
            LTsv_gdi32=ctypes.windll.gdi32
        elif sys.platform.startswith("linux"):
            pass
        else:
            LTsv_GUI,LTsv_Notify=LTsv_GUI_ERROR,LTsv_GUI_ERROR; LTsv_default_iconuri=""
    if not LTsv_GUI in [LTsv_GUI_ERROR,LTsv_GUI_GTK2,LTsv_GUI_Tkinter,LTsv_GUI_WinAPI]: LTsv_GUI=LTsv_GUI_ERROR
    return LTsv_GUI

def LTsv_global_GUI():                              return LTsv_GUI
def LTsv_global_Notify():                           return LTsv_Notify
def LTsv_global_GTK2():                             return LTsv_GUI_GTK2
def LTsv_global_Tkinter():                           return LTsv_GUI_Tkinter
def LTsv_global_WinAPI():                           return LTsv_GUI_WinAPI
def LTsv_global_libgtk():                           return LTsv_libgtk
def LTsv_global_libgdk():                           return LTsv_libgdk
def LTsv_global_libobj():                           return LTsv_libobj
def LTsv_global_canvasmotionX():                    return LTsv_canvas_motion_X
def LTsv_global_canvasmotionY():                    return LTsv_canvas_motion_Y
def LTsv_global_canvasmotionZ():                    return LTsv_canvas_motion_Z
def LTsv_global_canvascolor():                    return LTsv_canvascolor
def LTsv_global_canvasbgcolor():                    return LTsv_canvasbgcolor
#def LTsv_global_widgetgetltsv():                    return LTsv_widgetLTSV
def LTsv_global_widgetltsv(new_LTSV=None):
    global LTsv_widgetLTSV
    LTsv_widgetLTSV=LTsv_widgetLTSV if new_LTSV == None else new_LTSV
    return LTsv_widgetLTSV
def LTsv_global_widgetgetpage(LTsv_widgetPAGENAME): return LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
def LTsv_global_widgetOBJ(LTsv_objid):              return LTsv_widgetOBJ[LTsv_objid]
def LTsv_global_pictureOBJ(LTsv_objid):             return LTsv_pictureOBJ[LTsv_objid]
def LTsv_global_pictureW(LTsv_objid):               return LTsv_pictureW[LTsv_objid]
def LTsv_global_pictureH(LTsv_objid):               return LTsv_pictureH[LTsv_objid]
def LTsv_global_iconOBJ(LTsv_objid):                return LTsv_iconOBJ[LTsv_objid]
def LTsv_global_popupmenuOBJ(LTsv_objid):           return LTsv_popupmenuOBJ[LTsv_objid]

def LTsv_widget_newUUID(LTsv_widgetID=None):
    global LTsv_widget_oldID
    if LTsv_widgetID == False:
        LTsv_uuid=LTsv_widget_oldID
    else:
        LTsv_uuid=uuid.uuid4().hex+'+'+str(time.time())
        LTsv_widget_oldID=LTsv_uuid
    return LTsv_uuid
LTsv_widget_oldID=LTsv_widget_newUUID()

def LTsv_widget_newobj(LTsv_widgetPAGE,LTsv_widgetoption,widget_obj):
    global LTsv_widgetOBJ,LTsv_widgetOBJcount
    LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,LTsv_widgetoption,str(LTsv_widgetOBJcount))
    LTsv_widgetOBJ[str(LTsv_widgetOBJcount)]=widget_obj; LTsv_widgetOBJcount+=1
    return LTsv_widgetPAGE

def LTsv_widget_getobj(LTsv_widgetPAGE,LTsv_widgetoption):
    LTsv_widgetOBJcount=LTsv_readlinerest(LTsv_widgetPAGE,LTsv_widgetoption)
    if LTsv_widgetOBJcount in LTsv_widgetOBJ:
        return LTsv_widgetOBJ[LTsv_widgetOBJcount]
    else:
        return None

def LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=None,widget_k=None,widget_t=None,widget_u=None,widget_s=None,widget_e=None,widget_a=None,widget_v=None,widget_b=None, \
  widget_p=None,widget_m=None,widget_g=None,widget_f=None,widget_x=None,widget_y=None,widget_w=None,widget_h=None,widget_c=None, \
  event_z=None,event_k=None,event_y=None,event_b=None,event_p=None,event_r=None,event_e=None,event_m=None,event_l=None,event_a=None,event_u=None, \
  menu_o=None,menu_b=None,menu_c=None,dialog_t=None,dialog_c=None, \
  kbd_p=None,kbd_r=None,kbd_m=None,kbd_e=None,kbd_l=None,kbd_i=None,kbd_s=None,kbd_d=None,kbd_t=None,kbd_u=None,kbd_k=None):
    if widget_o != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetobj",widget_o)
    if widget_k != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetkind",widget_k)
    if widget_t != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgettext",widget_t)
    if widget_u != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgeturi",widget_u)
    if widget_s != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetstart",str(widget_s))
    if widget_e != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetend",str(widget_e))
    if widget_a != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetadd",str(widget_a))
    if widget_v != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetstringvar",widget_v)
    if widget_b != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetbooleanvar",widget_b)
    if widget_p != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetphotoimage",widget_p)
    if widget_m != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetpixmap",widget_m)
    if widget_g != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetgc",widget_g)
    if widget_f != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetfont",widget_f)
    if widget_x != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetsizeX",str(widget_x))
    if widget_y != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetsizeY",str(widget_y))
    if widget_w != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetsizeW",str(widget_w))
    if widget_h != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"widgetsizeH",str(widget_h))
    if widget_c != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetcontainer",widget_c)
    if event_z != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetresize",event_z)
    if event_k != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"keyboard_press",event_k)
    if event_y != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"keyboard_release",event_y)
    if event_b  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"widgetcallback",event_b)
    if event_p  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"mouse_press",event_p)
    if event_r  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"mouse_release",event_r)
    if event_e  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"mouse_enter",event_e)
    if event_m  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"mouse_motion",event_m)
    if event_l  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"mouse_leave",event_l)
    if event_a  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"notify_activate",event_a)
    if event_u  != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"notify_popupmenu",event_u)
    if menu_o   != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"popupmenuobj",menu_o)
    if menu_b   != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"popupmenulist",menu_b)
    if menu_c   != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"popupmenuclick",menu_c)
    if dialog_t != None:  LTsv_widgetPAGE=LTsv_pushlinerest(LTsv_widgetPAGE,"dialog_type",str(dialog_t))
    if dialog_c != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"dialog_close",dialog_c)
    if kbd_p    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_press",kbd_p)
    if kbd_r    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_release",kbd_r)
    if kbd_m    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_motion",kbd_m)
    if kbd_e    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_enter",kbd_e)
    if kbd_l    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_leave",kbd_l)
    if kbd_i    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_input",kbd_i)
    if kbd_s    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_settext",kbd_s)
    if kbd_d    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_deftext",kbd_d)
    if kbd_t    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_gettext",kbd_t)
    if kbd_u    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_geturi",kbd_u)
    if kbd_k    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_‎keyenter",kbd_k)
    return LTsv_widgetPAGE

def LTsv_widgetPAGEKBD(LTsv_widgetPAGE,clip_a=None,clip_b=None,clip_c=None,clip_d=None,clip_e=None,clip_f=None,clip_g=None, \
    clip_h=None,clip_i=None,clip_j=None,clip_k=None,clip_l=None,clip_m=None,clip_n=None, \
    clip_o=None,clip_p=None,clip_q=None,clip_r=None,clip_s=None,clip_t=None,clip_u=None, \
    clip_v=None,clip_w=None,clip_x=None,clip_y=None,clip_z=None):
    if clip_a    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_A",clip_a)
    if clip_b    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_V",clip_b)
    if clip_c    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_copy",clip_c)
    if clip_d    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_D",clip_d)
    if clip_e    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_R",clip_e)
    if clip_f    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_find",clip_f)
    if clip_g    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_G",clip_g)
    if clip_h    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_H",clip_h)
    if clip_i    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_I",clip_i)
    if clip_j    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_J",clip_j)
    if clip_k    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_K",clip_k)
    if clip_l    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_L",clip_l)
    if clip_m    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_M",clip_m)
    if clip_n    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_N",clip_n)
    if clip_o    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_open",clip_o)
    if clip_p    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_P",clip_p)
    if clip_q    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_Q",clip_q)
    if clip_r    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_R",clip_r)
    if clip_s    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_save",clip_s)
    if clip_t    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_T",clip_t)
    if clip_u    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_U",clip_u)
    if clip_v    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_‎paste",clip_v)
    if clip_w    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_W",clip_w)
    if clip_x    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_cut",clip_x)
    if clip_y    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_Y",clip_y)
    if clip_z    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"editcanvas_Z",clip_z)
    return LTsv_widgetPAGE

def LTsv_fonttuple(LTsv_line):
    LTsv_fontlist=None
    if LTsv_line != None:
        LTsv_fontopts=LTsv_line.replace('\n','\t').replace('\t',',').strip(',').split(',')
        LTsv_fontlist=[]
        for LTsv_fontopt in LTsv_fontopts:
            LTsv_fontlist.append(LTsv_fontopt)
            if len(LTsv_fontlist)>=3:
                break
    return tuple(LTsv_fontlist) if LTsv_fontlist != None else None

def LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f=None,widget_d=False):
    LTsv_libgtk.gtk_widget_set_size_request(widget_o,widget_w,widget_h)
    LTsv_libgtk.gtk_fixed_put(window_c,widget_o,widget_x,widget_y)
    if widget_f != None:
        LTsv_fontDesc=LTsv_libgtk.pango_font_description_from_string(widget_f.encode("utf-8"))
        if widget_d:
            LTsv_libgtk.gtk_widget_modify_font(LTsv_libgtk.gtk_bin_get_child(widget_o),LTsv_fontDesc)
        else:
            LTsv_libgtk.gtk_widget_modify_font(widget_o,LTsv_fontDesc)
        LTsv_libgtk.pango_font_description_free(LTsv_fontDesc)

def LTsv_tkinter_hideondelete_shell(LTsv_windowPAGENAME):
    def tkinter_hideondelete_kernel(window_objvoid=None,window_objptr=None):
        global LTsv_widgetLTSV
        LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
        widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
        widget_o.withdraw()
        return 0
    return tkinter_hideondelete_kernel

LTsv_GTK_WINDOW_TOPLEVEL=0
LTsv_GTK_WIN_POS_CENTER=1
class LTsv_GdkEventKey(ctypes.Structure):
    _fields_ = [
        ('type',ctypes.c_int),
        ('window',ctypes.c_void_p),
        ('send_event',ctypes.c_ubyte),
        ('time',ctypes.c_uint),
        ('state',ctypes.c_uint),
        ('keyval',ctypes.c_uint),
    ]
LTsv_CALLBACLTYPE_GdkEventKey=ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.POINTER(LTsv_GdkEventKey))
def LTsv_window_new(widget_n=None,event_b=None,widget_t="LTsv_window",widget_w=200,widget_h=120,event_z=None,event_k=None,event_y=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_windowPAGE=""
    LTsv_windowPAGE=LTsv_widgetPAGEXYWH(LTsv_windowPAGE,widget_k="window",widget_t=widget_t,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        window_o=LTsv_libgtk.gtk_window_new(LTsv_GTK_WINDOW_TOPLEVEL)
        LTsv_libgtk.gtk_window_set_title(window_o,widget_t.encode("utf-8","xmlcharrefreplace"))
        LTsv_libgtk.gtk_widget_set_size_request(window_o,widget_w,widget_h)
        LTsv_libgtk.gtk_window_set_resizable(window_o,True if event_z !=None else False)
        LTsv_libgtk.gtk_window_set_position(window_o,LTsv_GTK_WIN_POS_CENTER)
        widget_c=LTsv_libgtk.gtk_fixed_new()
        LTsv_libgtk.gtk_container_add(window_o,widget_c)
        event_b_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_libgtk.gtk_widget_hide_on_delete
        LTsv_libobj.g_signal_connect_data(window_o,"delete-event".encode("utf-8"),event_b_cbk,0,0,0)
        event_z_cbk,event_k_cbk,event_y_cbk=None,None,None
        if event_z:
            event_z_cbk=LTsv_CALLBACLTYPE(event_z)
            LTsv_libobj.g_signal_connect_data(window_o,"configure-event".encode("utf-8"),event_z_cbk,0,0,0)
        if event_k:
#            event_k_cbk=LTsv_CALLBACLTYPE(event_k)
            event_k_cbk=LTsv_CALLBACLTYPE_GdkEventKey(event_k)
            LTsv_libobj.g_signal_connect_data(window_o,"key-press-event".encode("utf-8"),event_k_cbk,0,0,0)
        if event_y:
#            event_y_cbk=LTsv_CALLBACLTYPE(event_y)
            event_y_cbk=LTsv_CALLBACLTYPE_GdkEventKey(event_y)
            LTsv_libobj.g_signal_connect_data(window_o,"key-release-event".encode("utf-8"),event_y_cbk,0,0,0)
        LTsv_windowPAGE=LTsv_widgetPAGEXYWH(LTsv_windowPAGE,widget_o=window_o,widget_t=widget_t,widget_c=widget_c,event_b=event_b_cbk,event_z=event_z_cbk,event_k=event_k_cbk,event_y=event_y_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        window_o=Tk.Tk()
        window_o.title(widget_t)
        window_o.minsize(widget_w,widget_h)
        window_o.geometry("{0}x{1}+{2}+{3}".format(widget_w,widget_h,(window_o.winfo_vrootwidth()-widget_w)//2,(window_o.winfo_vrootheight()-widget_h)//2))
        event_b_cbk=event_b if event_b != None else LTsv_tkinter_hideondelete_shell(LTsv_windowPAGENAME)
        window_o.protocol("WM_DELETE_WINDOW",event_b_cbk)
        if event_z:
            window_o.maxsize(window_o.winfo_vrootwidth(),window_o.winfo_vrootheight())
            window_o.bind('<Configure>',event_z)
        else:
            window_o.maxsize(widget_w,widget_h); window_o.resizable(0,0)
        if event_k:
            window_o.bind('<KeyPress>',event_k)
        if event_y:
            window_o.bind('<KeyRelease>',event_y)
        LTsv_windowPAGE=LTsv_widgetPAGEXYWH(LTsv_windowPAGE,widget_o=window_o,widget_t=widget_t,event_b=event_b_cbk,event_z=event_z,event_k=event_k,event_y=event_y)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_windowPAGENAME,LTsv_windowPAGE)
    return LTsv_windowPAGENAME

def LTsv_widget_settext(LTsv_widgetPAGENAME,widget_t=""):
    global LTsv_widgetLTSV
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
    widget_v=None
    if widget_k == "window":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_window_set_title(widget_o,widget_t.encode("utf-8","xmlcharrefreplace"))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.title(widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "label":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_label_set_text(widget_o,widget_t.encode("utf-8","xmlcharrefreplace"))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_v=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetstringvar")]; widget_v.set(widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "button":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_label_set_text(LTsv_libgtk.gtk_bin_get_child(widget_o),widget_t.encode("utf-8","xmlcharrefreplace"))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_v=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetstringvar")]; widget_v.set(widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "check":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_label_set_text(LTsv_libgtk.gtk_bin_get_child(widget_o),widget_t.encode("utf-8","xmlcharrefreplace"))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_v=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetstringvar")]; widget_v.set(widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "radio":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_label_set_text(LTsv_libgtk.gtk_bin_get_child(widget_o),widget_t.encode("utf-8","xmlcharrefreplace"))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_v=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetstringvar")]; widget_v.set(widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "clipboard":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_clipboard_set_text(widget_o,widget_t.encode("utf-8","xmlcharrefreplace"),-1)
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.clipboard_append(widget_t)
    if widget_k == "edit":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_v=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetstringvar")]; LTsv_libgtk.gtk_text_buffer_set_text(widget_v,widget_t.encode("utf-8","xmlcharrefreplace"),-1)
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.delete(1.0,Tk.END); widget_o.insert(1.0,widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE)
    if widget_k == "entry":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_entry_set_text(widget_o,widget_t.encode("utf-8","xmlcharrefreplace"))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.delete(0,Tk.END); widget_o.insert(0,widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "scale":
        widget_s=int(float(widget_t))
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_range_set_value(widget_o,ctypes.c_double(widget_s))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.set(int(widget_s))
    if widget_k == "spin":
        widget_s=int(float(widget_t))
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_spin_button_set_value(widget_o,ctypes.c_double(int(float(widget_s))))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.delete(0,Tk.END); widget_o.insert(0,widget_t)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "notify":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_status_icon_set_tooltip(widget_o,widget_t.encode("utf-8"))
        if LTsv_GUI == LTsv_GUI_Tkinter:
            widget_o.szTip=widget_t[:64].encode("utf-8")
            LTsv_shell32.Shell_NotifyIcon(ctypes.c_ulong(LTsv_ICON_NIM_MODIFY),ctypes.pointer(widget_o))
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    if widget_k == "combobox":
        if LTsv_GUI == LTsv_GUI_GTK2:
            if str(widget_o) in LTsv_popupmenuOBJ:
                widget_combo=LTsv_popupmenuOBJ[str(widget_o)].split('\n')
                widget_s=widget_combo.index(widget_t) if widget_t in widget_combo else 0
                LTsv_libgtk.gtk_combo_box_set_active(widget_o,widget_s)
    if widget_k == "editcanvas":
        LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"editcanvas_deftext")](LTsv_widgetPAGENAME,TT=widget_t)
    if widget_k == "filedialog":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_window_set_title(widget_o,widget_t.encode("utf-8","xmlcharrefreplace"))
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_t=widget_t)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)

class LTsv_TextIter(ctypes.Structure):
    _fields_ = [
        ('dummy1',          ctypes.c_void_p),
        ('dummy2',          ctypes.c_void_p),
        ('dummy3',          ctypes.c_uint),
        ('dummy4',          ctypes.c_uint),
        ('dummy5',          ctypes.c_uint),
        ('dummy6',          ctypes.c_uint),
        ('dummy7',          ctypes.c_uint),
        ('dummy8',          ctypes.c_uint),
        ('dummy9',          ctypes.c_uint),
        ('dummy10',         ctypes.c_void_p),
        ('dummy11',         ctypes.c_void_p),
        ('dummy12',         ctypes.c_uint),
        ('dummy13',         ctypes.c_uint),
        ('dummy14',         ctypes.c_void_p),
    ]
def LTsv_widget_gettext(LTsv_widgetPAGENAME):
    global LTsv_widgetLTSV
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
    widget_t=""
    if widget_k == "window":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_window_get_title(widget_o)).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=LTsv_readlinerest(LTsv_widgetPAGE,"widgettext")
    if widget_k == "label":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_label_get_text(widget_o)).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.cget("text")
    if widget_k == "button":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_label_get_text(LTsv_libgtk.gtk_bin_get_child(widget_o))).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.cget("text")
    if widget_k == "check":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_label_get_text(LTsv_libgtk.gtk_bin_get_child(widget_o))).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.cget("text")
    if widget_k == "radio":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_label_get_text(LTsv_libgtk.gtk_bin_get_child(widget_o))).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.cget("text")
    if widget_k == "clipboard":
        try:
            if LTsv_GUI == LTsv_GUI_GTK2:     widget_t="{0}".format(ctypes.c_char_p(LTsv_libgtk.gtk_clipboard_wait_for_text(widget_o)).value.decode("utf-8"))
            if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t="{0}".format(widget_o.clipboard_get())
        except:
            widget_t=""
    if widget_k == "entry":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_entry_get_text(widget_o)).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.get()
    if widget_k == "edit":
        if LTsv_GUI == LTsv_GUI_GTK2:
            widget_v=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetstringvar")]
            start_iter=LTsv_TextIter(); end_iter=LTsv_TextIter()
            LTsv_libgtk.gtk_text_buffer_get_start_iter(widget_v,ctypes.pointer(start_iter)); LTsv_libgtk.gtk_text_buffer_get_end_iter(widget_v,ctypes.pointer(end_iter))
            widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_text_buffer_get_text(widget_v,ctypes.pointer(start_iter),ctypes.pointer(end_iter),True)).value.decode("utf-8");
#            LTsv_libgtk.gtk_text_iter_free(ctypes.pointer(start_iter)); LTsv_libgtk.gtk_text_iter_free(ctypes.pointer(end_iter))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.get(1.0,Tk.END)
    if widget_k == "scale":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=str(int(ctypes.c_double(LTsv_libgtk.gtk_range_get_value(widget_o)).value))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=str(widget_o.get())
    if widget_k == "spin":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=str(int(ctypes.c_int(LTsv_libgtk.gtk_spin_button_get_value_as_int(widget_o)).value))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=str(widget_o.get())
    if widget_k == "notify":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=LTsv_readlinerest(LTsv_widgetPAGE,"widgettext")
    if widget_k == "combobox":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_combo_box_text_get_active_text(widget_o)).value.decode("utf-8") if LTsv_libgtk.gtk_tree_model_iter_n_children(LTsv_libgtk.gtk_combo_box_get_model(widget_o),None) > 0 else ""
    if widget_k == "editcanvas":
        widget_t=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"editcanvas_gettext")](LTsv_widgetPAGENAME)
    if widget_k == "filedialog":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_window_get_title(widget_o)).value.decode("utf-8")
    return widget_t

def LTsv_widget_setnumber(LTsv_widgetPAGENAME,widget_s=0):
    global LTsv_widgetLTSV
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
    widget_v=None
    if widget_k == "check":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_toggle_button_set_active(widget_o,ctypes.c_int(min(max(int(float(widget_s)),0),1)))
        if LTsv_GUI == LTsv_GUI_Tkinter:  LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetbooleanvar")].set(True if int(float(widget_s)) !=0 else False)
    if widget_k == "radio":
        if LTsv_GUI == LTsv_GUI_GTK2:
            radio_group=LTsv_libgtk.gtk_radio_button_get_group(widget_o)
            radio_len=LTsv_libgtk.g_slist_length(radio_group); widget_s=min(max(int(float(widget_s)),0),radio_len-1)
            LTsv_libgtk.gtk_toggle_button_set_active(LTsv_libgtk.g_slist_nth_data(radio_group,radio_len-widget_s-1),ctypes.c_int(1))
        if LTsv_GUI == LTsv_GUI_Tkinter:  LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetbooleanvar")].set(widget_s)
    if widget_k == "entry":
        LTsv_widget_settext(LTsv_widgetPAGENAME,widget_t="{0}".format(widget_s))
    if widget_k == "edit":
        LTsv_widget_settext(LTsv_widgetPAGENAME,widget_t="{0}".format(widget_s))
    if widget_k == "scale":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_range_set_value(widget_o,ctypes.c_double(int(float(widget_s))))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.set(int(widget_s))
    if widget_k == "spin":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_spin_button_set_value(widget_o,ctypes.c_double(int(float(widget_s))))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_o.delete(0,Tk.END); widget_o.insert(0,str(widget_s))
    if widget_k == "combobox":
        if LTsv_GUI == LTsv_GUI_GTK2:     LTsv_libgtk.gtk_combo_box_set_active(widget_o,max(min(widget_s,LTsv_libgtk.gtk_tree_model_iter_n_children(LTsv_libgtk.gtk_combo_box_get_model(widget_o),None)-1),0))
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)

def LTsv_widget_getnumber(LTsv_widgetPAGENAME):
    global LTsv_widgetLTSV
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
    widget_s=0
    if widget_k == "check":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_s=ctypes.c_int(LTsv_libgtk.gtk_toggle_button_get_active(widget_o)).value
        if LTsv_GUI == LTsv_GUI_Tkinter:   widget_s=1 if LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetbooleanvar")].get() == True else 0
    if widget_k == "radio":
        if LTsv_GUI == LTsv_GUI_GTK2:
            radio_group=LTsv_libgtk.gtk_radio_button_get_group(widget_o)
            radio_len=LTsv_libgtk.g_slist_length(radio_group); widget_s=radio_len
            for radio_count in range(radio_len):
                if ctypes.c_int(LTsv_libgtk.gtk_toggle_button_get_active(LTsv_libgtk.g_slist_nth_data(radio_group,radio_count))).value:
                    widget_s=radio_len-radio_count-1
        if LTsv_GUI == LTsv_GUI_Tkinter:   widget_s=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetbooleanvar")].get()
    if widget_k == "entry":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_entry_get_text(widget_o)).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.get()
        widget_s=int(widget_t) if widget_t.isdecimal() else 0
    if widget_k == "scale":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_s=int(float(ctypes.c_double(LTsv_libgtk.gtk_range_get_value(widget_o)).value))
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_s=int(widget_o.get())
    if widget_k == "spin":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_s=int(ctypes.c_int(LTsv_libgtk.gtk_spin_button_get_value_as_int(widget_o)).value)
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_s=LTsv_intstr0x(widget_o.get())
    if widget_k == "combobox":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_s=LTsv_libgtk.gtk_combo_box_get_active(widget_o)
    return widget_s

def LTsv_widget_seturi(LTsv_widgetPAGENAME,widget_u=""):
    global LTsv_widgetLTSV
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
    if widget_k == "image":
        if LTsv_GUI == LTsv_GUI_GTK2:
            widget_p=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetphotoimage")]
            LTsv_libgtk.gtk_image_set_from_file(widget_p,widget_u.encode("utf-8","xmlcharrefreplace"))
        if LTsv_GUI == LTsv_GUI_Tkinter:
            widget_p=Tk.PhotoImage(file=widget_u)
            widget_o.configure(image=widget_p)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_u=widget_u,widget_p=widget_p)
    if widget_k == "notify":
        if LTsv_GUI == LTsv_GUI_GTK2:
            picture_o=LTsv_pictureOBJ[widget_u] if widget_u in LTsv_pictureOBJ else LTsv_draw_picture_load(widget_u)
            if picture_o != None:
                LTsv_libgtk.gtk_status_icon_set_from_pixbuf(widget_o,picture_o)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            icon_o=LTsv_iconOBJ[widget_u] if widget_u in LTsv_iconOBJ else LTsv_icon_load(widget_u)
            if icon_o != None:
                widget_o.hIcon=icon_o
                LTsv_shell32.Shell_NotifyIcon(ctypes.c_ulong(LTsv_ICON_NIM_MODIFY),ctypes.pointer(widget_o))
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_u=widget_u)
    if widget_k == "editcanvas":
        LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"editcanvas_deftext")](LTsv_widgetPAGENAME,UT=widget_u)
    if widget_k == "filedialog":
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_u=widget_u)
        LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)

def LTsv_widget_geturi(LTsv_widgetPAGENAME):
    global LTsv_widgetLTSV
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
    widget_u=""
    if widget_k == "image":
        widget_u=LTsv_readlinerest(LTsv_widgetPAGE,"widgeturi")
    if widget_k == "notify":
        widget_u=LTsv_readlinerest(LTsv_widgetPAGE,"widgeturi")
    if widget_k == "editcanvas":
        widget_u=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"editcanvas_geturi")](LTsv_widgetPAGENAME)
    if widget_k == "filedialog":
        try:
            if LTsv_GUI == LTsv_GUI_GTK2:    widget_u=ctypes.c_char_p(LTsv_libgtk.gtk_file_chooser_get_filename(widget_o)).value.decode("utf-8")
            if LTsv_GUI == LTsv_GUI_Tkinter:  widget_u=LTsv_readlinerest(LTsv_widgetPAGE,"widgeturi")
        except:
            widget_u=""
    return widget_u

def LTsv_widget_showhide(LTsv_widgetPAGENAME,widget_i):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_windowPAGE,"widgetkind")
    if widget_k == "window":
        if LTsv_GUI == LTsv_GUI_GTK2:
            if widget_i:
                LTsv_libgtk.gtk_widget_show_all(widget_o)
            else:
                LTsv_libobj.g_signal_emit_by_name(widget_o,"delete-event".encode("utf-8"),0,0)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            if widget_i:
                widget_o.deiconify()
            else:
                widget_o.withdraw()
    elif widget_k == "filedialog":
        if LTsv_GUI == LTsv_GUI_GTK2:
            if widget_i:
                LTsv_libgtk.gtk_widget_show_all(widget_o)
            else:
                LTsv_libgtk.gtk_widget_hide(widget_o)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            if widget_i:
                widget_o()
            else:
                pass
    else:
        if LTsv_GUI == LTsv_GUI_GTK2:
            if widget_i:
                LTsv_libgtk.gtk_widget_show_all(widget_o)
            else:
                LTsv_libgtk.gtk_widget_hide(widget_o)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            if widget_i:
                pass
            else:
                pass
    return 0

def LTsv_widget_disableenable(LTsv_widgetPAGENAME,widget_i):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_windowPAGE,"widgetkind")
    if widget_k != "window":
        if LTsv_GUI == LTsv_GUI_GTK2:
            if widget_i:
                LTsv_libgtk.gtk_widget_set_sensitive(widget_o,True)
            else:
                LTsv_libgtk.gtk_widget_set_sensitive(widget_o,False)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            if widget_i:
                widget_o.configure(state=Tk.NORMAL)
            else:
                widget_o.configure(state=Tk.DISABLED)
    return 0

def LTsv_widget_focus(LTsv_widgetPAGENAME):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_libgtk.gtk_widget_grab_focus(widget_o);
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_o.focus_set()
    return 0

def LTsv_window_main(LTsv_windowPAGENAME):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_libgtk.gtk_main()
    if LTsv_GUI == LTsv_GUI_Tkinter:
        window_o.mainloop()

def LTsv_window_after(LTsv_windowPAGENAME,event_b=None,event_i="mousemotion",event_w=1000):
    global LTsv_widgetLTSV,LTsv_timerOBJ,LTsv_timer_cbk
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    if LTsv_GUI == LTsv_GUI_GTK2:
        if event_i in LTsv_timerOBJ:
            if LTsv_timerOBJ[event_i] != None:
#                LTsv_libobj.g_source_remove(LTsv_timerOBJ[event_i])
                LTsv_timerOBJ[event_i]=None
                LTsv_timer_cbk[event_i]=None
        if event_b != None:
            LTsv_timer_cbk[event_i]=LTsv_CALLBACLTYPE(event_b)
            LTsv_timerOBJ[event_i]=LTsv_libobj.g_timeout_add(max(event_w,10),LTsv_timer_cbk[event_i],None)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        if event_i in LTsv_timerOBJ:
            window_o.after_cancel(LTsv_timerOBJ[event_i])
        if event_b != None:
            LTsv_timerOBJ[event_i]=window_o.after(max(event_w,10),event_b)
    return 0

def LTsv_window_foreground():
    LTsv_window_activeID=""
    if sys.platform.startswith("linux"):
        LTsv_xprop=LTsv_subprocess("xprop -root")
        LTsv_posL=LTsv_xprop.find("_NET_ACTIVE_WINDOW(WINDOW)"); LTsv_posC=LTsv_xprop.find("# 0x",LTsv_posL); LTsv_posR=LTsv_xprop.find('\n',LTsv_posL)
        LTsv_window_activeID=LTsv_xprop[LTsv_posC+len("# "):LTsv_posR]
    if sys.platform.startswith("win"):
        LTsv_window_activeID="{0:#x}".format(LTsv_user32.GetForegroundWindow())
    return LTsv_window_activeID

def LTsv_window_title(LTsv_window_id):
    if sys.platform.startswith("linux"):
        LTsv_xwininfo=LTsv_subprocess("xwininfo -id {0}".format(LTsv_window_id))
        LTsv_posL=LTsv_xwininfo.find("xwininfo: Window id: {0}".format(LTsv_window_id)); LTsv_posC=LTsv_xwininfo.find('"',LTsv_posL); LTsv_posR=LTsv_xwininfo.find('\n',LTsv_posL)
        LTsv_window_titleID=LTsv_xwininfo[LTsv_posC+len('"'):LTsv_posR-len('"')]
    if sys.platform.startswith("win"):
        LTsv_window_titleID=""
        LTsv_window_titlelen=LTsv_user32.GetWindowTextLengthW(ctypes.c_int(int(LTsv_window_id,16)))+1
        LTsv_window_titlebuf=ctypes.create_unicode_buffer(LTsv_window_titlelen)
        LTsv_window_titleID=LTsv_window_titlebuf.value if LTsv_user32.GetWindowTextW(ctypes.c_int(int(LTsv_window_id,16)),LTsv_window_titlebuf,ctypes.sizeof(LTsv_window_titlebuf)) > 0 else ""
    return LTsv_window_titleID

def LTsv_window_exit(window_objvoid=None,window_objptr=None):
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_libgtk.gtk_exit(0)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        sys.exit(0)
    return 0
LTsv_window_exit_cbk=LTsv_CALLBACLTYPE(LTsv_window_exit)

def LTsv_window_none(window_objvoid=None,window_objptr=None):
    return 0
LTsv_window_none_cbk=LTsv_CALLBACLTYPE(LTsv_window_none)

def LTsv_screen_w(LTsv_windowPAGENAME):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    screen_w=-1
    if LTsv_GUI == LTsv_GUI_GTK2:
        screen_w=LTsv_libgtk.gdk_screen_get_width(LTsv_libgtk.gdk_screen_get_default())
    if LTsv_GUI == LTsv_GUI_Tkinter:
        if window_o!=None:
            screen_w=window_o.winfo_vrootwidth()
    return screen_w

def LTsv_screen_h(LTsv_windowPAGENAME):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    screen_h=-1
    if LTsv_GUI == LTsv_GUI_GTK2:
        screen_h=LTsv_libgtk.gdk_screen_height(LTsv_libgtk.gdk_screen_get_default())
    if LTsv_GUI == LTsv_GUI_Tkinter:
        if window_o!=None:
            screen_h=window_o.winfo_vrootheight()
    return screen_h

class LTsv_WINDOW_WIDTH(ctypes.Structure):
    _fields_ = [ ('width',  ctypes.c_uint) ]
class LTsv_WINDOW_HEIGHT(ctypes.Structure):
    _fields_ = [ ('height', ctypes.c_uint) ]
def LTsv_window_wh(LTsv_windowPAGENAME):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    window_w,window_h=0,0
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_window_width,LTsv_window_height=LTsv_WINDOW_WIDTH(),LTsv_WINDOW_HEIGHT()
        LTsv_libgtk.gtk_window_get_size(window_o,ctypes.byref(LTsv_window_width),ctypes.byref(LTsv_window_height))
        window_w,window_h=LTsv_window_width.width,LTsv_window_height.height
    if LTsv_GUI == LTsv_GUI_Tkinter:
        window_w,window_h=window_o.winfo_width(),window_o.winfo_height()
    return window_w,window_h
def LTsv_window_w(LTsv_windowPAGENAME):
    window_w,window_h=LTsv_window_wh(LTsv_windowPAGENAME)
    return window_w
def LTsv_window_h(LTsv_windowPAGENAME):
    window_w,window_h=LTsv_window_wh(LTsv_windowPAGENAME)
    return window_h

def LTsv_window_resize(LTsv_windowPAGENAME,widget_w=16,widget_h=16):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_libgtk.gtk_window_resize(window_o,widget_w,widget_h)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        window_o.geometry("{0}x{1}".format(widget_w,widget_h))

def LTsv_label_new(LTsv_windowPAGENAME,widget_n=None,widget_t="LTsv_label",widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="label",widget_t=widget_t,widget_f=widget_f,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_label_new(widget_t.encode("utf-8","xmlcharrefreplace"))
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,False)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_v=Tk.StringVar()
        widget_v.set(widget_t)
        widget_o=Tk.Label(window_o,textvariable=widget_v,font=LTsv_fonttuple(widget_f))
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_v=widget_v)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_image_new(LTsv_windowPAGENAME,widget_n=None,widget_t="LTsv_logo.png",widget_x=0,widget_y=0):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="image",widget_x=widget_x,widget_y=widget_y)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_p=LTsv_libgtk.gtk_image_new_from_file(widget_t.encode("utf-8","xmlcharrefreplace"))
        widget_o=LTsv_libgtk.gtk_event_box_new()
        LTsv_libgtk.gtk_container_add(widget_o,widget_p)
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_libgtk.gtk_fixed_put(window_c,widget_o,widget_x,widget_y)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_p=widget_p)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_p=Tk.PhotoImage(file=widget_t)
        widget_o=Tk.Label(window_o,image=widget_p)
        widget_o.place(x=widget_x,y=widget_y)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_p=widget_p)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_button_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_t="LTsv_button",widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="button",widget_t=widget_t,widget_f=widget_f,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_button_new_with_label(widget_t.encode("utf-8","xmlcharrefreplace"))
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,True)
        widget_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"clicked".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,event_b=widget_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_v=Tk.StringVar()
        widget_v.set(widget_t)
        widget_o=Tk.Button(window_o,textvariable=widget_v,command=event_b,font=LTsv_fonttuple(widget_f))
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_v=widget_v,event_b=event_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_check_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_t="LTsv_check",widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="check",widget_t=widget_t,widget_f=widget_f,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_check_button_new_with_label(widget_t.encode("utf-8","xmlcharrefreplace"))
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,True)
        widget_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"clicked".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,event_b=widget_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_v=Tk.StringVar()
        widget_v.set(widget_t)
        widget_b=Tk.BooleanVar()
        widget_b.set(False)
        widget_o=Tk.Checkbutton(window_o,textvariable=widget_v,variable=widget_b,command=event_b,font=LTsv_fonttuple(widget_f))
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_v=widget_v,widget_b=widget_b,event_b=event_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_radio_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_t="LTsv_radio",widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_radioPAGENAME=LTsv_widget_newUUID(False)
    LTsv_radioPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_radioPAGENAME)
    radio_k=LTsv_readlinerest(LTsv_radioPAGE,"widgetkind")
    radio_o=None if radio_k != "radio" else LTsv_widgetOBJ[LTsv_readlinerest(LTsv_radioPAGE,"widgetobj")]
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="radio",widget_t=widget_t,widget_f=widget_f,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_radio_button_new_with_label_from_widget(radio_o,widget_t.encode("utf-8","xmlcharrefreplace"))
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,True)
        widget_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"clicked".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,event_b=widget_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_v=Tk.StringVar()
        widget_v.set(widget_t)
        if radio_k != "radio":
            widget_b=Tk.IntVar(); widget_b.set(0)
        else:
            widget_b=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_radioPAGE,"widgetbooleanvar")]; widget_b.set(widget_b.get()+1)
        widget_o=Tk.Radiobutton(window_o,textvariable=widget_v,variable=widget_b,value=widget_b.get(),command=event_b,font=LTsv_fonttuple(widget_f))
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_v=widget_v,widget_b=widget_b,event_b=event_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_clipboard_new(LTsv_windowPAGENAME,widget_n=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="clipboard")
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_clipboard_get(LTsv_libgtk.gdk_atom_intern("CLIPBOARD".encode("utf-8"),0))
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_o=window_o
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_clipmenu_new(widget_o):
    global LTsv_popupmenuOBJ
    menu_o=Tk.Menu(widget_o,tearoff=False)
    menu_o.add_cascade(label="Ctrl+X(Cut)")
    menu_o.add_cascade(label='Ctrl+C(Copy)')
    menu_o.add_cascade(label='Ctrl+P(Paste)')
    menu_o.add_cascade(label='Ctrl+A(SelectAll)')
    LTsv_popupmenuOBJ[str(widget_o)]=menu_o
    def LTsv_entry_copypopup_show(event):
        global LTsv_popupmenuOBJ
        window_o=LTsv_popupmenuOBJ[str(event.widget)]
        window_o.post(event.x_root,event.y_root)
        window_o.entryconfigure("Ctrl+X(Cut)",command=lambda: event.widget.event_generate("<<Cut>>"))
        window_o.entryconfigure("Ctrl+C(Copy)",command=lambda: event.widget.event_generate("<<Copy>>"))
        window_o.entryconfigure("Ctrl+P(Paste)",command=lambda: event.widget.event_generate("<<Paste>>"))
        window_o.entryconfigure("Ctrl+A(SelectAll)",command=lambda: event.widget.event_generate("<<SelectAll>>"))
    menu_b=LTsv_entry_copypopup_show
    return menu_o,menu_b

LTsv_G_TYPE_STRING=64
LTsv_GTK_SELECTION_SINGLE=1
LTsv_GTK_POLICY_AUTOMATIC=1
LTsv_GTK_SHADOW_ETCHED_IN=3
def LTsv_edit_new(LTsv_windowPAGENAME,widget_n=None,widget_t="LTsv_edit",widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="edit",widget_t=widget_t,widget_f=widget_f,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_scrolled_window_new(0,0)
        widget_v=LTsv_libgtk.gtk_text_buffer_new(0)
        widget_c=LTsv_libgtk.gtk_text_view_new_with_buffer(widget_v)
        LTsv_libgtk.gtk_scrolled_window_set_policy(widget_o,LTsv_GTK_POLICY_AUTOMATIC,LTsv_GTK_POLICY_AUTOMATIC)
        LTsv_libgtk.gtk_scrolled_window_set_shadow_type(widget_o,LTsv_GTK_SHADOW_ETCHED_IN)
        LTsv_libgtk.gtk_container_add(widget_o,widget_c)
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,True)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_v=widget_v,widget_c=widget_c)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_o=Tk_sc.ScrolledText(window_o,font=LTsv_fonttuple(widget_f))
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o)
        menu_o,menu_b=LTsv_clipmenu_new(widget_o)
        widget_o.bind('<Button-3>',menu_b)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,menu_o=menu_o,menu_b=menu_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_entry_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_t="LTsv_entry",widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="entry",widget_t=widget_t,widget_f=widget_f,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_entry_new()
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,False)
        LTsv_libgtk.gtk_entry_set_text(widget_o,widget_t.encode("utf-8","xmlcharrefreplace"))
        widget_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"activate".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,event_b=widget_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_v=Tk.StringVar()
        widget_v.set(widget_t)
        widget_o=Tk.Entry(window_o,textvariable=widget_v,font=LTsv_fonttuple(widget_f))
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        if event_b != None:
            widget_o.bind('<Return>',event_b)
        menu_o,menu_b=LTsv_clipmenu_new(widget_o)
        widget_o.bind('<Button-3>',menu_b)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_v=widget_v,event_b=event_b,menu_o=menu_o,menu_b=menu_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_spin_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_s=0,widget_e=255,widget_a=1,widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="spin",widget_f=widget_f,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_spin_button_new_with_range(ctypes.c_double(widget_s),ctypes.c_double(widget_e),ctypes.c_double(widget_a))
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,False)
        LTsv_libgtk.gtk_spin_button_set_value(widget_o,str(widget_s).encode("utf-8","xmlcharrefreplace"))
        widget_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"activate".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_libobj.g_signal_connect_data(widget_o,"value-changed".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,event_b=widget_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_o=Tk.Spinbox(window_o,from_=widget_s,to=widget_e,increment=widget_a,command=event_b,font=LTsv_fonttuple(widget_f))
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,event_b=event_b)
        if event_b != None:
            widget_o.bind('<Return>',event_b)
        menu_o,menu_b=LTsv_clipmenu_new(widget_o)
        widget_o.bind('<Button-3>',menu_b)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,event_b=event_b,menu_o=menu_o,menu_b=menu_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_scale_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_s=0,widget_e=255,widget_a=1,widget_x=0,widget_y=0,widget_w=16,widget_h=16):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="scale",widget_s=widget_s,widget_e=widget_e,widget_a=widget_a,widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    LTsv_widget_orient='v' if widget_w < widget_h else 'h'
    if LTsv_GUI == LTsv_GUI_GTK2:
        if widget_w < widget_h:
            widget_o=LTsv_libgtk.gtk_vscale_new_with_range(ctypes.c_double(widget_s),ctypes.c_double(widget_e),ctypes.c_double(widget_a))
        else:
            widget_o=LTsv_libgtk.gtk_hscale_new_with_range(ctypes.c_double(widget_s),ctypes.c_double(widget_e),ctypes.c_double(widget_a))
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h)
        widget_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"value-changed".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,event_b=widget_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_o=Tk.Scale(window_o,orient=('v' if widget_w < widget_h else 'h'),from_=widget_s,to=widget_e,command=event_b)
        widget_o.place(x=widget_x,y=widget_y,width=widget_w,height=widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,event_b=event_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

def LTsv_scale_adjustment(LTsv_widgetPAGENAME,widget_s=0,widget_e=255,widget_a=1):
    global LTsv_widgetLTSV,LTsv_popupmenuOBJ
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
    if widget_k == "scale":
        if LTsv_GUI == LTsv_GUI_GTK2:
            widget_v=int(ctypes.c_double(LTsv_libgtk.gtk_range_get_value(widget_o)).value)
            adjustment_o=LTsv_libgtk.gtk_adjustment_new(ctypes.c_double(max(min(widget_v,widget_e),widget_s)),ctypes.c_double(widget_s),ctypes.c_double(widget_e),ctypes.c_double(widget_a),ctypes.c_double(1),ctypes.c_double(0),)
            LTsv_libgtk.gtk_range_set_adjustment(widget_o,adjustment_o)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            widget_o.configure(from_=widget_s,to=widget_e)
    if widget_k == "spin":
        if LTsv_GUI == LTsv_GUI_GTK2:
            widget_v=int(ctypes.c_double(LTsv_libgtk.gtk_spin_button_get_value_as_int(widget_o)).value)
            adjustment_o=LTsv_libgtk.gtk_adjustment_new(ctypes.c_double(max(min(widget_v,widget_e),widget_s)),ctypes.c_double(widget_s),ctypes.c_double(widget_e),ctypes.c_double(widget_a),ctypes.c_double(1),ctypes.c_double(0),)
            LTsv_libgtk.gtk_spin_button_set_adjustment(widget_o,adjustment_o)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            widget_o.configure(from_=widget_s,to=widget_e)
    return 0

def LTsv_combobox_list(LTsv_widgetPAGENAME,widget_t=""):
    global LTsv_widgetLTSV,LTsv_popupmenuOBJ
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
    LTsv_combobox_len=LTsv_libgtk.gtk_tree_model_iter_n_children(LTsv_libgtk.gtk_combo_box_get_model(widget_o),None)
    for LTsv_combobox_id in range(LTsv_combobox_len):
        LTsv_libgtk.gtk_combo_box_text_remove(widget_o,LTsv_combobox_len-LTsv_combobox_id-1)
    for LTsv_combobox_text in widget_t.split('\n'):
        if len(LTsv_combobox_text):
            LTsv_libgtk.gtk_combo_box_text_append_text(widget_o,LTsv_combobox_text.encode("utf-8","xmlcharrefreplace"))
    LTsv_libgtk.gtk_combo_box_set_active(widget_o,0)
    LTsv_popupmenuOBJ[str(widget_o)]=widget_t
    return 0

def LTsv_combobox_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="combobox",widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_o=LTsv_libgtk.gtk_combo_box_text_new()
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_GTKwidget_fixed(window_c,widget_o,widget_x,widget_y,widget_w,widget_h,widget_f,True)
        widget_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"changed".encode("utf-8"),widget_cbk,2,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,event_b=widget_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        pass  #Tkk
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

#  typedef struct{ unsigned int pixel; unsigned short red; unsigned short green; unsigned short blue; }GdkColor;
class LTsv_GDKCOLOR(ctypes.Structure):
    _fields_ = [
        ('pixel',ctypes.c_uint),
        ('colorR',ctypes.c_ushort),
        ('colorG',ctypes.c_ushort),
        ('colorB',ctypes.c_ushort)
    ]
    def __init__(self):
        LTsv_libgdk.gdk_color_parse("#ffffff".encode("utf-8"),ctypes.pointer(self))
#  typedef struct{ int x; int y; }GdkPoint;
class LTsv_GDKPOINT(ctypes.Structure):
    _fields_ = [
        ('X',ctypes.c_int),('Y',ctypes.c_int)
    ]
LTsv_GDK_POINTER_MOTION_MASK=1<<2
LTsv_GDK_BUTTON_RELEASE_MASK=1<<9
LTsv_GDK_KEY_PRESS_MASK=     1<<10
LTsv_GDK_SCROLL_MASK=        1<<21
LTsv_GDK_ARCFILL=23040

LTsv_canvascolor,LTsv_canvasbgcolor="black","white"
def LTsv_canvas_new(LTsv_windowPAGENAME,widget_n=None,widget_x=0,widget_y=0,widget_w=16,widget_h=16,event_p=None,event_r=None,event_e=None,event_m=None,event_l=None,event_w=100):
#    global LTsv_widgetLTSV,canvas_CBKtimeout,canvas_EMLenter,canvas_EMLmotion,canvas_EMLleave
    global LTsv_widgetLTSV
    global canvas_EMLenter,canvas_EMLmotion,canvas_EMLleave
    global canvas_CBKenter,canvas_CBKmotion,canvas_CBKleave,canvas_CBKtimeout,canvas_CBKafter,LTsv_canvasCBKpagename
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="canvas",widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    if LTsv_GUI == LTsv_GUI_GTK2:
        widget_p=LTsv_libgtk.gtk_image_new()
        widget_o=LTsv_libgtk.gtk_event_box_new()
        LTsv_libgtk.gtk_container_add(widget_o,widget_p)
        window_c=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetcontainer")]
        LTsv_libgtk.gtk_fixed_put(window_c,widget_o,widget_x,widget_y)
        widget_m=LTsv_libgdk.gdk_pixmap_new(LTsv_libgdk.gdk_get_default_root_window(),widget_w,widget_h,-1)
        LTsv_libgtk.gtk_image_set_from_pixmap(widget_p,widget_m,0)
        widget_g=LTsv_libgdk.gdk_gc_new(widget_m)
        widget_gccolor=LTsv_GDKCOLOR(); LTsv_libgdk.gdk_color_parse("white".encode("utf-8"),ctypes.pointer(widget_gccolor))
        LTsv_libgdk.gdk_gc_set_rgb_bg_color(widget_g,ctypes.pointer(widget_gccolor))
        LTsv_libgdk.gdk_gc_set_rgb_fg_color(widget_g,ctypes.pointer(widget_gccolor))
        LTsv_libgdk.gdk_draw_rectangle(widget_m,widget_g,True,0,0,widget_w,widget_h)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_p=widget_p,widget_m=widget_m,widget_g=widget_g)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        widget_o=Tk.Canvas(window_o,width=widget_w,height=widget_h,bg="white")
        widget_o.place(x=widget_x,y=widget_y)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o)
    def LTsv_canvas_enter(window_objvoid=None,window_objptr=None):
        global LTsv_canvas_motion_X,LTsv_canvas_motion_Y,LTsv_canvas_motion_Z
        global canvas_CBKafter
        if canvas_CBKafter[LTsv_widgetPAGENAME] == False:
            canvas_CBKafter[LTsv_widgetPAGENAME]=True; LTsv_canvas_motion_Z=LTsv_widgetPAGENAME
            if canvas_EMLenter[LTsv_widgetPAGENAME] != None:
                LTsv_window_after(LTsv_windowPAGENAME,event_b=canvas_EMLenter[LTsv_widgetPAGENAME],event_i="{0}_enter".format(LTsv_canvasCBKpagename[LTsv_widgetPAGENAME]),event_w=event_w)
            LTsv_canvas_timeout()
        return 0
    def LTsv_canvas_motion(window_objvoid=None,window_objptr=None):
        global LTsv_canvas_motion_X,LTsv_canvas_motion_Y,LTsv_canvas_motion_Z
        if LTsv_GUI == LTsv_GUI_GTK2:
            mouse_x,mouse_y=ctypes.c_int(),ctypes.c_int(); LTsv_libgdk.gdk_window_at_pointer(ctypes.byref(mouse_x),ctypes.byref(mouse_y))
            LTsv_canvas_motion_X,LTsv_canvas_motion_Y=int(mouse_x.value),int(mouse_y.value)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            if window_objvoid != None:
                mouse_x,mouse_y=window_objvoid.x,window_objvoid.y
                LTsv_canvas_motion_X,LTsv_canvas_motion_Y=int(mouse_x),int(mouse_y)
        return 0
    def LTsv_canvas_timeout(window_objvoid=None,window_objptr=None):
        global canvas_CBKafter
        if canvas_CBKafter[LTsv_widgetPAGENAME] == True:
            if canvas_EMLmotion[LTsv_widgetPAGENAME] != None: canvas_EMLmotion[LTsv_widgetPAGENAME]()
            LTsv_window_after(LTsv_windowPAGENAME,event_b=LTsv_canvas_timeout,event_i="{0}_motion".format(LTsv_canvasCBKpagename[LTsv_widgetPAGENAME]),event_w=event_w)
        return 0
    def LTsv_canvas_leave(window_objvoid=None,window_objptr=None):
        global LTsv_canvas_motion_X,LTsv_canvas_motion_Y,LTsv_canvas_motion_Z
        global canvas_CBKafter,LTsv_canvasCBKpagename
        canvas_CBKafter[LTsv_widgetPAGENAME]=False; LTsv_canvas_motion_Z=""
        if canvas_EMLleave[LTsv_widgetPAGENAME] != None:
            LTsv_window_after(LTsv_windowPAGENAME,event_b=canvas_EMLleave[LTsv_widgetPAGENAME],event_i="{0}_leave".format(LTsv_canvasCBKpagename[LTsv_widgetPAGENAME]),event_w=event_w)
        LTsv_canvas_motion_X,LTsv_canvas_motion_Y=-1,-1
        return 0
    canvas_EMLenter[LTsv_widgetPAGENAME],canvas_EMLmotion[LTsv_widgetPAGENAME],canvas_EMLleave[LTsv_widgetPAGENAME]=event_e,event_m,event_l
    canvas_CBKenter[LTsv_widgetPAGENAME],canvas_CBKmotion[LTsv_widgetPAGENAME],canvas_CBKleave[LTsv_widgetPAGENAME]=LTsv_canvas_enter,LTsv_canvas_motion,LTsv_canvas_leave
    canvas_CBKtimeout[LTsv_widgetPAGENAME],canvas_CBKafter[LTsv_widgetPAGENAME],LTsv_canvasCBKpagename[LTsv_widgetPAGENAME]=LTsv_canvas_timeout,False,LTsv_widgetPAGENAME
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_libgtk.gtk_widget_set_events(widget_o,LTsv_GDK_POINTER_MOTION_MASK)
        event_p_cbk=LTsv_CALLBACLTYPE(event_p) if event_p != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"button-press-event".encode("utf-8"),event_p_cbk,0,0,0)
        event_r_cbk=LTsv_CALLBACLTYPE(event_r) if event_r != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"button-release-event".encode("utf-8"),event_r_cbk,0,0,0)
        event_e_cbk=LTsv_CALLBACLTYPE(canvas_CBKenter[LTsv_widgetPAGENAME]) if LTsv_canvas_enter != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"enter-notify-event".encode("utf-8"),event_e_cbk,0,0,0)
        event_m_cbk=LTsv_CALLBACLTYPE(canvas_CBKmotion[LTsv_widgetPAGENAME]) if LTsv_canvas_motion != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"motion-notify-event".encode("utf-8"),event_m_cbk,0,0,0)
        event_l_cbk=LTsv_CALLBACLTYPE(canvas_CBKleave[LTsv_widgetPAGENAME]) if LTsv_canvas_leave != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"leave-notify-event".encode("utf-8"),event_l_cbk,0,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,event_p=event_p_cbk,event_r=event_r_cbk,event_e=event_e_cbk,event_m=event_m_cbk,event_l=event_l_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        if event_p != None:
            widget_o.bind("<ButtonPress>",event_p)
        if event_r != None:
            widget_o.bind("<ButtonRelease>",event_r)
        widget_o.bind("<Enter>",canvas_CBKenter[LTsv_widgetPAGENAME])
        widget_o.bind("<Motion>",canvas_CBKmotion[LTsv_widgetPAGENAME])
        widget_o.bind("<Leave>",canvas_CBKleave[LTsv_widgetPAGENAME])
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,event_p=event_p,event_r=event_r,event_e=LTsv_canvas_enter,event_m=LTsv_canvas_motion,event_l=LTsv_canvas_leave)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

LTsv_GTKcanvasPAGE,LTsv_GTKcanvas_o,LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,LTsv_GTKcanvas_font=None,None,None,None,None
LTsv_GTKcanvasW,LTsv_GTKcanvasH,LTsv_GTKcanvas_gccolor,LTsv_canvas_bccolor=None,None,None,None
def LTsv_drawGTK_selcanvas(LTsv_canvasPAGENAME,draw_g="LTsv_draw_tkTAG"):
    global LTsv_GTKcanvasPAGE,LTsv_GTKcanvas_o,LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,LTsv_GTKcanvas_font
    global LTsv_GTKcanvasW,LTsv_GTKcanvasH,LTsv_GTKcanvas_gccolor,LTsv_canvas_bccolor
    LTsv_GTKcanvasPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_canvasPAGENAME)
    LTsv_GTKcanvasW=int(LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetsizeW"))
    LTsv_GTKcanvasH=int(LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetsizeH"))
    LTsv_GTKcanvas_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetobj")]
    LTsv_GTKcanvas_m=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetpixmap")]
    LTsv_GTKcanvas_g=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetgc")]
    LTsv_GTKcanvas_gccolor=LTsv_GDKCOLOR()
    LTsv_canvas_bccolor=LTsv_GDKCOLOR()
    LTsv_GTKcanvas_font=""
    LTsv_drawGTK_color("")
    LTsv_drawGTK_bgcolor("")

LTsv_TkintercanvasPAGE,LTsv_Tkintercanvas_o,LTsv_Tkintercanvas_TAG,LTsv_Tkintercanvas_font=None,None,None,None
LTsv_TkintercanvasW,LTsv_TkintercanvasH=None,None
def LTsv_drawTkinter_selcanvas(LTsv_canvasPAGENAME,draw_g="LTsv_draw_tkTAG"):
    global LTsv_TkintercanvasPAGE,LTsv_Tkintercanvas_o,LTsv_Tkintercanvas_TAG
    global LTsv_TkintercanvasW,LTsv_TkintercanvasH
    LTsv_TkintercanvasPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_canvasPAGENAME)
    LTsv_GTKcanvasW=int(LTsv_readlinerest(LTsv_TkintercanvasPAGE,"widgetsizeW"))
    LTsv_GTKcanvasH=int(LTsv_readlinerest(LTsv_TkintercanvasPAGE,"widgetsizeH"))
    LTsv_Tkintercanvas_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_TkintercanvasPAGE,"widgetobj")]
    LTsv_Tkintercanvas_TAG=draw_g
    LTsv_Tkintercanvas_font=""
    LTsv_drawTkinter_color("")
    LTsv_drawTkinter_bgcolor("")

def LTsv_draw_selcanvas_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_selcanvas
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_selcanvas

def LTsv_drawGTK_delete(draw_c="white"):
    LTsv_drawGTK_color(draw_c)
    LTsv_drawGTK_bgcolor(draw_c)
    LTsv_libgdk.gdk_draw_rectangle(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,0,0,LTsv_GTKcanvasW,LTsv_GTKcanvasH)

def LTsv_drawTkinter_delete(draw_c="white"):
    LTsv_drawTkinter_color(draw_c)
    LTsv_drawTkinter_bgcolor(draw_c)
    LTsv_Tkintercanvas_o.delete(LTsv_Tkintercanvas_TAG)

def LTsv_draw_delete_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_delete
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_delete

def LTsv_drawGTK_color(draw_c=""):
    global LTsv_canvascolor,LTsv_canvasbgcolor
    LTsv_canvascolor=draw_c
    LTsv_libgdk.gdk_color_parse(draw_c.encode("utf-8"),ctypes.pointer(LTsv_GTKcanvas_gccolor))
    LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKcanvas_gccolor))

def LTsv_drawTkinter_color(draw_c=""):
    global LTsv_canvascolor,LTsv_canvasbgcolor
    LTsv_canvascolor=draw_c

def LTsv_draw_color_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_color
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_color

def LTsv_drawGTK_bgcolor(draw_c=""):
    global LTsv_canvascolor,LTsv_canvasbgcolor
    LTsv_canvasbgcolor=draw_c
    LTsv_libgdk.gdk_color_parse(draw_c.encode("utf-8"),ctypes.pointer(LTsv_canvas_bccolor))
    LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_canvas_bccolor))

def LTsv_drawTkinter_bgcolor(draw_c=""):
    global LTsv_canvascolor,LTsv_canvasbgcolor
    LTsv_canvasbgcolor=draw_c

def LTsv_draw_bgcolor_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_bgcolor
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_bgcolor

def LTsv_drawGTK_gcfcolor():
    LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKcanvas_gccolor))

def LTsv_drawGTK_gcbcolor():
    LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_canvas_bccolor))

def LTsv_drawGTK_polygon(*draw_xy):
    draw_xylen=len(draw_xy)//2; gdkpointsArrayType=LTsv_GDKPOINT*draw_xylen; gdkpointsArray=gdkpointsArrayType()
    for draw_xy_count,gdkpoint in enumerate(gdkpointsArray):
        gdkpoint.X,gdkpoint.Y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
    LTsv_libgdk.gdk_draw_polygon(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,ctypes.pointer(gdkpointsArray),draw_xylen)

def LTsv_drawTkinter_polygon(*draw_xy):
    xyloop=draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]
    if len(xyloop) > 0:
        LTsv_Tkintercanvas_o.create_polygon(*xyloop,fill="",outline=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_polygon_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_polygon
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_polygon

def LTsv_drawGTK_polygonfill(*draw_xy):
    draw_xylen=len(draw_xy)//2; gdkpointsArrayType=LTsv_GDKPOINT*draw_xylen; gdkpointsArray=gdkpointsArrayType()
    for draw_xy_count,gdkpoint in enumerate(gdkpointsArray):
        gdkpoint.X,gdkpoint.Y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
    LTsv_libgdk.gdk_draw_polygon(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,ctypes.pointer(gdkpointsArray),draw_xylen)

def LTsv_drawTkinter_polygonfill(*draw_xy):
    xyloop=draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]
    if len(xyloop) > 0:
#        LTsv_Tkintercanvas_o.create_polygon(*xyloop,fill=LTsv_canvascolor,outline=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)
        LTsv_Tkintercanvas_o.create_polygon(*xyloop,fill=LTsv_canvascolor,outline="",tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_polygonfill_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_polygonfill
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_polygonfill

def LTsv_drawTkinter_fontfill(*draw_xy):
    xyloop=draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]
    if len(xyloop) > 0:
        LTsv_Tkintercanvas_o.create_polygon(*xyloop,fill=LTsv_canvasbgcolor,outline=LTsv_canvasbgcolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_squares(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_rectangle(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh)

def LTsv_drawTkinter_squares(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_rectangle(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill="",outline=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_squares_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_squares
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_squares

def LTsv_drawGTK_squaresfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_rectangle(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh)

def LTsv_drawTkinter_squaresfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_rectangle(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill=LTsv_canvascolor,outline=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_squaresfill_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_squaresfill
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_squaresfill

def LTsv_drawGTK_circles(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh,0,LTsv_GDK_ARCFILL)

def LTsv_drawTkinter_circles(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_oval(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill="",outline=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_circles_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_circles
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_circles

def LTsv_drawGTK_circlesfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh,0,LTsv_GDK_ARCFILL)

def LTsv_drawTkinter_circlesfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_oval(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill=LTsv_canvascolor,outline=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_circlesfill_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_circlesfill
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_circlesfill

def LTsv_drawGTK_points(*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_point(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,draw_x,draw_y)

def LTsv_drawTkinter_points(*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_line(draw_x,draw_y,draw_x+1,draw_y+1,fill=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_points_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_points
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_points

def LTsv_drawGTK_arc(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,draw_x,draw_y,draw_w,draw_h,int(draw_s*LTsv_GDK_ARCFILL/2.0/math.pi),int(draw_e*LTsv_GDK_ARCFILL/2.0/math.pi))

def LTsv_drawTkinter_arc(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_Tkintercanvas_o.create_arc(draw_x,draw_y,draw_x+draw_w,draw_y+draw_h,fill="",outline=LTsv_canvascolor,start=draw_s*360.0/2.0/math.pi,extent=draw_e*360.0/2.0/math.pi,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_arc_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_arc
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_arc

def LTsv_drawGTK_arcfill(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,draw_x,draw_y,draw_w,draw_h,int(draw_s*LTsv_GDK_ARCFILL/2.0/math.pi),int(draw_e*LTsv_GDK_ARCFILL/2.0/math.pi))

def LTsv_drawTkinter_arcfill(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_Tkintercanvas_o.create_arc(draw_x,draw_y,draw_x+draw_w,draw_y+draw_h,fill=LTsv_canvascolor,outline=LTsv_canvascolor,start=draw_s*360.0/2.0/math.pi,extent=draw_e*360.0/2.0/math.pi,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_arcfill_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_arcfill
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_arcfill

def LTsv_drawGTK_font(draw_f=""):
    global LTsv_GTKcanvas_font
    LTsv_GTKcanvas_font=draw_f

def LTsv_drawTkinter_font(draw_f=None):
    global LTsv_Tkintercanvas_font
    LTsv_Tkintercanvas_font=LTsv_fonttuple(draw_f)

def LTsv_draw_font_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_font
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_font

def LTsv_drawGTK_text(draw_t="",draw_x=0,draw_y=0):
    pango_l=LTsv_libgtk.gtk_widget_create_pango_layout(LTsv_GTKcanvas_o,0)
    LTsv_libgtk.pango_layout_set_text(pango_l,draw_t.encode("utf-8","xmlcharrefreplace"),-1)
    LTsv_fontDesc=LTsv_libgtk.pango_font_description_from_string(LTsv_GTKcanvas_font.encode("utf-8"))
    LTsv_libgtk.pango_layout_set_font_description(pango_l,LTsv_fontDesc)
    LTsv_libgdk.gdk_draw_layout_with_colors(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,draw_x,draw_y,pango_l,ctypes.pointer(LTsv_GTKcanvas_gccolor),0)
    LTsv_libobj.g_object_unref(pango_l)
    LTsv_libgtk.pango_font_description_free(LTsv_fontDesc)

def LTsv_drawTkinter_text(draw_t="",draw_x=0,draw_y=0):
    LTsv_Tkintercanvas_o.create_text(draw_x,draw_y,text=draw_t,font=LTsv_Tkintercanvas_font,anchor="nw",fill=LTsv_canvascolor,tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_text_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_text
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_text

def LTsv_draw_picture_load(LTsv_picturepath):
    global LTsv_pictureOBJ,LTsv_pictureW,LTsv_pictureH
    if os.path.isfile(LTsv_picturepath):
        if LTsv_GUI == LTsv_GUI_GTK2:
            LTsv_pictureOBJ[LTsv_picturepath]=LTsv_libgdk.gdk_pixbuf_new_from_file(LTsv_picturepath.encode("utf-8","xmlcharrefreplace"),0)
            LTsv_pictureW[LTsv_picturepath]=LTsv_libgdk.gdk_pixbuf_get_width(LTsv_pictureOBJ[LTsv_picturepath])
            LTsv_pictureH[LTsv_picturepath]=LTsv_libgdk.gdk_pixbuf_get_height(LTsv_pictureOBJ[LTsv_picturepath])
        if LTsv_GUI == LTsv_GUI_Tkinter:
            LTsv_pictureOBJ[LTsv_picturepath]=Tk.PhotoImage(file=LTsv_picturepath)
            LTsv_pictureW[LTsv_picturepath]=LTsv_pictureOBJ[LTsv_picturepath].width()
            LTsv_pictureH[LTsv_picturepath]=LTsv_pictureOBJ[LTsv_picturepath].height()
    else:
        LTsv_pictureOBJ[LTsv_picturepath]=None
        LTsv_pictureW[LTsv_picturepath]=0
        LTsv_pictureH[LTsv_picturepath]=0
    return LTsv_pictureOBJ[LTsv_picturepath]

def LTsv_draw_picture_celldiv(LTsv_picturepath,picture_divw,picture_divh):
    global LTsv_pictureOBJ
    picture_divptr=""
    if not LTsv_picturepath in LTsv_pictureOBJ:
        LTsv_draw_picture_load(LTsv_picturepath)
    picture_o=LTsv_pictureOBJ[LTsv_picturepath]
    if picture_o != None:
        picture_divw,picture_divh=max(picture_divw,1),max(picture_divh,1)
        picture_w=LTsv_libgdk.gdk_pixbuf_get_width(picture_o);   cell_w=picture_w//picture_divw
        picture_h=LTsv_libgdk.gdk_pixbuf_get_height(picture_o);  cell_h=picture_h//picture_divh
        if picture_w%cell_w != 0: picture_divw=picture_divw-1
        if picture_h%cell_h != 0: picture_divh=picture_divh-1
        if LTsv_GUI == LTsv_GUI_GTK2:
            for picture_y in range(picture_divh):
                for picture_x in range(picture_divw):
                    picture_t="{0}[{1}]".format(LTsv_picturepath,picture_y*picture_divw+picture_x)
                    LTsv_pictureOBJ[picture_t]=LTsv_libgdk.gdk_pixbuf_new_subpixbuf(ctypes.c_char_p(picture_o),picture_x*cell_w,picture_y*cell_h,cell_w,cell_h)
                    LTsv_pictureW[picture_t]=LTsv_libgdk.gdk_pixbuf_get_width(LTsv_pictureOBJ[picture_t])
                    LTsv_pictureH[picture_t]=LTsv_libgdk.gdk_pixbuf_get_height(LTsv_pictureOBJ[picture_t])
        if LTsv_GUI == LTsv_GUI_Tkinter:
            pass

def LTsv_draw_picture_save(LTsv_pictureoldpath,LTsv_picturenewpath):
    global LTsv_pictureOBJ
    picture_o=LTsv_pictureOBJ[LTsv_pictureoldpath]
    if picture_o != None:
        if LTsv_GUI == LTsv_GUI_GTK2:
            LTsv_picturenewext=os.path.splitext(LTsv_picturenewpath)[1].lstrip('.').lower()
            if LTsv_picturenewext == "png":
                LTsv_libgdk.gdk_pixbuf_save(picture_o,LTsv_picturenewpath.encode("utf-8","xmlcharrefreplace"),"png".encode("utf-8"),None,"compression".encode("utf-8"),"9".encode("utf-8"),None)
            elif LTsv_picturenewext == "ico":
                LTsv_libgdk.gdk_pixbuf_save(picture_o,LTsv_picturenewpath.encode("utf-8","xmlcharrefreplace"),"ico".encode("utf-8"),None,"depth".encode("utf-8"),"16".encode("utf-8"),None)
            else:
                LTsv_libgdk.gdk_pixbuf_save(picture_o,LTsv_picturenewpath.encode("utf-8","xmlcharrefreplace"),LTsv_picturenewext.encode("utf-8"),None)

def LTsv_draw_canvas_save(LTsv_canvasPAGENAME,LTsv_picturenewpath):
    global LTsv_widgetLTSV
    LTsv_canvasPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_canvasPAGENAME)
    canvas_w=int(LTsv_readlinerest(LTsv_canvasPAGE,"widgetsizeW"))
    canvas_h=int(LTsv_readlinerest(LTsv_canvasPAGE,"widgetsizeH"))
    LTsv_picturenewext=os.path.splitext(LTsv_picturenewpath)[1].lstrip('.').lower()
    if LTsv_GUI == LTsv_GUI_GTK2:
        canvas_m=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_canvasPAGE,"widgetpixmap")]
        canvas_d=LTsv_libgdk.gdk_pixbuf_get_from_drawable(0,canvas_m,LTsv_libgdk.gdk_colormap_get_system(),0,0,0,0,canvas_w,canvas_h)
        if LTsv_picturenewext == "png":
            LTsv_libgdk.gdk_pixbuf_save(canvas_d,LTsv_picturenewpath.encode("utf-8","xmlcharrefreplace"),"png".encode("utf-8"),None,"compression".encode("utf-8"),"9".encode("utf-8"),None)
        else:
            LTsv_libgdk.gdk_pixbuf_save(canvas_d,LTsv_picturenewpath.encode("utf-8","xmlcharrefreplace"),LTsv_picturenewext.encode("utf-8"),None)
        LTsv_libobj.g_object_unref(canvas_d)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        canvas_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_canvasPAGE,"widgetobj")]
#        canvas_d=Image.new("RGB",(canvas_w,canvas_h),(255,255,255))
#        canvas_d.paste(canvas_o,(0,0))
#        canvas_d.save(fileName,returnFormat(LTsv_picturenewext))

def LTsv_drawGTK_picture(draw_t="",draw_x=0,draw_y=0):
    picture_o,picture_w,picture_h=LTsv_pictureOBJ[draw_t],LTsv_pictureW[draw_t],LTsv_pictureH[draw_t]
    LTsv_libgdk.gdk_draw_pixbuf(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,picture_o,0,0,draw_x,draw_y,picture_w,picture_h,0,0,0)

def LTsv_drawTkinter_picture(draw_t="",draw_x=0,draw_y=0):
    picture_o,picture_w,picture_h=LTsv_pictureOBJ[draw_t],LTsv_pictureW[draw_t],LTsv_pictureH[draw_t]
    LTsv_Tkintercanvas_o.create_image(draw_x,draw_y,image=picture_o,anchor="nw",tag=LTsv_Tkintercanvas_TAG)

def LTsv_draw_picture_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_picture
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_picture

def LTsv_drawGTK_queue():
    global LTsv_GTKcanvas_o
    LTsv_libgtk.gtk_widget_queue_draw(LTsv_GTKcanvas_o)

def LTsv_drawTkinter_queue():
    pass

def LTsv_draw_queue_shell(LTsv_GUI):
    if LTsv_GUI == LTsv_GUI_GTK2: return LTsv_drawGTK_queue
    if LTsv_GUI == LTsv_GUI_Tkinter: return LTsv_drawTkinter_queue

def LTsv_clockwise(*draw_xy):
    clockwise=0
    if len(draw_xy) >= 6:
        xyloop=draw_xy+draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]+draw_xy[:-1]
        for draw_xy_count in range(0,len(draw_xy),2):
            Px,Py,Cx,Cy,Qx,Qy=range(draw_xy_count,draw_xy_count+6)
            PCQ=(xyloop[Px]-xyloop[Cx])*(xyloop[Qy]-xyloop[Cy])-(xyloop[Py]-xyloop[Cy])*(xyloop[Qx]-xyloop[Cx])
            clockwise=clockwise+1 if PCQ < 0 else clockwise-1 if PCQ > 0 else clockwise
    return clockwise


LTsv_WM_TRAYEVENTSTART=0x900
LTsv_ICON_NIM_ADD   =0x0000
LTsv_ICON_NIM_MODIFY=0x0001
LTsv_ICON_NIM_DELETE=0x0002
class LTsv_EXTRACTICON(ctypes.Structure):
    _fields_ = [
        ('phIcon',ctypes.c_uint*1)
    ]
class LTsv_NOTIFYICONDATAUNION(ctypes.Structure):
    _fields_ = [
        ('uTimeout',ctypes.c_uint),
        ('uVersion',ctypes.c_uint)
    ]
class LTsv_GUID(ctypes.Structure):
    _fields_ = [
        ('Data1',ctypes.c_ulong),
        ('Data2',ctypes.c_ushort),
        ('Data3',ctypes.c_ushort),
        ('Data4',ctypes.c_ubyte*8)
    ]
class LTsv_NOTIFYICONDATA(ctypes.Structure):
    _fields_ = [
        ('cbSize',          ctypes.c_ulong),
        ('hWnd',            ctypes.c_void_p),
        ('uID',             ctypes.c_uint),
        ('uFlags',          ctypes.c_uint),
        ('uCallbackMessage',ctypes.c_uint),
        ('hIcon',           ctypes.c_void_p),
        ('szTip',           ctypes.c_char*64),
        ('dwState',         ctypes.c_ulong),
        ('dwStateMask',     ctypes.c_ulong),
        ('szInfo',          ctypes.c_char*256),
        ('union',           LTsv_NOTIFYICONDATAUNION),
        ('szInfoTitle',     ctypes.c_char* 64),
        ('dwInfoFlags',     ctypes.c_ulong),
        ('guidItem',        LTsv_GUID)
    ]
    def __init__(self):
        self.cbSize=ctypes.sizeof(self)
        self.uFlags=7
        self.uCallbackMessage=LTsv_WM_TRAYEVENTSTART
def LTsv_icon_load(LTsv_picturepath):
    global LTsv_iconOBJ
    if os.path.isfile(LTsv_picturepath):
        if LTsv_Notify == LTsv_GUI_GTK2:
            pass
        if LTsv_Notify == LTsv_GUI_WinAPI:
            LTsv_phIconSmall,LTsv_phIconLarge=0,0
            LTsv_EXEICON=LTsv_EXTRACTICON()
            LTsv_Icons=LTsv_shell32.ExtractIconEx(LTsv_picturepath.encode(sys.stdout.encoding,"xmlcharrefreplace"),-1,0,0,0)
            if LTsv_Icons > 0:
                LTsv_shell32.ExtractIconEx(LTsv_picturepath.encode(sys.stdout.encoding,"xmlcharrefreplace"),0,LTsv_phIconLarge,ctypes.pointer(LTsv_EXEICON),1)
                LTsv_iconOBJ[LTsv_picturepath]=LTsv_EXEICON.phIcon[0]
                for icon_n in range(LTsv_Icons):
                    LTsv_shell32.ExtractIconEx(LTsv_picturepath.encode(sys.stdout.encoding,"xmlcharrefreplace"),icon_n,LTsv_phIconLarge,ctypes.pointer(LTsv_EXEICON),1)
                    LTsv_iconOBJ["{0}[{1}]".format(LTsv_picturepath,icon_n)]=LTsv_EXEICON.phIcon[0]
    return LTsv_Icons

def LTsv_notifyicon_new(LTsv_windowPAGENAME,notify_n=None,widget_t="",widget_u="",menu_b=None,menu_c=None):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(notify_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="notify")
    iconuri=widget_u
    if LTsv_GUI == LTsv_GUI_GTK2:
        picture_o=LTsv_pictureOBJ[iconuri] if iconuri in LTsv_pictureOBJ else None
        if picture_o == None:
            iconuri=LTsv_default_iconuri
            LTsv_draw_picture_load(iconuri)
            picture_o=LTsv_pictureOBJ[iconuri]
        widget_o=LTsv_libgtk.gtk_status_icon_new_from_pixbuf(picture_o)
        LTsv_libgtk.gtk_status_icon_set_tooltip(widget_o,widget_t.encode("utf-8"))
        menu_o=LTsv_libgtk.gtk_menu_new()
        LTsv_notify_popupmenu_cbk=LTsv_CALLBACLTYPE(menu_c) if menu_c != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"popup-menu".encode("utf-8"),LTsv_notify_popupmenu_cbk,0,0,0)
        def LTsv_notifyicon_defmenu_yield():
            yield ("window exit",LTsv_window_exit_cbk)
            yield ("-----------",None)
            yield ("notify click",LTsv_notify_popupmenu_cbk)
        LTsv_notifyicon_menu_yield=menu_b if menu_b != None else LTsv_notifyicon_defmenu_yield()
        for LTsv_popup_count,LTsv_popup_menu in enumerate(LTsv_notifyicon_menu_yield):
            if LTsv_popup_menu[0]=="" or LTsv_popup_menu[1] == None:
                LTsv_popup_menu_label=LTsv_libgtk.gtk_separator_menu_item_new()
                LTsv_libgtk.gtk_menu_shell_append(menu_o,LTsv_popup_menu_label)
            else:
                LTsv_popup_menu_label=LTsv_libgtk.gtk_menu_item_new_with_label(LTsv_popup_menu[0].encode("utf-8","xmlcharrefreplace"))
                LTsv_libgtk.gtk_menu_shell_append(menu_o,LTsv_popup_menu_label)
                LTsv_libobj.g_signal_connect_data(LTsv_popup_menu_label,"activate".encode("utf-8"),LTsv_popup_menu[1],LTsv_popup_count,0,0)
        def LTsv_notifyicon_activate(window_objvoid=None,window_objptr=None):
            LTsv_libgtk.gtk_widget_show_all(menu_o)
            LTsv_libgtk.gtk_menu_popup(menu_o,0,0,LTsv_libgtk.gtk_status_icon_position_menu,widget_o,0,0)
            LTsv_widget_showhide(LTsv_windowPAGENAME,True)
        LTsv_notify_activate_cbk=LTsv_CALLBACLTYPE(LTsv_notifyicon_activate)
        LTsv_libobj.g_signal_connect_data(widget_o,"activate".encode("utf-8"),LTsv_notify_activate_cbk,-1,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_u=iconuri,event_a=LTsv_notify_activate_cbk,event_u=LTsv_notify_popupmenu_cbk,menu_o=menu_o,menu_b=LTsv_notifyicon_menu_yield,menu_c=menu_c)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        icon_o=LTsv_iconOBJ[iconuri] if iconuri in LTsv_iconOBJ else None
        if icon_o == None:
            iconuri=LTsv_default_iconuri
            LTsv_icon_load(sys.executable)
            icon_o=LTsv_iconOBJ[iconuri]
        if LTsv_widgetPAGENAME not in LTsv_iconOBJnotify:
            LTsv_iconOBJnotify.append(LTsv_widgetPAGENAME)
        widget_o=LTsv_NOTIFYICONDATA()
        widget_o.hWnd=int(window_o.frame(),16)
        widget_o.hIcon=icon_o
        widget_o.uID=LTsv_iconOBJnotify.index(LTsv_widgetPAGENAME)
        widget_o.szTip=widget_t[:64].encode("utf-8")
        LTsv_shell32.Shell_NotifyIcon(ctypes.c_ulong(LTsv_ICON_NIM_ADD),ctypes.pointer(widget_o))
        def LTsv_notifyicon_activate(window_objvoid=None,window_objptr=None):
            LTsv_widget_showhide(LTsv_windowPAGENAME,True)
#       window_o.protocol("WM_TRAYEVENTSTART",LTsv_notifyicon_activate)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,widget_u=iconuri)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

LTsv_GTK_RESPONSE_ACCEPT=      -3
LTsv_GTK_RESPONSE_APPLY=       -10
LTsv_GTK_RESPONSE_CANCEL=      -6
LTsv_GTK_RESPONSE_CLOSE=       -7
LTsv_GTK_RESPONSE_DELETE_EVENT=-4
LTsv_GTK_RESPONSE_HELP=        -11
LTsv_GTK_RESPONSE_NO=          -9
LTsv_GTK_RESPONSE_OK=          -5
LTsv_GTK_RESPONSE_YES=         -8
def LTsv_filedialog_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_t="LTsv_filedialog",dialog_t=0):
    global LTsv_widgetLTSV
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="filedialog")
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_dialogtype=max(dialog_t,0)%4
        LTsv_dialogtypename=["fileopen","filesave","diropen","dirsave"]
        widget_w,widget_h=LTsv_screen_w(LTsv_windowPAGENAME)//2,LTsv_screen_h(LTsv_windowPAGENAME)//2
        widget_o=LTsv_libgtk.gtk_file_chooser_dialog_new(widget_t.encode("utf-8","xmlcharrefreplace"),0,LTsv_dialogtype,"gtk-cancel".encode("utf-8"),LTsv_GTK_RESPONSE_CANCEL,LTsv_dialogtypename[LTsv_dialogtype].encode("utf-8","xmlcharrefreplace"),LTsv_GTK_RESPONSE_ACCEPT,0)
        LTsv_libgtk.gtk_widget_set_size_request(widget_o,widget_w,widget_h)
        LTsv_libgtk.gtk_window_set_resizable(widget_o,True)
        LTsv_libgtk.gtk_window_set_position(window_o,LTsv_GTK_WIN_POS_CENTER)
        event_r_cbk=LTsv_CALLBACLTYPE(event_b) if event_b != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"response".encode("utf-8"),event_r_cbk,0,0,0)
        event_c_cbk=LTsv_libgtk.gtk_widget_hide_on_delete
        LTsv_libobj.g_signal_connect_data(widget_o,"delete-event".encode("utf-8"),event_c_cbk,0,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,dialog_t=dialog_t,dialog_c=event_c_cbk,event_b=event_r_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_dialogtype=max(dialog_t,0)%4
        def LTsv_filedialog_askopen(window_objvoid=None,window_objptr=None):
            global LTsv_widgetLTSV
            LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
            widget_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetobj")]
            widget_k=LTsv_readlinerest(LTsv_widgetPAGE,"widgetkind")
            if widget_k == "filedialog":
                dialog_t=int(LTsv_readlinerest(LTsv_widgetPAGE,"dialog_type"))
                print(dialog_t)
                if dialog_t == 0:
                    widget_u=Tk_fd.askopenfilename()
                if dialog_t == 1:
                    widget_u=Tk_fd.asksaveasfile()
                if dialog_t == 2:
                    widget_u=Tk_fd.askdirectory()
                if dialog_t == 3:
                    widget_u=Tk_fd.asksaveasdirectory()
                LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_u=widget_u)
                LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
                LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"widgetcallback")]()
        widget_o=LTsv_filedialog_askopen
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=widget_o,widget_t=widget_t,dialog_t=LTsv_dialogtype,event_b=event_b)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME


def debug_canvas(window_objvoid=None,window_objptr=None):
    global debug_scaleRGB
    LTsv_draw_selcanvas(debug_keysetup_canvas)
    LTsv_draw_delete("white")
    LTsv_draw_font(debug_font_entry)
    LTsv_draw_color("#fffff0"); LTsv_draw_polygonfill(0,0,debug_canvas_W,0,debug_canvas_W,debug_canvas_H,0,debug_canvas_H)
    mouse_x,mouse_y=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    LTsv_draw_color(debug_scaleRGB); LTsv_draw_text("mouseX,Y\n[{0},{1}]".format(mouse_x,mouse_y),draw_x=mouse_x,draw_y=mouse_y)
    LTsv_putdaytimenow(); LTsv_checkFPS()
    LTsv_draw_color("black"); LTsv_draw_text(LTsv_getdaytimestr(LTsv_widget_gettext(debug_keysetup_timentry)),draw_x=0,draw_y=0)
    LTsv_setkbddata(25,25)
    kbdlabels=LTsv_getkbdlabels().replace('\t',' ').replace('た','\nた').replace('ち','\nち').replace('つ','\nつ').replace('NFER','\nNFER')
    if LTsv_joymax > 0:
        LTsv_setjoydata(0); pad_axis=LTsv_readlinerest(LTsv_getjoystr(0),LTsv_joyaxis_label())
    for pad_xy,pad_circle in enumerate([LTsv_draw_squares,LTsv_draw_circles,LTsv_draw_circles]):
        pad_x,pad_y=debug_joypad_X+pad_xy*debug_joypad_W,debug_joypad_Y
        pad_circle(debug_joypad_W,*(pad_x,pad_y))
        LTsv_draw_points(pad_x,pad_y)
        if LTsv_joymax > 0:
            stick_w=int(LTsv_pickdatalabel(pad_axis,debug_padxkey[pad_xy]))
            stick_h=int(LTsv_pickdatalabel(pad_axis,debug_padykey[pad_xy]))
            stick_t=math.atan2(stick_w,stick_h)
            stick_s=LTsv_atanscalar(stick_w,stick_h)
            LTsv_draw_polygon(*(pad_x,pad_y,pad_x+int(math.sin(stick_t)*stick_s*debug_joypad_W/2/LTsv_WINJOYCENTER),pad_y+int(math.cos(stick_t)*stick_s*debug_joypad_W/2/LTsv_WINJOYCENTER)))
            LTsv_draw_text("{0},{1}\n{2},{3}\nθ{4}\n∇{5}".format(debug_padxkey[pad_xy],debug_padykey[pad_xy],LTsv_pickdatalabel(pad_axis,debug_padxkey[pad_xy]),LTsv_pickdatalabel(pad_axis,debug_padykey[pad_xy]),stick_t,stick_s),draw_x=pad_x+3,draw_y=pad_y+3)
        else:
            LTsv_draw_text("{0},{1}".format(debug_padxkey[pad_xy],debug_padykey[pad_xy]),draw_x=pad_x+3,draw_y=pad_y+3)
    debug_arc_W=debug_joypad_X+int(debug_joypad_W*2.5)
    LTsv_draw_arc(debug_arc_W,debug_joypad_Y-debug_joypad_W//2,debug_canvas_W-debug_arc_W-2,debug_joypad_W,-math.pi*0.5,math.pi*1.8)
    txt_x,txt_y=500,debug_joypad_Y+debug_joypad_H//2
    if LTsv_joymax > 0:
        LTsv_draw_text(LTsv_getjoystr(0).replace('\t',' '),draw_x=0,draw_y=txt_y)
    LTsv_draw_text(kbdlabels,draw_x=0,draw_y=txt_y+debug_label_WH*3)
    LTsv_draw_text("getkbdnames:{0}".format(LTsv_getkbdnames()),draw_x=txt_x,draw_y=txt_y+debug_label_WH*1)
    LTsv_draw_text("getkbdcodes:{0}".format(LTsv_getkbdcodes()),draw_x=txt_x,draw_y=txt_y+debug_label_WH*2)
    LTsv_draw_text("getkbdkanas:{0}".format(LTsv_getkbdkanas()),draw_x=txt_x,draw_y=txt_y+debug_label_WH*3)
    LTsv_draw_text("debug_keyevent:\n{0}".format(debug_keyevent),draw_x=txt_x,draw_y=txt_y+debug_label_WH*5)
    LTsv_draw_color(debug_scaleRGB)
    LTsv_draw_polygon(*tuple(debug_polygonpointlist))
    if LTsv10_logoOBJ:
        LTsv_draw_picture(LTsv10_logoPATH,debug_arc_W+LTsv_global_pictureW(LTsv10_logoPATH),debug_joypad_Y-LTsv_global_pictureH(LTsv10_logoPATH)//2)
    LTsv_draw_queue()
    LTsv_window_after(debug_keysetup_window,event_b=debug_canvas,event_i="debug_canvas",event_w=50)

def debug_timebutton(callback_void=None,callback_ptr=None):
    LTsv_widget_settext(debug_keysetup_timentry,widget_t=debug_timentry_default)

def debug_calc(callback_void=None,callback_ptr=None):
    calc_value=LTsv_widget_gettext(debug_keysetup_calcentry)
    if not calc_value.endswith('⇔'):
        calc_value+='⇔'
    calc_Q=calc_value[:calc_value.find('⇔')]
    calc_A=LTsv_calc(calc_Q)
    LTsv_widget_settext(debug_keysetup_calcentry,calc_Q+'⇔'+calc_A)

def debug_polygonpoints(callback_void=None,callback_ptr=None):
    global debug_polygonpointlist
    polygonpoints=LTsv_widget_gettext(debug_keysetup_polygonentry).strip("[]").replace(" ","").split(',')
    debug_polygonpointlist=map(LTsv_intstr0x,polygonpoints)
    if len(debug_polygonpointlist)%2 == 1:
        debug_polygonpointlist.pop()
    LTsv_widget_settext(debug_keysetup_polygonentry,widget_t="{0}".format(debug_polygonpointlist))

def debug_activewindow(callback_void=None,callback_ptr=None):
    LTsv_widget_settext(debug_keysetup_activelabel,widget_t=LTsv_window_foreground())
    LTsv_window_after(debug_keysetup_window,event_b=debug_activewindow,event_i="debug_activewindow",event_w=500)

def debug_canvas_press(callback_void=None,callback_ptr=None):
    global debug_polygonpointlist
    mouse_x,mouse_y=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    LTsv_setkbddata(0,25); debug_getkbdstr=LTsv_getkbdlabels("MouseL\tMouseR\tMouseC")
    cursorLCR="{0}{1}{2}".format(LTsv_pickdatalabel(debug_getkbdstr,"MouseL"),LTsv_pickdatalabel(debug_getkbdstr,"MouseC"),LTsv_pickdatalabel(debug_getkbdstr,"MouseR"))
    if cursorLCR == "100" or cursorLCR == "000":
        debug_polygonpointlist+=[mouse_x]; debug_polygonpointlist+=[mouse_y]
    if cursorLCR == "001" or cursorLCR == "010":
        debug_polygonbutton()
    LTsv_widget_settext(debug_keysetup_polygonentry,widget_t="{0}".format(debug_polygonpointlist))
    LTsv_widget_focus(debug_keysetup_polygonentry)

def debug_polygonbutton(callback_void=None,callback_ptr=None):
    global debug_polygonpointlist
    if len(debug_polygonpointlist) >= 2:
        debug_polygonpointlist.pop(); debug_polygonpointlist.pop()
    LTsv_widget_settext(debug_keysetup_polygonentry,widget_t="{0}".format(debug_polygonpointlist))

def debug_color_scale(window_objvoid=None,window_objptr=None):
    global debug_scaleRGB
    scaleR,scaleG,scaleB=hex(LTsv_widget_getnumber(debug_keysetup_scaleR)).replace("0x",""),hex(LTsv_widget_getnumber(debug_keysetup_scaleG)).replace("0x",""),hex(LTsv_widget_getnumber(debug_keysetup_scaleB)).replace("0x","")
    scaleR,scaleG,scaleB=scaleR if len(scaleR) == 2 else "0"+scaleR,scaleG if len(scaleG) == 2 else "0"+scaleG,scaleB if len(scaleB) == 2 else "0"+scaleB
    debug_scaleRGB="#{0}{1}{2}".format(scaleR,scaleG,scaleB)

def debug_color_combo(window_objvoid=None,window_objptr=None):
    global debug_scaleRGB
    if LTsv_widget_gettext(debug_keysetup_combobox) in debug_colordic:
        scaleR,scaleG,scaleB=debug_colordic[LTsv_widget_gettext(debug_keysetup_combobox)]
        LTsv_widget_setnumber(debug_keysetup_scaleR,scaleR)
        LTsv_widget_setnumber(debug_keysetup_scaleG,scaleG)
        LTsv_widget_setnumber(debug_keysetup_scaleB,scaleB)

def debug_edit_clip(window_objvoid=None,window_objptr=None):
    edit_clip=LTsv_widget_gettext(debug_edit)
    LTsv_libc_printf("edit_clip={0}".format(edit_clip))
    LTsv_widget_settext(debug_clipboard,widget_t=edit_clip)

debug_check=[""]*3
def debug_checkbutton_shell(checkNumber):
    def debug_checkbutton_kernel(window_objvoid=None,window_objptr=None):
        LTsv_widget_settext(debug_edit,widget_t="{0}:{1}\n".format(LTsv_widget_gettext(debug_check[checkNumber]),LTsv_widget_getnumber(debug_check[checkNumber])))
    return debug_checkbutton_kernel

debug_radio=[""]*3
def debug_radiobutton_shell(radioNumber):
    def debug_radiobutton_kernel(window_objvoid=None,window_objptr=None):
#        LTsv_libc_printf("{0}".format(LTsv_widget_gettext(debug_radio[radioNumber])))
        LTsv_widget_settext(debug_edit,widget_t="{0}:{1}\n".format(LTsv_widget_gettext(debug_radio[radioNumber]),LTsv_widget_getnumber(debug_radio[radioNumber])))
    return debug_radiobutton_kernel

#class LTsv_GdkEventKey(ctypes.Structure):
#    _fields_ = [
#        ('type',ctypes.c_int),
#        ('window',ctypes.c_void_p),
#        ('send_event',ctypes.c_ubyte),
#        ('time',ctypes.c_uint),
#        ('state',ctypes.c_uint),
#        ('keyval',ctypes.c_uint),
#    ]
debug_keyevent=""
def debug_keypress(window_objvoid=None,window_objptr=None):
    global debug_keyevent
    if LTsv_GUI == LTsv_GUI_GTK2:
        print("debug_keypress",window_objvoid,window_objptr)
#        window_objptr.restype = ctypes.POINTER(LTsv_GdkEventKey)
        debug_keyevent="debug_keypress"
    if LTsv_GUI == LTsv_GUI_Tkinter:
        debug_keyevent+="\t{0}".format(window_objvoid.char)
def debug_keyrelease(window_objvoid=None,window_objptr=None):
    global debug_keyevent
    if LTsv_GUI == LTsv_GUI_GTK2:
        print("debug_keyrelease",window_objvoid,window_objptr)
        debug_keyevent="debug_keyrelease"
    if LTsv_GUI == LTsv_GUI_Tkinter:
        debug_keyevent=debug_keyevent.replace("\t{0}".format(window_objvoid.char),"")

def debug_filedialog(window_objvoid=None,window_objptr=None):
    LTsv_widget_settext(debug_filedialogwindow,"")
    LTsv_widget_showhide(debug_filedialogwindow,True)

#LTsv_GTK_RESPONSE_ACCEPT
def debug_filedialog_response(window_objvoid=None,window_objptr=None):
    filedialog_filename=LTsv_widget_geturi(debug_filedialogwindow)
    LTsv_widget_showhide(debug_filedialogwindow,False)
    LTsv_widget_settext(debug_edit,widget_t=filedialog_filename)


if __name__=="__main__":
    from LTsv_printf import *
    from LTsv_file   import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
#    LTsv_GUI=LTsv_guiinit(LTsv_GUI_Tkinter)
    if len(LTsv_GUI) > 0:
        import math
        from LTsv_joy    import *
        from LTsv_calc   import *
        from LTsv_kbd    import *
        LTsv_kbdinit("./LTsv_kbd.tsv",LTsv_initmouse=False)
        LTsv_joymax=LTsv_joyinit()
        debug_fontname="kan5x5comic"
        debug_fontsize_entry=10; debug_font_entry="{0},{1}".format(debug_fontname,debug_fontsize_entry); debug_label_WH=debug_fontsize_entry*2
        debug_keysetup_W,debug_keysetup_H=800,600
        debug_canvas_X,debug_canvas_Y,debug_canvas_W,debug_canvas_H=0,debug_label_WH,debug_keysetup_W-120,debug_keysetup_H*3//5
        debug_combobox_X,debug_combobox_Y,debug_combobox_W,debug_combobox_H=debug_canvas_W,debug_canvas_Y,debug_keysetup_W-debug_canvas_W,debug_label_WH*2
        debug_scale_X,debug_scale_Y,debug_scale_W,debug_scale_H=debug_canvas_W,debug_canvas_Y+debug_combobox_H,debug_keysetup_W-debug_canvas_W,debug_canvas_H-debug_combobox_H
        debug_joypad_X,debug_joypad_Y,debug_joypad_W,debug_joypad_H=debug_canvas_W//6,debug_canvas_H*1//4+debug_label_WH*2,debug_canvas_H*2//4,debug_canvas_H*2//4
        debug_padxkey,debug_padykey=["Px","Lx","Rx"],["Py","Ly","Ry"]
        debug_keyspin_X,debug_keyspin_Y,debug_keyspin_W,debug_keyspin_H=0,debug_keysetup_H-debug_label_WH*9,debug_keysetup_W//14,debug_label_WH
        debug_keysetup_window=LTsv_window_new(widget_t="L:Tsv GUI test and KeyCode Setup",event_b=LTsv_window_exit,widget_w=debug_keysetup_W,widget_h=debug_keysetup_H,event_z=None,event_k=debug_keypress,event_y=debug_keyrelease)
        debug_timentry_default="@000y年-@0m月(@0wnyi/@ywi週)-@0dm日(@wdj曜)@0h:@0n:@0s FPS:@0fpc"
        debug_keysetup_timentry=LTsv_entry_new(debug_keysetup_window,widget_t="",widget_x=0,widget_y=0,widget_w=debug_keysetup_W-debug_keyspin_W*1,widget_h=debug_label_WH,widget_f=debug_font_entry)
        debug_keysetup_timebutton=LTsv_button_new(debug_keysetup_window,widget_t="reset",widget_x=debug_keysetup_W-debug_keyspin_W*1,widget_y=0,widget_w=debug_keyspin_W*1,widget_h=debug_label_WH,widget_f=debug_font_entry,event_b=debug_timebutton)
        debug_keysetup_canvas=LTsv_canvas_new(debug_keysetup_window,widget_x=debug_canvas_X,widget_y=debug_canvas_Y,widget_w=debug_canvas_W,widget_h=debug_canvas_H,event_w=50,event_p=debug_canvas_press)
        LTsv10_logoPATH="../icon_cap/LTsv10_logo.png"; LTsv10_logoOBJ=LTsv_draw_picture_load(LTsv10_logoPATH)
        debug_polygonpointlist=[556, 12, 566, 31, 583, 33, 574, 47, 581, 63, 561, 55, 537, 60, 547, 42, 529, 32, 552, 28]
        debug_keysetup_scaleR=LTsv_scale_new(debug_keysetup_window,widget_x=debug_scale_X+debug_scale_W*0//3,widget_y=debug_scale_Y,widget_w=debug_scale_W//3,widget_h=debug_scale_H,widget_s=0,widget_e=255,widget_a=1,event_b=debug_color_scale)
        debug_keysetup_scaleG=LTsv_scale_new(debug_keysetup_window,widget_x=debug_scale_X+debug_scale_W*1//3,widget_y=debug_scale_Y,widget_w=debug_scale_W//3,widget_h=debug_scale_H,widget_s=0,widget_e=255,widget_a=1,event_b=debug_color_scale)
        debug_keysetup_scaleB=LTsv_scale_new(debug_keysetup_window,widget_x=debug_scale_X+debug_scale_W*2//3,widget_y=debug_scale_Y,widget_w=debug_scale_W//3,widget_h=debug_scale_H,widget_s=0,widget_e=255,widget_a=1,event_b=debug_color_scale)
        debug_scaleRGB=""
        debug_keysetup_calcentry=LTsv_entry_new(debug_keysetup_window,widget_t="2/3⇔2|3",widget_x=0,widget_y=debug_canvas_Y+debug_canvas_H,widget_w=(debug_keysetup_W-debug_scale_W)*2//3,widget_h=debug_label_WH,widget_f=debug_font_entry,event_b=debug_calc)
        debug_keysetup_polygonentry=LTsv_entry_new(debug_keysetup_window,widget_t="{0}".format(debug_polygonpointlist),widget_x=(debug_keysetup_W-debug_scale_W)*2//3,widget_y=debug_canvas_Y+debug_canvas_H,widget_w=(debug_keysetup_W-debug_scale_W)*1//3-debug_keyspin_W,widget_h=debug_label_WH,widget_f=debug_font_entry,event_b=debug_polygonpoints)
        debug_keysetup_polygonbutton=LTsv_button_new(debug_keysetup_window,widget_t="del",widget_x=debug_scale_X-debug_keyspin_W,widget_y=debug_canvas_Y+debug_canvas_H,widget_w=debug_keyspin_W,widget_h=debug_label_WH,widget_f=debug_font_entry,event_b=debug_polygonbutton)
        debug_keysetup_activelabel=LTsv_label_new(debug_keysetup_window,widget_t="0x--------",widget_x=debug_keysetup_W-debug_scale_W,widget_y=debug_canvas_Y+debug_canvas_H,widget_w=debug_scale_W,widget_h=debug_label_WH,widget_f=debug_font_entry)
        debug_keysetup_keys=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ",
                               "た","て","い","す","か","ん","な","に","ら","せ","゛","゜",
                                 "ち","と","し","は","き","く","ま","の","り","れ","け","む",
                                   "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥",
                                     "NFER","　","XFER","KANA"]
        debug_keysetup_spin,debug_keysetup_label=[None]*len(debug_keysetup_keys),[None]*len(debug_keysetup_keys)
        for debug_kbdxy,debug_kbdlabel in enumerate(debug_keysetup_keys):
            debug_kbdx,debug_kbd_y=(debug_kbdxy%12*debug_keyspin_W if debug_kbdlabel != "￥" else debug_keyspin_W*10+debug_keyspin_W//2),(debug_kbdxy//12*debug_keyspin_H*2 if debug_kbdlabel != "￥" else 0); debug_kbdx+=(debug_keyspin_W//2)*(debug_kbdxy//12+1 if debug_kbdxy < 48 else 9 if debug_kbdxy < 50 else 12)
            debug_keysetup_spin[debug_kbdxy]=LTsv_spin_new(debug_keysetup_window,widget_x=debug_keyspin_X+debug_kbdx,widget_y=debug_keyspin_Y+debug_kbd_y,widget_w=debug_keyspin_W if debug_kbdlabel != "　" else debug_keyspin_W*3,widget_h=debug_keyspin_H,widget_s=1,widget_e=255,widget_a=1,widget_f=debug_font_entry)
            LTsv_widget_setnumber(debug_keysetup_spin[debug_kbdxy],LTsv_kbdgettypegana(debug_kbdlabel))
            LTsv_widget_disableenable(debug_keysetup_spin[debug_kbdxy],False)
            debug_kbdcodename="「{0}」({1})".format(debug_kbdlabel,LTsv_kbdgettypename(LTsv_kbdgettypegana(debug_kbdlabel))) if debug_kbdlabel != "NFER" and debug_kbdlabel != "NFER" and debug_kbdlabel != "XFER" and debug_kbdlabel != "KANA" else "「{0}」".format(debug_kbdlabel)
            debug_keysetup_label[debug_kbdxy]=LTsv_label_new(debug_keysetup_window,widget_t=debug_kbdcodename,widget_x=debug_keyspin_X+debug_kbdx,widget_y=debug_keyspin_Y+debug_kbd_y-debug_keyspin_H,widget_w=debug_keyspin_W if debug_kbdlabel != "　" else debug_keyspin_W*3,widget_h=debug_keyspin_H,widget_f=debug_font_entry)
        debug_edit=LTsv_edit_new(debug_keysetup_window,widget_t="",widget_x=0,widget_y=debug_keysetup_H-debug_keyspin_H*4,widget_w=debug_keyspin_W*2,widget_h=debug_keyspin_H*4,widget_f=debug_font_entry)
        debug_clipboard=LTsv_clipboard_new(debug_keysetup_window)
        debug_clipbutton=LTsv_button_new(debug_keysetup_window,widget_t="clip",widget_x=0,widget_y=debug_keysetup_H-debug_keyspin_H*5,widget_w=debug_keyspin_W*1,widget_h=debug_keyspin_H*1,widget_f=debug_font_entry,event_b=debug_edit_clip)
        debug_filedialogbutton=LTsv_button_new(debug_keysetup_window,widget_t="open",widget_x=debug_keyspin_W*2,widget_y=debug_keysetup_H-debug_keyspin_H*1,widget_w=debug_keyspin_W*1,widget_h=debug_keyspin_H*1,widget_f=debug_font_entry,event_b=debug_filedialog)
        debug_filedialogwindow=LTsv_filedialog_new(debug_keysetup_window,widget_t="debug_filedialog",dialog_t=3,event_b=debug_filedialog_response)
        for count,label in enumerate(["Acheck","Bcheck","Ccheck"]):
            debug_check[count]=LTsv_check_new(debug_keysetup_window,widget_t=label,widget_x=debug_keysetup_W-debug_keyspin_W*(3-count),widget_y=debug_keysetup_H-debug_keyspin_H*1,widget_w=debug_keyspin_W*1,widget_h=debug_keyspin_H*1,widget_f=debug_font_entry,event_b=debug_checkbutton_shell(count))
        for count,label in enumerate(["Aradio","Bradio","Cradio"]):
            debug_radio[count]=LTsv_radio_new(debug_keysetup_window,widget_t=label,widget_x=debug_keysetup_W-debug_keyspin_W*(3-count),widget_y=debug_keysetup_H-debug_keyspin_H*2,widget_w=debug_keyspin_W*1,widget_h=debug_keyspin_H*1,widget_f=debug_font_entry,event_b=debug_radiobutton_shell(count))
        if LTsv_GUI == LTsv_GUI_GTK2:
            debug_keysetup_combobox=LTsv_combobox_new(debug_keysetup_window,widget_x=debug_combobox_X,widget_y=debug_combobox_Y,widget_w=debug_combobox_W,widget_h=debug_combobox_H,widget_f=debug_font_entry,event_b=debug_color_combo)
            #/usr/share/X11/rgb.txt
            #c:\Python34\Tools\pynche\X\rgb.txt
            debug_Tk_colors="DarkGray,DarkBlue,DarkCyan,DarkMagenta,DarkRed,LightGreen,GhostWhite,FloralWhite,OldLace,linen," \
              "PapayaWhip,BlanchedAlmond,moccasin,MintCream,AliceBlue,lavender,white,black,DimGray,LightSlateGray," \
              "gray,LightGray,MidnightBlue,navy,NavyBlue,CornflowerBlue,DarkSlateBlue,MediumSlateBlue,LightSlateBlue,MediumBlue,PowderBlue," \
              "DarkTurquoise,MediumTurquoise,MediumAquamarine,DarkGreen,MediumSeaGreen,LightSeaGreen,LawnGreen,MediumSpringGreen,GreenYellow,LimeGreen," \
              "YellowGreen,ForestGreen,DarkKhaki,PaleGoldenrod,LightGoldenrodYellow,SaddleBrown,peru,beige,SandyBrown,DarkSalmon," \
              "LightCoral,MediumVioletRed,violet,DarkViolet,BlueViolet".replace(',','\n')
            debug_Tk_colors1234="snow,seashell,AntiqueWhite,bisque,PeachPuff,NavajoWhite,LemonChiffon,cornsilk,ivory,honeydew," \
              "LavenderBlush,MistyRose,azure,SlateBlue,RoyalBlue,blue,DodgerBlue,SteelBlue,DeepSkyBlue,SkyBlue," \
              "LightSkyBlue,SlateGray,LightSteelBlue,LightBlue,LightCyan,PaleTurquoise,CadetBlue,turquoise,cyan,DarkSlateGray," \
              "aquamarine,DarkSeaGreen,SeaGreen,PaleGreen,SpringGreen,green,chartreuse,OliveDrab,DarkOliveGreen,khaki," \
              "LightGoldenrod,LightYellow,yellow,gold,goldenrod,DarkGoldenrod,RosyBrown,IndianRed,sienna,burlywood," \
              "wheat,tan,chocolate,firebrick,brown,salmon,LightSalmon,orange,DarkOrange,coral," \
              "tomato,OrangeRed,red,DeepPink,HotPink,pink,LightPink,PaleVioletRed,maroon,VioletRed," \
              "magenta,orchid,plum,MediumOrchid,DarkOrchid,purple,MediumPurple,thistle".split(',')
            for debug_colors1234 in debug_Tk_colors1234: debug_Tk_colors+="".join("\n{0}{1}".format(debug_colors1234,debug_gray) for debug_gray in ["","1","2","3","4"])
            debug_colordic={"IndianRed":[205,92,92]}
            LTsv_combobox_list(debug_keysetup_combobox,debug_Tk_colors)
        LTsv_widget_showhide(debug_keysetup_window,True)
        LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
        LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
        LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
        LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
        LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
        LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
        LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
        debug_timebutton()
        debug_canvas()
        debug_color_scale()
        debug_activewindow()
        if LTsv_GUI == LTsv_GUI_GTK2:
            LTsv_widget_settext(debug_keysetup_combobox,"IndianRed")
        LTsv_window_main(debug_keysetup_window)
    else:
        LTsv_libc_printf("LTsv_GUI,LTsv_Notify→{0},{1}".format(LTsv_GUI,LTsv_Notify))
        LTsv_libc_printf("GUIの設定に失敗しました。")
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
