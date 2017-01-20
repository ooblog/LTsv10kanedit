#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
sys.path.append("LTsv")
from LTsv_printf  import *
from LTsv_file    import *
from LTsv_time    import *
#from LTsv_calc    import *
#from LTsv_joy     import *
#from LTsv_kbd     import *
from LTsv_gui     import *
#from LTsv_glyph  import *

kanchar_dic_inF   ="LTsv/kanchar.tsv"
kanchar_dic_outF ="./kanchar.tsv"

LTsv_glyphSVG5xdic={"M ":"[","z ":"]",
 "0,1000 ":"0","200,1000 ":"1","400,1000 ":"2","600,1000 ":"3","800,1000 ":"4","1000,1000 ":"5",
 "0,800 ":"6","200,800 ":"7","400,800 ":"8","600,800 ":"9","800,800 ":"a","1000,800 ":"b",
 "0,600 ":"c","200,600 ":"d","400,600 ":"e","600,600 ":"f","800,600 ":"g","1000,600 ":"h",
 "0,400 ":"i","200,400 ":"j","400,400 ":"k","600,400 ":"l","800,400 ":"m","1000,400 ":"n",
 "0,200 ":"o","200,200 ":"p","400,200 ":"q","600,200 ":"r","800,200 ":"s","1000,200 ":"t",
 "0,0 ":"u","200,0 ":"v","400,0 ":"w","600,0 ":"x","800,0 ":"y","1000,0 ":"z"
}
LTsv_glyphSVG10xdic={"M ":"[","z ":"]",
 "0,":"A","100,":"B","200,":"C","300,":"D","400,":"E","500,":"F","600,":"G","700,":"H","800,":"I","900,":"J","1000,":"K",
 "0 ":"Y","100 ":"X","200 ":"W","300 ":"V","400 ":"U","500 ":"T","600 ":"S","700 ":"R","800 ":"Q","900 ":"P","1000 ":"O"
}
LTsv_glyphSVG5xdicMz=dict([(dic_value,dic_key) for dic_key,dic_value in LTsv_glyphSVG5xdic.items()])
LTsv_glyphSVG10xdicMz=dict([(dic_value,dic_key) for dic_key,dic_value in LTsv_glyphSVG10xdic.items()])

def LTsv_glyphSVG5x10x(LTsv_glyph_path):
    if not "[" in LTsv_glyph_path: return LTsv_glyph_path;
    LTsv_glyph_path5x=""
    for path5x in LTsv_glyph_path:
        if path5x in LTsv_glyphSVG5xdicMz:
            LTsv_glyph_path5x+=path5x.replace(path5x,LTsv_glyphSVG5xdicMz[path5x])
        elif path5x in LTsv_glyphSVG10xdicMz:
            LTsv_glyph_path5x+=path5x.replace(path5x,LTsv_glyphSVG10xdicMz[path5x])
        else:
            LTsv_glyph_path5x=""; break;
    return LTsv_glyph_path5x.rstrip(' ')

