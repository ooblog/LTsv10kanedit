#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import locale
import subprocess
import codecs
import ctypes
import re
if sys.version_info.major == 2:
    import htmlentitydefs
if sys.version_info.major == 3:
    import html.entities
LTsv_name2codepoint=html.entities.name2codepoint if sys.version_info.major == 3 else htmlentitydefs.name2codepoint
LTsv_chrcode=chr if sys.version_info.major == 3 else unichr

LTsv_libc=None
if sys.platform.startswith("win"):
    LTsv_libc=ctypes.cdll.msvcrt
if sys.platform.startswith("linux"):
    LTsv_libc=ctypes.CDLL("libc.so.6")
#if sys.platform.startswith('cygwin'):
#    LTsv_libc=ctypes.CDLL("libc.so.6")
#if sys.platform.startswith("darwin"):
#    LTsv_libc=ctypes.CDLL("libSystem.B.dylib")

def LTsv_getpreferredencoding():
    LTsv_stdout=sys.stdout.encoding
    if LTsv_stdout is None:
        LTsv_stdout=locale.getpreferredencoding();
#        print("LTsv_getpreferredencoding",LTsv_stdout)
    return LTsv_stdout

def LTsv_libc_printf(LTsv_text,LTsv_log=None):
    if not LTsv_libc is None:
#        LTsv_Btext=LTsv_text.encode(sys.stdout.encoding,"xmlcharrefreplace")
        LTsv_Btext=LTsv_text.encode(LTsv_getpreferredencoding(),"xmlcharrefreplace")
        LTsv_libc.printf(b"%s\n",LTsv_Btext)
    else:
        print(LTsv_text)
    if not LTsv_log is None:
        LTsv_page=LTsv_log+LTsv_text
        LTsv_page=re.sub(re.compile("^\[(.+?)\|$",re.MULTILINE),"[\\1|\t//#L:Tsv.tag",LTsv_page)
        LTsv_page=re.sub(re.compile("^\|(.+?)\]$",re.MULTILINE),"|\\1]\t//#L:Tsv.tag",LTsv_page)
        if not LTsv_page.endswith('\n'):
            LTsv_page+='\n'
        return LTsv_page

def LTsv_libc_printcat(LTsv_text):
    if not LTsv_libc is None:
        LTsv_Btext=LTsv_text.encode(sys.stdout.encoding,"xmlcharrefreplace")
        LTsv_libc.printf(b"%s",LTsv_Btext)

def LTsv_libc_printf_type(LTsv_text,LTsv_log=None):
#    Btext=LTsv_text.encode(sys.stdout.encoding,"xmlcharrefreplace")
    LTsv_Btext=LTsv_text.encode(LTsv_getpreferredencoding(),"xmlcharrefreplace")
    LTsv_page=LTsv_libc_printf("{0} {1}".format(type(LTsv_Btext),[LTsv_Btext]),LTsv_log)
    return LTsv_page

def LTsv_utf2xml(LTsv_text):
    LTsv_xmltext=""
    for LTsv_unichar in LTsv_text:
        LTsv_xmltext+="&#"+str(ord(LTsv_unichar))+";"
    return LTsv_xmltext

def LTsv_xml2utf(LTsv_text):
    LTsv_utftext=LTsv_text
    for LTsv_unichar in re.findall(re.compile("&[/#a-zA-Z0-9]+?;"),LTsv_text):
        if LTsv_unichar.startswith("&#"):
            LTsv_unicharcode=int("0"+LTsv_unichar.lstrip("&#").rstrip(";"),16) if LTsv_unichar[2] in ('x','X') else int(LTsv_unichar.lstrip("&#").rstrip(";"))
            LTsv_utftext=LTsv_utftext.replace(LTsv_unichar,LTsv_chrcode(LTsv_unicharcode))
        else:
            LTsv_unicharcode=LTsv_name2codepoint.get(LTsv_unichar.lstrip("&").rstrip(";"))
            LTsv_utftext=LTsv_utftext.replace(LTsv_unichar,LTsv_chrcode(LTsv_unicharcode)) if not LTsv_unicharcode is None else LTsv_utftext
