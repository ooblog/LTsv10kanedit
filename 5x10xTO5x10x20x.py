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
from LTsv_glyph  import *

kanchar_dic_inF   ="LTsv/kanchar.tsv"
kanchar_dic_outF ="./kanchar.tsv"

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
