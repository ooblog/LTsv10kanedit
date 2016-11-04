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
from LTsv_calc    import *
#from LTsv_joy     import *
#from LTsv_kbd     import *
from LTsv_gui     import *
from LTsv_glyph  import *


def LTsvDOCdef_python(LTsvDOClaunch_deffile):
    LTsvDOClaunch_deffile=re.sub(re.compile("^(?!def).+$",re.MULTILINE),"",LTsvDOClaunch_deffile)
    LTsvDOClaunch_deffile=re.sub(re.compile("^\n",re.MULTILINE),"",LTsvDOClaunch_deffile)
    LTsvDOClaunch_deffile=re.sub(re.compile("^def ",re.MULTILINE),"",LTsvDOClaunch_deffile)
    LTsvDOClaunch_deffile=re.sub(re.compile("[:].*$",re.MULTILINE),"",LTsvDOClaunch_deffile)
    return LTsvDOClaunch_deffile

def LTsvDOClaunch_kernel_plane(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname):
    LTsvDOC_tagdata=LTsvDOC_tagname
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
    LTsvDOC_tagline=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_outname)
    LTsvDOC_tagdata=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagline)
    if len(LTsvDOC_tagdata) == 0:
        LTsvDOC_tagdata=LTsvDOC_tagline
    LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagname,LTsvDOC_tagdata)
    return LTsvDOClaunch_main

def LTsvDOClaunch_kernel_timedata(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname):
    LTsvDOC_tagdata=LTsvDOC_tagname
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
    LTsvDOC_tagline=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_outname)
    LTsvDOC_tagline=LTsv_getdaytimestr(LTsvDOC_tagline)
    LTsvDOC_tagdata=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagline)
    if len(LTsvDOC_tagdata) == 0:
        LTsvDOC_tagdata=LTsvDOC_tagline
    LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagname,LTsvDOC_tagdata)
    return LTsvDOClaunch_main

def LTsvDOClaunch_kernel_regularexpression(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname):
    LTsvDOC_tagdata=LTsvDOC_tagname
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
    LTsvDOC_tagcases=LTsvDOC_tagpage.split('\n')
    for LTsvDOC_tagcase in LTsvDOC_tagcases:
        if len(LTsvDOC_tagcase) == 0: continue;
        LTsvDOC_casefirst=LTsv_readlinefirsts(LTsvDOC_tagcase)
        LTsvDOC_research=None
        try:
            LTsvDOC_research=re.search(re.compile(LTsvDOC_casefirst),LTsvDOC_outname)
        except re.error:
            continue
        else:
            if LTsvDOC_research:
                LTsvDOC_caseline=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_casefirst)
                LTsvDOC_tagdata=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_caseline)
                if len(LTsvDOC_tagdata) == 0:
                    LTsvDOC_tagdata=LTsvDOC_caseline;
                LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagname,LTsvDOC_tagdata)
    return LTsvDOClaunch_main

def LTsvDOClaunch_kernel_deflist(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_tagname,LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR):
    global LTsvDOClaunch_firstL,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC,LTsvDOClaunch_restR
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
    LTsvDOC_tagdata=""
    LTsvDOC_tagcases=LTsvDOC_tagpage.split('\n')
    for LTsvDOC_tagcase in LTsvDOC_tagcases:
        if len(LTsvDOC_tagcase) == 0: continue;
        LTsvDOC_casefirst=LTsv_readlinefirsts(LTsvDOC_tagcase)
        LTsvDOC_caserest=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_casefirst)
        LTsvDOC_caserest=LTsvDOC_caserest.split('\t')
        LTsvDOC_tagdata+="{0}{1}{2}\n{3}{4}{5}\n".format(LTsvDOClaunch_firstL,LTsvDOC_casefirst,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC.join(LTsvDOC_caserest),LTsvDOClaunch_restR)
    LTsvDOC_tagdata=LTsvDOC_tagdata.rstrip('\n')
    LTsvDOClaunch_main=LTsvDOClaunch_main.replace("{0}{1}{2}".format(LTsvDOClaunch_deftagL,LTsvDOC_tagname,LTsvDOClaunch_deftagR),LTsvDOC_tagdata)
    return LTsvDOClaunch_main

LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_main_defindent="","","",2
LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir,LTsvDOClaunch_defdir=0,0,"",""
LTsvDOClaunch_outlist,LTsvDOClaunch_taglist,LTsvDOClaunch_timlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist=[],[],[],[],[]
LTsvDOClaunch_defpage,LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR="","",""
LTsvDOClaunch_firstL,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC,LTsvDOClaunch_restR="【","】","  ","\n  ","\n"
def LTsvDOClaunch_kernel_count(window_objvoid=None,window_objptr=None):
    global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_main_defindent
    global LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir,LTsvDOClaunch_defdir
    global LTsvDOClaunch_outlist,LTsvDOClaunch_taglist,LTsvDOClaunch_timlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
    global LTsvDOClaunch_defpage,LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR
    global LTsvDOClaunch_firstL,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC,LTsvDOClaunch_restR
    if LTsvDOClaunch_outcount < 0:
        LTsvDOClaunch_tsvname=LTsvDOClaunch_tsvlist[LTsvDOClaunch_kernel_clickID]
        LTsvDOClaunch_ltsv=LTsv_loadfile(os.path.normpath(LTsvDOClaunch_tsvname))
        LTsvDOClaunch_headtag="L:Tsv"
        LTsvDOClaunch_head=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOClaunch_headtag)
        LTsvDOClaunch_configtag=LTsv_readlinerest(LTsvDOClaunch_head,"1st","LTsvDOC_tsv")
        LTsvDOClaunch_config=LTsv_getpage(LTsvDOClaunch_ltsv,LTsv_readlinerest(LTsvDOClaunch_head,"1st",LTsvDOClaunch_configtag))
        LTsvDOClaunch_skplistT=LTsv_readlinerest(LTsvDOClaunch_config,"skplist"); LTsvDOClaunch_skplist=LTsvDOClaunch_skplistT.split('\t') if len(LTsvDOClaunch_skplistT) else []
        LTsvDOClaunch_skplist.extend([LTsvDOClaunch_headtag,LTsvDOClaunch_configtag])
#        print(LTsvDOClaunch_skplist)
        LTsvDOClaunch_pages=LTsv_readlinepages(LTsvDOClaunch_ltsv)
#        print(LTsvDOClaunch_pages)
        for skplist in LTsvDOClaunch_skplist:
            LTsvDOClaunch_pages=LTsv_setdatanum(LTsvDOClaunch_pages,LTsv_pickdatafind(LTsvDOClaunch_pages,skplist))
#        print("--\n",LTsvDOClaunch_pages)
        LTsvDOClaunch_outdir=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"outdir",os.path.dirname(os.path.normpath(LTsvDOClaunch_tsvname))))
        LTsvDOClaunch_defdir=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"defdir",os.path.dirname(os.path.normpath(LTsvDOClaunch_tsvname))))
        LTsvDOClaunch_mainname=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"main","LTsv_doc_main"))
        LTsvDOClaunch_main=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOClaunch_mainname)
        LTsvDOClaunch_outlistT=LTsv_readlinerest(LTsvDOClaunch_config,"outlist"); LTsvDOClaunch_outlist=LTsvDOClaunch_outlistT.split('\t') if len(LTsvDOClaunch_outlistT) else []
        LTsvDOClaunch_taglistT=LTsv_readlinerest(LTsvDOClaunch_config,"taglist"); LTsvDOClaunch_taglist=LTsvDOClaunch_taglistT.split('\t') if len(LTsvDOClaunch_taglistT) else []
        LTsvDOClaunch_timlistT=LTsv_readlinerest(LTsvDOClaunch_config,"timlist"); LTsvDOClaunch_timlist=LTsvDOClaunch_timlistT.split('\t') if len(LTsvDOClaunch_timlistT) else []
        LTsvDOClaunch_reglistT=LTsv_readlinerest(LTsvDOClaunch_config,"reglist"); LTsvDOClaunch_reglist=LTsvDOClaunch_reglistT.split('\t') if len(LTsvDOClaunch_reglistT) else []
        LTsvDOClaunch_deflistT=LTsv_readlinerest(LTsvDOClaunch_config,"deflist"); LTsvDOClaunch_deflist=LTsvDOClaunch_deflistT.split('\t') if len(LTsvDOClaunch_deflistT) else []
        LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(LTsvDOClaunch_config,"deftag"),"L","R"))
        LTsvDOClaunch_firstL,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC,LTsvDOClaunch_restR=LTsv_tsv2list(LTsv_unziptuplelabelsdata(LTsv_readlinerest(LTsvDOClaunch_config,"defindent"),"firstL","firstR","restL","restC","restR"),5)
        LTsvDOClaunch_firstL=LTsvDOClaunch_firstL.replace('\\n','\n').replace('\\t','\t')
        LTsvDOClaunch_firstR=LTsvDOClaunch_firstR.replace('\\n','\n').replace('\\t','\t')
        LTsvDOClaunch_restL=LTsvDOClaunch_restL.replace('\\n','\n').replace('\\t','\t')
        LTsvDOClaunch_restC=LTsvDOClaunch_restC.replace('\\n','\n').replace('\\t','\t')
        LTsvDOClaunch_restR=LTsvDOClaunch_restR.replace('\\n','\n').replace('\\t','\t')
        for LTsvDOC_defcount,LTsvDOC_defname in enumerate(LTsvDOClaunch_deflist):
            LTsvDOClaunch_defnewpage=""
            LTsvDOClaunch_defpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_defname)
            LTsvDOClaunch_deffile=LTsv_loadfile(os.path.normpath(LTsvDOClaunch_defdir+"/"+LTsvDOC_defname))
            LTsvDOClaunch_deffile=LTsvDOCdef_python(LTsvDOClaunch_deffile)
            LTsvDOC_defcases=LTsvDOClaunch_deffile.split('\n')
            for LTsvDOC_defcase in LTsvDOC_defcases:
                if len(LTsvDOC_defcase) == 0: continue;
                LTsvDOClaunch_defrest=LTsv_readlinerest(LTsvDOClaunch_defpage,LTsvDOC_defcase)
                LTsvDOClaunch_defnewpage=LTsv_pushlinerest(LTsvDOClaunch_defnewpage,LTsvDOC_defcase,LTsvDOClaunch_defrest,)
            LTsvDOClaunch_ltsv=LTsv_putpage(LTsvDOClaunch_ltsv,LTsvDOC_defname,LTsvDOClaunch_defnewpage)
            LTsv_savefile(os.path.normpath(LTsvDOClaunch_tsvname),LTsvDOClaunch_ltsv)
        LTsvDOClaunch_outcount=0
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=LTsvDOC_T)
#    for LTsvDOC_outcount,LTsvDOC_outname in enumerate(LTsvDOClaunch_outlist):
    if 0 <= LTsvDOClaunch_outcount < len(LTsvDOClaunch_outlist):
        LTsvDOC_outname=LTsvDOClaunch_outlist[LTsvDOClaunch_outcount]
        LTsv_widget_settext(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],"{0}→{1}".format(LTsvDOClaunch_tsvname,LTsvDOC_outname))
        for LTsvDOC_tagname in LTsvDOClaunch_taglist:
            LTsvDOClaunch_main=LTsvDOClaunch_kernel_plane(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname)
        for LTsvDOC_tagname in LTsvDOClaunch_reglist:
            LTsvDOClaunch_main=LTsvDOClaunch_kernel_regularexpression(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname)
        for LTsvDOC_defname in LTsvDOClaunch_deflist:
            LTsvDOClaunch_main=LTsvDOClaunch_kernel_deflist(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_defname,LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR)
        for LTsvDOC_tagname in LTsvDOClaunch_timlist:
            LTsvDOClaunch_main=LTsvDOClaunch_kernel_timedata(LTsvDOClaunch_ltsv,LTsvDOClaunch_main,LTsvDOC_outname,LTsvDOC_tagname)
        if len(LTsvDOClaunch_deflist) > 0:
            LTsv_saveplain(os.path.normpath(LTsvDOClaunch_outdir+"/"+LTsvDOC_outname),LTsvDOClaunch_main)
        LTsvDOClaunch_outcount+=1
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=LTsvDOC_T)
    else:
        LTsv_widget_disableenable(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],True)
        LTsv_widget_settext(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],"{0}({1})".format(LTsvDOClaunch_tsvname,LTsv_getdaytimestr(LTsvDOClaunch_modify)))

def LTsvDOClaunch_shell(LTsvDOClaunch_tsvcount):
    def LTsvDOClaunch_kernel(window_objvoid=None,window_objptr=None):
        LTsv_putdaytimenow()
        global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_main_defindent
        global LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir,LTsvDOClaunch_defdir
        global LTsvDOClaunch_outlist,LTsvDOClaunch_taglist,LTsvDOClaunch_timlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
        LTsvDOClaunch_kernel_clickID=LTsvDOClaunch_tsvcount
        LTsv_widget_disableenable(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],False)
        LTsvDOClaunch_outcount=-1
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=10)
    return LTsvDOClaunch_kernel

if __name__=="__main__":
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
    if len(LTsv_GUI) > 0:
        LTsvDOC_ltsv=LTsv_loadfile("LTsv_doc.tsv")
        LTsvDOC_head=LTsv_getpage(LTsvDOClaunch_ltsv,"L:Tsv")
        LTsvDOC_config=LTsv_getpage(LTsvDOC_ltsv,LTsv_readlinerest(LTsvDOC_head,"1st","LTsvDOC_tsv"))
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