LTsv_glyphSVG20xOdic=OrderedDict([('M ','['),('z ',']'),
('0,1000 ','0'),('200,1000 ','1'),('400,1000 ','2'),('600,1000 ','3'),('800,1000 ','4'),('1000,1000 ','5'),
('0,800 ','6'),('200,800 ','7'),('400,800 ','8'),('600,800 ','9'),('800,800 ','?'),('1000,800 ','!'),
('0,600 ','+'),('200,600 ','-'),('400,600 ','*'),('600,600 ','/'),('800,600 ','%'),('1000,600 ','^'),
('0,400 ','#'),('200,400 ','$'),('400,400 ','&'),('600,400 ',';'),('800,400 ','@'),('1000,400 ','='),
('0,200 ','_'),('200,200 ','L'),('400,200 ','M'),('600,200 ','N'),('800,200 ','`'),('1000,200 ','Z'),
('0,0 ','k'),('200,0 ','l'),('400,0 ','m'),('600,0 ','n'),('800,0 ','y'),('1000,0 ','z'),
('0,','A'),('50,','a'),('100,','B'),('150,','b'),('200,','C'),('250,','c'),('300,','D'),('350,','d'),('400,','E'),('450,','e'),('500,','F'),('550,','f'),('600,','G'),('650,','g'),('700,','H'),('750,','h'),('800,','I'),('850,','i'),('900,','J'),('950,','j'),('1000,','K'),
('1000 ','O'),('950 ','o'),('900 ','P'),('850 ','p'),('800 ','Q'),('750 ','q'),('700 ','R'),('650 ','r'),('600 ','S'),('550 ','s'),('500 ','T'),('450 ','t'),('400 ','U'),('350 ','u'),('300 ','V'),('250 ','v'),('200 ','W'),('150 ','w'),('100 ','X'),('50 ','x'),('0 ','Y')
])
LTsv_glyphSVG20xOdicMz=OrderedDict([(dic_value,dic_key) for dic_key,dic_value in LTsv_glyphSVG20xOdic.items()])

def LTsv_glyphSVG5x10x20x(LTsv_kanpath5x10x20x):
    if not "[" in LTsv_kanpath5x10x20x: return LTsv_kanpath5x10x20x;
    LTsv_kanpathSVG=""
    for path20x in LTsv_kanpath5x10x20x:
        if path20x in LTsv_glyphSVG20xOdicMz:
            LTsv_kanpathSVG+=path20x.replace(path20x,LTsv_glyphSVG20xOdicMz[path20x])
        else:
            LTsv_kanpathSVG=""; break;
    return LTsv_kanpathSVG

def LTsv_glyph5x10x20x(LTsv_kanpathSVG):
    LTsv_kanpath5x10x20x=""
    LTsv_kanpathSVGsplit=LTsv_kanpathSVG.strip(' ')+' '
    LTsv_kanpathSVGsplit=LTsv_kanpathSVGsplit.replace(' ',' \n').rstrip('\n').split('\n')
    for path20x in LTsv_kanpathSVGsplit:
        if path20x in LTsv_glyphSVG20xOdic:
            LTsv_kanpath5x10x20x+=LTsv_glyphSVG20xOdic[path20x]
        else:
            for path20xLR in path20x.replace(',',',\n').split('\n'):
                if path20xLR in LTsv_glyphSVG20xOdic:
                    LTsv_kanpath5x10x20x+=LTsv_glyphSVG20xOdic[path20xLR]
                else:
                    LTsv_kanpath5x10x20x=LTsv_kanpathSVG; break;
            if LTsv_kanpath5x10x20x==LTsv_kanpathSVG: break;
        if LTsv_kanpath5x10x20x==LTsv_kanpathSVG: break;
    return LTsv_kanpath5x10x20x

LTsv_glyph_kbdinit(LTsv_tsvpath="LTsv/LTsv_glyph.tsv",LTsv_glyph_GUI=LTsv_GUI,LTsv_glyph_kbddefsize=1)
kanchar_inL=LTsv_global_kandic().rstrip('\n').split('\n')
kanchar_outL=[""]*len(kanchar_inL)
for kanline_count,kanline in enumerate(kanchar_inL):
    for glyphtype in LTsv_global_glyphtype():
        kanpath=LTsv_glyphSVG5x10x(LTsv_pickdatalabel(kanline,glyphtype))
        kanpath=LTsv_glyph5x10x20x(kanpath)
#        kanpathSVG=LTsv_glyphSVG5x10x20x(kanpath)
#        print(kanpath,kanpathSVG)
        kanline=LTsv_setdatalabel(kanline,glyphtype,kanpath)
    kanchar_outL[kanline_count]=kanline
kanchar_outT="\n".join(kanchar_outL)
LTsv_saveplain(kanchar_dic_outF,kanchar_outT)

# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
