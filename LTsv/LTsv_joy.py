#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
from LTsv_file import *
from LTsv_time import *
import math
import os
import sys
import array
import ctypes
import struct
if sys.platform.startswith("linux"):
    import fcntl
if sys.platform.startswith("win"):
    LTsv_winmm=ctypes.windll.winmm
#from ctypes import wintypes
# BYTE = c_byte
# WORD = c_ushort
# DWORD = c_ulong
# WCHAR = c_wchar
# UINT = c_uint
# INT = c_int
# DOUBLE = c_double
# FLOAT = c_float
# BOOLEAN = BYTE
# BOOL = c_long
LTsv_JOY_RETURNX       =0x001
LTsv_JOY_RETURNY       =0x002
LTsv_JOY_RETURNZ       =0x004
LTsv_JOY_RETURNR       =0x008
LTsv_JOY_RETURNU       =0x010
LTsv_JOY_RETURNV       =0x020
LTsv_JOY_RETURNPOV     =0x040
LTsv_JOY_RETURNBUTTONS =0x080
LTsv_JOY_RETURNRAWDATA =0x100
LTsv_JOY_RETURNPOVCTS  =0x200
LTsv_JOY_RETURNCENTERED=0x400
LTsv_JOY_USEDEADZONE   =0x800
LTsv_JOY_RETURNALL=LTsv_JOY_RETURNX|LTsv_JOY_RETURNY|LTsv_JOY_RETURNZ|LTsv_JOY_RETURNR|LTsv_JOY_RETURNU|LTsv_JOY_RETURNV|LTsv_JOY_RETURNPOV|LTsv_JOY_RETURNBUTTONS
LTsv_JSIOCGAXES        =0x80016a11
LTsv_JSIOCGBUTTONS     =0x80016a12
class LTsv_JOYINFOEX(ctypes.Structure):
    _fields_ = [
        ('dwSize',         ctypes.c_ulong),
        ('dwFlags',        ctypes.c_ulong),
        ('dwXpos',         ctypes.c_ulong),
        ('dwYpos',         ctypes.c_ulong),
        ('dwZpos',         ctypes.c_ulong),
        ('dwRpos',         ctypes.c_ulong),
        ('dwUpos',         ctypes.c_ulong),
        ('dwVpos',         ctypes.c_ulong),
        ('dwButtons',      ctypes.c_ulong),
        ('dwButtonNumber', ctypes.c_ulong),
        ('dwPOV',          ctypes.c_ulong),
        ('dwReserved1',    ctypes.c_ulong),
        ('dwReserved2',    ctypes.c_ulong)
    ]
    def __init__(self):
        self.dwSize=ctypes.sizeof(self)
        self.dwFlags=LTsv_JOY_RETURNALL

LTsv_MAXPNAMELEN=32
LTsv_MAXJOYSTICKOEMVXDNAME=260
class LTsv_JOYCAPS(ctypes.Structure):
    _fields_ = [
        ('wMid',           ctypes.c_ushort),
        ('wPid',           ctypes.c_ushort),
        ('szPname',        ctypes.c_wchar*LTsv_MAXPNAMELEN),
        ('wXmin',          ctypes.c_uint),
        ('wXmax',          ctypes.c_uint),
        ('wYmin',          ctypes.c_uint),
        ('wYmax',          ctypes.c_uint),
        ('wZmin',          ctypes.c_uint),
        ('wZmax',          ctypes.c_uint),
        ('wNumButtons',    ctypes.c_uint),
        ('wPeriodMin',     ctypes.c_uint),
        ('wPeriodMax',     ctypes.c_uint),
        ('wRmin',          ctypes.c_uint),
        ('wRmax',          ctypes.c_uint),
        ('wUmin',          ctypes.c_uint),
        ('wUmax',          ctypes.c_uint),
        ('wVmin',          ctypes.c_uint),
        ('wVmax',          ctypes.c_uint),
        ('wCaps',          ctypes.c_uint),
        ('wMaxAxes',       ctypes.c_uint),
        ('wNumAxes',       ctypes.c_uint),
        ('wMaxButtons',    ctypes.c_uint),
        ('szRegKey',       ctypes.c_wchar*LTsv_MAXPNAMELEN),
        ('szOEMVxD',       ctypes.c_wchar*LTsv_MAXJOYSTICKOEMVXDNAME)
    ]

