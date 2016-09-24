#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
if sys.version_info.major == 2:
    import urllib
if sys.version_info.major == 3:
    import urllib.request
import zipfile
import datetime
import re
from LTsv_time import *

def LTsv_newfile(LTsv_program,LTsv_default=None):
    LTsv_1st="" if LTsv_default is None else LTsv_default
    LTsv_text= "[L:Tsv|\n" \
               "code\tUTF-8\n" \
               "enter\tLF\n" \
               "tab\t8\n"
    if len(LTsv_program) > 0:
        LTsv_text+="program\t{0}\n".format(LTsv_program)
    if len(LTsv_1st) > 0:
        LTsv_text+="1st\t{0}\n".format(LTsv_1st)
    LTsv_text+="LTsvver\t{0}\n".format(LTsv_file_ver())
    LTsv_text+="modify\t{0}\n".format(LTsv_getdaytimestr(overhour=24,diffminute=0))
    LTsv_text+="|L:Tsv]\n"
    return LTsv_text

def LTsv_download(LTsv_url,LTsv_path,LTsv_reporthook=None):
    if sys.version_info.major == 2:
        urllib.urlretrieve(LTsv_url,LTsv_path,LTsv_reporthook)
    if sys.version_info.major == 3:
        urllib.request.urlretrieve(LTsv_url,LTsv_path,LTsv_reporthook)

def LTsv_zipload(LTsv_zip,LTsv_name,LTsv_path):
    LTsv_ZipFile=None
    if sys.version_info.major == 2:
        try:
            LTsv_ZipFile=zipfile.ZipFile(LTsv_zip,'r')
            LTsv_ziplist=LTsv_ZipFile.namelist()
        except zipfile.BadZipfile as err:
            pass
    if sys.version_info.major == 3:
        try:
            LTsv_ZipFile=zipfile.ZipFile(LTsv_zip,'r')
            LTsv_ziplist=LTsv_ZipFile.namelist()
        except zipfile.BadZipFile as err:
            pass
    if LTsv_ZipFile != None:
        LTsv_nameLU=None       if not LTsv_name         in LTsv_ziplist else LTsv_name
        LTsv_nameLU=LTsv_nameLU if not LTsv_name.upper() in LTsv_ziplist else LTsv_name.upper()
        LTsv_nameLU=LTsv_nameLU if not LTsv_name.lower() in LTsv_ziplist else LTsv_name.lower()
        if LTsv_nameLU != None:
            with open(LTsv_path,'wb') as LTsv_fobj:
                LTsv_fobj.write(LTsv_ZipFile.read(LTsv_nameLU))

def LTsv_loadfile(LTsv_path,LTsv_default=None):
    LTsv_text="" if LTsv_default is None else LTsv_default
    if os.path.isfile(LTsv_path):
        if os.path.getsize(LTsv_path)!=len(LTsv_text.encode('utf-8')):
            if sys.version_info.major == 2:
                with open(LTsv_path,"r") as LTsv_fobj:
                    LTsv_byte=LTsv_fobj.read()
                LTsv_text=unicode(LTsv_byte,"utf-8",errors="xmlcharrefreplace")
            if sys.version_info.major == 3:
                with open(LTsv_path,mode="r",encoding="utf-8",errors="xmlcharrefreplace") as LTsv_fobj:
                    LTsv_text=LTsv_fobj.read()
            if not LTsv_text.endswith('\n'):
                LTsv_text+='\n'
    return LTsv_text

def LTsv_loadcp932file(LTsv_path,LTsv_default="cp932"):
    LTsv_text=""
    if os.path.isfile(LTsv_path):
        if sys.version_info.major == 2:
            with open(LTsv_path,"r") as LTsv_fobj:
                LTsv_byte=LTsv_fobj.read()
            LTsv_text=unicode(LTsv_byte,LTsv_default,errors="xmlcharrefreplace")
        if sys.version_info.major == 3:
            with open(LTsv_path,mode="r",encoding=LTsv_default,errors="xmlcharrefreplace") as LTsv_fobj:
                LTsv_text=LTsv_fobj.read()
        if not LTsv_text.endswith('\n'):
            LTsv_text+='\n'
    return LTsv_text

def LTsv_readlinepages(LTsv_text):
    LTsv_line=""
    for ltsv_tag in re.findall(re.compile("^\[(.+?)\|$",re.MULTILINE),LTsv_text):
        LTsv_line+='\t'+ltsv_tag
    LTsv_line=LTsv_line.lstrip('\t')
    return LTsv_line

def LTsv_getpage(LTsv_text,LTsv_tag,LTsv_default=None):
    LTsv_page="" if LTsv_default is None else LTsv_default
    LTsv_tagL="[{0}|\n".format(LTsv_tag); LTsv_tagR="|{0}]\n".format(LTsv_tag)
    if len(LTsv_tag) > 0:
        LTsv_posL=LTsv_text.find(LTsv_tagL); LTsv_posR=LTsv_text.find(LTsv_tagR)
        if 0 <= LTsv_posL < LTsv_posR <= len(LTsv_text):
            LTsv_page=LTsv_text[LTsv_posL+len(LTsv_tagL):LTsv_posR]
    return LTsv_page

