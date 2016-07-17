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
try:
   import cPickle as pickle
except:
   import pickle
from LTsv_file    import *
from LTsv_printf import *
try:
    from LTsv_kbd  import *
except:
    pass
LTsv_Tkinter=True
try:
    import tkinter as Tk
    import tkinter.scrolledtext as Tk_sc
#    import tkFileDialog
#    import tkMessageBox
except:
    LTsv_Tkinter=False
LTsv_libgtk,LTsv_libgdk,LTsv_libobj=None,None,None
LTsv_user32,LTsv_shell32,LTsv_kernel32,LTsv_gdi32=None,None,None,None
LTsv_GUI_ERROR,LTsv_GUI_GTK2,LTsv_GUI_Tkinter,LTsv_GUI_WinAPI="","GTK2","Tkinter","WinAPI"
LTsv_GUI,LTsv_Notify=LTsv_GUI_ERROR,LTsv_GUI_ERROR
#LTsv_CALLBACLTYPE=ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.POINTER(ctypes.c_ulong))
#LTsv_CALLBACLTYPE=ctypes.CFUNCTYPE(ctypes.c_bool,ctypes.c_void_p)
LTsv_CALLBACLTYPE=ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_void_p)
LTsv_widgetLTSV=LTsv_newfile("LTsv_gui",LTsv_default=None)
LTsv_widgetOBJ={}; LTsv_widgetOBJcount=0
LTsv_timerOBJ={}; LTsv_timer_cbk={}
LTsv_canvas_motion_X,LTsv_canvas_motion_Y=0,0
canvas_EMLtimeout,canvas_EMLenter,canvas_EMLmotion,canvas_EMLleave,canvas_EMLafter={},{},{},{},{}
LTsv_pictureOBJ,LTsv_pictureW,LTsv_pictureH={},{},{}
LTsv_iconOBJ={}; LTsv_iconOBJnotify=[]
LTsv_popupmenuOBJ={}
LTsv_default_iconuri=""
LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ={},{},{}

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
def LTsv_global_libgtk():                           return LTsv_libgtk
def LTsv_global_libgdk():                           return LTsv_libgdk
def LTsv_global_libobj():                           return LTsv_libobj
def LTsv_global_canvasmotionX():                    return LTsv_canvas_motion_X
def LTsv_global_canvasmotionY():                    return LTsv_canvas_motion_Y
def LTsv_global_widgetgetltsv():                    return LTsv_widgetLTSV
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

def LTsv_widget_newobj(LTsv_widgetpagelocal,LTsv_widgetoption,widget_obj):
    global LTsv_widgetOBJ,LTsv_widgetOBJcount
    LTsv_widgetpagelocal=LTsv_pushlinerest(LTsv_widgetpagelocal,LTsv_widgetoption,str(LTsv_widgetOBJcount))
    LTsv_widgetOBJ[str(LTsv_widgetOBJcount)]=widget_obj; LTsv_widgetOBJcount+=1
    return LTsv_widgetpagelocal

def LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_o=None,widget_k=None,widget_t=None,widget_u=None,widget_s=None,widget_e=None,widget_a=None,widget_v=None,widget_b=None, \
  widget_p=None,widget_m=None,widget_g=None,widget_f=None,widget_x=None,widget_y=None,widget_w=None,widget_h=None,widget_c=None, \
  event_z=None,event_k=None,event_y=None,event_b=None,event_p=None,event_r=None,event_e=None,event_m=None,event_l=None,event_a=None,event_u=None, \
  menu_o=None,menu_b=None,menu_c=None,kbd_d=None,kbd_g=None,kbd_s=None):
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
    if menu_b   != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"popupmenubind",menu_b)
    if menu_c   != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"popupmenubind",menu_b)
    if kbd_d    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"keyboard_draw",kbd_d)
    if kbd_g    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"keyboard_getkey",kbd_g)
    if kbd_s    != None:  LTsv_widgetPAGE=LTsv_widget_newobj(LTsv_widgetPAGE,"keyboard_setkey",kbd_s)
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
            event_k_cbk=LTsv_CALLBACLTYPE(event_k)
            LTsv_libobj.g_signal_connect_data(window_o,"key-press-event".encode("utf-8"),event_k_cbk,0,0,0)
        if event_y:
            event_y_cbk=LTsv_CALLBACLTYPE(event_y)
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
    if widget_k == "clipboard":
        if LTsv_GUI == LTsv_GUI_GTK2:     widget_t=ctypes.c_char_p(LTsv_libgtk.gtk_clipboard_wait_for_text(widget_o)).value.decode("utf-8")
        if LTsv_GUI == LTsv_GUI_Tkinter:  widget_t=widget_o.clipboard_get()
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

def LTsv_check_new(LTsv_windowPAGENAME,widget_n=None,event_b=None,widget_t="Tsv_check",widget_x=0,widget_y=0,widget_w=16,widget_h=16,widget_f=None):
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

def LTsv_canvas_new(LTsv_windowPAGENAME,widget_n=None,widget_x=0,widget_y=0,widget_w=16,widget_h=16,event_p=None,event_r=None,event_e=None,event_m=None,event_l=None,event_w=100):
    global LTsv_widgetLTSV,canvas_EMLtimeout,canvas_EMLenter,canvas_EMLmotion,canvas_EMLleave
    LTsv_windowPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_windowPAGENAME)
    window_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_windowPAGE,"widgetobj")]
    LTsv_widgetPAGENAME=LTsv_widget_newUUID(widget_n); LTsv_widgetPAGE=""
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,widget_k="canvas",widget_x=widget_x,widget_y=widget_y,widget_w=widget_w,widget_h=widget_h)
    canvas_EMLafter[LTsv_widgetPAGENAME]=False
    canvas_EMLenter[LTsv_widgetPAGENAME],canvas_EMLmotion[LTsv_widgetPAGENAME],canvas_EMLleave[LTsv_widgetPAGENAME]=event_e,event_m,event_l
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
        global canvas_EMLafter
        if canvas_EMLafter[LTsv_widgetPAGENAME] == False:
            canvas_EMLafter[LTsv_widgetPAGENAME]=True
            if canvas_EMLenter[LTsv_widgetPAGENAME] != None: canvas_EMLenter[LTsv_widgetPAGENAME]()
            LTsv_canvas_timeout()
        return 0
    def LTsv_canvas_motion(window_objvoid=None,window_objptr=None):
        global LTsv_canvas_motion_X,LTsv_canvas_motion_Y
        if LTsv_GUI == LTsv_GUI_GTK2:
            mouse_x,mouse_y=ctypes.c_int(),ctypes.c_int(); LTsv_libgdk.gdk_window_at_pointer(ctypes.byref(mouse_x),ctypes.byref(mouse_y))
            LTsv_canvas_motion_X,LTsv_canvas_motion_Y=int(mouse_x.value),int(mouse_y.value)
        if LTsv_GUI == LTsv_GUI_Tkinter:
            if window_objvoid != None:
                mouse_x,mouse_y=window_objvoid.x,window_objvoid.y
                LTsv_canvas_motion_X,LTsv_canvas_motion_Y=int(mouse_x),int(mouse_y)
        return 0
    def LTsv_canvas_timeout(window_objvoid=None,window_objptr=None):
        global canvas_EMLafter
        if canvas_EMLafter[LTsv_widgetPAGENAME] == True:
            if canvas_EMLmotion[LTsv_widgetPAGENAME] != None: canvas_EMLmotion[LTsv_widgetPAGENAME]()
            LTsv_window_after(LTsv_windowPAGENAME,event_b=LTsv_canvas_timeout,event_i=LTsv_windowPAGENAME,event_w=event_w)
        return 0
    canvas_EMLtimeout[LTsv_widgetPAGENAME]=LTsv_canvas_timeout
    def LTsv_canvas_leave(window_objvoid=None,window_objptr=None):
        global canvas_EMLafter
        canvas_EMLafter[LTsv_widgetPAGENAME]=False
        if canvas_EMLleave[LTsv_widgetPAGENAME] != None: canvas_EMLleave[LTsv_widgetPAGENAME]()
        return 0
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_libgtk.gtk_widget_set_events(widget_o,LTsv_GDK_POINTER_MOTION_MASK)
        event_p_cbk=LTsv_CALLBACLTYPE(event_p) if event_p != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"button-press-event".encode("utf-8"),event_p_cbk,0,0,0)
        event_r_cbk=LTsv_CALLBACLTYPE(event_r) if event_r != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"button-release-event".encode("utf-8"),event_r_cbk,0,0,0)
        event_e_cbk=LTsv_CALLBACLTYPE(LTsv_canvas_enter) if LTsv_canvas_enter != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"enter-notify-event".encode("utf-8"),event_e_cbk,0,0,0)
        event_m_cbk=LTsv_CALLBACLTYPE(LTsv_canvas_motion) if LTsv_canvas_motion != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"motion-notify-event".encode("utf-8"),event_m_cbk,0,0,0)
        event_l_cbk=LTsv_CALLBACLTYPE(LTsv_canvas_leave) if LTsv_canvas_leave != None else LTsv_CALLBACLTYPE(LTsv_window_none)
        LTsv_libobj.g_signal_connect_data(widget_o,"leave-notify-event".encode("utf-8"),event_l_cbk,0,0,0)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,event_p=event_p_cbk,event_r=event_r_cbk,event_e=event_e_cbk,event_m=event_m_cbk,event_l=event_l_cbk)
    if LTsv_GUI == LTsv_GUI_Tkinter:
        if event_p != None:
            widget_o.bind("<ButtonPress>",event_p)
        if event_r != None:
            widget_o.bind("<ButtonRelease>",event_r)
        if event_r != LTsv_canvas_enter:
            widget_o.bind("<Enter>",LTsv_canvas_enter)
        if event_r != LTsv_canvas_motion:
            widget_o.bind("<Motion>",LTsv_canvas_motion)
        if event_r != LTsv_canvas_leave:
            widget_o.bind("<Leave>",LTsv_canvas_leave)
        LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,event_p=event_p,event_r=event_r,event_e=LTsv_canvas_enter,event_m=LTsv_canvas_motion,event_l=LTsv_canvas_leave)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME,LTsv_widgetPAGE)
    return LTsv_widgetPAGENAME

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

LTsv_GTKcanvasPAGE,LTsv_GTKcanvas_o,LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,LTsv_GTKcanvas_gccolor,LTsv_GTKcanvas_font=None,None,None,None,None,None
LTsv_GTKcanvasW,LTsv_GTKcanvasH,LTsv_GTKfont_gccolor=None,None,None
def LTsv_drawGTK_selcanvas(LTsv_canvasPAGENAME,draw_g="LTsv_draw_tkTAG"):
    global LTsv_GTKcanvasPAGE,LTsv_GTKcanvas_o,LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,LTsv_GTKcanvas_gccolor,LTsv_GTKcanvas_font
    global LTsv_GTKcanvasW,LTsv_GTKcanvasH,LTsv_GTKfont_gccolor
    LTsv_GTKcanvasPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_canvasPAGENAME)
    LTsv_GTKcanvasW=int(LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetsizeW"))
    LTsv_GTKcanvasH=int(LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetsizeH"))
    LTsv_GTKcanvas_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetobj")]
    LTsv_GTKcanvas_m=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetpixmap")]
    LTsv_GTKcanvas_g=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_GTKcanvasPAGE,"widgetgc")]
    LTsv_GTKcanvas_gccolor=LTsv_GDKCOLOR()
    LTsv_GTKfont_gccolor=LTsv_GDKCOLOR()
    LTsv_GTKcanvas_font=""
    LTsv_drawGTK_color()

LTsv_TkintercanvasPAGE,LTsv_Tkintercanvas_o,LTsv_Tkintercanvas_color,LTsv_Tkintercanvas_TAG,LTsv_Tkintercanvas_font=None,None,None,None,None
LTsv_TkintercanvasW,LTsv_TkintercanvasH,LTsv_Tkinterfont_color=None,None,None
def LTsv_drawTkinter_selcanvas(LTsv_canvasPAGENAME,draw_g="LTsv_draw_tkTAG"):
    global LTsv_TkintercanvasPAGE,LTsv_Tkintercanvas_o,LTsv_Tkintercanvas_color,LTsv_Tkintercanvas_TAG
    global LTsv_TkintercanvasW,LTsv_TkintercanvasH,LTsv_Tkinterfont_color
    LTsv_TkintercanvasPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_canvasPAGENAME)
    LTsv_GTKcanvasW=int(LTsv_readlinerest(LTsv_TkintercanvasPAGE,"widgetsizeW"))
    LTsv_GTKcanvasH=int(LTsv_readlinerest(LTsv_TkintercanvasPAGE,"widgetsizeH"))
    LTsv_Tkintercanvas_o=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_TkintercanvasPAGE,"widgetobj")]
    LTsv_Tkintercanvas_TAG=draw_g
    LTsv_Tkintercanvas_font=""
    LTsv_drawTkinter_color()

def LTsv_drawGTK_delete(draw_c="white"):
    global LTsv_GTKcanvasW,LTsv_GTKcanvasH,LTsv_GTKfont_gccolor
    LTsv_libgdk.gdk_color_parse(draw_c.encode("utf-8"),ctypes.pointer(LTsv_GTKfont_gccolor))
    LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKfont_gccolor))
    LTsv_libgdk.gdk_draw_rectangle(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,0,0,LTsv_GTKcanvasW,LTsv_GTKcanvasH)

def LTsv_drawTkinter_delete(draw_c="white"):
    global LTsv_Tkinterfont_color,LTsv_Tkintercanvas_o
    LTsv_Tkinterfont_color=draw_c
    LTsv_Tkintercanvas_o.delete(LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_color(draw_c=""):
    LTsv_libgdk.gdk_color_parse(draw_c.encode("utf-8"),ctypes.pointer(LTsv_GTKcanvas_gccolor))
    LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKcanvas_gccolor))

def LTsv_drawTkinter_color(draw_c=""):
    global LTsv_Tkintercanvas_color
    LTsv_Tkintercanvas_color=draw_c

def LTsv_drawGTK_bgcolor(draw_c=""):
    LTsv_libgdk.gdk_color_parse(draw_c.encode("utf-8"),ctypes.pointer(LTsv_GTKfont_gccolor))
    LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKfont_gccolor))

def LTsv_drawTkinter_bgcolor(draw_c=""):
    global LTsv_Tkinterfont_color
    LTsv_Tkinterfont_color=draw_c

def LTsv_drawGTK_polygon(*draw_xy):
    draw_xylen=len(draw_xy)//2; gdkpointsArrayType=LTsv_GDKPOINT*draw_xylen; gdkpointsArray=gdkpointsArrayType()
    for draw_xy_count,gdkpoint in enumerate(gdkpointsArray):
        gdkpoint.X,gdkpoint.Y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
    LTsv_libgdk.gdk_draw_polygon(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,ctypes.pointer(gdkpointsArray),draw_xylen)

def LTsv_drawTkinter_polygon(*draw_xy):
    xyloop=draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]
    if len(xyloop) > 0:
        LTsv_Tkintercanvas_o.create_polygon(*xyloop,fill="",outline=LTsv_Tkintercanvas_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_polygonfill(*draw_xy):
    draw_xylen=len(draw_xy)//2; gdkpointsArrayType=LTsv_GDKPOINT*draw_xylen; gdkpointsArray=gdkpointsArrayType()
    for draw_xy_count,gdkpoint in enumerate(gdkpointsArray):
        gdkpoint.X,gdkpoint.Y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
    LTsv_libgdk.gdk_draw_polygon(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,ctypes.pointer(gdkpointsArray),draw_xylen)

def LTsv_drawTkinter_polygonfill(*draw_xy):
    xyloop=draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]
    if len(xyloop) > 0:
        LTsv_Tkintercanvas_o.create_polygon(*xyloop,fill=LTsv_Tkintercanvas_color,outline=LTsv_Tkintercanvas_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawTkinter_fontfill(*draw_xy):
    xyloop=draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]
    if len(xyloop) > 0:
        LTsv_Tkintercanvas_o.create_polygon(*xyloop,fill=LTsv_Tkinterfont_color,outline=LTsv_Tkinterfont_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_squares(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_rectangle(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh)

def LTsv_drawTkinter_squares(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_rectangle(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill="",outline=LTsv_Tkintercanvas_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_squaresfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_rectangle(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh)

def LTsv_drawTkinter_squaresfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_rectangle(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill=LTsv_Tkintercanvas_color,outline=LTsv_Tkintercanvas_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_circles(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh,0,LTsv_GDK_ARCFILL)

def LTsv_drawTkinter_circles(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_oval(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill="",outline=LTsv_Tkintercanvas_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_circlesfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh,draw_wh,0,LTsv_GDK_ARCFILL)

def LTsv_drawTkinter_circlesfill(draw_wh=16,*draw_xy):
    for draw_xy_count in range(len(draw_xy)//2):
        draw_x,draw_y=draw_xy[draw_xy_count*2],draw_xy[draw_xy_count*2+1]
        LTsv_Tkintercanvas_o.create_oval(-draw_wh//2+draw_x,-draw_wh//2+draw_y,draw_wh//2+draw_x,draw_wh//2+draw_y,fill=LTsv_Tkintercanvas_color,outline=LTsv_Tkintercanvas_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_arc(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,False,draw_x,draw_y,draw_w,draw_h,int(draw_s*LTsv_GDK_ARCFILL/2.0/math.pi),int(draw_e*LTsv_GDK_ARCFILL/2.0/math.pi))

def LTsv_drawTkinter_arc(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_Tkintercanvas_o.create_arc(draw_x,draw_y,draw_x+draw_w,draw_y+draw_h,fill="",outline=LTsv_Tkintercanvas_color,start=draw_s*360.0/2.0/math.pi,extent=draw_e*360.0/2.0/math.pi,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_arcfill(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_libgdk.gdk_draw_arc(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,True,draw_x,draw_y,draw_w,draw_h,int(draw_s*LTsv_GDK_ARCFILL/2.0/math.pi),int(draw_e*LTsv_GDK_ARCFILL/2.0/math.pi))

def LTsv_drawTkinter_arcfill(draw_x,draw_y,draw_w,draw_h,draw_s=-math.pi,draw_e=math.pi):
    LTsv_Tkintercanvas_o.create_arc(draw_x,draw_y,draw_x+draw_w,draw_y+draw_h,fill=LTsv_Tkintercanvas_color,outline=LTsv_Tkintercanvas_color,start=draw_s*360.0/2.0/math.pi,extent=draw_e*360.0/2.0/math.pi,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_font(draw_f=""):
    global LTsv_GTKcanvas_font
    LTsv_GTKcanvas_font=draw_f

def LTsv_drawTkinter_font(draw_f=None):
    global LTsv_Tkintercanvas_font
    LTsv_Tkintercanvas_font=LTsv_fonttuple(draw_f)

def LTsv_drawGTK_text(draw_t="",draw_x=0,draw_y=0):
    pango_l=LTsv_libgtk.gtk_widget_create_pango_layout(LTsv_GTKcanvas_o,0)
    LTsv_libgtk.pango_layout_set_text(pango_l,draw_t.encode("utf-8","xmlcharrefreplace"),-1)
    LTsv_fontDesc=LTsv_libgtk.pango_font_description_from_string(LTsv_GTKcanvas_font.encode("utf-8"))
    LTsv_libgtk.pango_layout_set_font_description(pango_l,LTsv_fontDesc)
    LTsv_libgdk.gdk_draw_layout_with_colors(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,draw_x,draw_y,pango_l,ctypes.pointer(LTsv_GTKcanvas_gccolor),0)
    LTsv_libobj.g_object_unref(pango_l)
    LTsv_libgtk.pango_font_description_free(LTsv_fontDesc)

def LTsv_drawTkinter_text(draw_t="",draw_x=0,draw_y=0):
    LTsv_Tkintercanvas_o.create_text(draw_x,draw_y,text=draw_t,font=LTsv_Tkintercanvas_font,anchor="nw",fill=LTsv_Tkintercanvas_color,tag=LTsv_Tkintercanvas_TAG)

def LTsv_drawGTK_picture(draw_t="",draw_x=0,draw_y=0):
    picture_o,picture_w,picture_h=LTsv_pictureOBJ[draw_t],LTsv_pictureW[draw_t],LTsv_pictureH[draw_t]
    LTsv_libgdk.gdk_draw_pixbuf(LTsv_GTKcanvas_m,LTsv_GTKcanvas_g,picture_o,0,0,draw_x,draw_y,picture_w,picture_h,0,0,0)

def LTsv_drawTkinter_picture(draw_t="",draw_x=0,draw_y=0):
    picture_o,picture_w,picture_h=LTsv_pictureOBJ[draw_t],LTsv_pictureW[draw_t],LTsv_pictureH[draw_t]
    LTsv_Tkintercanvas_o.create_image(draw_x,draw_y,image=picture_o,anchor="nw",tag=LTsv_Tkintercanvas_TAG)

def LTsv_clockwise(*draw_xy):
    clockwise=0
    if len(draw_xy) >= 6:
        xyloop=draw_xy+draw_xy if len(draw_xy)%2 == 0 else draw_xy[:-1]+draw_xy[:-1]
        for draw_xy_count in range(0,len(draw_xy),2):
            Px,Py,Cx,Cy,Qx,Qy=range(draw_xy_count,draw_xy_count+6)
            PCQ=(xyloop[Px]-xyloop[Cx])*(xyloop[Qy]-xyloop[Cy])-(xyloop[Py]-xyloop[Cy])*(xyloop[Qx]-xyloop[Cx])
            clockwise=clockwise+1 if PCQ < 0 else clockwise-1 if PCQ > 0 else clockwise
    return clockwise

LTsv_PSfont_ZW,LTsv_PSfont_CW,LTsv_PSchar_ZW,LTsv_PSchar_CW=1024,624,1000,600
LTsv_glyph_kandic=""
def LTsv_glyphdicload(dicname="kanchar.tsv"):
    global LTsv_glyph_kandic
    LTsv_glyph_kandic=LTsv_loadfile(dicname) if os.path.isfile(dicname) else LTsv_keyboard_dic()

def LTsv_glyphOBJpickle(filename="kanpickle.bin"):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    glyphOBJpickle=(LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ)
    with open(filename,mode='wb') as pickle_fobj:
        pickle.dump(glyphOBJpickle,pickle_fobj,protocol=2)

def LTsv_glyphOBJunpickle(filename="kanpickle.bin"):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    if os.path.isfile(filename):
        with open(filename,mode='rb') as pickle_fobj:
            glyphOBJpickle=pickle.load(pickle_fobj)
        LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ=glyphOBJpickle

def LTsv_glyphdicread(dictext):
    global LTsv_glyph_kandic
    LTsv_glyph_kandic=dictext

def LTsv_glyphpath(glyphcode):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    global LTsv_glyph_kandic
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
    LTsv_glyph_path,LTsv_glyph_wide=LTsv_pickdatalabel(LTsv_glyph_kanline,"活"),LTsv_pickdatalabel(LTsv_glyph_kanline,"幅")
    LTsv_glyph_pathZ=LTsv_glyph_path.strip(' ').replace('Z','z').rstrip('z').split('z') if len(LTsv_glyph_path) else []
    LTsv_glyphnote,LTsv_glyphclock=[],[]
    for LTsv_glyphline in LTsv_glyph_pathZ:
        LTsv_glyphdata=LTsv_glyphline.split(' '); LTsv_glyphpointlist=[]
        for LTsv_glyphpoint in LTsv_glyphdata:
            if LTsv_glyphpoint.count(',') != 1: continue;
            LTsv_glyphpoints=LTsv_glyphpoint.strip(' ').split(',')
            LTsv_glyphpointlist+=[int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0]
            LTsv_glyphpointlist+=[(LTsv_PSchar_ZW-int(LTsv_glyphpoints[1])) if LTsv_glyphpoints[1].isdigit() else 0]
        LTsv_glyphnote.append(LTsv_glyphpointlist); LTsv_glyphclock.append(LTsv_clockwise(*tuple(LTsv_glyphpointlist)))
    LTsv_kanglyphOBJ[glyphcode]=LTsv_glyphnote
    LTsv_kanclockOBJ[glyphcode]=LTsv_glyphclock
    LTsv_kanwideOBJ[glyphcode]=int(LTsv_glyph_wide) if len(LTsv_glyph_wide) else LTsv_PSfont_ZW

def LTsv_glyphpath_outer(glyphcode):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    global LTsv_glyph_kandic
    LTsv_glyph_kanline=LTsv_readlinerest(LTsv_glyph_kandic,glyphcode)
    LTsv_glyph_path,LTsv_glyph_wide=LTsv_pickdatalabel(LTsv_glyph_kanline,"活"),LTsv_pickdatalabel(LTsv_glyph_kanline,"幅")
    LTsv_glyph_pathZ=LTsv_glyph_path.strip(' ').replace('Z','z').rstrip('z').split('z') if len(LTsv_glyph_path) else []
    LTsv_glyphnote,LTsv_glyphclock=[],[]
    for LTsv_glyphline in LTsv_glyph_pathZ:
        LTsv_glyphdata=LTsv_glyphline.split(' '); LTsv_glyphpointlist=[]
        for LTsv_glyphpoint in LTsv_glyphdata:
            if LTsv_glyphpoint.count(',') != 1: continue;
            LTsv_glyphpoints=LTsv_glyphpoint.strip(' ').split(',')
#            LTsv_glyphpointlist+=[int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0]
#            LTsv_glyphpointlist+=[(LTsv_PSchar_ZW-int(LTsv_glyphpoints[1])) if LTsv_glyphpoints[1].isdigit() else 0]
            LTsv_glyphpoint98=int(LTsv_glyphpoints[0]) if LTsv_glyphpoints[0].isdigit() else 0
            LTsv_glyphpoint98=LTsv_glyphpoint98 if LTsv_glyphpoint98 % 100 != 98 else LTsv_glyphpoint98+2
            LTsv_glyphpointlist+=[LTsv_glyphpoint98]
            LTsv_glyphpoint98=int(LTsv_glyphpoints[1]) if LTsv_glyphpoints[1].isdigit() else 0
            LTsv_glyphpoint98=LTsv_glyphpoint98 if LTsv_glyphpoint98 % 100 != 2 else LTsv_glyphpoint98-2
            LTsv_glyphpointlist+=[LTsv_PSchar_ZW-LTsv_glyphpoint98]
        LTsv_glyphnote.append(LTsv_glyphpointlist); LTsv_glyphclock.append(LTsv_clockwise(*tuple(LTsv_glyphpointlist)))
    LTsv_kanglyphOBJ[glyphcode]=LTsv_glyphnote
    LTsv_kanclockOBJ[glyphcode]=LTsv_glyphclock
    LTsv_kanwideOBJ[glyphcode]=int(LTsv_glyph_wide) if len(LTsv_glyph_wide) else LTsv_PSfont_ZW

def LTsv_drawGTK_glyph(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv_glyphpath_outer(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_drawGTK_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_drawTkinter_glyph(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv_glyphpath(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist in LTsv_glyphnote:
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            LTsv_drawTkinter_polygon(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_drawGTK_glyphfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv_glyphpath_outer(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            if LTsv_kanclockOBJ[glyphcode][LTsv_glyphpointlist_count] > 0:
                LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKcanvas_gccolor))
            else:
                LTsv_libgdk.gdk_gc_set_rgb_fg_color(LTsv_GTKcanvas_g,ctypes.pointer(LTsv_GTKfont_gccolor))
            LTsv_drawGTK_polygonfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_drawTkinter_glyphfill(draw_t,draw_x=0,draw_y=0,draw_f=10,draw_w=1,draw_h=1,draw_LF=False,draw_HT=False,draw_SP=False):
    global LTsv_kanglyphOBJ,LTsv_kanclockOBJ,LTsv_kanwideOBJ
    draw_xf,draw_yf=draw_x,draw_y
    for glyphcode in draw_t:
        if glyphcode == '\n':
            if draw_LF:
                glyphcode=""
            else:
                draw_xf,draw_yf=draw_x,draw_yf+draw_f+draw_h
                continue
        if glyphcode == '\t':
            if draw_HT:
                glyphcode=""
        if glyphcode == ' ':
            if draw_SP:
                glyphcode=""
        if not glyphcode in LTsv_kanglyphOBJ:
            LTsv_glyphpath(glyphcode)
        LTsv_glyphnote=LTsv_kanglyphOBJ[glyphcode]
        for LTsv_glyphpointlist_count,LTsv_glyphpointlist in enumerate(LTsv_glyphnote):
            LTsv_glyphpointresize=[xy*draw_f//LTsv_PSchar_ZW+draw_yf if odd%2 else xy*draw_f//LTsv_PSchar_ZW+draw_xf for odd,xy in enumerate(LTsv_glyphpointlist)]
            if LTsv_kanclockOBJ[glyphcode][LTsv_glyphpointlist_count] > 0:
                LTsv_drawTkinter_polygonfill(*tuple(LTsv_glyphpointresize))
            else:
                LTsv_drawTkinter_fontfill(*tuple(LTsv_glyphpointresize))
        draw_xf=draw_xf+LTsv_kanwideOBJ[glyphcode]*draw_f//LTsv_PSchar_ZW+draw_w

def LTsv_drawGTK_queue():
    global LTsv_GTKcanvas_o
    LTsv_libgtk.gtk_widget_queue_draw(LTsv_GTKcanvas_o)

def LTsv_drawTkinter_queue():
    pass

def LTsv_keyboard_size(keyboard_fontsize=12):
    keyboard_fontKP=3; keyboard_buttonsize=keyboard_fontKP+keyboard_fontsize+keyboard_fontKP
    widget_w,widget_h=keyboard_fontKP+keyboard_buttonsize*14+keyboard_fontKP,keyboard_fontKP+keyboard_buttonsize*4+keyboard_fontKP
    return "{0}\t{1}".format(widget_w,widget_h)

def LTsv_keyboard_new(LTsv_windowPAGENAME,widget_n=None,widget_x=0,widget_y=0,event_w=50,keyboard_getkey=None,keyboard_setkey=None,widget_f="kantray5x5comic,12"):
    keyboard_colorF,keyboard_colorB,keyboard_colorN,keyboard_colorX,keyboard_colorK,keyboard_colorO,keyboard_colorI="#111111","#FFFFFF","#2591FC","#1CDA00","#F6B555","#FF007C","#FCAEAF"
    keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX=LTsv_keyboard_iroha_guide()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    keyboard_fontsize,keyboard_fontKP=LTsv_intstr0x(LTsv_fonttuple(widget_f)[1]),3
    keyboard_buttonsize=keyboard_fontKP+keyboard_fontsize+keyboard_fontKP; keyboard_buttonsizehalf=keyboard_buttonsize//2
    keyboard_fontX,keyboard_fontY=[0]*(keyboard_dicselpos+1),[0]*(keyboard_dicselpos+1)
    for kbd_xy in range(keyboard_irohamax):
        keyboard_fontY[kbd_xy]=keyboard_fontKP+keyboard_buttonsize*(kbd_xy//12)
        keyboard_fontX[kbd_xy]=keyboard_fontKP+keyboard_buttonsize*(kbd_xy%12)+keyboard_fontY[kbd_xy]//2+keyboard_buttonsizehalf
    kbd_xy=keyboard_irohamax-1;  keyboard_fontX[kbd_xy],keyboard_fontY[kbd_xy]=keyboard_fontX[12*3-1],keyboard_fontY[0];
    kbd_xy=keyboard_alphapos-1;  keyboard_fontX[kbd_xy],keyboard_fontY[kbd_xy]=keyboard_fontX[0]-keyboard_buttonsizehalf,keyboard_fontY[12*3];
    kbd_xy=keyboard_guidepos-1;  keyboard_fontX[kbd_xy],keyboard_fontY[kbd_xy]=keyboard_fontX[keyboard_irohamax],keyboard_fontY[12*3-1];
    kbd_xy=keyboard_dicinppos-1; keyboard_fontX[kbd_xy],keyboard_fontY[kbd_xy]=keyboard_fontX[keyboard_irohamax]+keyboard_buttonsize,keyboard_fontY[keyboard_irohamax]+keyboard_fontKP;
    kbd_xy=keyboard_dicselpos-1; keyboard_fontX[kbd_xy],keyboard_fontY[kbd_xy]=keyboard_fontX[keyboard_irohamax-2]+keyboard_buttonsize,keyboard_fontY[keyboard_dicinppos-1];
    keyboard_keyX,keyboard_keyY,keyboard_keyXY=[0]*(keyboard_alphapos+1),[0]*(keyboard_alphapos+1),[]
    for kbd_xy in range(keyboard_alphapos):
        keyboard_keyX[kbd_xy],keyboard_keyY[kbd_xy]=keyboard_fontX[kbd_xy]+keyboard_buttonsizehalf,keyboard_fontY[kbd_xy]+keyboard_buttonsizehalf
        keyboard_keyXY.extend((keyboard_keyX[kbd_xy],keyboard_keyY[kbd_xy]))
    keyboard_WH=LTsv_keyboard_size(keyboard_fontsize); keyboard_W,keyboard_H=LTsv_intstr0x(LTsv_pickdatanum(keyboard_WH,0)),LTsv_intstr0x(LTsv_pickdatanum(keyboard_WH,1))
    keyboard_cursorNXx,keyboard_cursorKy={"True":keyboard_keyX[22],"False":keyboard_keyX[13]},{"1":keyboard_keyY[0],"-1":keyboard_keyY[0],"0":keyboard_fontY[keyboard_dicinppos-1]}
    def LTsv_setkey_None(): pass
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_font,LTsv_drawtk_color,LTsv_drawtk_text,LTsv_drawtk_squares,LTsv_drawtk_squaresfill,LTsv_drawtk_polygonfill=LTsv_drawGTK_selcanvas,LTsv_drawGTK_font,LTsv_drawGTK_color,LTsv_drawGTK_text,LTsv_drawGTK_squares,LTsv_drawGTK_squaresfill,LTsv_drawGTK_polygonfill
        LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_delete,LTsv_drawGTK_queue
        def LTsv_drawtk_bmp(drawtk_bmp=""): return drawtk_bmp[0]
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_font,LTsv_drawtk_color,LTsv_drawtk_text,LTsv_drawtk_squares,LTsv_drawtk_squaresfill,LTsv_drawtk_polygonfill=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_font,LTsv_drawTkinter_color,LTsv_drawTkinter_text,LTsv_drawTkinter_squares,LTsv_drawTkinter_squaresfill,LTsv_drawTkinter_polygonfill
        LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
        def LTsv_drawtk_bmp(drawtk_bmp=""): return drawtk_bmp[0] if ord(drawtk_bmp[0]) < 65535 else keyboard_tofu
    def LTsv_keyboard_draw():
        keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
        keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
        keyboard_cursorIRm=min(keyboard_cursorIR,keyboard_irohamax)
        keyboard_cursor_iroha,keyboard_cursor_alpha=keyboard_iroha[keyboard_cursorIR],keyboard_alphatype[keyboard_cursorAF]
        keyboard_kanmapN["　"],keyboard_kanmapX["　"]=keyboard_kanmapN[keyboard_cursor_alpha],keyboard_kanmapX[keyboard_cursor_alpha]
        keyboard_guideN["　"],keyboard_guideX["　"]=keyboard_guideN[keyboard_cursor_alpha],keyboard_guideX[keyboard_cursor_alpha]
        keyboard_findN,keyboard_findX,keyboard_findNr,keyboard_findXr=LTsv_keyboard_findNX()
        LTsv_drawtk_selcanvas(kantray_kbdcanvas); LTsv_drawtk_font(widget_f)
        LTsv_drawtk_delete("white")
        LTsv_drawtk_color(keyboard_colorN); LTsv_drawtk_polygonfill(0,0,keyboard_W,0,keyboard_W,keyboard_H,0,keyboard_H)
        LTsv_drawtk_color(keyboard_colorX); LTsv_drawtk_polygonfill(keyboard_W,0,keyboard_cursorNXx[str(keyboard_cursorNX)],0,keyboard_cursorNXx[str(keyboard_cursorNX)],keyboard_H,keyboard_W,keyboard_H)
        LTsv_drawtk_color(keyboard_colorK); LTsv_drawtk_polygonfill(0,keyboard_cursorKy[str(keyboard_cursorK)],keyboard_W,keyboard_cursorKy[str(keyboard_cursorK)],keyboard_W,keyboard_H,0,keyboard_H)
        LTsv_drawtk_color(keyboard_colorB); LTsv_drawtk_squaresfill(keyboard_buttonsize,*tuple(keyboard_keyXY))
        LTsv_drawtk_color(keyboard_colorB); LTsv_drawtk_text(draw_t=keyboard_cursorDIC,draw_x=keyboard_fontX[keyboard_dicinppos-1],draw_y=keyboard_fontY[keyboard_dicinppos-1])
        if keyboard_cursorNX:
            LTsv_drawtk_text(draw_t=keyboard_findNr[keyboard_cursor_alpha],draw_x=keyboard_fontX[keyboard_dicselpos-1],draw_y=keyboard_fontY[keyboard_dicselpos-1])
            if keyboard_cursorK != 0:
                LTsv_drawtk_color(keyboard_colorF)
                if keyboard_cursorK < 0:
                    for kbd_xy in range(keyboard_alphapos):
                        LTsv_drawtk_text(draw_t=LTsv_drawtk_bmp(keyboard_guideKN[keyboard_iroha[kbd_xy]]),draw_x=keyboard_fontX[kbd_xy],draw_y=keyboard_fontY[kbd_xy])
                else:
                    for kbd_xy in range(keyboard_alphapos):
                        LTsv_drawtk_text(draw_t=LTsv_drawtk_bmp(keyboard_dicinput[kbd_xy]),draw_x=keyboard_fontX[kbd_xy],draw_y=keyboard_fontY[kbd_xy])
                LTsv_drawtk_color(keyboard_colorK)
            else:
                LTsv_drawtk_color(keyboard_colorI); LTsv_drawtk_squaresfill(keyboard_buttonsize,*tuple(keyboard_keyXY[keyboard_cursorIRm*2:keyboard_cursorIRm*2+2]))
                LTsv_drawtk_color(keyboard_colorF)
                for kbd_xy in range(keyboard_alphapos):
                    LTsv_drawtk_text(draw_t=LTsv_drawtk_bmp(keyboard_kanmapN[keyboard_cursor_iroha][kbd_xy]),draw_x=keyboard_fontX[kbd_xy],draw_y=keyboard_fontY[kbd_xy])
                LTsv_drawtk_color(keyboard_colorB); LTsv_drawtk_text(draw_t=keyboard_guideN[keyboard_cursor_iroha],draw_x=keyboard_fontX[keyboard_guidepos-1],draw_y=keyboard_fontY[keyboard_guidepos-1])
                LTsv_drawtk_color(keyboard_colorN)
        else:
            LTsv_drawtk_text(draw_t=keyboard_findXr[keyboard_cursor_alpha],draw_x=keyboard_fontX[keyboard_dicselpos-1],draw_y=keyboard_fontY[keyboard_dicselpos-1])
            if keyboard_cursorK != 0:
                LTsv_drawtk_color(keyboard_colorF)
                if keyboard_cursorK < 0:
                    for kbd_xy in range(keyboard_alphapos):
                        LTsv_drawtk_text(draw_t=LTsv_drawtk_bmp(keyboard_guideKX[keyboard_iroha[kbd_xy]]),draw_x=keyboard_fontX[kbd_xy],draw_y=keyboard_fontY[kbd_xy])
                else:
                    for kbd_xy in range(keyboard_alphapos):
                        LTsv_drawtk_text(draw_t=LTsv_drawtk_bmp(keyboard_dicinput[kbd_xy]),draw_x=keyboard_fontX[kbd_xy],draw_y=keyboard_fontY[kbd_xy])
                LTsv_drawtk_color(keyboard_colorK)
            else:
                LTsv_drawtk_color(keyboard_colorI); LTsv_drawtk_squaresfill(keyboard_buttonsize,*tuple(keyboard_keyXY[keyboard_cursorIRm*2:keyboard_cursorIRm*2+2]))
                LTsv_drawtk_color(keyboard_colorF)
                for kbd_xy in range(keyboard_alphapos):
                    LTsv_drawtk_text(draw_t=LTsv_drawtk_bmp(keyboard_kanmapX[keyboard_cursor_iroha][kbd_xy]),draw_x=keyboard_fontX[kbd_xy],draw_y=keyboard_fontY[kbd_xy])
                LTsv_drawtk_color(keyboard_colorB); LTsv_drawtk_text(draw_t=keyboard_guideX[keyboard_cursor_iroha],draw_x=keyboard_fontX[keyboard_guidepos-1],draw_y=keyboard_fontY[keyboard_guidepos-1])
                LTsv_drawtk_color(keyboard_colorX)
        if keyboard_cursorMS < keyboard_alphapos:
            LTsv_drawtk_squares(keyboard_buttonsize,*tuple(keyboard_keyXY[keyboard_cursorMS*2:keyboard_cursorMS*2+2]))
        if keyboard_cursorOLD < keyboard_alphapos:
            LTsv_drawtk_color(keyboard_colorO); LTsv_drawtk_squares(keyboard_buttonsize,*tuple(keyboard_keyXY[keyboard_cursorOLD*2:keyboard_cursorOLD*2+2]))
        LTsv_drawtk_queue()
    def LTsv_keyboard_press(callback_void=None,callback_ptr=None):
        keyboard_mouseX,keyboard_mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
        keyboard_mouseX,keyboard_mouseY=min(max(keyboard_mouseX,keyboard_fontKP+1),keyboard_W-keyboard_fontKP-1),min(max(keyboard_mouseY,keyboard_fontKP+1),keyboard_H-keyboard_fontKP-1)
        keyboard_getkbdstr=keyboard_getkey() if keyboard_getkey != None else "MouseL:0\tMouseC:0\tMouseR:0"
        keyboard_cursorLCR="{0}{1}{2}".format(LTsv_pickdatalabel(keyboard_getkbdstr,"MouseL"),LTsv_pickdatalabel(keyboard_getkbdstr,"MouseC"),LTsv_pickdatalabel(keyboard_getkbdstr,"MouseR"))
        keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK(cursorLCR=keyboard_cursorLCR,cursorOLD=keyboard_dicselpos+1)
        keyboard_cursorKy=keyboard_fontY[keyboard_dicinppos-1]
        for kbd_xy in range(keyboard_dicselpos+1):
            if keyboard_fontX[kbd_xy] <= keyboard_mouseX < keyboard_fontX[kbd_xy]+keyboard_buttonsize and keyboard_fontY[kbd_xy] <= keyboard_mouseY < keyboard_fontY[kbd_xy]+keyboard_buttonsize:
                keyboard_cursorMS=kbd_xy
        if keyboard_cursorMS < keyboard_alphapos:
            if keyboard_cursorLCR == "100" or keyboard_cursorLCR == "000":
                LTsv_keyboard_NXK(cursorOLD=keyboard_cursorMS)
                keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
                if keyboard_cursorNX:
                    keyboard_setkey(keyboard_kanmapN[keyboard_iroha[keyboard_cursorIR]][keyboard_cursorMS])
                else:
                    keyboard_setkey(keyboard_kanmapX[keyboard_iroha[keyboard_cursorIR]][keyboard_cursorMS])
            elif keyboard_cursorLCR == "010":
                keyboard_kandic=LTsv_keyboard_dic()
                keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
                if keyboard_cursorNX:
                    keyboard_dicinput[keyboard_cursorMS]=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,keyboard_kanmapN[keyboard_iroha[keyboard_cursorIR]][keyboard_cursorMS]),keyboard_cursorDIC)
                else:
                    keyboard_dicinput[keyboard_cursorMS]=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,keyboard_kanmapX[keyboard_iroha[keyboard_cursorIR]][keyboard_cursorMS]),keyboard_cursorDIC)
                keyboard_setkey(keyboard_dicinput[keyboard_cursorMS],setfind=False)
            elif keyboard_cursorLCR == "001":
                keyboard_cursorNX=False if keyboard_cursorNX else True
                keyboard_cursorLCR="swipe"; LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorLCR=keyboard_cursorLCR)
        elif keyboard_cursorMS == keyboard_dicinppos-1:
            if keyboard_cursorLCR == "100" or keyboard_cursorLCR == "000":
                LTsv_keyboard_NXK(cursorK=1)
                LTsv_keyboard_dicinput()
            elif keyboard_cursorLCR == "010":
                LTsv_keyboard_NXK(cursorK=-1)
            elif keyboard_cursorLCR == "001":
                keyboard_cursorNX=False if keyboard_cursorNX else True
                LTsv_keyboard_NXK(cursorK=-1,cursorNX=keyboard_cursorNX)
        elif keyboard_cursorMS == keyboard_dicselpos-1:
            if keyboard_cursorLCR == "100" or keyboard_cursorLCR == "000":
                LTsv_keyboard_NXK(cursorK=-1)
            elif keyboard_cursorLCR == "010":
                LTsv_keyboard_NXK(cursorK=-1)
            elif keyboard_cursorLCR == "001":
                keyboard_cursorNX=False if keyboard_cursorNX else True
                LTsv_keyboard_NXK(cursorK=-1,cursorNX=keyboard_cursorNX)
        else:
            if keyboard_cursorLCR == "100" or keyboard_cursorLCR == "000":
                keyboard_cursorNX=True if keyboard_mouseX < keyboard_W//2 else False
                keyboard_cursorLCR="swipe"; LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorLCR=keyboard_cursorLCR)
            elif keyboard_cursorLCR == "010":
                LTsv_keyboard_NXK(cursorK=-1)
            elif keyboard_cursorLCR == "001":
                keyboard_cursorNX=False if keyboard_cursorNX else True
                LTsv_keyboard_NXK(cursorK=-1,cursorNX=keyboard_cursorNX)
        LTsv_keyboard_draw()
    def LTsv_keyboard_motion(callback_void=None,callback_ptr=None):
        keyboard_mouseX,keyboard_mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
        keyboard_mouseX,keyboard_mouseY=min(max(keyboard_mouseX,keyboard_fontKP+1),keyboard_W-keyboard_fontKP-1),min(max(keyboard_mouseY,keyboard_fontKP+1),keyboard_H-keyboard_fontKP-1)
        keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
        keyboard_cursorMS=keyboard_alphapos
        for kbd_xy in range(keyboard_alphapos):
            if keyboard_fontX[kbd_xy] < keyboard_mouseX < keyboard_fontX[kbd_xy]+keyboard_buttonsize and keyboard_fontY[kbd_xy] < keyboard_mouseY < keyboard_fontY[kbd_xy]+keyboard_buttonsize:
                keyboard_cursorMS=kbd_xy
        if keyboard_cursorLCR == "swipe":
            if keyboard_cursorMS < keyboard_alphapos:
                keyboard_cursorIR=keyboard_cursorMS
        LTsv_keyboard_NXK(cursorMS=keyboard_cursorMS,cursorIR=keyboard_cursorIR)
        LTsv_keyboard_draw()
    def LTsv_keyboard_release(callback_void=None,callback_ptr=None):
        keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
        if keyboard_cursorMS < keyboard_alphapos:
            if keyboard_cursorK < 0:
                keyboard_cursor_alpha=keyboard_guideK[keyboard_cursorMS]
                if keyboard_cursor_alpha in keyboard_irohatype:
                    keyboard_cursorIR=keyboard_irohatype.index(keyboard_cursor_alpha); LTsv_keyboard_NXK(cursorIR=keyboard_cursorIR)
                elif keyboard_cursor_alpha in keyboard_alphatype:
                    keyboard_cursorIR,keyboard_cursorAF=LTsv_keyboard_irohamax,keyboard_alphatype.index(keyboard_cursor_alpha)
                    LTsv_keyboard_NXK(cursorIR=keyboard_cursorIR,cursorAF=keyboard_cursorAF)
                elif keyboard_cursor_alpha in keyboard_dictype:
                    keyboard_cursorDIC=keyboard_cursor_alpha; LTsv_keyboard_NXK(cursorDIC=keyboard_cursorDIC)
            if keyboard_cursorK > 0:
                keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
                keyboard_setkey(keyboard_dicinput[keyboard_cursorMS],setfind=False)
        LTsv_keyboard_NXK(cursorLCR="000",cursorK=0)
        LTsv_keyboard_draw()
    def LTsv_keyboard_leave():
        LCR=LTsv_keyboard_NXK(cursorMS=keyboard_dicselpos+1)
        LTsv_keyboard_draw()
    kantray_kbdcanvas=LTsv_canvas_new(LTsv_windowPAGENAME,widget_n=None,widget_x=widget_x,widget_y=widget_y,widget_w=keyboard_W,widget_h=keyboard_H,
     event_p=LTsv_keyboard_press,event_r=LTsv_keyboard_release,event_m=LTsv_keyboard_motion,event_l=LTsv_keyboard_leave,event_w=50)
    global LTsv_widgetLTSV
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,kantray_kbdcanvas)
    LTsv_widgetPAGE=LTsv_widgetPAGEXYWH(LTsv_widgetPAGE,kbd_g=keyboard_getkey,kbd_s=keyboard_setkey if keyboard_setkey!= None else LTsv_setkey_None(),kbd_d=LTsv_keyboard_draw)
    LTsv_widgetLTSV=LTsv_putpage(LTsv_widgetLTSV,kantray_kbdcanvas,LTsv_widgetPAGE)
    LTsv_keyboard_draw()
    return kantray_kbdcanvas

def LTsv_keyboard_find(LTsv_widgetPAGENAME,find_t="",find_min=1,find_max=65535,dic_t="",alpha_t="",NX_t=""):
    global LTsv_widgetLTSV
    keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX=LTsv_keyboard_iroha_guide()
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    if dic_t != "":
        if dic_t in keyboard_dictype:
            keyboard_cursorDIC=dic_t; LTsv_keyboard_NXK(cursorDIC=dic_t)
    if alpha_t != "":
        if alpha_t in keyboard_alphatype:
            keyboard_cursorIR,keyboard_cursorAF=LTsv_keyboard_irohamax,keyboard_alphatype.index(alpha_t)
            LTsv_keyboard_NXK(cursorIR=keyboard_cursorIR,cursorAF=keyboard_cursorAF)
    if NX_t != "":
        keyboard_findN,keyboard_findX,keyboard_findNr,keyboard_findXr=LTsv_keyboard_findNX()
        if NX_t in keyboard_findN:
            keyboard_cursor_alpha=keyboard_findN[NX_t]; keyboard_cursorNX=True
        elif NX_t in keyboard_findX:
            keyboard_cursor_alpha=keyboard_findX[NX_t]; keyboard_cursorNX=False
        if keyboard_cursor_alpha in keyboard_irohatype:
            keyboard_cursorIR=keyboard_irohatype.index(keyboard_cursor_alpha); LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR)
        elif keyboard_cursor_alpha in keyboard_alphatype:
            keyboard_cursorIR,keyboard_cursorAF=LTsv_keyboard_irohamax,keyboard_alphatype.index(keyboard_cursor_alpha)
            LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR,cursorAF=keyboard_cursorAF)
    find_existpos=-1; LTsv_keyboard_NXK(cursorOLD=keyboard_dicselpos+1)
    for exist_index,exist_char in enumerate(find_t):
        if find_min <= ord(exist_char) <= find_max:
            for cursor_iroha in keyboard_irohatype:
                if exist_char in keyboard_kanmapN[cursor_iroha]:
                    find_existpos=exist_index
                    keyboard_cursorNX,keyboard_cursorIR,keyboard_cursorOLD=True, keyboard_irohatype.index(cursor_iroha),keyboard_kanmapN[cursor_iroha].index(exist_char)
                    LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR,cursorOLD=keyboard_cursorOLD)
                if exist_char in keyboard_kanmapX[cursor_iroha]:
                    find_existpos=exist_index
                    keyboard_cursorNX,keyboard_cursorIR,keyboard_cursorOLD=False,keyboard_irohatype.index(cursor_iroha),keyboard_kanmapX[cursor_iroha].index(exist_char)
                    LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR,cursorOLD=keyboard_cursorOLD)
                if find_existpos >= 0: break
            for cursor_alpha in keyboard_alphatype:
                if exist_char in keyboard_kanmapN[cursor_alpha]:
                    find_existpos=exist_index
                    keyboard_cursorNX,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD=True, keyboard_irohamax,keyboard_alphatype.index(cursor_alpha),keyboard_kanmapN[cursor_alpha].index(exist_char)
                    LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR,cursorAF=keyboard_cursorAF,cursorOLD=keyboard_cursorOLD)
                if exist_char in keyboard_kanmapX[cursor_alpha]:
                    find_existpos=exist_index
                    keyboard_cursorNX,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD=False,keyboard_irohamax,keyboard_alphatype.index(cursor_alpha),keyboard_kanmapX[cursor_alpha].index(exist_char)
                    LTsv_keyboard_NXK(cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR,cursorAF=keyboard_cursorAF,cursorOLD=keyboard_cursorOLD)
                if find_existpos >= 0: break
            if find_existpos >= 0: break
        if find_existpos >= 0: break
    LTsv_widgetPAGE=LTsv_getpage(LTsv_widgetLTSV,LTsv_widgetPAGENAME)
    LTsv_keyboard_draw=LTsv_widgetOBJ[LTsv_readlinerest(LTsv_widgetPAGE,"keyboard_draw")]
    LTsv_keyboard_draw()
    return find_existpos

def LTsv_keyboard_dicinput():
    keyboard_kandic=LTsv_keyboard_dic()
    keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX=LTsv_keyboard_iroha_guide()
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    if keyboard_cursorNX:
        for kbd_xy in range(keyboard_alphapos):
            keyboard_dicinput[kbd_xy]=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,keyboard_kanmapN[keyboard_iroha[keyboard_cursorIR]][kbd_xy]),keyboard_cursorDIC)
            keyboard_dicinput[kbd_xy]=keyboard_dicinput[kbd_xy] if len(keyboard_dicinput[kbd_xy]) > 0 else " "
    else:
        for kbd_xy in range(keyboard_alphapos):
            keyboard_dicinput[kbd_xy]=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,keyboard_kanmapX[keyboard_iroha[keyboard_cursorIR]][kbd_xy]),keyboard_cursorDIC)
            keyboard_dicinput[kbd_xy]=keyboard_dicinput[kbd_xy] if len(keyboard_dicinput[kbd_xy]) > 0 else " "
    LTsv_keyboard_map(dicinput=keyboard_dicinput)

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


def debug_canvas(window_objvoid=None,window_objptr=None):
    global debug_scaleRGB
    LTsv_drawtk_selcanvas(debug_keysetup_canvas)
    LTsv_drawtk_delete("white")
    LTsv_drawtk_font(debug_font_entry)
    LTsv_drawtk_color("#fffff0"); LTsv_drawtk_polygonfill(0,0,debug_canvas_W,0,debug_canvas_W,debug_canvas_H,0,debug_canvas_H)
    LTsv_drawtk_color("white"); LTsv_drawtk_polygonfill(debug_kanzip_icon_X+0,debug_kanzip_icon_Y+0,debug_kanzip_icon_X+debug_kanzip_icon_WH,debug_kanzip_icon_Y+0,debug_kanzip_icon_X+debug_kanzip_icon_WH,debug_kanzip_icon_Y+debug_kanzip_icon_WH,debug_kanzip_icon_X+0,debug_kanzip_icon_Y+debug_kanzip_icon_WH)
    LTsv_drawtk_color("green")
    if sys.version_info.major == 2:
        LTsv_drawtk_color("green")
        LTsv_drawtk_glyph("{0}".format(unichr(61615)),draw_x=debug_kanzip_icon_X,draw_y=debug_kanzip_icon_Y,draw_f=debug_kanzip_icon_WH)
        LTsv_drawtk_color("IndianRed")
        LTsv_drawtk_glyph("{0}".format(unichr(12306)),draw_x=(debug_kanzip_icon_X+debug_kanzip_icon_WH//2),draw_y=(debug_kanzip_icon_Y+debug_kanzip_icon_WH//2),draw_f=debug_kanzip_icon_WH//2)
    if sys.version_info.major == 3:
        LTsv_drawtk_color("green")
        LTsv_drawtk_glyph("{0}".format(chr(61615)),draw_x=debug_kanzip_icon_X,draw_y=debug_kanzip_icon_Y,draw_f=debug_kanzip_icon_WH)
        LTsv_drawtk_color("IndianRed")
        LTsv_drawtk_glyph("{0}".format(chr(12306)),draw_x=(debug_kanzip_icon_X+debug_kanzip_icon_WH//2),draw_y=(debug_kanzip_icon_Y+debug_kanzip_icon_WH//2),draw_f=debug_kanzip_icon_WH//2)
    mouse_x,mouse_y=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    LTsv_drawtk_color(debug_scaleRGB); LTsv_drawtk_text("mouseX,Y\n[{0},{1}]".format(mouse_x,mouse_y),draw_x=mouse_x,draw_y=mouse_y)
    LTsv_putdaytimenow(); LTsv_checkFPS()
    LTsv_drawtk_color("black"); LTsv_drawtk_text(LTsv_getdaytimestr(LTsv_widget_gettext(debug_keysetup_timentry)),draw_x=0,draw_y=0)
    LTsv_setkbddata(25,25)
    kbdlabels=LTsv_getkbdlabels().replace('\t',' ').replace('た','\nた').replace('ち','\nち').replace('つ','\nつ').replace('NFER','\nNFER')
    if LTsv_joymax > 0:
        LTsv_setjoydata(0); pad_axis=LTsv_readlinerest(LTsv_getjoystr(0),LTsv_joyaxis_label())
    for pad_xy,pad_circle in enumerate([LTsv_drawtk_squares,LTsv_drawtk_circles,LTsv_drawtk_circles]):
        pad_x,pad_y=debug_joypad_X+pad_xy*debug_joypad_W,debug_joypad_Y
        pad_circle(debug_joypad_W,*(pad_x,pad_y))
        if LTsv_joymax > 0:
            stick_w=int(LTsv_pickdatalabel(pad_axis,debug_padxkey[pad_xy]))
            stick_h=int(LTsv_pickdatalabel(pad_axis,debug_padykey[pad_xy]))
            stick_t=math.atan2(stick_w,stick_h)
            stick_s=LTsv_atanscalar(stick_w,stick_h)
            LTsv_drawtk_polygon(*(pad_x,pad_y,pad_x+int(math.sin(stick_t)*stick_s*debug_joypad_W/2/LTsv_WINJOYCENTER),pad_y+int(math.cos(stick_t)*stick_s*debug_joypad_W/2/LTsv_WINJOYCENTER)))
            LTsv_drawtk_text("{0},{1}\n{2},{3}\nθ{4}\n∇{5}".format(debug_padxkey[pad_xy],debug_padykey[pad_xy],LTsv_pickdatalabel(pad_axis,debug_padxkey[pad_xy]),LTsv_pickdatalabel(pad_axis,debug_padykey[pad_xy]),stick_t,stick_s),draw_x=pad_x,draw_y=pad_y)
        else:
            LTsv_drawtk_text("{0},{1}".format(debug_padxkey[pad_xy],debug_padykey[pad_xy]),draw_x=pad_x,draw_y=pad_y)
    debug_arc_W=debug_joypad_X+int(debug_joypad_W*2.5)
    LTsv_drawtk_arc(debug_arc_W,debug_joypad_Y-debug_joypad_W//2,debug_canvas_W-debug_arc_W-2,debug_joypad_W,-math.pi*0.5,math.pi*1.8) #gdk_draw_arc
    txt_x,txt_y=500,debug_joypad_Y+debug_joypad_H//2
    if LTsv_joymax > 0:
        LTsv_drawtk_text(LTsv_getjoystr(0).replace('\t',' '),draw_x=0,draw_y=txt_y)
    LTsv_drawtk_text(kbdlabels,draw_x=0,draw_y=txt_y+debug_label_WH*3)
    LTsv_drawtk_text("getkbdnames:{0}".format(LTsv_getkbdnames()),draw_x=txt_x,draw_y=txt_y+debug_label_WH*1)
    LTsv_drawtk_text("getkbdcodes:{0}".format(LTsv_getkbdcodes()),draw_x=txt_x,draw_y=txt_y+debug_label_WH*2)
    LTsv_drawtk_text("getkbdkanas:{0}".format(LTsv_getkbdkanas()),draw_x=txt_x,draw_y=txt_y+debug_label_WH*3)
    LTsv_drawtk_color(debug_scaleRGB)
    LTsv_drawtk_polygon(*tuple(debug_polygonpointlist))
    if LTsv9_logoOBJ:
        LTsv_drawtk_picture(LTsv9_logoPATH,debug_kanzip_icon_X-LTsv_global_pictureW(LTsv9_logoPATH),debug_canvas_H-LTsv_global_pictureH(LTsv9_logoPATH))
    LTsv_drawtk_queue()
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

def debug_checkbutton(window_objvoid=None,window_objptr=None):
    print(LTsv_widget_gettext(debug_check),LTsv_widget_getnumber(debug_check))


if __name__=="__main__":
    from LTsv_printf import *
    from LTsv_file   import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
    LTsv_libc_printf("LTsv_GUI,LTsv_Notify→{0},{1}".format(LTsv_GUI,LTsv_Notify))
    if len(LTsv_GUI) > 0:
        import math
        from LTsv_joy    import *
        from LTsv_calc   import *
        from LTsv_kbd    import *
        LTsv_kbdinit("./LTsv_kbd.tsv",LTsv_initmouse=False)
        LTsv_glyphdicload()
        LTsv_joymax=LTsv_joyinit()
        debug_fontname="kantray5x5comic"
        debug_fontsize_entry=10; debug_font_entry="{0},{1}".format(debug_fontname,debug_fontsize_entry); debug_label_WH=debug_fontsize_entry*2
        debug_keysetup_W,debug_keysetup_H=800,600
        debug_canvas_X,debug_canvas_Y,debug_canvas_W,debug_canvas_H=0,debug_label_WH,debug_keysetup_W-120,debug_keysetup_H*3//5
        debug_combobox_X,debug_combobox_Y,debug_combobox_W,debug_combobox_H=debug_canvas_W,debug_canvas_Y,debug_keysetup_W-debug_canvas_W,debug_label_WH*2
        debug_scale_X,debug_scale_Y,debug_scale_W,debug_scale_H=debug_canvas_W,debug_canvas_Y+debug_combobox_H,debug_keysetup_W-debug_canvas_W,debug_canvas_H-debug_combobox_H
        debug_joypad_X,debug_joypad_Y,debug_joypad_W,debug_joypad_H=debug_canvas_W//6,debug_canvas_H*1//4+debug_label_WH*2,debug_canvas_H*2//4,debug_canvas_H*2//4
        debug_padxkey,debug_padykey=["Px","Lx","Rx"],["Py","Ly","Ry"]
        debug_keyspin_X,debug_keyspin_Y,debug_keyspin_W,debug_keyspin_H=0,debug_keysetup_H-debug_label_WH*9,debug_keysetup_W//14,debug_label_WH
        debug_keysetup_window=LTsv_window_new(widget_t="L:Tsv GUI test and KeyCode Setup",event_b=LTsv_window_exit,widget_w=debug_keysetup_W,widget_h=debug_keysetup_H,event_z=None)
        debug_timentry_default="@000y年-@0m月(@0wnyi/@ywi週)-@0dm日(@wdj曜)@0h:@0n:@0s FPS:@0fpc"
        debug_keysetup_timentry=LTsv_entry_new(debug_keysetup_window,widget_t="",widget_x=0,widget_y=0,widget_w=debug_keysetup_W-debug_keyspin_W*1,widget_h=debug_label_WH,widget_f=debug_font_entry)
        debug_keysetup_timebutton=LTsv_button_new(debug_keysetup_window,widget_t="reset",widget_x=debug_keysetup_W-debug_keyspin_W*1,widget_y=0,widget_w=debug_keyspin_W*1,widget_h=debug_label_WH,widget_f=debug_font_entry,event_b=debug_timebutton)
        debug_keysetup_canvas=LTsv_canvas_new(debug_keysetup_window,widget_x=debug_canvas_X,widget_y=debug_canvas_Y,widget_w=debug_canvas_W,widget_h=debug_canvas_H,event_w=50,event_p=debug_canvas_press)
        if LTsv_GUI == LTsv_GUI_GTK2:
            LTsv_drawtk_selcanvas,LTsv_drawtk_color,LTsv_drawtk_font,LTsv_drawtk_text,LTsv_drawtk_picture=LTsv_drawGTK_selcanvas,LTsv_drawGTK_color,LTsv_drawGTK_font,LTsv_drawGTK_text,LTsv_drawGTK_picture
            LTsv_drawtk_polygon,LTsv_drawtk_polygonfill,LTsv_drawtk_squares,LTsv_drawtk_circles,LTsv_drawtk_arc=LTsv_drawGTK_polygon,LTsv_drawGTK_polygonfill,LTsv_drawGTK_squares,LTsv_drawGTK_circles,LTsv_drawGTK_arc
            LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_glyph,LTsv_drawGTK_glyphfill,LTsv_drawGTK_delete,LTsv_drawGTK_queue
        if LTsv_GUI == LTsv_GUI_Tkinter:
            LTsv_drawtk_selcanvas,LTsv_drawtk_color,LTsv_drawtk_font,LTsv_drawtk_text,LTsv_drawtk_picture=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_color,LTsv_drawTkinter_font,LTsv_drawTkinter_text,LTsv_drawTkinter_picture
            LTsv_drawtk_polygon,LTsv_drawtk_polygonfill,LTsv_drawtk_squares,LTsv_drawtk_circles,LTsv_drawtk_arc=LTsv_drawTkinter_polygon,LTsv_drawTkinter_polygonfill,LTsv_drawTkinter_squares,LTsv_drawTkinter_circles,LTsv_drawTkinter_arc
            LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_glyph,LTsv_drawTkinter_glyphfill,LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
        LTsv9_logoPATH="../icon_cap/LTsv9_logo.png"; LTsv9_logoOBJ=LTsv_draw_picture_load(LTsv9_logoPATH)
        debug_polygonpointlist=[556, 12, 566, 31, 583, 33, 574, 47, 581, 63, 561, 55, 537, 60, 547, 42, 529, 32, 552, 28]
        debug_kanzip_icon_WH=48; debug_kanzip_icon_X,debug_kanzip_icon_Y=debug_canvas_W-debug_kanzip_icon_WH-2,debug_canvas_H-debug_kanzip_icon_WH-2
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
        debug_check=LTsv_check_new(debug_keysetup_window,widget_t="check",widget_x=debug_keysetup_W-debug_keyspin_W*2,widget_y=debug_keysetup_H-debug_keyspin_H*1,widget_w=debug_keyspin_W*2,widget_h=debug_keyspin_H*1,widget_f=debug_font_entry,event_b=debug_checkbutton)
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
        debug_timebutton()
        debug_canvas()
        debug_color_scale()
        debug_activewindow()
        if LTsv_GUI == LTsv_GUI_GTK2:
            LTsv_widget_settext(debug_keysetup_combobox,"IndianRed")
        LTsv_window_main(debug_keysetup_window)
    else:
        LTsv_libc_printf("GUIの設定に失敗しました。")
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE
