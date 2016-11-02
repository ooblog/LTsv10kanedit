#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
import re
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


def LTsvDOClaunch_kernel_plane(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname):
    LTsvDOC_tagdata=LTsvDOC_tagname
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
    LTsvDOC_tagline=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_outname)
    LTsvDOC_tagdata=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagline)
    if len(LTsvDOC_tagdata) == 0:
        LTsvDOC_tagdata=LTsvDOC_tagline;
    LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagname,LTsvDOC_tagdata)
    return LTsvDOClaunch_main

def LTsvDOClaunch_kernel_timedata(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname):
    LTsvDOC_tagdata=LTsvDOC_tagname
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
    LTsvDOC_tagline=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_outname)
    LTsvDOC_tagline=LTsv_getdaytimestr(LTsvDOC_tagline)
    LTsvDOC_tagdata=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagline)
    if len(LTsvDOC_tagdata) == 0:
        LTsvDOC_tagdata=LTsvDOC_tagline;
    LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagname,LTsvDOC_tagdata)
    return LTsvDOClaunch_main

def LTsvDOClaunch_kernel_regularexpression(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname):
    LTsvDOC_tagdata=LTsvDOC_tagname
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
    LTsvDOC_tagcases=LTsvDOC_tagpage.split('\n')
    for LTsvDOC_tagcase in LTsvDOC_tagcases:
        if len(LTsvDOC_tagcase) == 0: continue;
        LTsvDOC_tagfirst=LTsv_readlinefirsts(LTsvDOC_tagcase)
        LTsvDOC_research=None
        try:
            LTsvDOC_research=re.search(re.compile(LTsvDOC_tagfirst),LTsvDOC_outname)
        except re.error:
            continue
        else:
            if LTsvDOC_research:
                LTsvDOC_tagline=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_tagfirst)
                LTsvDOC_tagdata=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagline)
                if len(LTsvDOC_tagdata) == 0:
                    LTsvDOC_tagdata=LTsvDOC_tagline;
                LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagname,LTsvDOC_tagdata)
    return LTsvDOClaunch_main

LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname="",""
LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir=0,0,""
LTsvDOClaunch_outlist,LTsvDOClaunch_taglist,LTsvDOClaunch_timlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist=[],[],[],[],[]
def LTsvDOClaunch_kernel_count(window_objvoid=None,window_objptr=None):
    global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname
    global LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir
    global LTsvDOClaunch_outlist,LTsvDOClaunch_taglist,LTsvDOClaunch_timlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
    if LTsvDOClaunch_outcount == 0:
        LTsvDOClaunch_tsvname=LTsvDOClaunch_tsvlist[LTsvDOClaunch_kernel_clickID]
        LTsvDOClaunch_ltsv=LTsv_loadfile(os.path.normpath(LTsvDOClaunch_tsvname))
        LTsvDOClaunch_head=LTsv_getpage(LTsvDOC_ltsv,"L:Tsv")
        LTsvDOClaunch_config=LTsv_getpage(LTsvDOClaunch_ltsv,LTsv_readlinerest(LTsvDOClaunch_head,"1st","LTsvDOC_tsv"))
        LTsvDOClaunch_outdir=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"outdir",os.path.dirname(os.path.normpath(LTsvDOClaunch_tsvname))))
        LTsvDOClaunch_mainname=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"main","LTsv_doc_main"))
        LTsvDOClaunch_main=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOClaunch_mainname)
        LTsvDOClaunch_outlistT=LTsv_readlinerest(LTsvDOClaunch_config,"outlist"); LTsvDOClaunch_outlist=LTsvDOClaunch_outlistT.split('\t') if len(LTsvDOClaunch_outlistT) else []
        LTsvDOClaunch_taglistT=LTsv_readlinerest(LTsvDOClaunch_config,"taglist"); LTsvDOClaunch_taglist=LTsvDOClaunch_taglistT.split('\t') if len(LTsvDOClaunch_taglistT) else []
        LTsvDOClaunch_timlistT=LTsv_readlinerest(LTsvDOClaunch_config,"timlist"); LTsvDOClaunch_timlist=LTsvDOClaunch_timlistT.split('\t') if len(LTsvDOClaunch_timlistT) else []
        LTsvDOClaunch_reglistT=LTsv_readlinerest(LTsvDOClaunch_config,"reglist"); LTsvDOClaunch_reglist=LTsvDOClaunch_reglistT.split('\t') if len(LTsvDOClaunch_reglistT) else []