#    if sys.version_info.major == 2:
#        for LTsv_unichar in re.findall(re.compile("&[/#a-zA-Z0-9]+?;"),LTsv_text):
#            if LTsv_unichar.startswith("&#"):
#                LTsv_unicharcode=int("0"+LTsv_unichar.lstrip("&#").rstrip(";"),16) if LTsv_unichar[2] in ('x','X') else int(LTsv_unichar.lstrip("&#").rstrip(";"))
#                LTsv_utftext=LTsv_utftext.replace(LTsv_unichar,unichr(LTsv_unicharcode))
#            else:
#                LTsv_unicharcode=htmlentitydefs.name2codepoint.get(LTsv_unichar.lstrip("&").rstrip(";"))
#                LTsv_utftext=LTsv_utftext.replace(LTsv_unichar,unichr(LTsv_unicharcode)) if not LTsv_unicharcode is None else LTsv_utftext
#    if sys.version_info.major == 3:
#        for LTsv_unichar in re.findall(re.compile("&[/#a-zA-Z0-9]+?;"),LTsv_text):
#            if LTsv_unichar.startswith("&#"):
#                LTsv_unicharcode=int("0"+LTsv_unichar.lstrip("&#").rstrip(";"),16) if LTsv_unichar[2] in ('x','X') else int(LTsv_unichar.lstrip("&#").rstrip(";"))
#                LTsv_utftext=LTsv_utftext.replace(LTsv_unichar,chr(LTsv_unicharcode))
#            else:
#                LTsv_unicharcode=html.entities.name2codepoint.get(LTsv_unichar.lstrip("&").rstrip(";"))
#                LTsv_utftext=LTsv_utftext.replace(LTsv_unichar,chr(LTsv_unicharcode)) if not LTsv_unicharcode is None else LTsv_utftext
    return LTsv_utftext

LTsv_Hira_YOO="あいえおなにぬねのやゆよらりるれろわをんぁぃぅぇぉっゃゅょゎゐゑ"
LTsv_Kata_YOO="アイエオナニヌネノヤユヨラリルレロワヲンァィゥェォッャュョヮヰヱ"
LTsv_Hira_SEI="うかきくけこさしすせそたちつてとはひふへほゝ"
LTsv_Hira_DAK="ゔがぎぐげござじずぜぞだぢづでどばびぶべぼゞ"
LTsv_Kata_SEI="ウカキクケコサシスセソタチツテトハヒフヘホヽ"
LTsv_Kata_DAK="ヴガギグゲゴザジズゼゾダヂヅデドバビブベボヾ"
LTsv_Hira_HA="はひふへほ"; LTsv_Hira_MA="まみむめも"; LTsv_Hira_PA="ぱぴぷぺぽ"
LTsv_Kata_HA="ハヒフヘホ"; LTsv_Kata_MA="マミムメモ"; LTsv_Kata_PA="パピプペポ"
LTsv_HiraZen_SEI="あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんぁぃぅぇぉっゃゅょ「ー」・、。゛゜"
LTsv_KataZen_SEI="アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンァィゥェォッャュョ「ー」・、。゛゜"
LTsv_Hankaku_SEI="ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯｬｭｮ｢ｰ｣･､｡ﾞﾟ"
LTsv_HiraZen_GA="ヵヶ"
LTsv_Hankaku_GA="ｶｹ"
LTsv_HiraZen_DAK="ゔがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"
LTsv_KataZen_DAK="ヴガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ"
LTsv_Hankaku_DAK=['ｳﾞ','ｶﾞ','ｷﾞ','ｸﾞ','ｹﾞ','ｺﾞ','ｻﾞ','ｼﾞ','ｽﾞ','ｾﾞ','ｿﾞ','ﾀﾞ','ﾁﾞ','ﾂﾞ','ﾃﾞ','ﾄﾞ','ﾊﾞ','ﾋﾞ','ﾌﾞ','ﾍﾞ','ﾎﾞ','ﾊﾟ','ﾋﾟ','ﾌﾟ','ﾍﾟ','ﾎﾟ']
LTsv_DigitZEN="１２３４５６７８９０－＾＠［］；：，．／！＃＄％＆’（）＝～｜｀｛＋＊｝＜＞？＿" + '”'
LTsv_DigitHAN="1234567890-^@[];:,./!#$%&'()=~|`{+*}<>?_" + '"'
LTsv_YenZEN='￥'; LTsv_BSZEN='＼'
LTsv_YenHAN='\\'; LTsv_BSHAN='\\'
LTsv_AlphaSML_HAN="abcdefghijklmnopqrstuvwxyz"
LTsv_AlphaBIG_HAN="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LTsv_AlphabetSML="ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
LTsv_AlphabetBIG="ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
LTsv_GreekCyrillicSML="αβγδεζηθικλμνξοπρστυφχψω"+"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
LTsv_GreekCyrillicBIG="ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"+"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

LTsv_Hira2Kata=dict(zip(list(LTsv_Hira_YOO+LTsv_Hira_SEI+LTsv_Hira_DAK+LTsv_Hira_MA+LTsv_Hira_PA),list(LTsv_Kata_YOO+LTsv_Kata_SEI+LTsv_Kata_DAK+LTsv_Kata_MA+LTsv_Kata_PA)))
LTsv_Kata2Hira=dict(zip(list(LTsv_Kata_YOO+LTsv_Kata_SEI+LTsv_Kata_DAK+LTsv_Kata_MA+LTsv_Kata_PA),list(LTsv_Hira_YOO+LTsv_Hira_SEI+LTsv_Hira_DAK+LTsv_Hira_MA+LTsv_Hira_PA)))
LTsv_HiraKana2SeiH=dict(zip(list(LTsv_Hira_DAK+LTsv_Kata_DAK+LTsv_Hira_PA+LTsv_Kata_PA),list(LTsv_Hira_SEI+LTsv_Kata_SEI+LTsv_Hira_HA+LTsv_Kata_HA)))
LTsv_HiraKana2SeiM=dict(zip(list(LTsv_Hira_DAK+LTsv_Kata_DAK+LTsv_Hira_PA+LTsv_Kata_PA),list(LTsv_Hira_SEI+LTsv_Kata_SEI+LTsv_Hira_MA+LTsv_Kata_MA)))
LTsv_HiraKana2DakB=dict(zip(list(LTsv_Hira_SEI+LTsv_Kata_SEI),list(LTsv_Hira_DAK+LTsv_Kata_DAK)))
LTsv_HiraKana2DakP=dict(zip(list(LTsv_Hira_SEI+LTsv_Kata_SEI+LTsv_Hira_MA+LTsv_Kata_MA),list(LTsv_Hira_DAK+LTsv_Kata_DAK+LTsv_Hira_PA+LTsv_Kata_PA)))
LTsv_HiraKana2Han=dict(zip(list(LTsv_HiraZen_SEI+LTsv_KataZen_SEI+LTsv_HiraZen_DAK+LTsv_KataZen_DAK),list(LTsv_Hankaku_SEI+LTsv_Hankaku_SEI)+LTsv_Hankaku_DAK+LTsv_Hankaku_DAK))
LTsv_HiraKana2HanKaKe=dict(zip(list(LTsv_HiraZen_SEI+LTsv_KataZen_SEI+LTsv_HiraZen_GA+LTsv_HiraZen_DAK+LTsv_KataZen_DAK),list(LTsv_Hankaku_SEI+LTsv_Hankaku_SEI+LTsv_Hankaku_GA)+LTsv_Hankaku_DAK+LTsv_Hankaku_DAK))
LTsv_Han2HiraEz=dict(zip(list(LTsv_Hankaku_SEI),list(LTsv_HiraZen_SEI)))
LTsv_Han2KataEz=dict(zip(list(LTsv_Hankaku_SEI),list(LTsv_KataZen_SEI)))
LTsv_Han2Hira=dict(zip(LTsv_Hankaku_DAK,list(LTsv_HiraZen_DAK)))
LTsv_Han2Kata=dict(zip(LTsv_Hankaku_DAK,list(LTsv_KataZen_DAK)))
LTsv_Alpha2BIG=dict(zip(list(LTsv_AlphabetSML+LTsv_AlphaSML_HAN+LTsv_GreekCyrillicSML),list(LTsv_AlphabetBIG+LTsv_AlphaBIG_HAN+LTsv_GreekCyrillicBIG)))
LTsv_Alpha2SML=dict(zip(list(LTsv_AlphabetBIG+LTsv_AlphaBIG_HAN+LTsv_GreekCyrillicBIG),list(LTsv_AlphabetSML+LTsv_AlphaSML_HAN+LTsv_GreekCyrillicSML)))
LTsv_Alpha2HAN=dict(zip(list(LTsv_AlphabetBIG+LTsv_AlphabetSML+LTsv_DigitZEN+LTsv_YenZEN+LTsv_BSZEN),list(LTsv_AlphaBIG_HAN+LTsv_AlphaSML_HAN+LTsv_DigitHAN+LTsv_YenHAN+LTsv_BSHAN)))
LTsv_Alpha2ZENBS=dict(zip(list(LTsv_AlphaBIG_HAN+LTsv_AlphaSML_HAN+LTsv_DigitHAN+LTsv_BSHAN),list(LTsv_AlphabetBIG+LTsv_AlphabetSML+LTsv_DigitZEN+LTsv_BSZEN)))
LTsv_Alpha2ZENYen=dict(zip(list(LTsv_AlphaBIG_HAN+LTsv_AlphaSML_HAN+LTsv_DigitHAN+LTsv_YenHAN),list(LTsv_AlphabetBIG+LTsv_AlphabetSML+LTsv_DigitZEN+LTsv_YenZEN)))

LTsv_kanarecases={ "Hira2Kata":LTsv_Hira2Kata,"Kata2Hira":LTsv_Kata2Hira,
                   "HiraKana2SeiH":LTsv_HiraKana2SeiH,"HiraKana2SeiM":LTsv_HiraKana2SeiM,
                   "HiraKana2DakB":LTsv_HiraKana2DakB,"HiraKana2DakP":LTsv_HiraKana2DakP,
                   "HiraKana2Han":LTsv_HiraKana2Han,"HiraKana2HanKaKe":LTsv_HiraKana2HanKaKe,
                   "Han2HiraEz":LTsv_Han2HiraEz,"Han2KataEz":LTsv_Han2KataEz,
                   "Alpha2BIG":LTsv_Alpha2BIG,"Alpha2SML":LTsv_Alpha2SML,
                   "Alpha2HAN":LTsv_Alpha2HAN,"Alpha2ZENBS":LTsv_Alpha2ZENBS,"Alpha2ZENYen":LTsv_Alpha2ZENYen,
                      "Han2Hira":LTsv_Han2Hira,  "Han2Kata":LTsv_Han2Kata }
LTsv_kanarehankakyu ={"Han2Hira":LTsv_Han2HiraEz,"Han2Kata":LTsv_Han2KataEz }

def LTsv_kanare(LTsv_before,LTsv_recase):
    LTsv_during=LTsv_before
    global LTsv_kanarecases
    if LTsv_recase in LTsv_kanarecases:
        LTsv_dict=LTsv_kanarecases[LTsv_recase]
        if LTsv_recase in LTsv_kanarehankakyu:
            for LTsv_repstr in LTsv_dict:
                LTsv_during=LTsv_during.replace(LTsv_repstr,LTsv_dict[LTsv_repstr]) if LTsv_repstr in LTsv_dict else LTsv_during
            LTsv_dict=LTsv_kanarehankakyu[LTsv_recase]
        LTsv_after=""
        for LTsv_unichar in LTsv_during:
            LTsv_after+=LTsv_dict[LTsv_unichar] if LTsv_unichar in LTsv_dict else LTsv_unichar
    else:
        LTsv_after=LTsv_during
    return LTsv_after

LTsv_INK00=10240          #⠀
LTsv_INKFF=10240+0xff     #⣿
def LTsv_utf2ink(LTsv_text):
    LTsv_inktext=""
    LTsv_Btext=LTsv_text.encode("UTF-8","ignore")
#    for LTsv_unicode in LTsv_Btext:
#        LTsv_inktext+=LTsv_chrcode(LTsv_INK00+ord(LTsv_unicode))
    if sys.version_info.major == 2:
        for LTsv_unicode in LTsv_Btext:
            LTsv_inktext+=unichr(LTsv_INK00+ord(LTsv_unicode))
    if sys.version_info.major == 3:
        for LTsv_unicode in LTsv_Btext:
            LTsv_inktext+=chr(LTsv_INK00+LTsv_unicode)
    return LTsv_inktext

def LTsv_ink2utf(LTsv_text):
    LTsv_utftext=""; LTsv_Bcode=[]; LTsv_byteptr=0; LTsv_unicode=0
    for LTsv_unichar in LTsv_text:
       LTsv_Bcode.append(ord(LTsv_unichar)-LTsv_INK00 if LTsv_INK00 <= ord(LTsv_unichar) <= LTsv_INKFF else 0)
    while LTsv_byteptr < len(LTsv_Bcode):
        if LTsv_Bcode[LTsv_byteptr]//128 == 0:
            LTsv_unicode=(LTsv_Bcode[LTsv_byteptr]%128)
            LTsv_byteptr+=1
        elif LTsv_Bcode[LTsv_byteptr]//32 == 6:
            LTsv_unicode=(LTsv_Bcode[LTsv_byteptr]%32)*64+(LTsv_Bcode[LTsv_byteptr+1]%64)
            LTsv_byteptr+=2
        elif LTsv_Bcode[LTsv_byteptr]//16 == 14:
            LTsv_unicode=(LTsv_Bcode[LTsv_byteptr]%16)*4096+(LTsv_Bcode[LTsv_byteptr+1]%64)*64+(LTsv_Bcode[LTsv_byteptr+2]%64)
            LTsv_byteptr+=3
        elif LTsv_Bcode[LTsv_byteptr]//8  == 30:
            LTsv_unicode=(LTsv_Bcode[LTsv_byteptr]%8)*262144+(LTsv_Bcode[LTsv_byteptr+1]%64)*4096+(LTsv_Bcode[LTsv_byteptr+2]%64)*64+(LTsv_Bcode[LTsv_byteptr+3]%64)
            LTsv_byteptr+=4
        elif LTsv_Bcode[LTsv_byteptr]//4  == 62:
            LTsv_unicode=0
            LTsv_byteptr+=5
        elif LTsv_Bcode[LTsv_byteptr]//2  == 126:
            LTsv_unicode=0
            LTsv_byteptr+=6
        else:
            LTsv_unicode=0
            LTsv_byteptr+=1
        if LTsv_unicode > 0:
            LTsv_utftext+=LTsv_chrcode(LTsv_unicode)
#            if sys.version_info.major == 2:
#                LTsv_utftext+=unichr(LTsv_unicode)
#            if sys.version_info.major == 3:
#                LTsv_utftext+=chr(LTsv_unicode)
    return LTsv_utftext

def LTsv_subprocess(LTsv_subprocess_input="",LTsv_subprocess_shell=False):
    LTsv_subprocess_output=""
    try:
        if LTsv_subprocess_shell:
            if sys.version_info.major == 2:
                LTsv_subprocess_output=subprocess.check_output(LTsv_subprocess_input,shell=True).decode("utf-8")
            if sys.version_info.major == 3:
                LTsv_subprocess_output=subprocess.check_output(LTsv_subprocess_input,shell=True)
        else:
            if sys.version_info.major == 2:
                LTsv_subprocess_output=subprocess.check_output(LTsv_subprocess_input.split(' '),shell=LTsv_subprocess_shell).decode("utf-8")
            if sys.version_info.major == 3:
                LTsv_subprocess_output=subprocess.check_output(LTsv_subprocess_input.split(' '),shell=LTsv_subprocess_shell)
    except subprocess.CalledProcessError as err:
#        print("subprocess.CalledProcessError({0}):{1}".format(err.returncode,err.output))
        LTsv_subprocess_output=err.output if err.output != None else ""
    return LTsv_subprocess_output

def LTsv_otherprocess(LTsv_otherprocess_input=""):
    LTsv_subprocess_output=""
    try:
        if sys.version_info.major == 2:
            LTsv_otherprocess_proc=subprocess.Popen(LTsv_otherprocess_input.decode("utf-8"),shell=True)
        if sys.version_info.major == 3:
            LTsv_otherprocess_proc=subprocess.Popen(LTsv_otherprocess_input,shell=True)
    except subprocess.CalledProcessError as err:
#        print("subprocess.CalledProcessError({0}):{1}".format(err.returncode,err.output))
        pass
    return LTsv_otherprocess_proc


if __name__=="__main__":
    from LTsv_file   import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    test_workdir="./testfile/"; txtpath=test_workdir+"testprint.txt"; printlog=""
    printlog=LTsv_libc_printf("'hello world' {0}".format(type("hello world")),printlog)
    printlog=LTsv_libc_printf("'hello world'.encode('utf-8') {0}".format(type('hello world'.encode('utf-8'))),printlog)
    printlog=LTsv_libc_printf("'hello {0}'.format('world') {1}".format("{0}",type('hello {0}'.format('world'))),printlog)
    print("")
    LTsv_helloworld="helloワールド\u5496\u55B1"
    printlog=LTsv_libc_printf(LTsv_helloworld[0:5],printlog)
    printlog=LTsv_libc_printf_type(LTsv_helloworld[0:5],printlog)
    print("")
    printlog=LTsv_libc_printf(LTsv_helloworld[0:9],printlog)
    printlog=LTsv_libc_printf_type(LTsv_helloworld[0:9],printlog)
    print("")
    printlog=LTsv_libc_printf(LTsv_helloworld[5:11],printlog)
    printlog=LTsv_libc_printf_type(LTsv_helloworld[5:11],printlog)
    print("")
    print("")
    LTsv_xmltext=LTsv_utf2xml(LTsv_helloworld)
    printlog=LTsv_libc_printf("LTsv_utf2xml('{0}')↓\n{1}".format(LTsv_helloworld,LTsv_utf2xml(LTsv_helloworld)),printlog)
    print("")
    LTsv_xmltext+="&copy;&hoge;"
    printlog=LTsv_libc_printf("LTsv_xmltext+='&copy;&hoge;'→{0}".format(LTsv_xmltext),printlog)
    print("")
    printlog=LTsv_libc_printf("LTsv_xml2utf(LTsv_xmltext)↓\n{0}".format(LTsv_xml2utf(LTsv_xmltext)),printlog)
    print("")
    LTsv_inktext=LTsv_utf2ink(LTsv_helloworld)
    printlog=LTsv_libc_printf("LTsv_utf2ink('{0}')↓\n{1}".format(LTsv_helloworld,LTsv_utf2ink(LTsv_helloworld)),printlog)
    print("")
    printlog=LTsv_libc_printf("LTsv_ink2utf('{0}')↓\n{1}".format(LTsv_inktext,LTsv_ink2utf(LTsv_inktext)),printlog)
    print("")
    print("")
    kanarecases_order=["Hira2Kata","Kata2Hira","HiraKana2SeiH","HiraKana2SeiM","HiraKana2DakB","HiraKana2DakP","HiraKana2Han","HiraKana2HanKaKe","Han2HiraEz","Han2KataEz","Han2Hira","Han2Kata",
                       "Alpha2BIG","Alpha2SML","Alpha2HAN","Alpha2ZENBS","Alpha2ZENYen"]
    for kanare_key in kanarecases_order:
        if kanare_key in ["Han2HiraEz","Han2KataEz","Han2Hira","Han2Kata"]:
            kanare_value=LTsv_Hankaku_SEI+''.join(LTsv_Hankaku_DAK)
        elif kanare_key in ["HiraKana2Han","HiraKana2HanKaKe"]:
            kanare_value=LTsv_HiraZen_SEI+LTsv_KataZen_SEI+LTsv_HiraZen_DAK+LTsv_KataZen_DAK+LTsv_HiraZen_GA
        else:
            kanare_value=''.join(sorted(LTsv_kanarecases[kanare_key].keys()))
        kanare_replace=LTsv_kanare(kanare_value,kanare_key)
        printlog=LTsv_libc_printf("LTsv_kanare(kanare_value,'{0}')\n{1}↓\n{2}\n".format(kanare_key,kanare_value,kanare_replace),printlog)
    LTsv_saveplain(txtpath,printlog); LTsv_libc_printf("LTsv_savefile('{0}',printlog)".format(txtpath))
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