def LTsv_readlinedeno(LTsv_text):
    if len(LTsv_text) > 0:
        LTsv_linedeno=LTsv_text.count('\n')
        if not LTsv_text.endswith('\n'):
            LTsv_linedeno+=1
    else:
        LTsv_linedeno=0
    return LTsv_linedeno

def LTsv_readlinenum(LTsv_text,LTsv_linenum,LTsv_default=None):
    LTsv_line="" if LTsv_default is None else LTsv_default
    LTsv_splits=LTsv_text.rstrip('\n').split('\n')
    if 0 <= LTsv_linenum < len(LTsv_splits):
        LTsv_line=LTsv_splits[LTsv_linenum]
    return LTsv_line

def LTsv_readlinefirsts(LTsv_text):
    LTsv_line=""; LTsv_splits=LTsv_text.strip('\n').split('\n')
    for LTsv_split in LTsv_splits:
        LTsv_posR=LTsv_split.find('\t')
        if LTsv_posR >= 0:
            LTsv_line+='\t'+LTsv_split[0:LTsv_posR]
        else:
            LTsv_posR=LTsv_split
    LTsv_line=LTsv_line.lstrip('\t')
    return LTsv_line

def LTsv_readlinerest(LTsv_text,LTsv_first,LTsv_default=None):
    LTsv_rest="" if LTsv_default is None else LTsv_default
    LTsv_page='\n'+LTsv_text+'\n'; LTsv_tagL='\n'+LTsv_first+'\t'
    LTsv_posL=LTsv_page.find(LTsv_tagL); LTsv_posR=LTsv_page.find('\n',LTsv_posL+len(LTsv_tagL))
    if 0 <= LTsv_posL < LTsv_posR <= len(LTsv_page):
        LTsv_rest=LTsv_page[LTsv_posL+len(LTsv_tagL):LTsv_posR]
    return LTsv_rest.lstrip('\t')

def LTsv_pickdatadeno(LTsv_line):
    LTsv_datadeno=0; LTsv_splits=LTsv_line.replace('\n','\t').split('\t')
    for LTsv_split in LTsv_splits:
        if len(LTsv_split) > 0:
            LTsv_datadeno+=1
    return LTsv_datadeno

def LTsv_pickdatanum(LTsv_line,LTsv_datanum,LTsv_default=None):
    LTsv_data="" if LTsv_default is None else LTsv_default
    LTsv_datadeno=0; LTsv_splits=LTsv_line.replace('\n','\t').split('\t')
    for LTsv_split in LTsv_splits:
        if len(LTsv_split) > 0:
            if LTsv_datanum == LTsv_datadeno:
                LTsv_data=LTsv_split
                break
            LTsv_datadeno+=1
    return LTsv_data

def LTsv_split_label_data(LTsv_labeldata,LTsv_seldata=True):
    LTsv_data=LTsv_labeldata
    LTsv_posL=LTsv_labeldata.find(':')
    if LTsv_posL > 0:
        if LTsv_seldata:
            LTsv_data=LTsv_labeldata[LTsv_posL+len(':'):]
        else:
            LTsv_data=LTsv_labeldata[:LTsv_posL]
    return LTsv_data

def LTsv_pickdatas(LTsv_line,LTsv_dataL=0,LTsv_dataR=0):
    LTsv_datas=""
    LTsv_low,LTsv_high=(LTsv_dataL,LTsv_dataR) if LTsv_dataL <= LTsv_dataR else (LTsv_dataR,LTsv_dataL)
    LTsv_high=LTsv_high if LTsv_low < LTsv_high else LTsv_high+1
    LTsv_datadeno=0; LTsv_splits=LTsv_line.replace('\n','\t').split('\t')
    for LTsv_split in LTsv_splits:
        if len(LTsv_split) > 0:
            if LTsv_low <= LTsv_datadeno:
                LTsv_datas+=LTsv_split+'\t'
            LTsv_datadeno+=1
            if LTsv_high <= LTsv_datadeno:
                break
    return LTsv_datas.strip('\t')

def LTsv_pickdatafind(LTsv_line,LTsv_find):
    LTsv_datadeno=0; LTsv_splits=LTsv_line.replace('\n','\t').split('\t'); LTsv_datanum=-1
    for LTsv_split in LTsv_splits:
        if len(LTsv_split) > 0:
            if LTsv_find == LTsv_split:
                LTsv_datanum=LTsv_datadeno
                break
            LTsv_datadeno+=1
    return LTsv_datanum

def LTsv_joindatanum(LTsv_line,LTsv_datanum,LTsv_default=None):
    LTsv_data="" if LTsv_default is None else LTsv_default.replace('\n','\t')
    if len(LTsv_data) > 0:
        if not LTsv_data.startswith('\t'):
            LTsv_data='\t'+LTsv_data
    LTsv_datadeno=0; LTsv_splits=LTsv_line.replace('\n','\t').split('\t'); LTsv_join=""
    if LTsv_datanum < 0:
        LTsv_join+=LTsv_data
    for LTsv_split in LTsv_splits:
        if len(LTsv_split) > 0:
            if LTsv_datanum == LTsv_datadeno:
                LTsv_join+=LTsv_data
            LTsv_join+='\t'+LTsv_split
            LTsv_datadeno+=1
    if LTsv_datadeno <= LTsv_datanum:
        LTsv_join+=LTsv_data
    return LTsv_join.strip('\t')

def LTsv_setdatanum(LTsv_line,LTsv_datanum,LTsv_default=None):
    LTsv_data="" if LTsv_default is None else LTsv_default.replace('\n','\t')
    if len(LTsv_data) > 0:
        if not LTsv_data.startswith('\t'):
            LTsv_data='\t'+LTsv_data
    LTsv_datadeno=0; LTsv_splits=LTsv_line.replace('\n','\t').split('\t'); LTsv_join=""
    for LTsv_split in LTsv_splits:
        if len(LTsv_split) > 0:
            if LTsv_datanum == LTsv_datadeno:
                LTsv_join+=LTsv_data
            else:
                LTsv_join+='\t'+LTsv_split
            LTsv_datadeno+=1
    return LTsv_join.strip('\t')

def LTsv_pickdatalabel(LTsv_line,LTsv_label,LTsv_default=None):
    LTsv_data="" if LTsv_default is None else LTsv_default
    LTsv_splits='\t'+LTsv_line.replace('\n','\t')+'\t'; LTsv_tagL='\t'+LTsv_label+":"
    LTsv_posL=LTsv_splits.find(LTsv_tagL); LTsv_posR=LTsv_splits.find('\t',LTsv_posL+len(LTsv_tagL))
    if 0 <= LTsv_posL < LTsv_posR <= len(LTsv_splits):
        LTsv_data=LTsv_splits[LTsv_posL+len(LTsv_tagL):LTsv_posR]
    return LTsv_data

def LTsv_pickdic(LTsv_text,LTsv_first,LTsv_label):
    LTsv_data=""
    LTsv_page='\n'+LTsv_text+'\n'
    LTsv_tagL='\n'+LTsv_first+'\t'; LTsv_posL=LTsv_page.find(LTsv_tagL)
    if 0 <= LTsv_posL:
        LTsv_rest='\t'+LTsv_page[LTsv_posL+len(LTsv_tagL):LTsv_page.find('\n',LTsv_posL+1)]+'\t'
        LTsv_tagR='\t'+LTsv_label+":"; LTsv_posR=LTsv_rest.find(LTsv_tagR)
        if 0 <= LTsv_posR:
            LTsv_data=LTsv_rest[LTsv_posR+len(LTsv_tagR):LTsv_rest.find('\t',LTsv_posR+1)]
    return LTsv_data

def LTsv_setdatalabel(LTsv_line,LTsv_label,LTsv_default=None):
    LTsv_data="" if LTsv_default is None else LTsv_pickdatanum(LTsv_default,0)
    LTsv_join=LTsv_line; LTsv_splits='\t'+LTsv_line.replace('\n','\t')+'\t'; LTsv_tagL='\t'+LTsv_label+":"
    LTsv_posL=LTsv_splits.find(LTsv_tagL); LTsv_posR=LTsv_splits.find('\t',LTsv_posL+len(LTsv_tagL))
    if len(LTsv_label) > 0:
        if 0 <= LTsv_posL < LTsv_posR <= len(LTsv_splits):
            if LTsv_default is None:
                LTsv_join=LTsv_splits[:LTsv_posL]+LTsv_splits[LTsv_posR:]
            else:
                LTsv_join=LTsv_splits[:LTsv_posL+len(LTsv_tagL)]+LTsv_data+LTsv_splits[LTsv_posR:]
        else:
            LTsv_join=LTsv_join.rstrip('\t')
            LTsv_join+='\t'+LTsv_label+":"+LTsv_data
    return LTsv_join.strip('\t')

def LTsv_sievelabels(LTsv_rest,LTsv_labels=""):
    return LTsv_sievetuplelabels(LTsv_rest,*LTsv_tsv2tuple(LTsv_labels))

def LTsv_sievetuplelabels(LTsv_rest,*LTsv_labels):
    LTsv_line=""
    for LTsv_label in LTsv_labels:
        LTsv_data=LTsv_pickdatalabel(LTsv_rest,LTsv_label)
        if len(LTsv_data) > 0:
            LTsv_line+="{0}:{1}\t".format(LTsv_label,LTsv_data)
    return LTsv_line.rstrip('\t')

def LTsv_pushlinenum(LTsv_text,LTsv_linenum,LTsv_default=None):
    LTsv_line="" if LTsv_default is None else LTsv_default
    if len(LTsv_line) > 0:
        if not LTsv_line.endswith('\n'):
            LTsv_line+='\n'
    LTsv_join=""; LTsv_splits=LTsv_text.strip('\n').split('\n'); LTsv_linedeno=0
    for LTsv_linedeno,LTsv_split in enumerate(LTsv_splits):
        if LTsv_linenum == LTsv_linedeno:
            LTsv_join+=LTsv_line
        LTsv_join+=LTsv_split+'\n'
    return LTsv_join

def LTsv_overlinenum(LTsv_text,LTsv_linenum,LTsv_default=None):
    LTsv_line="" if LTsv_default is None else LTsv_default
    print("LTsv_line",LTsv_line)
    if len(LTsv_line) > 0:
        if not LTsv_line.endswith('\n'):
            LTsv_line+='\n'
    LTsv_join=""; LTsv_splits=LTsv_text.strip('\n').split('\n'); LTsv_linedeno=0
    for LTsv_linedeno,LTsv_split in enumerate(LTsv_splits):
        if LTsv_linenum == LTsv_linedeno:
            LTsv_join+=LTsv_line
        else:
            LTsv_join+=LTsv_split+'\n'
    return LTsv_join

def LTsv_pushlinerest(LTsv_page,LTsv_first,LTsv_default=None):
    LTsv_rest="" if LTsv_default is None else LTsv_default.replace('\n','\t').strip('\t')
    LTsv_join=LTsv_page; LTsv_tagL='\n'+LTsv_first
    if len(LTsv_join) > 0:
        if not LTsv_join.endswith('\n'):
            LTsv_join+='\n'
    if len(LTsv_first) > 0:
        if len(LTsv_page) > 0:
            LTsv_join='\n'+LTsv_join
            LTsv_posL=LTsv_join.find(LTsv_tagL); LTsv_posR=LTsv_join.find('\n',LTsv_posL+len(LTsv_tagL))
            if 0 <= LTsv_posL < LTsv_posR <= len(LTsv_join):
                if LTsv_default == None:
                    LTsv_join=LTsv_join[:LTsv_posL]+LTsv_rest+LTsv_join[LTsv_posR:]
                else:
                    LTsv_join=LTsv_join[:LTsv_posL+len(LTsv_tagL)]+'\t'+LTsv_rest+LTsv_join[LTsv_posR:]
            else:
                if LTsv_default != None:
                    LTsv_join+=LTsv_first+'\t'+LTsv_rest+'\n'
            LTsv_join=LTsv_join.lstrip('\n')
        else:
            if LTsv_default != None:
                LTsv_join=LTsv_first+'\t'+LTsv_rest+'\n'
    return LTsv_join

def LTsv_putpage(LTsv_text,LTsv_tag,LTsv_default=None):
    LTsv_page="" if LTsv_default is None else LTsv_default
    LTsv_join=LTsv_text; LTsv_tagL="[{0}|\n".format(LTsv_tag); LTsv_tagR="|{0}]\n".format(LTsv_tag);
    if LTsv_default != None:
        if len(LTsv_page) > 0:
            if not LTsv_page.endswith('\n'):
                LTsv_page+='\n'
    if len(LTsv_tag) > 0:
        LTsv_posL=LTsv_text.find(LTsv_tagL); LTsv_posR=LTsv_text.find(LTsv_tagR)
        if 0 <= LTsv_posL < LTsv_posR <= len(LTsv_text):
            if LTsv_default != None:
                LTsv_join=LTsv_text[:LTsv_posL+len(LTsv_tagL)]+LTsv_page+LTsv_text[LTsv_posR:]
            else:
                LTsv_join=LTsv_text[:LTsv_posL]+LTsv_text[LTsv_posR+len(LTsv_tagR):]
        else:
            if LTsv_default != None:
                if not LTsv_join.endswith('\n'):
                    LTsv_join=LTsv_join.rstrip('\n')
                LTsv_join+=LTsv_tagL+LTsv_page+LTsv_tagR
    return LTsv_join

def LTsv_putmodify(LTsv_text):
    LTsv_page=LTsv_getpage(LTsv_text,"L:Tsv")
    LTsv_page=LTsv_pushlinerest(LTsv_page,"modify",LTsv_getdaytimestr(overhour=24,diffminute=0))
    LTsv_text=LTsv_putpage(LTsv_text,"L:Tsv",LTsv_page)
    return LTsv_text

def LTsv_savedir(LTsv_path):
    LTsv_workdir=os.path.dirname(os.path.normpath(LTsv_path))
    if not os.path.exists(LTsv_workdir) and not os.path.isdir(LTsv_workdir) and len(LTsv_workdir): os.mkdir(LTsv_workdir)

def LTsv_savedirs(LTsv_path):
    LTsv_workdir=os.path.dirname(os.path.normpath(LTsv_path))
    if not os.path.exists(LTsv_workdir) and not os.path.isdir(LTsv_workdir) and len(LTsv_workdir): os.makedirs(LTsv_workdir)

def LTsv_savefile(LTsv_path,LTsv_default=None):
    LTsv_text="" if LTsv_default is None else LTsv_default
    if LTsv_default != None:
        LTsv_page=LTsv_getpage(LTsv_text,"L:Tsv")
        LTsv_page=LTsv_pushlinerest(LTsv_page,"LTsvver",LTsv_file_ver())
        LTsv_page=LTsv_pushlinerest(LTsv_page,"modify",LTsv_getdaytimestr(overhour=24,diffminute=0))
        LTsv_text=LTsv_putpage(LTsv_text,"L:Tsv",LTsv_page)
        LTsv_savedir(LTsv_path)
        if sys.version_info.major == 2:
            with open(LTsv_path,'wb') as LTsv_fobj:
                LTsv_fobj.write(LTsv_text.encode("utf-8"))
        if sys.version_info.major == 3:
            with open(LTsv_path,mode="w",encoding="utf-8",errors="xmlcharrefreplace",newline='\n') as LTsv_fobj:
                LTsv_fobj.write(LTsv_text)
    else:
        os.remove(LTsv_path)

def LTsv_saveplain(LTsv_path,LTsv_plain):
    LTsv_text="" if LTsv_plain is None else LTsv_plain
    if len(LTsv_text) > 0:
        LTsv_savedir(LTsv_path)
        if sys.version_info.major == 2:
            with open(LTsv_path,'wb') as LTsv_fobj:
                LTsv_fobj.write(LTsv_text.encode("utf-8"))
        if sys.version_info.major == 3:
            with open(LTsv_path,mode="w",encoding="utf-8",errors="xmlcharrefreplace",newline='\n') as LTsv_fobj:
                LTsv_fobj.write(LTsv_text)

def LTsv_labelzip(LTsv_labels,LTsv_datas):
    LTsv_join=""; LTsv_datadeno=0
    LTsv_splitlabels=LTsv_joindatanum(LTsv_labels,0,"").replace('\n','').split('\t')
    LTsv_splitdatas=LTsv_joindatanum(LTsv_datas,0,"").strip('\n').split('\t')
    for LTsv_split in LTsv_splitlabels:
        if LTsv_datadeno < len(LTsv_splitdatas):
            LTsv_join+="\t"+LTsv_split+":"+LTsv_splitdatas[LTsv_datadeno]
        else:
            LTsv_join+="\t"+LTsv_split+":"
        LTsv_datadeno+=1
    return LTsv_join.strip('\t')

def LTsv_unziplabel(LTsv_line):
    LTsv_labels=""
    LTsv_splitlabels=LTsv_joindatanum(LTsv_line,0,"").strip('\n').split('\t')
    for LTsv_split in LTsv_splitlabels:
        if len(LTsv_split) > 0:
            LTsv_posL=LTsv_split.find(':')
            if LTsv_posL > 0:
                LTsv_label=LTsv_split[:LTsv_posL]
                if len(LTsv_label) > 0:
                    LTsv_labels+=LTsv_label+'\t'
    return LTsv_labels.rstrip('\t')

def LTsv_unzipdata(LTsv_line):
    LTsv_datas=""
    LTsv_splitlabels=LTsv_joindatanum(LTsv_line,0,"").strip('\n').split('\t')
    for LTsv_split in LTsv_splitlabels:
        if len(LTsv_split) > 0:
            LTsv_posL=LTsv_split.find(':')
            if LTsv_posL > 0:
                LTsv_data=LTsv_split[LTsv_posL+len('\t'):]
                if len(LTsv_data) > 0:
                    LTsv_datas+=LTsv_data+'\t'
    return LTsv_datas.rstrip('\t')

def LTsv_unziplabelsdata(LTsv_line,LTsv_labels):
    LTsv_datas=""
    LTsv_splitlabels=LTsv_joindatanum(LTsv_line,0,"").strip('\n').split('\t')
    for LTsv_split in LTsv_splitlabels:
        if len(LTsv_split) > 0:
            LTsv_posL=LTsv_split.find(':')
            if LTsv_posL > 0:
                LTsv_label=LTsv_split[:LTsv_posL]
                LTsv_data=LTsv_split[LTsv_posL+len('\t'):]
                if LTsv_pickdatafind(LTsv_labels,LTsv_label) >= 0:
                    LTsv_datas+=LTsv_data+'\t'
    return LTsv_datas.rstrip('\t')

#pythonstyle

def LTsv_unziptuplelabelsdata(LTsv_line,*LTsv_labels):
    LTsv_datas=""
    LTsv_splitlabels=LTsv_joindatanum(LTsv_line,0,"").strip('\n').split('\t')
    for LTsv_split in LTsv_splitlabels:
        if len(LTsv_split) > 0:
            LTsv_posL=LTsv_split.find(':')
            if LTsv_posL > 0:
                LTsv_label=LTsv_split[:LTsv_posL]
                LTsv_data=LTsv_split[LTsv_posL+len('\t'):]
                if LTsv_label in LTsv_labels:
                    LTsv_datas+=LTsv_data+'\t'
    return LTsv_datas.rstrip('\t')

def LTsv_tuple2tsv(LTsv_tuple):
    return '\t'.join(LTsv_tuple)
#    LTsv_line=""
#    for LTsv_data in LTsv_tuple:
#        LTsv_line="{0}{1}\t".format(LTsv_line,LTsv_data)
#    return LTsv_line.rstrip('\t')

def LTsv_tsv2list(LTsv_line):
    LTsv_list=LTsv_line.replace('\n','\t').strip('\t').split('\t')
    return LTsv_list

def LTsv_tsv2tuple(LTsv_line):
    LTsv_tuple=tuple(LTsv_tsv2list(LTsv_line))
    return LTsv_tuple

def LTsv_intstr0x(LTsv_codestr):
    LTsv_codeint=0
    try:
        LTsv_codeint=int(float(LTsv_codestr))
    except ValueError:
        pass
    for LTsv_hexstr in ["0x","$"]:
        if LTsv_hexstr in LTsv_codestr:
            try:
                LTsv_codeint=int(LTsv_codestr.replace(LTsv_hexstr,""),16)
            except ValueError:
                pass
            break
    return LTsv_codeint

def LTsv_label2dictint(LTsv_line):
    LTsv_labels=""; LTsv_datas=""; LTsv_dict={}
    LTsv_splitlabels=LTsv_joindatanum(LTsv_line,0,"").strip('\n').split('\t')
    for LTsv_split in LTsv_splitlabels:
        if len(LTsv_split) > 0:
            LTsv_posL=LTsv_split.find(':')
            if LTsv_posL > 0:
                LTsv_label=LTsv_split[:LTsv_posL]
                LTsv_data=LTsv_split[LTsv_posL+len('\t'):]
                if len(LTsv_label) > 0 and len(LTsv_data) > 0:
                    LTsv_dict[LTsv_label]=LTsv_intstr0x(LTsv_data)
    return LTsv_dict

def LTsv_label2dictstr(LTsv_line):
    LTsv_labels=""; LTsv_datas=""; LTsv_dict={}
    LTsv_splitlabels=LTsv_joindatanum(LTsv_line,0,"").strip('\n').split('\t')
    for LTsv_split in LTsv_splitlabels:
        if len(LTsv_split) > 0:
            LTsv_posL=LTsv_split.find(':')
            if LTsv_posL > 0:
                LTsv_label=LTsv_split[:LTsv_posL]
                LTsv_data=LTsv_split[LTsv_posL+len('\t'):]
                if len(LTsv_label) > 0 and len(LTsv_data) > 0:
                    LTsv_dict[LTsv_label]=LTsv_data
    return LTsv_dict

def LTsv_dict2label(LTsv_dict):
    LTsv_line=""
    for LTsv_label,LTsv_data in list(LTsv_dict.items()):
        LTsv_line+=LTsv_label+':'+str(LTsv_data)+'\t'
    return LTsv_line.rstrip('\t')

def LTsv_file_ver():
    return "20160718M003911"

def LTsv_issue():
    LTsv_issuefile=""
    if sys.platform.startswith("linux"):
        LTsv_issuefile=LTsv_loadfile("/etc/issue")
    return LTsv_issuefile

if __name__=="__main__":
    from LTsv_printf import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    test_workdir="./testfile/"
    tsvpath=test_workdir+"testfile.tsv"; txtpath=test_workdir+"testfile.txt"; printlog=""
    newfile=LTsv_newfile('__name__=="__main__"',"LTsv8Py"); printlog=LTsv_libc_printf("LTsv_newfile('LTsv8Py')↓\n{0}-eof-".format(newfile),printlog)
    newfile=LTsv_putpage(newfile,"LTsv8Py","stdout\tHelloワールド\u5496\u55B1")
    newpage=LTsv_getpage(newfile,"LTsv8Py")
    newpage=LTsv_pushlinerest(newpage,"tsvtool","print\nfile\ntime\njoy\nkbd\ngui\nsdl")
    newpage=LTsv_pushlinerest(newpage,"tstfile","before:testfile.tsv\tafter:testfile.txt\treadme:readme.txt")
    newfile=LTsv_putpage(newfile,"LTsv8Py",newpage)
    LTsv_savefile(tsvpath,newfile); printlog=LTsv_libc_printf("LTsv_savefile('{0}',newfile)".format(tsvpath),printlog)
    loadfile=LTsv_loadfile(tsvpath,newfile); printlog=LTsv_libc_printf("LTsv_loadfile(tsvpath)↓\n{0}-eof-".format(loadfile),printlog)
    print("")
    pages=LTsv_readlinepages(loadfile); printlog=LTsv_libc_printf("LTsv_readlinepages(loadfile)↓\n{0}".format(pages),printlog)
    getpage=LTsv_getpage(loadfile,"LTsv8Py"); printlog=LTsv_libc_printf("LTsv_getpage(loadfile,'LTsv8Py')↓\n{0}-eop-".format(getpage),printlog)
    firsts=LTsv_readlinefirsts(getpage); printlog=LTsv_libc_printf("LTsv_readlinefirsts(getpage)↓\n{0}".format(firsts),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatadeno(firsts)→{0}".format(LTsv_pickdatadeno(firsts)),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatafind(firsts,'tsvtool')→{0}".format(LTsv_pickdatafind(firsts,'tsvtool')),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatanum(firsts,1)→{0}".format(LTsv_pickdatanum(firsts,1)),printlog)
    print("")
    printlog=LTsv_libc_printf("LTsv_split_label_data('Label:Data',False)→{0}".format(LTsv_split_label_data('Label:Data',False)),printlog)
    printlog=LTsv_libc_printf("LTsv_split_label_data('Label:Data',True)→{0}".format(LTsv_split_label_data('Label:Data',True)),printlog)
    print("")
    readline=LTsv_readlinenum(getpage,1); printlog=LTsv_libc_printf("LTsv_readlinenum(getpage,1)↓\n{0}".format(readline),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatas(readline,2,5)→{0}".format(LTsv_pickdatas(readline,2,5)),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatas(readline,5,2)→{0}".format(LTsv_pickdatas(readline,5,2)),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatas(readline)→{0}".format(LTsv_pickdatas(readline,0,0)),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatas(readline,5)→{0}".format(LTsv_pickdatas(readline,5)),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatas(readline,3,3)→{0}".format(LTsv_pickdatas(readline,3,3)),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatas(readline,3,4)→{0}".format(LTsv_pickdatas(readline,3,4)),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatas(readline,3,5)→{0}".format(LTsv_pickdatas(readline,3,5)),printlog)
    printlog=LTsv_libc_printf("LTsv_joindatanum(readline,2,'midi')↓\n{0}".format(LTsv_joindatanum(readline,2,'midi')),printlog)
    printlog=LTsv_libc_printf("LTsv_setdatanum(readline,2,'midi')↓\n{0}".format(LTsv_setdatanum(readline,2,'midi')),printlog)
    printlog=LTsv_libc_printf("LTsv_setdatanum(readline,2)↓\n{0}".format(LTsv_setdatanum(readline,2)),printlog)
    print("")
    printlog=LTsv_libc_printf("LTsv_pushlinenum(getpage,1,'wine\\tLTsv_printf.sh')↓\n{0}-eop-".format(LTsv_pushlinenum(getpage,1,"wine\tLTsv_printf.sh")),printlog)
    printlog=LTsv_libc_printf("LTsv_pushlinenum(getpage,1,'')↓\n{0}-eop-".format(LTsv_pushlinenum(getpage,1,'')),printlog)
    printlog=LTsv_libc_printf("LTsv_pushlinenum(getpage,1,'\\n')↓\n{0}-eop-".format(LTsv_pushlinenum(getpage,1,'\n')),printlog)
    printlog=LTsv_libc_printf("LTsv_overlinenum(getpage,1,'wine\\tLTsv_printf.sh')↓\n{0}-eop-".format(LTsv_overlinenum(getpage,1,"wine\tLTsv_printf.sh")),printlog)
    printlog=LTsv_libc_printf("LTsv_overlinenum(getpage,1)↓\n{1}-eop-".format(LTsv_file_ver(),LTsv_overlinenum(getpage,1)),printlog)
    printlog=LTsv_libc_printf("LTsv_overlinenum(getpage,1,'\\n')↓\n{1}-eop-".format(LTsv_file_ver(),LTsv_overlinenum(getpage,1,'\n')),printlog)
    print("")
    readline=LTsv_readlinerest(getpage,"tstfile"); printlog=LTsv_libc_printf("LTsv_readlinerest(getpage,'tstfile')↓\n{0}".format(readline),printlog)
    printlog=LTsv_libc_printf("LTsv_pickdatalabel(readline,'after')→{0}".format(LTsv_pickdatalabel(readline,"after")),printlog)
    printlog=LTsv_libc_printf("LTsv_setdatalabel(readline,'icon','LTsv8Py_logo.png')↓\n{0}".format(LTsv_setdatalabel(readline,"icon","LTsv8Py_logo.png.png")),printlog)
    printlog=LTsv_libc_printf("LTsv_setdatalabel(readline,'after','LTsv8Py.png')↓\n{0}".format(LTsv_setdatalabel(readline,"after","LTsv8Py.png")),printlog)
    printlog=LTsv_libc_printf("LTsv_setdatalabel(readline,'after','')↓\n{0}".format(LTsv_setdatalabel(readline,"after",'')),printlog)
    printlog=LTsv_libc_printf("LTsv_setdatalabel(readline,'after')↓\n{0}".format(LTsv_setdatalabel(readline,"after")),printlog)
    print("")
    printlog=LTsv_libc_printf("LTsv_pushlinerest(getpage,'wine','LTsv_printf.sh')↓\n{0}-eop-".format(LTsv_pushlinerest(getpage,"wine","LTsv_printf.sh")),printlog)
    printlog=LTsv_libc_printf("LTsv_pushlinerest(getpage,'tsvtool','LTsv_printf.sh')↓\n{0}-eop-".format(LTsv_pushlinerest(getpage,"tsvtool","LTsv_printf.sh")),printlog)
    printlog=LTsv_libc_printf("LTsv_pushlinerest(getpage,'tsvtool','')↓\n{0}-eop-".format(LTsv_pushlinerest(getpage,"tsvtool",'')),printlog)
    printlog=LTsv_libc_printf("LTsv_pushlinerest(getpage,'tsvtool')↓\n{0}-eop-".format(LTsv_pushlinerest(getpage,"tsvtool")),printlog)
    print("")
    joylabel="X\tY\tA\tB\tC\tZ\tL\tR"
    joydata= "0\t1\t0\t0\t0\t0"
    printlog=LTsv_libc_printf("joylabel={0}".format(joylabel),printlog)
    printlog=LTsv_libc_printf("joydatal={0}".format(joydata),printlog)
    joytsv=LTsv_labelzip(joylabel,joydata)
    printlog=LTsv_libc_printf("joytsv=LTsv_labelzip(joylabel,joydata)↓\n{0}".format(joytsv),printlog)
    printlog=LTsv_libc_printf("LTsv_unziplabel(joytsv)↓\n{0}".format(LTsv_unziplabel(joytsv)),printlog)
    printlog=LTsv_libc_printf("LTsv_unzipdata(joytsv)↓\n{0}".format(LTsv_unzipdata(joytsv)),printlog)
    printlog=LTsv_libc_printf("LTsv_unziplabelsdata(joytsv,'X\\tY\\tA\\tB')↓\n{0}".format(LTsv_unziplabelsdata(joytsv,'X\tY\tA\tB')),printlog)
    printlog=LTsv_libc_printf("LTsv_unziptuplelabelsdata(joytsv,'X','Y','A','B')↓\n{0}".format(LTsv_unziptuplelabelsdata(joytsv,'X','Y','A','B')),printlog)
    printlog=LTsv_libc_printf("LTsv_unziptuplelabelsdata(joytsv,*('X','Y','A','B'))↓\n{0}".format(LTsv_unziptuplelabelsdata(joytsv,*('X','Y','A','B'))),printlog)
    printlog=LTsv_libc_printf("LTsv_unziptuplelabelsdata(joytsv,*tuple(['X','Y','A','B']))↓\n{0}".format(LTsv_unziptuplelabelsdata(joytsv,*tuple(['X','Y','A','B']))),printlog)
    joydic=LTsv_label2dictstr(joytsv)
    printlog=LTsv_libc_printf("joytsv=LTsv_label2dictstr(joytsv)↓\n{0}".format(joydic),printlog)
    joytsv=LTsv_dict2label(joydic)
    printlog=LTsv_libc_printf("joytsv=LTsv_dict2label(joydic)↓\n{0}".format(joytsv),printlog)
    print("")
    joytuple=LTsv_tsv2tuple(joylabel)
    printlog=LTsv_libc_printf("LTsv_tsv2tuple(joylabel)↓\n{0}".format(joytuple),printlog)
    joylist=LTsv_tsv2list(joylabel)
    printlog=LTsv_libc_printf("LTsv_tsv2list(joylabel)↓\n{0}".format(joylist),printlog)
    joylabel=LTsv_tuple2tsv(joytuple)
    printlog=LTsv_libc_printf("LTsv_tuple2tsv(joytuple)↓\n{0}".format(joylabel),printlog)
    joylabel=LTsv_tuple2tsv(joylist)
    printlog=LTsv_libc_printf("LTsv_tuple2tsv(joylist)↓\n{0}".format(joylabel),printlog)
    printlog=LTsv_libc_printf("LTsv_sievetuplelabels(joytsv,*tuple(['A','B','N','X','Y']))↓\n{0}".format(LTsv_sievetuplelabels(joytsv,*tuple(['A','B','N','X','Y']))),printlog)
    printlog=LTsv_libc_printf("LTsv_sievelabels(joytsv,'A\\tB\\tN\\tX\\tY')↓\n{0}".format(LTsv_sievelabels(joytsv,'A\tB\tN\tX\tY')),printlog)
    print("")
    printlog=LTsv_libc_printf("LTsv_issue()↓\n{0}".format(LTsv_issue()),printlog)
    print("")
    loadfile=LTsv_putpage(loadfile,"printlog",printlog)
    LTsv_savefile(txtpath,loadfile); LTsv_libc_printf("LTsv_savefile('{0}',loadfile)".format(txtpath))
    loadfile=LTsv_loadfile(txtpath); LTsv_libc_printf("LTsv_loadfile(txtpath)↓\n{0}-eof-".format(loadfile))
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