#    for LTsvDOC_outcount,LTsvDOC_outname in enumerate(LTsvDOClaunch_outlist):
    if LTsvDOClaunch_outcount < len(LTsvDOClaunch_outlist):
        LTsvDOC_outname=LTsvDOClaunch_outlist[LTsvDOClaunch_outcount]
        LTsv_widget_settext(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],"{0}→{1}".format(LTsvDOClaunch_tsvname,LTsvDOC_outname))
        for LTsvDOC_tagcount,LTsvDOC_tagname in enumerate(LTsvDOClaunch_reglist):
            LTsvDOClaunch_main=LTsvDOClaunch_kernel_regularexpression(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname)
        for LTsvDOC_tagcount,LTsvDOC_tagname in enumerate(LTsvDOClaunch_timlist):
            LTsvDOClaunch_main=LTsvDOClaunch_kernel_timedata(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname)
        for LTsvDOC_tagcount,LTsvDOC_tagname in enumerate(LTsvDOClaunch_taglist):
            LTsvDOClaunch_main=LTsvDOClaunch_kernel_plane(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname)
        LTsv_saveplain(os.path.normpath(LTsvDOClaunch_outdir+"/"+LTsvDOC_outname),LTsvDOClaunch_main)
        LTsvDOClaunch_outcount+=1
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=LTsvDOC_T)
    else:
        LTsv_widget_disableenable(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],True)
        LTsv_widget_settext(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],"{0}({1})".format(LTsvDOClaunch_tsvname,LTsv_getdaytimestr(LTsvDOClaunch_modify)))
#        LTsv_saveplain(os.path.normpath(LTsvDOClaunch_tsvname),LTsvDOClaunch_ltsv)

def LTsvDOClaunch_shell(LTsvDOClaunch_tsvcount):
    def LTsvDOClaunch_kernel(window_objvoid=None,window_objptr=None):
        LTsv_putdaytimenow()
        global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname
        global LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir
        global LTsvDOClaunch_outlist,LTsvDOClaunch_taglist,LTsvDOClaunch_timlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
        LTsvDOClaunch_kernel_clickID=LTsvDOClaunch_tsvcount
        LTsv_widget_disableenable(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],False)
        LTsvDOClaunch_outcount=0
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=10)
    return LTsvDOClaunch_kernel

if __name__=="__main__":
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
    if len(LTsv_GUI) > 0:
        LTsvDOC_ltsv=LTsv_loadfile("LTsv_doc.tsv"); LTsvDOC_config=LTsv_getpage(LTsvDOC_ltsv,"LTsv_doc")
        LTsvDOC_resizeW,LTsvDOC_resizeH,LTsvDOC_resizeT,LTsvDOC_resizeF=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(LTsvDOC_config,"window_size"),"width","height","wait","fontsize"))
        LTsvDOC_W,LTsvDOC_H=min(max(LTsv_intstr0x(LTsvDOC_resizeW),LTsv_global_glyphkbdW()),LTsv_screen_w() if LTsv_screen_w() > 0 else 1024),min(max(LTsv_intstr0x(LTsvDOC_resizeH),LTsv_global_glyphkbdH()),LTsv_screen_h() if LTsv_screen_w() > 0 else 768)
        LTsvDOC_T=min(max(LTsv_intstr0x(LTsvDOC_resizeT),10),1000)
        LTsvDOC_F=min(max(LTsv_intstr0x(LTsvDOC_resizeF),5),100)
        LTsvDOClaunch_tsvlistT=LTsv_readlinerest(LTsvDOC_config,"tsvlist","LTsv_doc.tsv"); LTsvDOClaunch_tsvlist=LTsvDOClaunch_tsvlistT.split('\t') if len(LTsvDOClaunch_tsvlistT) else []
        LTsvDOClaunch_modify=LTsv_readlinerest(LTsvDOC_config,"modify","@000y@0m@0dm@wdec@0h@0n@0s")
        LTsvDOC_font="{0},{1}".format("kan5x5comic",LTsvDOC_F//2); 
        LTsvDOC_window=LTsv_window_new(widget_t="LTsv_doc",widget_w=LTsvDOC_W,widget_h=LTsvDOC_H)
        LTsvDOC_button=[0]*len(LTsvDOClaunch_tsvlist)
        for LTsvDOClaunch_tsvcount,LTsvDOClaunch_tsvname in enumerate(LTsvDOClaunch_tsvlist):
            LTsvDOC_button[LTsvDOClaunch_tsvcount]=LTsv_button_new(LTsvDOC_window,widget_t=LTsvDOClaunch_tsvname,widget_x=0,widget_y=LTsvDOClaunch_tsvcount*LTsvDOC_F,widget_w=LTsvDOC_W,widget_h=LTsvDOC_F,widget_f=LTsvDOC_font,event_b=LTsvDOClaunch_shell(LTsvDOClaunch_tsvcount))
            if not os.path.isfile(os.path.normpath(LTsvDOClaunch_tsvname)):
                LTsv_widget_disableenable(LTsvDOC_button[LTsvDOClaunch_tsvcount],False)
        LTsv_widget_showhide(LTsvDOC_window,True)
        LTsv_window_main(LTsvDOC_window)
    else:
        LTsv_libc_printf("LTsv_GUI,LTsv_Notify→{0},{1}".format(LTsv_GUI,LTsv_Notify))
        LTsv_libc_printf("GUIの設定に失敗しました。")
    print("")
    print("__main__",LTsv_file_ver())

# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