LTsv_JS_EVENT_AXIS=0x02
LTsv_JS_EVENT_BUTTON=0x01
LTsv_JOYEVENT_unpack=b"IhBB" if sys.version_info.major == 2 else "IhBB"
LTsv_WINJOYCENTER=65535//2
class LTsv_JOYEVENT(ctypes.Structure):
    _fields_ = [
        ('time',           ctypes.c_uint),
        ('value',          ctypes.c_short),
        ('type',           ctypes.c_ubyte),
        ('number',         ctypes.c_ubyte)
    ]

LTsv_defjoydevpath="/dev/input/js"; LTsv_joydevpath=LTsv_defjoydevpath;
LTsv_JOYHANDMAXLIMIT=16
LTsv_joyhandmax=0
LTsv_joyhands=[0]*LTsv_JOYHANDMAXLIMIT
LTsv_joyaxis=[0]*LTsv_JOYHANDMAXLIMIT
LTsv_joyaxismax=[0]*LTsv_JOYHANDMAXLIMIT
LTsv_joybuttons=[0]*LTsv_JOYHANDMAXLIMIT
LTsv_buttonsmax=[0]*LTsv_JOYHANDMAXLIMIT

LTsv_joykbdformat="axisL\tLx\tLy\t_\tRx\tRy\tPx\tPy\n" \
                 "axisW\tLx\tLy\tRy\tRx\tPx\tPy\n" \
                 "button\tX\tY\tA\tB\tC\tZ\tL\tR\tF\tJ\tS\tP\n"
def LTsv_joyreset(LTsv_tsvpath):
    global LTsv_joydevpath,LTsv_joykbdformat
    LTsv_joyltsv=LTsv_loadfile(LTsv_tsvpath)
    LTsv_deviceL_page=LTsv_getpage(LTsv_joyltsv,"LTsv_deviceL")
    if len(LTsv_deviceL_page) > 0:
        LTsv_joydevpath=LTsv_readlinerest(LTsv_deviceL_page,"joy")
    if not os.path.exists("{0}0".format(LTsv_joydevpath)):
        LTsv_joydevpath=LTsv_defjoydevpath
    LTsv_keydefault_page=LTsv_getpage(LTsv_joyltsv,"keydefault")
    if len(LTsv_keydefault_page) > 0:
        LTsv_joykbdformat=LTsv_keydefault_page

def LTsv_joyexit():
    global LTsv_joydevpath,LTsv_joyhandmax,LTsv_joyhands,LTsv_joyaxismax,LTsv_joyaxis,LTsv_joybuttons,LTsv_buttonsmax
    if sys.platform.startswith("win"):
        pass
    if sys.platform.startswith("linux"):
        for LTsv_joyid in range(LTsv_joyhandmax):
            os.close(LTsv_joyhands[LTsv_joyid])
    for LTsv_joyid in range(LTsv_joyhandmax):
        LTsv_joyaxis[LTsv_joyid],LTsv_joyaxismax[LTsv_joyid],LTsv_joybuttons[LTsv_joyid],LTsv_buttonsmax[LTsv_joyid]=0,[0],0,[0]; 

def LTsv_joyinit(LTsv_tsvpath="LTsv/LTsv_joy.tsv"):
    global LTsv_joydevpath,LTsv_joyhandmax,LTsv_joyhands,LTsv_joyaxismax,LTsv_joyaxis,LTsv_joybuttons,LTsv_buttonsmax
    LTsv_joyexit()
    LTsv_joyreset(LTsv_tsvpath)
    LTsv_joycaps=LTsv_JOYCAPS()
    if sys.platform.startswith("win"):
        LTsv_numdev=LTsv_winmm.joyGetNumDevs() if LTsv_winmm.joyGetNumDevs()<=LTsv_JOYHANDMAXLIMIT else LTsv_JOYHANDMAXLIMIT
        for LTsv_joyid in range(LTsv_numdev):
            if LTsv_winmm.joyGetDevCapsW(LTsv_joyid,ctypes.pointer(LTsv_joycaps),ctypes.sizeof(LTsv_JOYCAPS)) == 0:
                LTsv_joyhandmax=LTsv_joyid+1
        LTsv_joyaxismax=[None for col in range(LTsv_joyhandmax)]
        LTsv_buttonsmax=[None for col in range(LTsv_joyhandmax)]
        for LTsv_joyid in range(LTsv_joyhandmax):
            LTsv_winmm.joyGetDevCapsW(LTsv_joyid,ctypes.pointer(LTsv_joycaps),ctypes.sizeof(LTsv_JOYCAPS))
            LTsv_joyaxismax[LTsv_joyid]=6 if LTsv_joycaps.wNumAxes < 6 else 8
            LTsv_joyaxis=[[0 for LTsv_col in range(LTsv_joyaxismax[LTsv_joyid])] for LTsv_row in range(LTsv_joyhandmax)]
            LTsv_buttonsmax[LTsv_joyid]=LTsv_joycaps.wNumButtons
            LTsv_joybuttons=[[0 for LTsv_col in range(LTsv_buttonsmax[LTsv_joyid])] for LTsv_row in range(LTsv_joyhandmax)]
    if sys.platform.startswith("linux"):
        LTsv_numdev=LTsv_JOYHANDMAXLIMIT
        for LTsv_joyid in range(LTsv_numdev):
            LTsv_joydevpath_no=LTsv_joydevpath+str(LTsv_joyid)
            try:
                LTsv_joyhands[LTsv_joyid]=os.open(LTsv_joydevpath_no,os.O_RDONLY|os.O_NONBLOCK)
            except OSError as err:
#                print("OSError({0}):{1}".format(err.errno,err.strerror))
                break
#            print(LTsv_joydevpath_no)
            if LTsv_joyhands[LTsv_joyid] != 0:
                LTsv_joyhandmax=LTsv_joyid+1
        LTsv_joyaxismax=[None for LTsv_col in range(LTsv_joyhandmax)]
        LTsv_joyaxis=[[] for LTsv_col in range(LTsv_joyhandmax)]
        LTsv_buttonsmax=[None for LTsv_col in range(LTsv_joyhandmax)]
        LTsv_joybuttons=[[] for LTsv_col in range(LTsv_joyhandmax)]
        for LTsv_joyid in range(LTsv_joyhandmax):
            LTsv_ioctlbuf=array.array(b'B',[0]) if sys.version_info.major == 2 else array.array('B',[0])
            fcntl.ioctl(LTsv_joyhands[LTsv_joyid],LTsv_JSIOCGAXES,LTsv_ioctlbuf)
            LTsv_joyaxismax[LTsv_joyid]=LTsv_ioctlbuf[0]
            LTsv_joyaxis[LTsv_joyid]=[0 for LTsv_row in range(LTsv_joyaxismax[LTsv_joyid])]
            fcntl.ioctl(LTsv_joyhands[LTsv_joyid],LTsv_JSIOCGBUTTONS,LTsv_ioctlbuf)
            LTsv_buttonsmax[LTsv_joyid]=LTsv_ioctlbuf[0]
            LTsv_joybuttons[LTsv_joyid]=[0 for LTsv_row in range(LTsv_buttonsmax[LTsv_joyid])]
    return LTsv_joyhandmax

def LTsv_setjoydata(LTsv_joyid,LTsv_default=None):
    if not 0 <= LTsv_joyid < LTsv_joyhandmax: return None
    if sys.platform.startswith("win"):
        LTsv_joyinfo=LTsv_JOYINFOEX()
        LTsv_winmm.joyGetPosEx(0,ctypes.pointer(LTsv_joyinfo))
        LTsv_joyaxis[LTsv_joyid][0]=LTsv_joyinfo.dwXpos-LTsv_WINJOYCENTER
        LTsv_joyaxis[LTsv_joyid][1]=LTsv_joyinfo.dwYpos-LTsv_WINJOYCENTER
        LTsv_joyaxis[LTsv_joyid][2]=LTsv_joyinfo.dwRpos-LTsv_WINJOYCENTER
        LTsv_joyaxis[LTsv_joyid][3]=LTsv_joyinfo.dwUpos-LTsv_WINJOYCENTER
        if LTsv_joyinfo.dwPOV > 36000:
            LTsv_joyaxis[LTsv_joyid][4]=0
            LTsv_joyaxis[LTsv_joyid][5]=0
        else:
            LTsv_povaxis=(18000.0-LTsv_joyinfo.dwPOV)*2*math.pi/36000.0
#            LTsv_joyaxis[LTsv_joyid][4]=int(math.sin(LTsv_povaxis)*LTsv_WINJOYCENTER)
#            LTsv_joyaxis[LTsv_joyid][5]=int(math.cos(LTsv_povaxis)*LTsv_WINJOYCENTER)
            LTsv_joyaxis[LTsv_joyid][4]=min(max(int(math.sin(LTsv_povaxis)*LTsv_WINJOYCENTER*2),-LTsv_WINJOYCENTER),LTsv_WINJOYCENTER)
            LTsv_joyaxis[LTsv_joyid][5]=min(max(int(math.cos(LTsv_povaxis)*LTsv_WINJOYCENTER*2),-LTsv_WINJOYCENTER),LTsv_WINJOYCENTER)
        for LTsv_bshift in range(LTsv_buttonsmax[LTsv_joyid]):
            LTsv_joybuttons[LTsv_joyid][LTsv_bshift]=1 if LTsv_joyinfo.dwButtons&(1<<LTsv_bshift) else 0
        if LTsv_joyaxismax[LTsv_joyid] > 6:
            LTsv_joyaxis[LTsv_joyid][6]=LTsv_joyinfo.dwZpos
            LTsv_joyaxis[LTsv_joyid][7]=LTsv_joyinfo.dwVpos
    if sys.platform.startswith("linux"):
        LTsv_joystacks=LTsv_joyaxismax[LTsv_joyid]+LTsv_buttonsmax[LTsv_joyid] if LTsv_default is None else LTsv_default
        for LTsv_stack in range(LTsv_joystacks):
            try:
                LTsv_joybyte=""
                LTsv_joybyte=os.read(LTsv_joyhands[LTsv_joyid],ctypes.sizeof(LTsv_JOYEVENT))
            except OSError as err:
#                print("OSError({0}):{1}".format(err.errno,err.strerror))
                break
            if LTsv_joybyte:
                LTsv_joyeve=LTsv_JOYEVENT
                LTsv_joyeve.time,LTsv_joyeve.value,LTsv_joyeve.type,LTsv_joyeve.number=struct.unpack(LTsv_JOYEVENT_unpack,LTsv_joybyte)
                if LTsv_joyeve.type==LTsv_JS_EVENT_AXIS:
                    LTsv_joyaxis[LTsv_joyid][LTsv_joyeve.number]=LTsv_joyeve.value
                if LTsv_joyeve.type==LTsv_JS_EVENT_BUTTON:
                    LTsv_joybuttons[LTsv_joyid][LTsv_joyeve.number]=LTsv_joyeve.value
    return LTsv_joyaxis[LTsv_joyid],LTsv_joybuttons[LTsv_joyid]

def LTsv_getjoystr(LTsv_joyid,joyformat=None):
    if not 0 <= LTsv_joyid < LTsv_joyhandmax: return ""
    joyformat=LTsv_joykbdformat if joyformat == None else joyformat
    LTsv_codes=joyformat; LTsv_firsts=LTsv_readlinefirsts(LTsv_codes).split('\t')
    for LTsv_first in LTsv_firsts:
        if LTsv_first == "button":
            LTsv_codes=LTsv_pushlinerest(LTsv_codes,LTsv_first,LTsv_labelzip(LTsv_readlinerest(LTsv_codes,LTsv_first),LTsv_tuple2tsv(LTsv_joybuttons[LTsv_joyid])))
        if LTsv_first == "axisL":
            LTsv_codes=LTsv_pushlinerest(LTsv_codes,LTsv_first,LTsv_labelzip(LTsv_readlinerest(LTsv_codes,LTsv_first),LTsv_tuple2tsv(LTsv_joyaxis[LTsv_joyid])))
        if LTsv_first == "axisW":
            LTsv_codes=LTsv_pushlinerest(LTsv_codes,LTsv_first,LTsv_labelzip(LTsv_readlinerest(LTsv_codes,LTsv_first),LTsv_tuple2tsv(LTsv_joyaxis[LTsv_joyid])))
        if LTsv_first == "status":
            LTsv_codes=LTsv_pushlinerest(LTsv_codes,LTsv_first,LTsv_labelzip(LTsv_readlinerest(LTsv_codes,LTsv_first),str(LTsv_joyaxismax[LTsv_joyid])+'\t'+str(LTsv_buttonsmax[LTsv_joyid])))
    return LTsv_codes

def LTsv_atanscalar(LTsv_atanX,LTsv_atanY):
    LTsv_atanS=0
    LTsv_vectR=math.sqrt(LTsv_atanX**2+LTsv_atanY**2)
    if LTsv_vectR > 0:
        LTsv_atanA=LTsv_atanX/LTsv_atanY if abs(LTsv_atanX) < abs(LTsv_atanY) else LTsv_atanY/LTsv_atanX
        LTsv_atanS=LTsv_vectR/math.sqrt(1.0+LTsv_atanA**2)
    else:
        LTsv_atanS=0
    return LTsv_atanS

def LTsv_atanclock(LTsv_atanX,LTsv_atanY,LTsv_labels):
    LTsv_atanT=math.pi-math.atan2(LTsv_atanX,LTsv_atanY)
    LTsv_dialLen=LTsv_pickdatadeno(LTsv_labels)
    LTsv_radian=int(((LTsv_atanT-(math.pi/LTsv_dialLen))*LTsv_dialLen/(math.pi*2)+LTsv_dialLen)%LTsv_dialLen)
    LTsv_dialchar=LTsv_pickdatanum(LTsv_labels,LTsv_radian)
    return LTsv_dialchar

def LTsv_joyaxis_label():
    LTsv_joyaxislabel=""
    if sys.platform.startswith("win"):   LTsv_joyaxislabel="axisW"
    if sys.platform.startswith("linux"): LTsv_joyaxislabel="axisL"
    return LTsv_joyaxislabel


if __name__=="__main__":
    from LTsv_printf import *
    from LTsv_file   import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    joylabel="１\t２\t３\t４\t５\t６\t７\t８\t９\t10\t11\t12"
    LTsv_libc_printf("joylabel={0}".format(joylabel))
    LTsv_libc_printf("LTsv_atanclock(1,0,joylabel)→{0}".format(LTsv_atanclock(1,0,joylabel)))
    LTsv_libc_printf("LTsv_atanclock(0,1,joylabel)→{0}".format(LTsv_atanclock(0,1,joylabel)))
    LTsv_libc_printf("LTsv_atanclock(-1,0,joylabel)→{0}".format(LTsv_atanclock(-1,0,joylabel)))
    LTsv_libc_printf("LTsv_atanclock(0,-1,joylabel)→{0}".format(LTsv_atanclock(0,-1,joylabel)))
    print("")
    handmax=LTsv_joyinit("./LTsv_joy.tsv")
    for LTsv_joyidcount in range(handmax):
        LTsv_setjoydata(0)
        LTsv_jf=LTsv_getjoystr(0,"status\t{0}\tbutton".format(LTsv_joyaxis_label()))
        LTsv_libc_printf(LTsv_jf)
    print("---")
    LTsv_joyidcount=0
    for j in range(10):
        LTsv_libc_printf("LTsv_setjoydata(0)→{0}".format(LTsv_setjoydata(0)))
        LTsv_libc_printf(LTsv_getjoystr(LTsv_joyidcount))
        time.sleep(0.5)
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE
