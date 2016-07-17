#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import re
import math

def LTsv_calc_GCM(LTsv_calcL,LTsv_calcR):
    LTsv_GCMm,LTsv_GCMn=abs(int(LTsv_calcL)),abs(int(LTsv_calcR))
    if LTsv_GCMm < LTsv_GCMn:
        LTsv_GCMm,LTsv_GCMn=LTsv_GCMn,LTsv_GCMm
    while LTsv_GCMn > 0:
        LTsv_GCMm,LTsv_GCMn=LTsv_GCMn,LTsv_GCMm%LTsv_GCMn
    return LTsv_GCMm
def LTsv_calc_LCM(LTsv_calcL,LTsv_calcR):
    return abs(int(LTsv_calcL))*abs(int(LTsv_calcR))//LTsv_calc_GCM(LTsv_calcL,LTsv_calcR)

LTsv_character="１２３４５６７８９０""一二三四五六七八九〇""壱弐参肆伍陸漆捌玖零""陌阡萬仙" \
               "．｜ＰｐPＭｍMＹｙYπｅＥEＣｃCＮｎN""小円分正負周底数無∞" \
               "＋－％×／＼÷＃""加減乗除余""足引掛割""和差積商" \
               "（ΣＳｓS～！ＬｌlＧｇg）""列但※〜方約倍「」『』括弧{}｛｝[][]"
LTsv_operator= "1234567890"          "1234567890"          "1234567890"          "百千万銭" \
               ".|pppmmmyyyyeeecccnnn"               "..|pmyecnn" \
               "+-%*/\\/#"      "+-*/#"     "+-*/"    "+-*/" \
               "(SSSS~!LLLGGG)"         "SSS~!LG()()()()()()()"
LTsv_opechardic=dict(zip(list(LTsv_character),list(LTsv_operator)))

LTsv_okusenman="垓京兆億万千百十銭"
LTsv_okusenzero=["*1"+'0'*20+"+","*1"+'0'*16+"+","*1"+'0'*12+"+","*1"+'0'*8+"+","*1"+'0'*4+"+","1000+","100+","10+","+1/100"]
LTsv_okusendic=dict(zip(list(LTsv_okusenman),LTsv_okusenzero))

LTsv_calcusemark=LTsv_okusenman+"1234567890.|pmyecn+-*/\\#%(S!LG~)"

LTsv_opemark=["*+","*-","/+","/-","#+","#-","|+","|-","++","+-","-+","--",
              "0c", "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", ".c",
              "0(", "1(", "2(", "3(", "4(", "5(", "6(", "7(", "8(", "9(", ".(",
              ")0", ")1", ")2", ")3", ")4", ")5", ")6", ")7", ")8", ")9", ").",
              ")(", "|("]
LTsv_opechar=["*p","*m","/p","/m","#p","#m","|p","|m","+p","+m","-p","-m",
              "0*c","1*c","2*c","3*c","4*c","5*c","6*c","7*c","8*c","9*c",".*c",
              "0*(","1*(","2*(","3*(","4*(","5*(","6*(","7*(","8*(","9*(",".*(",
              ")*0",")*1",")*2",")*3",")4*",")*5",")*6",")*7",")*8",")*9",")*.",
              ")*(", "/("]
LTsv_opemarkdic=dict(zip(LTsv_opemark,LTsv_opechar))

def LTsv_calc_bracketsbalance(LTsv_calcQbase):
    LTsv_calcQ=LTsv_calcQbase.replace('\n','\t').replace('\t',''); LTsv_calcA=""
    LTsv_bracketLR=0; LTsv_bracketCAP=0
    for LTsv_Q in LTsv_calcQ:
        if LTsv_Q in LTsv_opechardic:
            LTsv_Q=LTsv_opechardic[LTsv_Q]
        if LTsv_Q in LTsv_calcusemark:
            LTsv_calcA+=LTsv_Q
        if LTsv_Q == '(':
            LTsv_bracketLR+=1
        if LTsv_Q == ')':
            LTsv_bracketLR-=1
            if LTsv_bracketLR<LTsv_bracketCAP:
                LTsv_bracketCAP=LTsv_bracketLR
    if LTsv_bracketLR > 0:
        LTsv_calcA=LTsv_calcA+')'*abs(LTsv_bracketLR)
    if LTsv_bracketLR < 0:
        LTsv_calcA='('*abs(LTsv_bracketLR)+LTsv_calcA
    LTsv_calcA='('*abs(LTsv_bracketCAP)+LTsv_calcA+')'*abs(LTsv_bracketCAP)
    LTsv_calcA=LTsv_calcA.replace('y','('+str(math.pi)+')').replace('e','('+str(math.e)+')').replace('n','(n|0)')
    for LTsv_opecase in LTsv_opemarkdic:
        if LTsv_opecase in LTsv_calcA:
            LTsv_calcA=LTsv_calcA.replace(LTsv_opecase,LTsv_opemarkdic[LTsv_opecase])
#    print("LTsv_calcA",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9千百十]+?)銭"),"+(\\1/100)",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9千百十]+?)万"),"(\\1)*1"+'0'*4+"+",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9千百十]+?)億"),"(\\1)*1"+'0'*8+"+",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9千百十]+?)兆"),"(\\1)*1"+'0'*12+"+",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9千百十]+?)京"),"(\\1)*1"+'0'*16+"+",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9千百十]+?)垓"),"(\\1)*1"+'0'*20+"+",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9]+?)千"),"(\\1*1000)+",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9]+?)百"),"(\\1*100)+",LTsv_calcA)
    LTsv_calcA=re.sub(re.compile("([0-9]+?)十"),"(\\1*10)+",LTsv_calcA)
    for LTsv_okusen in LTsv_okusenman:
        LTsv_calcA=LTsv_calcA.replace(LTsv_okusen,LTsv_okusendic[LTsv_okusen])
#    print("LTsv_calcA",LTsv_calcA)
    return LTsv_calcA

def LTsv_calc_decimalize(LTsv_calcQbase):
    LTsv_calcQ=LTsv_calcQbase.replace('\n','\t').replace('\t','').replace('\t',''); LTsv_calcA="n|0"
    if not '|' in LTsv_calcQ:
        LTsv_calcQ+='|1'
    LTsv_calcQ=LTsv_calcQ.replace('/','|')
    LTsv_calcQsplits=LTsv_calcQ.split('|')
    LTsv_calcQmulti=LTsv_calcQsplits.pop(0)
    if 'n' in LTsv_calcQmulti:
        LTsv_calcQsplits=[0.0]
    else:
        LTsv_decinum=float(LTsv_calcQmulti)
    for LTsv_calcQmulti in LTsv_calcQsplits:
        if float(LTsv_calcQmulti) == 0.0:
            break
        LTsv_decinum/=float(LTsv_calcQmulti)
    else:
        LTsv_calcA=str(LTsv_decinum)
    return LTsv_calcA

def LTsv_calc_fractalize(LTsv_calcQbase):
    LTsv_calcQ=LTsv_calcQbase.replace('\n','\t').replace('\t','').replace('\t',''); LTsv_calcA="n|0"
    if not '|' in LTsv_calcQ:
        LTsv_calcQ+='|1'
    LTsv_calcQ=LTsv_calcQ.replace('/','|')
    LTsv_calcQsplits=LTsv_calcQ.split('|')
    LTsv_calcQmulti=LTsv_calcQsplits.pop(0)
    if 'n' in LTsv_calcQmulti:
        LTsv_calcQsplits=["0.0"]
    else:
        LTsv_calcQmulti=LTsv_calcQmulti.replace('+','').replace('-','') if not '-' in LTsv_calcQmulti else '-'+LTsv_calcQmulti.replace('+','').replace('-','')
        LTsv_calcQmulti=LTsv_calcQmulti if '.' in LTsv_calcQmulti else LTsv_calcQmulti+'.'
        LTsv_fractdeno=int('1'+'0'*(len(LTsv_calcQmulti)-1-LTsv_calcQmulti.find('.')))
        LTsv_calcQmulti=LTsv_calcQmulti.replace('.','')
        LTsv_fractnum=int(LTsv_calcQmulti) if len(LTsv_calcQmulti) > 0 and LTsv_calcQmulti != "-" else 0
    for LTsv_calcQmulti in LTsv_calcQsplits:
        LTsv_calcQmulti=LTsv_calcQmulti.replace('+','').replace('-','') if not '-' in LTsv_calcQmulti else '-'+LTsv_calcQmulti.replace('+','').replace('-','')
        LTsv_calcQmulti=LTsv_calcQmulti if '.' in LTsv_calcQmulti else LTsv_calcQmulti+'.'
        if LTsv_calcQmulti in [".","-."]:
            LTsv_calcQmulti="0.0"
        if LTsv_calcQmulti.count('.') > 1:
            LTsv_calcQmulti="0.0"
        if float(LTsv_calcQmulti) == 0.0:
            break
        LTsv_fractnum*=int('1'+'0'*(len(LTsv_calcQmulti)-1-LTsv_calcQmulti.find('.')))
        LTsv_calcQmulti=LTsv_calcQmulti.replace('.','')
        LTsv_fractdeno*=int(LTsv_calcQmulti) if len(LTsv_calcQmulti) > 0 else 0
    else:
        LTsv_GCM=LTsv_calc_GCM(LTsv_fractnum,LTsv_fractdeno)
        LTsv_fractdeno=LTsv_fractdeno//LTsv_GCM
        LTsv_fractnum=LTsv_fractnum//LTsv_GCM
        LTsv_calcA=str(LTsv_fractnum)+"|"+str(LTsv_fractdeno)
    return LTsv_calcA

def LTsv_calc(LTsv_calcQbase):
    LTsv_calcQ=LTsv_calcQbase.replace('\n','\t').replace('\t',''); LTsv_calcA="n|0"
    LTsv_calcQ=LTsv_calc_bracketsbalance(LTsv_calcQbase); LTsv_calcA=LTsv_calcQ
    LTsv_bracketreg=re.compile("[(](?<=[(])[^()]*(?=[)])[)]")
    while "(" in LTsv_calcA:
        for LTsv_func in re.findall(LTsv_bracketreg,LTsv_calcA):
            LTsv_calcA=LTsv_calcA.replace(LTsv_func,LTsv_calc_function(LTsv_func))
    LTsv_calcA=LTsv_calcA.replace(LTsv_calcA,LTsv_calc_function(LTsv_calcA))
    LTsv_calcA=LTsv_calc_fractalize(LTsv_calcA)
    if LTsv_calcA==LTsv_calcQ:
        LTsv_calcA=LTsv_calc_decimalize(LTsv_calcA)
    return LTsv_calcA

def LTsv_calc_function(LTsv_calcQbase):
    LTsv_calcQ=LTsv_calcQbase.replace('\n','\t').replace('\t','').replace('\t',''); LTsv_calcA=""
    LTsv_calcQ=LTsv_calcQ.lstrip("(").rstrip(")")
#    print("LTsv_calcQ",LTsv_calcQ)
    for LTsv_opecase in LTsv_opemarkdic:
        if LTsv_opecase in LTsv_calcQ:
            LTsv_calcQ=LTsv_calcQ.replace(LTsv_opecase,LTsv_opemarkdic[LTsv_opecase])
#    print("LTsv_calcQ",LTsv_calcQ)
    if not 'S' in LTsv_calcQ and not '!' in LTsv_calcQ:
        LTsv_calcQ+="S1"
    LTsv_Count="1|1"; LTsv_fractC='S'; LTsv_fractC_BF=LTsv_fractC; LTsv_limmark='+'
    LTsv_limstart,LTsv_limgoal,LTsv_limstep=1,2,+1
    LTsv_calcQ=LTsv_calcQ.replace('S',"\tS").replace('!',"\t!").replace('~',"\t~")
    LTsv_calcQsplits=LTsv_calcQ.strip('\t').split('\t')
    LTsv_calcAfirst=LTsv_calcQsplits.pop(0)
    for LTsv_calcQadd in LTsv_calcQsplits:
        LTsv_fractC_BF=LTsv_fractC; LTsv_fractC=LTsv_calcQadd[0]
        LTsv_Count_BF=LTsv_Count; LTsv_Count=LTsv_calc_addition(LTsv_calcQadd.lstrip('S~!'),LTsv_Count)
        if 'n' in LTsv_Count:
            break
        if LTsv_fractC == 'S':
            LTsv_limmark='+'
            LTsv_limstart=int(float(LTsv_calc_decimalize(LTsv_Count)))
            LTsv_limgoal=int(float(LTsv_calc_decimalize(LTsv_Count)))+1
        elif LTsv_fractC == '!':
            LTsv_limmark='*'
            LTsv_limstart=int(float(LTsv_calc_decimalize(LTsv_Count)))
            LTsv_limgoal=int(float(LTsv_calc_decimalize(LTsv_Count)))+1
        else:
            LTsv_limstart=int(float(LTsv_calc_decimalize(LTsv_Count_BF)))
            LTsv_limgoal=int(float(LTsv_calc_decimalize(LTsv_Count)))
            if LTsv_limstart < LTsv_limgoal:
                LTsv_limstart+=1; LTsv_limgoal+=1
            if LTsv_limgoal < LTsv_limstart:
                LTsv_limstart-=1; LTsv_limgoal-=1
        LTsv_limstep=1 if LTsv_limstart < LTsv_limgoal else -1
        for LTsv_lim in range(LTsv_limstart,LTsv_limgoal,LTsv_limstep):
            LTsv_calcA=LTsv_calcA+LTsv_limmark+LTsv_calc_addition(LTsv_calcAfirst,str(LTsv_lim))
#    print("LTsv_calcA",LTsv_calcA)
    LTsv_calcA=LTsv_calc_addition(LTsv_calcA,LTsv_Count)
    return LTsv_calcA

def LTsv_calc_addition(LTsv_calcQbase,LTsv_Count):
    LTsv_calcQ=LTsv_calcQbase.replace('\n','\t').replace('\t','').replace('\t',''); LTsv_calcA="n|0"
    LTsv_calcQ=LTsv_calcQ.replace('c',LTsv_Count)
    LTsv_calcQ=LTsv_calcQ.replace("++","+").replace("+-","-").replace("--","+").replace("-+","-")
    LTsv_calcQ=LTsv_calcQ.replace('+','\t+').replace('-','\t-')
    LTsv_fractnum,LTsv_fractdeno=0,1
    LTsv_calcQsplits=LTsv_calcQ.strip('\t').split('\t')
    for LTsv_calcQmulti in LTsv_calcQsplits:
        LTsv_fractC='' if not '%' in LTsv_calcQmulti else '%'
        LTsv_calcR=LTsv_calc_multiplication(LTsv_calcQmulti.replace('%',''))
        LTsv_fractR=LTsv_calcR.split('|')
        if float(LTsv_fractR[1]) == 0.0:
            break
        if LTsv_fractC == '%':
            LTsv_fractnum=LTsv_fractnum*int(LTsv_fractR[1])*100+LTsv_fractnum*int(LTsv_fractR[0])
            LTsv_fractdeno*=int(LTsv_fractR[1])*100
        else:
            LTsv_fractnum=LTsv_fractnum*int(LTsv_fractR[1])+LTsv_fractdeno*int(LTsv_fractR[0])
            LTsv_fractdeno*=int(LTsv_fractR[1])
    else:
        if LTsv_fractdeno < 0:
            LTsv_fractnum,LTsv_fractdeno=-LTsv_fractnum,-LTsv_fractdeno
        LTsv_calcA=str(LTsv_fractnum)+'|'+str(LTsv_fractdeno)
    return LTsv_calcA

def LTsv_calc_multiplication(LTsv_calcQbase):
    LTsv_calcQ=LTsv_calcQbase.replace('\n','\t').replace('\t','').replace('\t',''); LTsv_calcA="n|0"
    LTsv_calcQ=LTsv_calcQ.replace('*',"\t*").replace('/',"\t/").replace('\\',"\t\\").replace('#',"\t#").replace('L',"\tL").replace('G',"\tG")
    LTsv_calcQ=LTsv_calcQ.replace("+p","+").replace("+m","-").replace("-m","+").replace("-p","-")
    LTsv_calcQ=LTsv_calcQ.replace("p","+").replace("m","-")
    LTsv_fractnum,LTsv_fractdeno=1,1; LTsv_fractC='*'
    LTsv_calcQsplits=LTsv_calcQ.strip('\t').split('\t')
    for LTsv_calcQfraction in LTsv_calcQsplits:
        LTsv_fractC=LTsv_calcQfraction[0] if len(LTsv_calcQfraction)>0 else '*'
        LTsv_calcR=LTsv_calc_fractalize(LTsv_calcQfraction.lstrip('*/\\#LG'))
        LTsv_fractR=LTsv_calcR.split('|')
        if LTsv_fractC == '/':
            if int(LTsv_fractR[0]) == 0:
                break
            LTsv_fractnum*=int(LTsv_fractR[1])
            LTsv_fractdeno*=int(LTsv_fractR[0])
        elif LTsv_fractC == '\\':
            if int(LTsv_fractR[0]) == 0:
                break
            LTsv_fractnum*=int(LTsv_fractR[1])
            LTsv_fractdeno*=int(LTsv_fractR[0])
            LTsv_fractnum,LTsv_fractdeno=LTsv_fractnum//LTsv_fractdeno,1
        elif LTsv_fractC == '#':
            if int(LTsv_fractR[0]) == 0 or int(LTsv_fractR[1]) == 0:
                break
            LTsv_fractnum=(LTsv_fractnum*int(LTsv_fractR[1]))%(LTsv_fractdeno*int(LTsv_fractR[0]))
            LTsv_fractdeno*=int(LTsv_fractR[1])
        elif LTsv_fractC == 'L':
            if LTsv_fractdeno == int(LTsv_fractR[1]):
                LTsv_fractnum=LTsv_calc_LCM(LTsv_fractnum,int(LTsv_fractR[0]))
                LTsv_fractdeno=1
            else:
                break
        elif LTsv_fractC == 'G':
            if LTsv_fractdeno == int(LTsv_fractR[1]):
                LTsv_fractnum=LTsv_calc_GCM(LTsv_fractnum,int(LTsv_fractR[0]))
                LTsv_fractdeno=1
            else:
                break
        else:
            if int(LTsv_fractR[1]) == 0:
                break
            LTsv_fractnum*=int(LTsv_fractR[0])
            LTsv_fractdeno*=int(LTsv_fractR[1])
    else:
        LTsv_calcA=LTsv_calc_fractalize(str(LTsv_fractnum)+'|'+str(LTsv_fractdeno))
    return LTsv_calcA


if __name__=="__main__":
    from LTsv_printf import *
    from LTsv_file   import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_calcQlist=[ "1/3","1|3*3","1-m2",
                     "1|6+1|3","3|4-1|4","2|3*3|4","2|5/4|5","7\\3","10#3","3|2#1|3","10000+8%","24G36","24L36","24|7G36|7","24|7G36|11",
                     "0.5|3.5","0.5/3.5","1|2/7|2","2|3|5|7","2||3","2|--|3","2|p-|3","2|..|3","2|p4.|3","2|m.4|3",
                     "(c+2)(c+1)","(c+2)*(c+1)","1|-3","1|(2-5)","(4-3)|-3","(4-3)|(2-5)","(3+5)|(2-5)",
                     "cΣ1Σ2Σ3Σ4","cΣ1~4","cS1~4","c|2S1~4","c!1!2!3!4","c!1~4","c!4～1","2!1～16","2!～15","2!0～15",
                     "c","1|1","π","314159265359|100000000000","3.1416","ｅ","135914091423|50000000000","2.71828","n","n|0","123456789/0",
                     "8765垓4321京0987兆8901億987万6543円210銭","一千二百三十四万五千六百七十八","千百十","億千万","壱萬円" ]
    for LTsv_calcQ in LTsv_calcQlist:
        LTsv_libc_printf("{0}⇔{1}".format(LTsv_calcQ,LTsv_calc(LTsv_calcQ)))
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE
