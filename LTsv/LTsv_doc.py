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

LTsvDOClaunch_tagseparate="*"
def LTsvDOClaunch_kernel_regularexpression(LTsvDOC_outname,LTsvDOC_tagnames):
    global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_maintag
    global LTsvDOClaunch_outlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
    LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagnames)
    LTsv_settimerCounter(0)
    if '\t' in LTsvDOC_tagpage:
        LTsvDOC_tagnamesL=LTsvDOC_tagnames.split(LTsvDOClaunch_tagseparate) if len(LTsvDOClaunch_tagseparate) > 0 else [LTsvDOC_tagnames]
        LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagnames,"".join(LTsvDOC_tagnamesL))
        for LTsvDOC_tagname in LTsvDOC_tagnamesL:
            if len(LTsvDOC_tagname) == 0: continue;
            LTsvDOC_tagdata=""
            LTsvDOC_tagcases=LTsvDOC_tagpage.rstrip('\n').split('\n')
            for LTsvDOC_tagcase in LTsvDOC_tagcases:
                LTsvDOC_casefirst=LTsv_readlinefirsts(LTsvDOC_tagcase)
                LTsvDOC_research=None
                try:
                    LTsvDOC_research=re.search(re.compile(LTsvDOC_casefirst),LTsvDOC_outname)
                except re.error:
                    continue
                else:
                    if LTsvDOC_research:
                        LTsvDOC_caserest=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_casefirst)
                        if len(LTsvDOC_caserest) > 0:
                            LTsvDOC_caseline=LTsv_getdaytimestr(LTsvDOC_caserest)
                            LTsvDOC_tagdata=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_caseline)
                            if len(LTsvDOC_tagdata) == 0 or '\t' in LTsvDOC_tagdata:
                                LTsvDOC_tagdata=LTsvDOC_caseline
                        break
            LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagname,LTsvDOC_tagdata)
    if len(LTsvDOC_tagpage) > 0:
         LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOC_tagnames,LTsvDOC_tagpage)
    return LTsvDOClaunch_main

def LTsvDOCdef_python(LTsvDOClaunch_deffile):
    LTsvDOClaunch_deffile=re.sub(re.compile(", +\\\\\n +",re.MULTILINE),", ",LTsvDOClaunch_deffile)
    LTsvDOClaunch_deffile=re.sub(re.compile("^(?!def).+$",re.MULTILINE),"",LTsvDOClaunch_deffile)
    LTsvDOClaunch_deffile=re.sub(re.compile("^\n",re.MULTILINE),"",LTsvDOClaunch_deffile)
    LTsvDOClaunch_deffile=re.sub(re.compile("^def ",re.MULTILINE),"",LTsvDOClaunch_deffile)
    LTsvDOClaunch_deffile=re.sub(re.compile("[:].*$",re.MULTILINE),"",LTsvDOClaunch_deffile)
    return LTsvDOClaunch_deffile

def LTsvDOCdef_LTSV(LTsvDOClaunch_deffile):
    LTsvDOClaunch_defnewfile=""
    LTsvDOClaunch_tsvpages=LTsv_readlinepages(LTsvDOClaunch_deffile)
    LTsvDOClaunch_tsvpagelist=LTsvDOClaunch_tsvpages.split('\t') if len(LTsvDOClaunch_tsvpages) else []
    if "L:Tsv" in LTsvDOClaunch_tsvpagelist: LTsvDOClaunch_tsvpagelist.remove("L:Tsv")
    for LTsvDOClaunch_tsvpagename in LTsvDOClaunch_tsvpagelist:
        LTsvDOClaunch_tsvpage=LTsv_getpage(LTsvDOClaunch_deffile,LTsvDOClaunch_tsvpagename)
        LTsvDOClaunch_pagefirsts=LTsv_readlinefirsts(LTsvDOClaunch_tsvpage)
        LTsvDOClaunch_pagefirstslist=LTsvDOClaunch_pagefirsts.split('\t') if len(LTsvDOClaunch_pagefirsts) else []
        for pagefirst in LTsvDOClaunch_pagefirstslist[:]:
            if ":" in pagefirst: LTsvDOClaunch_pagefirstslist.remove(pagefirst)
        LTsvDOClaunch_pagefirstslist=["[{0}|".format(LTsvDOClaunch_tsvpagename)]+LTsvDOClaunch_pagefirstslist
        LTsvDOClaunch_defnewfile+="\n".join(LTsvDOClaunch_pagefirstslist)+"\n"
    return LTsvDOClaunch_defnewfile

LTsvDOCdefextlist={".py":LTsvDOCdef_python,".tsv":LTsvDOCdef_LTSV,".ltsv":LTsvDOCdef_LTSV}
LTsvDOCbase64extlist=[".png",".gif",".jpg",".jpeg"]
def LTsvDOClaunch_kernel_listfile(LTsvDOC_outname,LTsvDOC_tagname):
    global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_maintag
    global LTsvDOClaunch_outlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
    LTsvDOC_tagdata=""
    LTsvDOC_defnameext=os.path.splitext(LTsvDOC_tagname)[1]
    if LTsvDOC_defnameext in LTsvDOCdefextlist:
        if not LTsvDOC_tagname in LTsvDOClaunch_deflist:
            LTsvDOClaunch_deffile=LTsv_loadfile(os.path.normpath(LTsvDOClaunch_defdir+"/"+LTsvDOC_tagname))
            LTsvDOClaunch_defpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
            LTsvDOClaunch_deffile=LTsvDOCdefextlist[LTsvDOC_defnameext](LTsvDOClaunch_deffile)
            LTsvDOC_defcases=LTsvDOClaunch_deffile.rstrip('\n').split('\n')
            LTsvDOClaunch_defnewpage=""
            for LTsvDOC_defname in LTsvDOC_defcases:
                LTsvDOClaunch_defrest=LTsv_readlinerest(LTsvDOClaunch_defpage,LTsvDOC_defname)
                LTsvDOClaunch_defnewpage=LTsv_pushlinerest(LTsvDOClaunch_defnewpage,LTsvDOC_defname,LTsvDOClaunch_defrest)
            LTsvDOClaunch_ltsv=LTsv_putpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname,LTsvDOClaunch_defnewpage)
            LTsvDOClaunch_deflist=LTsvDOClaunch_deflist+[LTsvDOC_tagname]
        LTsvDOC_tagpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
        LTsvDOC_tagcases=LTsvDOC_tagpage.rstrip('\n').split('\n')
        LTsvDOC_tagcasesLast=len(LTsvDOC_tagcases)-1
        for LTsvDOClaunch_tagcount,LTsvDOC_tagcase in enumerate(LTsvDOC_tagcases):
            LTsvDOC_casefirst=LTsv_readlinefirsts(LTsvDOC_tagcase)
            LTsvDOC_caserest=LTsv_readlinerest(LTsvDOC_tagpage,LTsvDOC_casefirst); LTsvDOC_caserest=LTsvDOC_caserest.rstrip('\t'); LTsvDOC_caserestL=LTsvDOC_caserest.split('\t')
            LTsvDOC_tagdata+="{0}{1}{2}{3}{4}{5}".format(LTsvDOClaunch_firstL,LTsvDOC_casefirst,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC.join(LTsvDOC_caserestL),LTsvDOClaunch_restR if LTsvDOClaunch_tagcount < LTsvDOC_tagcasesLast else LTsvDOClaunch_restRLast)
    elif LTsvDOC_defnameext in LTsvDOCbase64extlist:
        if not LTsvDOC_tagname in LTsvDOClaunch_deflist:
            LTsvDOClaunch_defpage=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname)
            if len(LTsvDOClaunch_defpage) == 0:
                LTsvDOC_tagdata=LTsv_64load(os.path.normpath(LTsvDOClaunch_defdir+"/"+LTsvDOC_tagname))
                LTsvDOClaunch_ltsv=LTsv_putpage(LTsvDOClaunch_ltsv,LTsvDOC_tagname,LTsvDOC_tagdata)
            LTsvDOClaunch_deflist=LTsvDOClaunch_deflist+[LTsvDOC_tagname]
    LTsvDOClaunch_main=LTsvDOClaunch_main.replace("{0}{1}{2}".format(LTsvDOClaunch_deftagL,LTsvDOC_tagname,LTsvDOClaunch_deftagR),LTsvDOC_tagdata)
    return LTsvDOClaunch_main

def LTsvDOClaunch_kernel_listdir(LTsvDOC_outname,LTsvDOC_tagname):
    global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_maintag
    global LTsvDOClaunch_outlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
    return LTsvDOClaunch_main

LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_maintag="","","",""
LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir,LTsvDOClaunch_defdir=0,0,"",""
LTsvDOClaunch_outlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist=[],[],[]
LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR="<！",">"
LTsvDOClaunch_firstL,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC,LTsvDOClaunch_restR,LTsvDOClaunch_restRLast="【","】","  ","\n  ","\n",""
LTsvDOClaunch_LTsvver="<！L:TsvLTsvver>"
def LTsvDOClaunch_kernel_count(window_objvoid=None,window_objptr=None):
    global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_maintag
    global LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir,LTsvDOClaunch_defdir
    global LTsvDOClaunch_tagseparate
    global LTsvDOClaunch_outlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
    global LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR
    global LTsvDOClaunch_firstL,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC,LTsvDOClaunch_restR,LTsvDOClaunch_restRLast
    global LTsvDOClaunch_LTsvver
    if LTsvDOClaunch_outcount < 0:
        LTsvDOClaunch_tsvname=LTsvDOClaunch_tsvlist[LTsvDOClaunch_kernel_clickID]
        LTsvDOClaunch_ltsv=LTsv_loadfile(os.path.normpath(LTsvDOClaunch_tsvname))
        LTsvDOClaunch_headtag="L:Tsv"
        LTsvDOClaunch_head=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOClaunch_headtag)
        LTsvDOClaunch_configtag=LTsv_readlinerest(LTsvDOClaunch_head,"1st","LTsv_doc")
        LTsvDOClaunch_config=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOClaunch_configtag)
        LTsvDOClaunch_outdir=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"outdir",os.path.dirname(os.path.normpath(LTsvDOClaunch_tsvname))))
        LTsvDOClaunch_defdir=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"defdir",os.path.dirname(os.path.normpath(LTsvDOClaunch_tsvname))))
        LTsvDOClaunch_maintag=os.path.normpath(LTsv_readlinerest(LTsvDOClaunch_config,"main","LTsv_doc_main"))
        LTsvDOClaunch_main=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOClaunch_maintag,"<#LTsv_doc_main>")
        LTsvDOClaunch_tagseparate=LTsv_readlinerest(LTsvDOClaunch_config,"tagseparate","*")
        LTsvDOClaunch_outlistT=LTsv_readlinerest(LTsvDOClaunch_config,"outlist"); LTsvDOClaunch_outlist=LTsvDOClaunch_outlistT.split('\t') if len(LTsvDOClaunch_outlistT) else []
        LTsvDOClaunch_deftagL,LTsvDOClaunch_deftagR=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(LTsvDOClaunch_config,"deftag","L:<！\tR:>"),"L","R"),2)
        LTsvDOClaunch_firstL,LTsvDOClaunch_firstR,LTsvDOClaunch_restL,LTsvDOClaunch_restC,LTsvDOClaunch_restR,LTsvDOClaunch_restRLast=LTsv_tsv2list(LTsv_unziptuplelabelsdata(LTsv_readlinerest(LTsvDOClaunch_config,"defindent","firstL:<！firstL>\tfirstR:<！firstR>\trestL:<！restL>\trestC:<！restC>\trestR:<！restR>\trestRLast:<！restRLast>"),"firstL","firstR","restL","restC","restR","restRLast"),6)
        LTsvDOClaunch_LTsvver=LTsv_readlinerest(LTsvDOClaunch_config,"LTsvver","<！L:TsvLTsvver>")
        LTsvDOClaunch_pages=LTsv_readlinepages(LTsvDOClaunch_ltsv)
        LTsvDOClaunch_pages=LTsv_setdatanum(LTsvDOClaunch_pages,LTsv_pickdatafind(LTsvDOClaunch_pages,LTsvDOClaunch_maintag))
        LTsvDOClaunch_skplistT=LTsv_readlinerest(LTsvDOClaunch_config,"skplist"); LTsvDOClaunch_skplist=LTsvDOClaunch_skplistT.split('\t') if len(LTsvDOClaunch_skplistT) else []
        LTsvDOClaunch_skplist.extend([LTsvDOClaunch_headtag,LTsvDOClaunch_configtag,LTsvDOClaunch_maintag])
        for skplist in LTsvDOClaunch_skplist:
            LTsvDOClaunch_pages=LTsv_setdatanum(LTsvDOClaunch_pages,LTsv_pickdatafind(LTsvDOClaunch_pages,skplist))
        LTsvDOClaunch_reglist=LTsvDOClaunch_pages.split('\t') if len(LTsvDOClaunch_pages) else []
        LTsvDOClaunch_outcount=0
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=LTsvDOC_T)
    elif 0 <= LTsvDOClaunch_outcount < len(LTsvDOClaunch_outlist):
        LTsvDOC_outname=LTsvDOClaunch_outlist[LTsvDOClaunch_outcount]
        LTsv_widget_settext(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],"{0}→{1}".format(LTsvDOClaunch_tsvname,LTsvDOC_outname))
        for LTsvDOC_tagnames in LTsvDOClaunch_reglist:
            if os.path.isfile(LTsvDOClaunch_defdir+"/"+LTsvDOC_tagnames):
                LTsvDOClaunch_main=LTsvDOClaunch_kernel_listfile(LTsvDOC_outname,LTsvDOC_tagnames)
            elif os.path.isdir(LTsvDOClaunch_defdir+"/"+LTsvDOC_tagnames):
                LTsvDOClaunch_main=LTsvDOClaunch_kernel_listdir(LTsvDOC_outname,LTsvDOC_tagnames)
            else:
                LTsvDOClaunch_main=LTsvDOClaunch_kernel_regularexpression(LTsvDOC_outname,LTsvDOC_tagnames)
        LTsvDOClaunch_main=LTsvDOClaunch_main.replace(LTsvDOClaunch_LTsvver,LTsv_file_ver())
        LTsv_saveplain(os.path.normpath(LTsvDOClaunch_outdir+"/"+LTsvDOC_outname),LTsvDOClaunch_main)
        LTsvDOClaunch_outcount+=1
        LTsvDOClaunch_main=LTsv_getpage(LTsvDOClaunch_ltsv,LTsvDOClaunch_maintag)
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=LTsvDOC_T)
    else:
        if len(LTsvDOClaunch_deflist) > 0:
            LTsv_savefile(os.path.normpath(LTsvDOClaunch_tsvname),LTsvDOClaunch_ltsv)
        LTsv_widget_disableenable(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],True)
        LTsv_widget_settext(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],"{0}({1})".format(LTsvDOClaunch_tsvname,LTsv_getdaytimestr(LTsvDOClaunch_modify)))

def LTsvDOClaunch_shell(LTsvDOClaunch_tsvcount):
    def LTsvDOClaunch_kernel(window_objvoid=None,window_objptr=None):
        LTsv_putdaytimenow()
        global LTsvDOClaunch_ltsv,LTsvDOClaunch_tsvname,LTsvDOClaunch_main,LTsvDOClaunch_maintag
        global LTsvDOClaunch_kernel_clickID,LTsvDOClaunch_outcount,LTsvDOClaunch_outdir,LTsvDOClaunch_defdir
        global LTsvDOClaunch_outlist,LTsvDOClaunch_reglist,LTsvDOClaunch_deflist
        LTsvDOClaunch_kernel_clickID=LTsvDOClaunch_tsvcount
        LTsv_widget_disableenable(LTsvDOC_button[LTsvDOClaunch_kernel_clickID],False)
        LTsvDOClaunch_outcount=-1
        LTsvDOClaunch_deflist=[]
        LTsv_window_after(LTsvDOC_window,event_b=LTsvDOClaunch_kernel_count,event_i="LTsvDOClaunch_kernel_main",event_w=10)
    return LTsvDOClaunch_kernel

if __name__=="__main__":
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_GUI=LTsv_guiinit()
    if len(LTsv_GUI) > 0:
        LTsvDOC_ltsv=LTsv_loadfile("LTsv_doc.tsv")
        LTsvDOC_head=LTsv_getpage(LTsvDOC_ltsv,"L:Tsv")
        LTsvDOC_config=LTsv_getpage(LTsvDOC_ltsv,"LTsv_doc")
        LTsvDOC_resizeW,LTsvDOC_resizeH,LTsvDOC_resizeT,LTsvDOC_resizeF=LTsv_tsv2tuple(LTsv_unziptuplelabelsdata(LTsv_readlinerest(LTsvDOC_config,"window_size"),"width","height","wait","fontsize"))
        LTsvDOC_W,LTsvDOC_H=min(max(LTsv_intstr0x(LTsvDOC_resizeW),LTsv_global_glyphkbdW()),LTsv_screen_w() if LTsv_screen_w() > 0 else 1024),min(max(LTsv_intstr0x(LTsvDOC_resizeH),LTsv_global_glyphkbdH()),LTsv_screen_h() if LTsv_screen_w() > 0 else 768)
        LTsvDOC_T=min(max(LTsv_intstr0x(LTsvDOC_resizeT),10),1000)
        LTsvDOC_F=min(max(LTsv_intstr0x(LTsvDOC_resizeF),5),100)
        LTsvDOClaunch_tsvlistT=LTsv_readlinerest(LTsvDOC_config,"tsvlist","LTsv_doc.tsv"); LTsvDOClaunch_tsvlist=LTsvDOClaunch_tsvlistT.split('\t') if len(LTsvDOClaunch_tsvlistT) else []
        LTsvDOClaunch_modify=LTsv_readlinerest(LTsvDOC_config,"modify","@000y@0m@0dm@wdec@0h@0n@0s")
        LTsvDOC_font="{0},{1}".format("kan5x5comic",LTsvDOC_F//2); 
        LTsvDOC_window=LTsv_window_new(widget_t="LTsv_doc",event_b=LTsv_window_exit,widget_w=LTsvDOC_W,widget_h=LTsvDOC_H)
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
