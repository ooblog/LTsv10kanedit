#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import time
import datetime
import os

LTsv_HourMAXLower,LTsv_HourMAXUpper=(24,48)
LTsv_overhour=LTsv_HourMAXLower
LTsv_diffminute=0
LTsv_zodiacjp=("鼠","牛","虎","兎","龍","蛇","馬","羊","猿","鶏","犬","猪")
LTsv_zodiacch=("子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥")
LTsv_maxmonth=    (31,31,28,31,30,31,30,31,31,30,31,30,31,31)
LTsv_maxmonthleep=(31,31,29,31,30,31,30,31,31,30,31,30,31,31)
LTsv_monthjp=   (  "睦月",   "如月",  "弥生",   "卯月",  "皐月","水無月",  "文月",  "葉月",  "長月",   "神無月",   "霜月",  "師走")
LTsv_month_jp=  ("　睦月", "　如月","　弥生", "　卯月","　皐月","水無月","　文月","　葉月","　長月",   "神無月", "　霜月","　師走")
LTsv_monthjpiz= (  "睦月",   "如月",  "弥生",   "卯月",  "皐月","水無月",  "文月",  "葉月",  "長月",   "神有月",   "霜月",  "師走")
LTsv_month_jpiz=("　睦月", "　如月","　弥生", "　卯月","　皐月","水無月","　文月","　葉月","　長月",   "神有月", "　霜月","　師走")
LTsv_monthenl=  ("January","February","March","April", "May",   "June",  "July",  "August","September","October","November","December")
LTsv_monthens=  ("Jan",    "Feb",     "Mar",  "Apr"  , "May",   "Jun",   "Jul",   "Aug",   "Sep",      "Oct",    "Nov",     "Dec")
LTsv_monthenc=  ("J",      "F",          "C", "A",     "M",       "N",     "L",    "U",    "S",        "O",      "N"       ,"D")
LTsv_monthenh=  ("January","February","marCh","April", "May",   "juNe",  "juLy",  "aUgust","September","October","November","December")
LTsv_weekdayjp =("月",    "火",     "水",       "木",      "金",    "土",     "日")
LTsv_weekdayens=("Mon",   "Tue",    "Wed"      ,"Thu",     "Fri",   "Sat",     "Sun")
LTsv_weekdayenl=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
LTsv_weekdayenc=("M",     "T",      "W",           "R",    "F",     "S",        "U")
LTsv_weekdayenh=("Monday","Tuesday","Wednesday","thuRsday","Friday","Saturday","sUnday")
LTsv_ampmjp= ("午前","午後","徹夜")
LTsv_ampmenl=("am",  "pm", "an")
LTsv_ampmenu=("AM",  "PM", "AN")

def LTsv_yearleap(LTsv_toyear):
    return LTsv_toyear%4==0 and LTsv_toyear%100!=0 or LTsv_toyear%400==0

def LTsv_yearweeks(LTsv_toyear):
    LTsv_Y,LTsv_WN,LTsv_WD=datetime.date(LTsv_toyear,12,31).isocalendar()
    LTsv_YW=LTsv_WN if LTsv_Y==LTsv_toyear else datetime.date(LTsv_toyear,12,24).isocalendar()[1]
    return LTsv_YW

def LTsv_monthleap(LTsv_toyear,LTsv_tomonth):
    return LTsv_maxmonth[LTsv_tomonth] if not LTsv_yearleap(LTsv_toyear) else LTsv_maxmonthleep[LTsv_tomonth]

def LTsv_beat864(LTsv_tohour,LTsv_tominute,LTsv_tosecond):
    LTsv_Beat=LTsv_tohour*3600+LTsv_tominute*60+LTsv_tosecond
    LTsv_BeatInteger=LTsv_Beat*1000//86400
    LTsv_BeatPoint=(LTsv_Beat*1000000//86400)%1000
    return LTsv_Beat,LTsv_BeatInteger,LTsv_BeatPoint

LTsv_earlier_now=datetime.datetime.now()
LTsv_meridian_now=LTsv_earlier_now
LTsv_meridian_Year=LTsv_meridian_now.year
LTsv_meridian_Yearlower=LTsv_meridian_Year%100
LTsv_meridian_YearZodiac=(LTsv_meridian_Year+8)%12
LTsv_meridian_YearDays=365 if not LTsv_yearleap(LTsv_meridian_Year) else 366
LTsv_meridian_YearIso,LTsv_meridian_WeekNumberYearIso,LTsv_meridian_WeekDayIso=LTsv_meridian_now.isocalendar()
LTsv_meridian_YearWeeksIso=LTsv_yearweeks(LTsv_meridian_Year)
LTsv_meridian_Month=LTsv_meridian_now.month
LTsv_meridian_MonthDays=LTsv_monthleap(LTsv_meridian_Year,LTsv_meridian_Month)
LTsv_meridian_WeekDay=LTsv_meridian_now.weekday()
LTsv_meridian_WeekNumberMonth=LTsv_meridian_WeekDay//7+1
LTsv_meridian_DayMonth=LTsv_meridian_now.day
LTsv_meridian_DayYear=LTsv_meridian_now.toordinal()-datetime.date(LTsv_meridian_Year,1,1).toordinal()+1
LTsv_meridian_Hour=LTsv_meridian_now.hour
LTsv_meridian_HourAP=LTsv_meridian_Hour%12
LTsv_meridian_AP=LTsv_meridian_Hour//12
LTsv_meridian_APO=LTsv_meridian_Hour//12
LTsv_meridian_miNute=LTsv_meridian_now.minute
LTsv_meridian_Second=LTsv_meridian_now.second
LTsv_meridian_micRoSecond=LTsv_meridian_now.microsecond
LTsv_meridian_miLliSecond=LTsv_meridian_micRoSecond//1000
LTsv_meridian_Beat,LTsv_meridian_BeatInteger,LTsv_meridian_BeatPoint=LTsv_beat864(LTsv_meridian_Hour,LTsv_meridian_miNute,LTsv_meridian_Second)
LTsv_allnight_now=LTsv_meridian_now
LTsv_allnight_Year=LTsv_meridian_Year
LTsv_allnight_Yearlower=LTsv_meridian_Yearlower
LTsv_allnight_YearZodiac=LTsv_meridian_YearZodiac
LTsv_allnight_YearDays=LTsv_meridian_YearDays
LTsv_allnight_YearIso,LTsv_allnight_WeekNumberYearIso,LTsv_allnight_WeekDayIso=LTsv_meridian_YearIso,LTsv_meridian_WeekNumberYearIso,LTsv_meridian_WeekDayIso
LTsv_allnight_YearWeeksIso=LTsv_meridian_YearWeeksIso
LTsv_allnight_Month=LTsv_meridian_Month
LTsv_allnight_MonthDays=LTsv_meridian_MonthDays
LTsv_allnight_WeekDay=LTsv_meridian_WeekDay
LTsv_allnight_WeekNumberMonth=LTsv_allnight_WeekDay//7+1
LTsv_allnight_DayMonth=LTsv_meridian_DayMonth
LTsv_allnight_DayYear=LTsv_meridian_DayYear
LTsv_allnight_Hour=LTsv_meridian_Hour
LTsv_allnight_miNute=LTsv_meridian_miNute
LTsv_allnight_Second=LTsv_meridian_Second
LTsv_allnight_micRoSecond=LTsv_meridian_now.microsecond
LTsv_allnight_miLliSecond=LTsv_meridian_miLliSecond

LTsv_start_now=LTsv_meridian_now
LTsv_lap_now=LTsv_start_now+datetime.timedelta(microseconds=0)
LTsv_goal_now=LTsv_start_now+datetime.timedelta(microseconds=0)
LTsv_passed_TotalSeconds=(LTsv_lap_now-LTsv_start_now).total_seconds()
LTsv_passed_micRoSecond=int(LTsv_passed_TotalSeconds*1000000)%1000000
LTsv_passed_miLliSecond=int(LTsv_passed_TotalSeconds*1000)%1000
LTsv_passed_Second=int(LTsv_passed_TotalSeconds)%60
LTsv_passed_miNute=int(LTsv_passed_TotalSeconds/60)%60
LTsv_passed_Hour=int(LTsv_passed_TotalSeconds/3600)%24
LTsv_passed_DayHour=int(LTsv_passed_TotalSeconds/3600)
LTsv_passed_Day=int(LTsv_passed_TotalSeconds/86400)
LTsv_passed_Beat,LTsv_passed_BeatInteger,LTsv_passed_BeatPoint=LTsv_beat864(LTsv_passed_Hour,LTsv_passed_miNute,LTsv_passed_Second)
LTsv_timeleft_TotalSeconds=(LTsv_goal_now-LTsv_lap_now).total_seconds()
LTsv_timeleft_micRoSecond=int(LTsv_timeleft_TotalSeconds*1000000)%1000000
LTsv_timeleft_miLliSecond=int(LTsv_timeleft_TotalSeconds*1000)%1000
LTsv_timeleft_Second=int(LTsv_timeleft_TotalSeconds)%60
LTsv_timeleft_miNute=int(LTsv_timeleft_TotalSeconds/60)%60
LTsv_timeleft_Hour=int(LTsv_timeleft_TotalSeconds/3600)%24
LTsv_timeleft_DayHour=int(LTsv_timeleft_TotalSeconds/3600)
LTsv_timeleft_Day=int(LTsv_timeleft_TotalSeconds/86400)
LTsv_timeleft_Beat,LTsv_timeleft_BeatInteger,LTsv_timeleft_BeatPoint=LTsv_beat864(LTsv_timeleft_Hour,LTsv_timeleft_miNute,LTsv_timeleft_Second)
LTsv_limit_TotalSeconds=(LTsv_goal_now-LTsv_start_now).total_seconds()
LTsv_limit_micRoSecond=int(LTsv_limit_TotalSeconds*1000000)%1000000
LTsv_limit_miLliSecond=int(LTsv_limit_TotalSeconds*1000)%1000
LTsv_limit_Second=int(LTsv_limit_TotalSeconds)%60
LTsv_limit_miNute=int(LTsv_limit_TotalSeconds/60)%60
LTsv_limit_Hour=int(LTsv_limit_TotalSeconds/3600)%24
LTsv_limit_DayHour=int(LTsv_limit_TotalSeconds/3600)
LTsv_limit_Day=int(LTsv_limit_TotalSeconds/86400)
LTsv_limit_Beat,LTsv_limit_BeatInteger,LTsv_limit_BeatPoint=LTsv_beat864(LTsv_limit_Hour,LTsv_limit_miNute,LTsv_limit_Second)
LTsv_FPS_now=datetime.datetime.now()
LTsv_FPS_earlier=LTsv_FPS_now
LTsv_FPS_TotalSeconds=(LTsv_FPS_now-LTsv_FPS_earlier).total_seconds()
LTsv_FPS_fPsK=min(max(int(1/LTsv_FPS_TotalSeconds),1),999) if LTsv_FPS_TotalSeconds > 0 else 999
LTsv_FPS_fPsC=min(max(int(1/LTsv_FPS_TotalSeconds),1),99) if LTsv_FPS_TotalSeconds > 0 else 99

#FPS
def LTsv_checkFPS():
    global LTsv_FPS_now,LTsv_FPS_earlier,LTsv_FPS_TotalSeconds,LTsv_FPS_fPsK,LTsv_FPS_fPsC
    LTsv_FPS_now=datetime.datetime.now()
    LTsv_FPS_TotalSeconds=(LTsv_FPS_now-LTsv_FPS_earlier).total_seconds()
    LTsv_FPS_fPsK=min(max(int(1/LTsv_FPS_TotalSeconds),0),999) if LTsv_FPS_TotalSeconds > 0 else 999
    LTsv_FPS_fPsC=min(max(int(1/LTsv_FPS_TotalSeconds),0),99) if LTsv_FPS_TotalSeconds > 0 else 99
    LTsv_FPS_earlier=LTsv_FPS_now
    return LTsv_FPS_fPsK

#daytime
def LTsv_setdaytimeshift():
    global LTsv_meridian_now,LTsv_overhour,LTsv_diffminute,LTsv_HourMAXLower,LTsv_HourMAXUpper
    global LTsv_meridian_miNute,LTsv_meridian_Second,LTsv_meridian_micRoSecond,LTsv_meridian_miLliSecond
    global LTsv_meridian_Beat,LTsv_meridian_BeatInteger,LTsv_meridian_BeatPoint
    global LTsv_meridian_Hour,LTsv_meridian_HourAP,LTsv_meridian_AP,LTsv_meridian_APO
    LTsv_meridian_miNute=LTsv_meridian_now.minute
    LTsv_meridian_Second=LTsv_meridian_now.second
    LTsv_meridian_micRoSecond=LTsv_meridian_now.microsecond
    LTsv_meridian_miLliSecond=LTsv_meridian_micRoSecond//1000
    LTsv_meridian_Hour=LTsv_meridian_now.hour
    LTsv_meridian_HourAP=LTsv_meridian_Hour%12
    LTsv_meridian_AP=LTsv_meridian_Hour//12
    LTsv_meridian_APO=LTsv_meridian_Hour//12
    LTsv_meridian_Beat,LTsv_meridian_BeatInteger,LTsv_meridian_BeatPoint=LTsv_beat864(LTsv_meridian_Hour,LTsv_meridian_miNute,LTsv_meridian_Second)
    global LTsv_meridian_DayMonth,LTsv_meridian_DayYear
    if LTsv_meridian_DayMonth != LTsv_meridian_now.day:
        LTsv_meridian_APO=2
        global LTsv_meridian_Year,LTsv_meridian_Yearlower,LTsv_meridian_YearZodiac,LTsv_meridian_YearDays,LTsv_meridian_YearIso
        global LTsv_meridian_Month,LTsv_meridian_MonthDays,LTsv_meridian_WeekNumberYearIso
        global LTsv_meridian_WeekDay,LTsv_meridian_WeekNumberMonth,LTsv_meridian_WeekDayIso
        LTsv_meridian_Year=LTsv_meridian_now.year
        LTsv_meridian_Yearlower=LTsv_meridian_Year%100
        LTsv_meridian_YearZodiac=(LTsv_meridian_Year+8)%12
        LTsv_meridian_YearDays=365 if not LTsv_yearleap(LTsv_meridian_Year) else 366
        LTsv_meridian_YearIso,LTsv_meridian_WeekNumberYearIso,LTsv_meridian_WeekDayIso=LTsv_meridian_now.isocalendar()
        LTsv_meridian_YearWeeksIso=LTsv_yearweeks(LTsv_meridian_Year)
        LTsv_meridian_Month=LTsv_meridian_now.month
        LTsv_meridian_MonthDays=LTsv_monthleap(LTsv_meridian_Year,LTsv_meridian_Month)
        LTsv_meridian_WeekDay=LTsv_meridian_now.weekday()
        LTsv_meridian_WeekNumberMonth=LTsv_meridian_WeekDay//7+1
        LTsv_meridian_DayMonth=LTsv_meridian_now.day
        LTsv_meridian_DayYear=LTsv_meridian_now.toordinal()-datetime.date(LTsv_meridian_Year,1,1).toordinal()+1

    global LTsv_allnight_now
    global LTsv_allnight_miNute,LTsv_allnight_Second,LTsv_allnight_micRoSecond,LTsv_allnight_miLliSecond
    LTsv_allnight_miNute=LTsv_meridian_miNute
    LTsv_allnight_Second=LTsv_meridian_Second
    LTsv_allnight_miLliSecond=LTsv_meridian_miLliSecond
    LTsv_allnight_micRoSecond=LTsv_meridian_micRoSecond
    global LTsv_allnight_Hour
    if LTsv_HourMAXLower+LTsv_meridian_Hour < LTsv_overhour:
        LTsv_allnight_now=LTsv_meridian_now-datetime.timedelta(days=1)
        LTsv_allnight_Hour=LTsv_HourMAXLower+LTsv_meridian_Hour
    else:
        LTsv_allnight_now=LTsv_meridian_now
        LTsv_allnight_Hour=LTsv_meridian_Hour
    global LTsv_allnight_DayMonth,LTsv_allnight_DayYear
    if LTsv_allnight_DayMonth != LTsv_allnight_now.day:
        global LTsv_allnight_Year,LTsv_allnight_Yearlower,LTsv_allnight_YearZodiac,LTsv_allnight_YearDays,LTsv_allnight_YearIso
        global LTsv_allnight_Month,LTsv_allnight_MonthDays,LTsv_allnight_WeekNumberYearIso
        global LTsv_allnight_WeekDay,LTsv_allnight_WeekNumberMonth,LTsv_allnight_WeekDayIso
        LTsv_allnight_Year=LTsv_allnight_now.year
        LTsv_allnight_Yearlower=LTsv_allnight_Year%100
        LTsv_allnight_YearZodiac=(LTsv_allnight_Year+8)%12
        LTsv_allnight_YearDays=365 if not LTsv_yearleap(LTsv_allnight_Year) else 366
        LTsv_allnight_YearIso,LTsv_allnight_WeekNumberYearIso,LTsv_allnight_WeekDayIso=LTsv_allnight_now.isocalendar()
        LTsv_allnight_YearWeeksIso=LTsv_yearweeks(LTsv_allnight_Year)
        LTsv_allnight_Month=LTsv_allnight_now.month
        LTsv_allnight_MonthDays=LTsv_monthleap(LTsv_allnight_Year,LTsv_allnight_Month)
        LTsv_allnight_WeekDay=LTsv_allnight_now.weekday()
        LTsv_allnight_WeekNumberMonth=LTsv_allnight_WeekDay//7+1
        LTsv_allnight_DayMonth=LTsv_allnight_now.day
        LTsv_allnight_DayYear=LTsv_allnight_now.toordinal()-datetime.date(LTsv_allnight_Year,1,1).toordinal()+1

def LTsv_setdaytimeoption(overhour=None,diffminute=None):
    global LTsv_meridian_now,LTsv_overhour,LTsv_diffminute,LTsv_HourMAXLower,LTsv_HourMAXUpper
    LTsv_overhour=LTsv_overhour if overhour is None else min(max(overhour,LTsv_HourMAXLower),LTsv_HourMAXUpper)
    LTsv_diffminute=LTsv_diffminute if diffminute is None else min(max(diffminute,-24*60),+24*60)

def LTsv_putdaytimespecify(LTsv_toyear,LTsv_tomonth,LTsv_today,LTsv_tohour,LTsv_tominute,LTsv_tosecond,LTsv_tomicrosecond,overhour=None,diffminute=None):
    LTsv_setdaytimeoption(overhour,diffminute)
    global LTsv_meridian_now,LTsv_overhour,LTsv_diffminute,LTsv_HourMAXLower,LTsv_HourMAXUpper
    LTsv_year=min(max(LTsv_toyear,datetime.MINYEAR),datetime.MAXYEAR)
    LTsv_month=min(max(LTsv_tomonth,1),12)
    LTsv_day=min(max(LTsv_today,1),LTsv_monthleap(LTsv_year,LTsv_month))
    LTsv_hour=min(max(LTsv_tohour,0),23)
    LTsv_minute=min(max(LTsv_tominute,0),59)
    LTsv_second=min(max(LTsv_tosecond,0),59)
    LTsv_microsecond=min(max(LTsv_tomicrosecond,0),999999)
    LTsv_meridian_now=datetime.datetime(LTsv_year,LTsv_month,LTsv_day,LTsv_hour,LTsv_minute,LTsv_second,LTsv_microsecond)+datetime.timedelta(minutes=LTsv_diffminute)
    LTsv_setdaytimeshift()
    return LTsv_meridian_now

def LTsv_putdaytimever(LTsv_verstr,overhour=None,diffminute=None):
    LTsv_setdaytimeoption(overhour,diffminute)
    global LTsv_meridian_now,LTsv_overhour,LTsv_diffminute,LTsv_HourMAXLower,LTsv_HourMAXUpper
    LTsv_ymd,LTsv_hns=0,0
    try:
        LTsv_ymd=int(LTsv_verstr[0:8])
        LTsv_hns=int(LTsv_verstr[-6:])
    except ValueError:
        pass
    LTsv_year=min(max(LTsv_ymd//10000,datetime.MINYEAR),datetime.MAXYEAR)
    LTsv_month=min(max(LTsv_ymd//100%100,1),12)
    LTsv_day=min(max(LTsv_ymd%100,1),LTsv_monthleap(LTsv_year,LTsv_month))
    LTsv_hour=min(max(LTsv_hns//10000,0),23)
    LTsv_minute=min(max(LTsv_hns//100%100,0),59)
    LTsv_second=min(max(LTsv_hns%100,0),59)
    LTsv_microsecond=0
    LTsv_meridian_now=datetime.datetime(LTsv_year,LTsv_month,LTsv_day,LTsv_hour,LTsv_minute,LTsv_second,LTsv_microsecond)+datetime.timedelta(minutes=LTsv_diffminute)
    LTsv_setdaytimeshift()
    return LTsv_meridian_now

def LTsv_putdaytimenow(overhour=None,diffminute=None):
    LTsv_setdaytimeoption(overhour,diffminute)
    global LTsv_earlier_now
    global LTsv_meridian_now,LTsv_overhour,LTsv_diffminute,LTsv_HourMAXLower,LTsv_HourMAXUpper
    LTsv_earlier_now=datetime.datetime.now()
    LTsv_meridian_now=LTsv_earlier_now+datetime.timedelta(minutes=LTsv_diffminute)
    LTsv_setdaytimeshift()
    return LTsv_meridian_now

def LTsv_putdaytimeearlier(overhour=None,diffminute=None):
    LTsv_setdaytimeoption(overhour,diffminute)
    global LTsv_earlier_now
    global LTsv_meridian_now,LTsv_overhour,LTsv_diffminute,LTsv_HourMAXLower,LTsv_HourMAXUpper
    LTsv_meridian_now=LTsv_earlier_now+datetime.timedelta(minutes=LTsv_diffminute)
    LTsv_setdaytimeshift()
    return LTsv_meridian_now

def LTsv_putdaytimemodify(LTsv_path,overhour=None,diffminute=None):
    LTsv_setdaytimeoption(overhour,diffminute)
    global LTsv_meridian_now,LTsv_overhour,LTsv_diffminute,LTsv_HourMAXLower,LTsv_HourMAXUpper
    LTsv_meridian_now=datetime.datetime.fromtimestamp(os.stat(LTsv_path).st_mtime)+datetime.timedelta(minutes=LTsv_diffminute)
    LTsv_setdaytimeshift()
    return LTsv_meridian_now

def LTsv_getdaytimestr(timeformat=None,overhour=None,diffminute=None):
    global LTsv_overhour,LTsv_diffminute
    if not overhour is None or not diffminute is None:
        LTsv_overhour=LTsv_overhour if overhour is None else overhour
        LTsv_diffminute=LTsv_diffminute if diffminute is None else diffminute
        LTsv_putdaytimenow(LTsv_overhour,LTsv_diffminute)
    LTsv_tf="@000y@0m@0dm@wdec@0h@0n@0s" if timeformat is None else timeformat
    LTsv_tf=LTsv_tf if not "@@"     in LTsv_tf else LTsv_tf.replace("@@","\t")

    global LTsv_meridian_miNute,LTsv_meridian_Second,LTsv_meridian_micRoSecond,LTsv_meridian_miLliSecond
    global LTsv_meridian_Hour,LTsv_meridian_HourAP,LTsv_meridian_AP,LTsv_meridian_APO
    global LTsv_meridian_DayMonth,LTsv_meridian_DayYear
    global LTsv_meridian_Year,LTsv_meridian_Yearlower,LTsv_meridian_YearZodiac,LTsv_meridian_YearDays,LTsv_meridian_YearIso
    global LTsv_meridian_Month,LTsv_meridian_MonthDays,LTsv_meridian_WeekNumberYearIso
    global LTsv_meridian_WeekDay,LTsv_meridian_WeekNumberMonth,LTsv_meridian_WeekDayIso
    global LTsv_allnight_miNute,LTsv_allnight_Second,LTsv_allnight_micRoSecond,LTsv_allnight_miLliSecond
    global LTsv_meridian_Beat,LTsv_meridian_BeatInteger,LTsv_meridian_BeatPoint
    global LTsv_allnight_Hour
    global LTsv_allnight_DayMonth,LTsv_allnight_DayYear
    global LTsv_allnight_Year,LTsv_allnight_Yearlower,LTsv_allnight_YearZodiac,LTsv_allnight_YearDays,LTsv_allnight_YearIso
    global LTsv_allnight_Month,LTsv_allnight_MonthDays,LTsv_allnight_WeekNumberYearIso
    global LTsv_allnight_WeekDay,LTsv_allnight_WeekNumberMonth,LTsv_allnight_WeekDayIso
    global LTsv_FPS_now,LTsv_FPS_earlier,LTsv_FPS_TotalSeconds,LTsv_FPS_fPsK,LTsv_FPS_fPsC
    LTsv_tf=LTsv_tf if not "@yzj"   in LTsv_tf else LTsv_tf.replace("@yzj"  ,"{0}".format(LTsv_zodiacjp[LTsv_meridian_YearZodiac]))
    LTsv_tf=LTsv_tf if not "@yzc"   in LTsv_tf else LTsv_tf.replace("@yzc"  ,"{0}".format(LTsv_zodiacch[LTsv_meridian_YearZodiac]))
    LTsv_tf=LTsv_tf if not "@0yz"   in LTsv_tf else LTsv_tf.replace("@0yz"  ,"{0:0>2}".format(LTsv_meridian_YearZodiac))
    LTsv_tf=LTsv_tf if not "@_yz"   in LTsv_tf else LTsv_tf.replace("@_yz"  ,"{0: >2}".format(LTsv_meridian_YearZodiac))
    LTsv_tf=LTsv_tf if not "@yz"    in LTsv_tf else LTsv_tf.replace("@yz"   ,"{0:2}".format(LTsv_meridian_YearZodiac))
    LTsv_tf=LTsv_tf if not "@0yd"   in LTsv_tf else LTsv_tf.replace("@0yd"  ,"{0:0>3}".format(LTsv_meridian_YearDays))
    LTsv_tf=LTsv_tf if not "@_yd"   in LTsv_tf else LTsv_tf.replace("@_yd"  ,"{0:0>3}".format(LTsv_meridian_YearDays))
    LTsv_tf=LTsv_tf if not "@yd"    in LTsv_tf else LTsv_tf.replace("@yd"   ,"{0}".format(LTsv_meridian_YearDays))
    LTsv_tf=LTsv_tf if not "@0ywi"  in LTsv_tf else LTsv_tf.replace("@0ywi" ,"{0:0>2}".format(LTsv_meridian_YearWeeksIso))
    LTsv_tf=LTsv_tf if not "@_ywi"  in LTsv_tf else LTsv_tf.replace("@_ywi" ,"{0: >2}".format(LTsv_meridian_YearWeeksIso))
    LTsv_tf=LTsv_tf if not "@ywi"   in LTsv_tf else LTsv_tf.replace("@ywi"  ,"{0}".format(LTsv_meridian_YearWeeksIso))
    LTsv_tf=LTsv_tf if not "@000yi" in LTsv_tf else LTsv_tf.replace("@000y" ,"{0:0>4}".format(LTsv_meridian_YearIso))
    LTsv_tf=LTsv_tf if not "@___yi" in LTsv_tf else LTsv_tf.replace("@___yi","{0: >4}".format(LTsv_meridian_YearIso))
    LTsv_tf=LTsv_tf if not "@4yi"   in LTsv_tf else LTsv_tf.replace("@4yi"  ,"{0:4}".format(LTsv_meridian_YearIso))
    LTsv_tf=LTsv_tf if not "@0yi"   in LTsv_tf else LTsv_tf.replace("@0yi"  ,"{0:0>2}".format(LTsv_meridian_YearIso))
    LTsv_tf=LTsv_tf if not "@_yi"   in LTsv_tf else LTsv_tf.replace("@_yi"  ,"{0: >2}".format(LTsv_meridian_YearIso))
    LTsv_tf=LTsv_tf if not "@2yi"   in LTsv_tf else LTsv_tf.replace("@2yi"  ,"{0:2}".format(LTsv_meridian_YearIso))
    LTsv_tf=LTsv_tf if not "@yi"    in LTsv_tf else LTsv_tf.replace("@yi"   ,"{0}".format(LTsv_meridian_YearIso))
    LTsv_tf=LTsv_tf if not "@000y"  in LTsv_tf else LTsv_tf.replace("@000y" ,"{0:0>4}".format(LTsv_meridian_Year))
    LTsv_tf=LTsv_tf if not "@___y"  in LTsv_tf else LTsv_tf.replace("@___y" ,"{0: >4}".format(LTsv_meridian_Year))
    LTsv_tf=LTsv_tf if not "@4y"    in LTsv_tf else LTsv_tf.replace("@4y"   ,"{0:4}".format(LTsv_meridian_Year))
    LTsv_tf=LTsv_tf if not "@0y"    in LTsv_tf else LTsv_tf.replace("@0y"   ,"{0:0>2}".format(LTsv_meridian_Yearlower))
    LTsv_tf=LTsv_tf if not "@_y"    in LTsv_tf else LTsv_tf.replace("@_y"   ,"{0: >2}".format(LTsv_meridian_Yearlower))
    LTsv_tf=LTsv_tf if not "@2y"    in LTsv_tf else LTsv_tf.replace("@2y"   ,"{0:2}".format(LTsv_meridian_Yearlower))
    LTsv_tf=LTsv_tf if not "@y"     in LTsv_tf else LTsv_tf.replace("@y"    ,"{0}".format(LTsv_meridian_Year))
    LTsv_tf=LTsv_tf if not "@Yzj"   in LTsv_tf else LTsv_tf.replace("@Yzj"  ,"{0}".format(LTsv_zodiacjp[LTsv_allnight_YearZodiac]))
    LTsv_tf=LTsv_tf if not "@Yzc"   in LTsv_tf else LTsv_tf.replace("@Yzc"  ,"{0}".format(LTsv_zodiacch[LTsv_allnight_YearZodiac]))
    LTsv_tf=LTsv_tf if not "@0Yz"   in LTsv_tf else LTsv_tf.replace("@0Yz"  ,"{0:0>2}".format(LTsv_allnight_YearZodiac))
    LTsv_tf=LTsv_tf if not "@_Yz"   in LTsv_tf else LTsv_tf.replace("@_Yz"  ,"{0: >2}".format(LTsv_allnight_YearZodiac))
    LTsv_tf=LTsv_tf if not "@Yz"    in LTsv_tf else LTsv_tf.replace("@Yz"   ,"{0:2}".format(LTsv_allnight_YearZodiac))
    LTsv_tf=LTsv_tf if not "@0Yd"   in LTsv_tf else LTsv_tf.replace("@0Yd"  ,"{0:0>3}".format(LTsv_allnight_YearDays))
    LTsv_tf=LTsv_tf if not "@_Yd"   in LTsv_tf else LTsv_tf.replace("@_Yd"  ,"{0:0>3}".format(LTsv_allnight_YearDays))
    LTsv_tf=LTsv_tf if not "@Yd"    in LTsv_tf else LTsv_tf.replace("@Yd"   ,"{0}".format(LTsv_allnight_YearDays))
    LTsv_tf=LTsv_tf if not "@0Ywi"  in LTsv_tf else LTsv_tf.replace("@0Ywi" ,"{0:0>2}".format(LTsv_allnight_YearWeeksIso))
    LTsv_tf=LTsv_tf if not "@_Ywi"  in LTsv_tf else LTsv_tf.replace("@_Ywi" ,"{0: >2}".format(LTsv_allnight_YearWeeksIso))
    LTsv_tf=LTsv_tf if not "@Ywi"   in LTsv_tf else LTsv_tf.replace("@Ywi"  ,"{0}".format(LTsv_allnight_YearWeeksIso))
    LTsv_tf=LTsv_tf if not "@000Yi" in LTsv_tf else LTsv_tf.replace("@000Y" ,"{0:0>4}".format(LTsv_allnight_YearIso))
    LTsv_tf=LTsv_tf if not "@___Yi" in LTsv_tf else LTsv_tf.replace("@___Yi","{0: >4}".format(LTsv_allnight_YearIso))
    LTsv_tf=LTsv_tf if not "@4Yi"   in LTsv_tf else LTsv_tf.replace("@4Yi"  ,"{0:4}".format(LTsv_allnight_YearIso))
    LTsv_tf=LTsv_tf if not "@0Yi"   in LTsv_tf else LTsv_tf.replace("@0Yi"  ,"{0:0>2}".format(LTsv_allnight_YearIso))
    LTsv_tf=LTsv_tf if not "@_Yi"   in LTsv_tf else LTsv_tf.replace("@_Yi"  ,"{0: >2}".format(LTsv_allnight_YearIso))
    LTsv_tf=LTsv_tf if not "@2Yi"   in LTsv_tf else LTsv_tf.replace("@2Yi"  ,"{0:2}".format(LTsv_allnight_YearIso))
    LTsv_tf=LTsv_tf if not "@Yi"    in LTsv_tf else LTsv_tf.replace("@Yi"   ,"{0}".format(LTsv_allnight_YearIso))
    LTsv_tf=LTsv_tf if not "@000Y"  in LTsv_tf else LTsv_tf.replace("@000Y" ,"{0:0>4}".format(LTsv_allnight_Year))
    LTsv_tf=LTsv_tf if not "@___Y"  in LTsv_tf else LTsv_tf.replace("@___Y" ,"{0: >4}".format(LTsv_allnight_Year))
    LTsv_tf=LTsv_tf if not "@4Y"    in LTsv_tf else LTsv_tf.replace("@4Y"   ,"{0:4}".format(LTsv_allnight_Year))
    LTsv_tf=LTsv_tf if not "@0Y"    in LTsv_tf else LTsv_tf.replace("@0Y"   ,"{0:0>2}".format(LTsv_allnight_Yearlower))
    LTsv_tf=LTsv_tf if not "@_Y"    in LTsv_tf else LTsv_tf.replace("@_Y"   ,"{0: >2}".format(LTsv_allnight_Yearlower))
    LTsv_tf=LTsv_tf if not "@2Y"    in LTsv_tf else LTsv_tf.replace("@2Y"   ,"{0:2}".format(LTsv_allnight_Yearlower))
    LTsv_tf=LTsv_tf if not "@Y"     in LTsv_tf else LTsv_tf.replace("@Y"    ,"{0}".format(LTsv_allnight_Year))

    LTsv_tf=LTsv_tf if not "@0md"   in LTsv_tf else LTsv_tf.replace("@0md"  ,"{0:0>2}".format(LTsv_meridian_MonthDays))
    LTsv_tf=LTsv_tf if not "@_md"   in LTsv_tf else LTsv_tf.replace("@_md"  ,"{0:0>2}".format(LTsv_meridian_MonthDays))
    LTsv_tf=LTsv_tf if not "@md"    in LTsv_tf else LTsv_tf.replace("@md"   ,"{0}".format(LTsv_meridian_MonthDays))
    LTsv_tf=LTsv_tf if not "@mec"   in LTsv_tf else LTsv_tf.replace("@mec"  ,"{0}".format(LTsv_monthenc[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@mes"   in LTsv_tf else LTsv_tf.replace("@mes"  ,"{0}".format(LTsv_monthens[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@mel"   in LTsv_tf else LTsv_tf.replace("@mel"  ,"{0}".format(LTsv_monthenl[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@_mel"  in LTsv_tf else LTsv_tf.replace("@_mel" ,"{0: >9}".format(LTsv_monthenl[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@meh"   in LTsv_tf else LTsv_tf.replace("@meh"  ,"{0}".format(LTsv_monthenh[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@_meh"  in LTsv_tf else LTsv_tf.replace("@_meh" ,"{0: >9}".format(LTsv_monthenh[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@mjiz"  in LTsv_tf else LTsv_tf.replace("@mjiz" ,"{0}".format(LTsv_monthjpiz[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@_mjiz" in LTsv_tf else LTsv_tf.replace("@mjiz" ,"{0}".format(LTsv_monthjpiz[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@mj"    in LTsv_tf else LTsv_tf.replace("@mj"   ,"{0}".format(LTsv_monthjp[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@_mj"   in LTsv_tf else LTsv_tf.replace("@mj"   ,"{0}".format(LTsv_monthjp[LTsv_meridian_Month]))
    LTsv_tf=LTsv_tf if not "@0m"    in LTsv_tf else LTsv_tf.replace("@0m"   ,"{0:0>2}".format(LTsv_meridian_Month))
    LTsv_tf=LTsv_tf if not "@_m"    in LTsv_tf else LTsv_tf.replace("@_m"   ,"{0: >2}".format(LTsv_meridian_Month))
    LTsv_tf=LTsv_tf if not "@mz"    in LTsv_tf else LTsv_tf.replace("@mz"  ,"０１２３４５６７８９"[LTsv_allnight_Month]) if LTsv_meridian_Month <= 9 else LTsv_tf.replace("@Mz","{0}".format(LTsv_allnight_Month))
    LTsv_tf=LTsv_tf if not "@m"     in LTsv_tf else LTsv_tf.replace("@m"    ,"{0}".format(LTsv_meridian_Month))
    LTsv_tf=LTsv_tf if not "@0Md"   in LTsv_tf else LTsv_tf.replace("@0Md"  ,"{0:0>2}".format(LTsv_allnight_MonthDays))
    LTsv_tf=LTsv_tf if not "@_Md"   in LTsv_tf else LTsv_tf.replace("@_Md"  ,"{0:0>2}".format(LTsv_allnight_MonthDays))
    LTsv_tf=LTsv_tf if not "@Md"    in LTsv_tf else LTsv_tf.replace("@Md"   ,"{0}".format(LTsv_allnight_MonthDays))
    LTsv_tf=LTsv_tf if not "@Mec"   in LTsv_tf else LTsv_tf.replace("@Mec"  ,"{0}".format(LTsv_monthenc[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@Mes"   in LTsv_tf else LTsv_tf.replace("@Mes"  ,"{0}".format(LTsv_monthens[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@Mel"   in LTsv_tf else LTsv_tf.replace("@Mel"  ,"{0}".format(LTsv_monthenl[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@_Mel"  in LTsv_tf else LTsv_tf.replace("@_Mel" ,"{0: >9}".format(LTsv_monthenl[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@Meh"   in LTsv_tf else LTsv_tf.replace("@Meh"  ,"{0}".format(LTsv_monthenh[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@_Meh"  in LTsv_tf else LTsv_tf.replace("@_Meh" ,"{0: >9}".format(LTsv_monthenh[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@Mjiz"  in LTsv_tf else LTsv_tf.replace("@Mjiz" ,"{0}".format(LTsv_monthjpiz[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@_Mjiz" in LTsv_tf else LTsv_tf.replace("@Mjiz" ,"{0}".format(LTsv_monthjpiz[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@Mj"    in LTsv_tf else LTsv_tf.replace("@Mj"   ,"{0}".format(LTsv_monthjp[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@_Mj"   in LTsv_tf else LTsv_tf.replace("@Mj"   ,"{0}".format(LTsv_monthjp[LTsv_allnight_Month]))
    LTsv_tf=LTsv_tf if not "@0M"    in LTsv_tf else LTsv_tf.replace("@0M"   ,"{0:0>2}".format(LTsv_allnight_Month))
    LTsv_tf=LTsv_tf if not "@_M"    in LTsv_tf else LTsv_tf.replace("@_M"   ,"{0: >2}".format(LTsv_allnight_Month))
    LTsv_tf=LTsv_tf if not "@Mz"    in LTsv_tf else LTsv_tf.replace("@Mz"  ,"０１２３４５６７８９"[LTsv_allnight_Month]) if LTsv_meridian_Month <= 9 else LTsv_tf.replace("@Mz","{0}".format(LTsv_allnight_Month))
    LTsv_tf=LTsv_tf if not "@M"     in LTsv_tf else LTsv_tf.replace("@M"    ,"{0}".format(LTsv_allnight_Month))

    LTsv_tf=LTsv_tf if not "@0wnyi" in LTsv_tf else LTsv_tf.replace("@0wnyi","{0:0>2}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@_wnyi" in LTsv_tf else LTsv_tf.replace("@_wnyi","{0: >2}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@wnyiz" in LTsv_tf else LTsv_tf.replace("@wnyiz","０１２３４５６７８９"[LTsv_meridian_WeekNumberYearIso]) if LTsv_meridian_WeekNumberYearIso <= 9 else LTsv_tf.replace("@wnyiz","{0}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@wnyi"  in LTsv_tf else LTsv_tf.replace("@wnyi" ,"{0}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@0Wnyi" in LTsv_tf else LTsv_tf.replace("@0Wnyi","{0:0>2}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@_Wnyi" in LTsv_tf else LTsv_tf.replace("@_Wnyi","{0: >2}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@Wnyiz" in LTsv_tf else LTsv_tf.replace("@Wnyiz","０１２３４５６７８９"[LTsv_meridian_WeekNumberYearIso]) if LTsv_meridian_WeekNumberYearIso <= 9 else LTsv_tf.replace("@Wnyiz","{0}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@Wnyi"  in LTsv_tf else LTsv_tf.replace("@Wnyi" ,"{0}".format(LTsv_meridian_WeekNumberYearIso))
    LTsv_tf=LTsv_tf if not "@0wnm"  in LTsv_tf else LTsv_tf.replace("@0wnm" ,"{0:0>2}".format(LTsv_meridian_WeekNumberMonth))
    LTsv_tf=LTsv_tf if not "@_wnm"  in LTsv_tf else LTsv_tf.replace("@_wnm" ,"{0: >2}".format(LTsv_meridian_WeekNumberMonth))
    LTsv_tf=LTsv_tf if not "@wnmz"  in LTsv_tf else LTsv_tf.replace("@wnmz" ,"０１２３４５６７８９"[LTsv_meridian_WeekNumberMonth]) if LTsv_meridian_WeekNumberMonth <= 9 else LTsv_tf.replace("@wnmz","{0}".format(LTsv_meridian_WeekNumberMonth))
    LTsv_tf=LTsv_tf if not "@wnm"   in LTsv_tf else LTsv_tf.replace("@wnm"  ,"{0}".format(LTsv_meridian_WeekNumberMonth))
    LTsv_tf=LTsv_tf if not "@0Wnm"  in LTsv_tf else LTsv_tf.replace("@0Wnm" ,"{0:0>2}".format(LTsv_meridian_WeekNumberMonth))
    LTsv_tf=LTsv_tf if not "@_Wnm"  in LTsv_tf else LTsv_tf.replace("@_Wnm" ,"{0: >2}".format(LTsv_meridian_WeekNumberMonth))
    LTsv_tf=LTsv_tf if not "@Wnmz"  in LTsv_tf else LTsv_tf.replace("@Wnmz" ,"０１２３４５６７８９"[LTsv_meridian_WeekNumberMonth]) if LTsv_meridian_WeekNumberMonth <= 9 else LTsv_tf.replace("@Wnmz","{0}".format(LTsv_meridian_WeekNumberMonth))
    LTsv_tf=LTsv_tf if not "@Wnm"   in LTsv_tf else LTsv_tf.replace("@Wnm"  ,"{0}".format(LTsv_meridian_WeekNumberMonth))

    LTsv_tf=LTsv_tf if not "@wdj"   in LTsv_tf else LTsv_tf.replace("@wdj"  ,"{0}".format(LTsv_weekdayjp[LTsv_meridian_WeekDay]))
    LTsv_tf=LTsv_tf if not "@wdec"  in LTsv_tf else LTsv_tf.replace("@wdec" ,"{0}".format(LTsv_weekdayenc[LTsv_meridian_WeekDay]))
    LTsv_tf=LTsv_tf if not "@wdes"  in LTsv_tf else LTsv_tf.replace("@wdes" ,"{0}".format(LTsv_weekdayens[LTsv_meridian_WeekDay]))
    LTsv_tf=LTsv_tf if not "@wdel"  in LTsv_tf else LTsv_tf.replace("@wdel" ,"{0}".format(LTsv_weekdayenl[LTsv_meridian_WeekDay]))
    LTsv_tf=LTsv_tf if not "@_wdel" in LTsv_tf else LTsv_tf.replace("@_wdel","{0: >9}".format(LTsv_weekdayenl[LTsv_meridian_WeekDay]))
    LTsv_tf=LTsv_tf if not "@wdeh"  in LTsv_tf else LTsv_tf.replace("@wdeh" ,"{0}".format(LTsv_weekdayenh[LTsv_meridian_WeekDay]))
    LTsv_tf=LTsv_tf if not "@_wdeh" in LTsv_tf else LTsv_tf.replace("@_wdeh","{0: >9}".format(LTsv_weekdayenh[LTsv_meridian_WeekDay]))
    LTsv_tf=LTsv_tf if not "@wdi"   in LTsv_tf else LTsv_tf.replace("@wdi"  ,"{0}".format(LTsv_meridian_WeekDayIso))
    LTsv_tf=LTsv_tf if not "@wd"    in LTsv_tf else LTsv_tf.replace("@wd"   ,"{0}".format(LTsv_meridian_WeekDay))
    LTsv_tf=LTsv_tf if not "@Wdj"   in LTsv_tf else LTsv_tf.replace("@Wdj"  ,"{0}".format(LTsv_weekdayjp[LTsv_allnight_WeekDay]))
    LTsv_tf=LTsv_tf if not "@Wdec"  in LTsv_tf else LTsv_tf.replace("@Wdec" ,"{0}".format(LTsv_weekdayenc[LTsv_allnight_WeekDay]))
    LTsv_tf=LTsv_tf if not "@Wdes"  in LTsv_tf else LTsv_tf.replace("@Wdes" ,"{0}".format(LTsv_weekdayens[LTsv_allnight_WeekDay]))
    LTsv_tf=LTsv_tf if not "@Wdel"  in LTsv_tf else LTsv_tf.replace("@Wdel" ,"{0}".format(LTsv_weekdayenl[LTsv_allnight_WeekDay]))
    LTsv_tf=LTsv_tf if not "@_Wdel" in LTsv_tf else LTsv_tf.replace("@_Wdel","{0: >9}".format(LTsv_weekdayenl[LTsv_allnight_WeekDay]))
    LTsv_tf=LTsv_tf if not "@Wdeh"  in LTsv_tf else LTsv_tf.replace("@Wdeh" ,"{0}".format(LTsv_weekdayenh[LTsv_allnight_WeekDay]))
    LTsv_tf=LTsv_tf if not "@_Wdeh" in LTsv_tf else LTsv_tf.replace("@_Wdeh","{0: >9}".format(LTsv_weekdayenh[LTsv_allnight_WeekDay]))
    LTsv_tf=LTsv_tf if not "@Wdi"   in LTsv_tf else LTsv_tf.replace("@Wdi"  ,"{0}".format(LTsv_allnight_WeekDayIso))
    LTsv_tf=LTsv_tf if not "@Wd"    in LTsv_tf else LTsv_tf.replace("@Wd"   ,"{0}".format(LTsv_allnight_WeekDay))

    LTsv_tf=LTsv_tf if not "@0dm"   in LTsv_tf else LTsv_tf.replace("@0dm"  ,"{0:0>2}".format(LTsv_meridian_DayMonth))
    LTsv_tf=LTsv_tf if not "@_dm"   in LTsv_tf else LTsv_tf.replace("@_dm"  ,"{0: >2}".format(LTsv_meridian_DayMonth))
    LTsv_tf=LTsv_tf if not "@dmz"   in LTsv_tf else LTsv_tf.replace("@dmz"  ,"０１２３４５６７８９"[LTsv_meridian_DayMonth]) if LTsv_meridian_DayMonth <= 9 else LTsv_tf.replace("@dmz","{0}".format(LTsv_meridian_DayMonth))
    LTsv_tf=LTsv_tf if not "@dm"    in LTsv_tf else LTsv_tf.replace("@dm"   ,"{0}".format(LTsv_meridian_DayMonth))
    LTsv_tf=LTsv_tf if not "@0dy"   in LTsv_tf else LTsv_tf.replace("@0dy"  ,"{0:0>2}".format(LTsv_meridian_DayYear))
    LTsv_tf=LTsv_tf if not "@_dy"   in LTsv_tf else LTsv_tf.replace("@_dy"  ,"{0: >2}".format(LTsv_meridian_DayYear))
    LTsv_tf=LTsv_tf if not "@dy"    in LTsv_tf else LTsv_tf.replace("@dy"   ,"{0}".format(LTsv_meridian_DayYear))
    LTsv_tf=LTsv_tf if not "@0Dm"   in LTsv_tf else LTsv_tf.replace("@0Dm"  ,"{0:0>2}".format(LTsv_allnight_DayMonth))
    LTsv_tf=LTsv_tf if not "@_Dm"   in LTsv_tf else LTsv_tf.replace("@_Dm"  ,"{0: >2}".format(LTsv_allnight_DayMonth))
    LTsv_tf=LTsv_tf if not "@Dmz"   in LTsv_tf else LTsv_tf.replace("@Dmz"  ,"０１２３４５６７８９"[LTsv_allnight_DayMonth]) if LTsv_allnight_DayMonth <= 9 else LTsv_tf.replace("@Dmz","{0}".format(LTsv_allnight_DayMonth))
    LTsv_tf=LTsv_tf if not "@Dm"    in LTsv_tf else LTsv_tf.replace("@Dm"   ,"{0}".format(LTsv_allnight_DayMonth))
    LTsv_tf=LTsv_tf if not "@0Dy"   in LTsv_tf else LTsv_tf.replace("@0Dy"  ,"{0:0>2}".format(LTsv_allnight_DayYear))
    LTsv_tf=LTsv_tf if not "@_Dy"   in LTsv_tf else LTsv_tf.replace("@_Dy"  ,"{0: >2}".format(LTsv_allnight_DayYear))
    LTsv_tf=LTsv_tf if not "@Dy"    in LTsv_tf else LTsv_tf.replace("@Dy"   ,"{0}".format(LTsv_allnight_DayYear))

    LTsv_tf=LTsv_tf if not "@apj"   in LTsv_tf else LTsv_tf.replace("@apj"  ,"{0}".format(LTsv_ampmjp[LTsv_meridian_AP]))
    LTsv_tf=LTsv_tf if not "@apel"  in LTsv_tf else LTsv_tf.replace("@apl"  ,"{0}".format(LTsv_ampmenl[LTsv_meridian_AP]))
    LTsv_tf=LTsv_tf if not "@apeu"  in LTsv_tf else LTsv_tf.replace("@apu"  ,"{0}".format(LTsv_ampmenu[LTsv_meridian_AP]))
    LTsv_tf=LTsv_tf if not "@ap"    in LTsv_tf else LTsv_tf.replace("@ap"   ,"{0}".format(LTsv_meridian_AP))
    LTsv_tf=LTsv_tf if not "@Apj"   in LTsv_tf else LTsv_tf.replace("@Apj"  ,"{0}".format(LTsv_ampmjp[LTsv_meridian_APO]))
    LTsv_tf=LTsv_tf if not "@Apel"  in LTsv_tf else LTsv_tf.replace("@Apl"  ,"{0}".format(LTsv_ampmenl[LTsv_meridian_APO]))
    LTsv_tf=LTsv_tf if not "@Apeu"  in LTsv_tf else LTsv_tf.replace("@Apu"  ,"{0}".format(LTsv_ampmenu[LTsv_meridian_APO]))
    LTsv_tf=LTsv_tf if not "@Ap"    in LTsv_tf else LTsv_tf.replace("@Ap"   ,"{0}".format(LTsv_meridian_APO))
    LTsv_tf=LTsv_tf if not "@0hap"  in LTsv_tf else LTsv_tf.replace("@0hap" ,"{0:0>2}".format(LTsv_meridian_HourAP))
    LTsv_tf=LTsv_tf if not "@_hap"  in LTsv_tf else LTsv_tf.replace("@_hap" ,"{0: >2}".format(LTsv_meridian_HourAP))
    LTsv_tf=LTsv_tf if not "@hapz"  in LTsv_tf else LTsv_tf.replace("@hapz" ,"０１２３４５６７８９"[LTsv_meridian_HourAP]) if LTsv_meridian_HourAP <= 9 else LTsv_tf.replace("@hapz","{0}".format(LTsv_meridian_HourAP))
    LTsv_tf=LTsv_tf if not "@hap"   in LTsv_tf else LTsv_tf.replace("@hap"  ,"{0}".format(LTsv_meridian_HourAP))
    LTsv_tf=LTsv_tf if not "@0h"    in LTsv_tf else LTsv_tf.replace("@0h"   ,"{0:0>2}".format(LTsv_meridian_Hour))
    LTsv_tf=LTsv_tf if not "@_h"    in LTsv_tf else LTsv_tf.replace("@_h"   ,"{0: >2}".format(LTsv_meridian_Hour))
    LTsv_tf=LTsv_tf if not "@hz"    in LTsv_tf else LTsv_tf.replace("@hz"   ,"０１２３４５６７８９"[LTsv_meridian_Hour]) if LTsv_meridian_Hour <= 9 else LTsv_tf.replace("@hz","{0}".format(LTsv_meridian_Hour))
    LTsv_tf=LTsv_tf if not "@h"     in LTsv_tf else LTsv_tf.replace("@h"    ,"{0}".format(LTsv_meridian_Hour))
    LTsv_tf=LTsv_tf if not "@0H"    in LTsv_tf else LTsv_tf.replace("@0H"   ,"{0:0>2}".format(LTsv_allnight_Hour))
    LTsv_tf=LTsv_tf if not "@_H"    in LTsv_tf else LTsv_tf.replace("@_H"   ,"{0: >2}".format(LTsv_allnight_Hour))
    LTsv_tf=LTsv_tf if not "@Hz"    in LTsv_tf else LTsv_tf.replace("@Hz"   ,"０１２３４５６７８９"[LTsv_allnight_Hour]) if LTsv_allnight_Hour <= 9 else LTsv_tf.replace("@Hz","{0}".format(LTsv_allnight_Hour))
    LTsv_tf=LTsv_tf if not "@H"     in LTsv_tf else LTsv_tf.replace("@H"    ,"{0}".format(LTsv_allnight_Hour))

    LTsv_tf=LTsv_tf if not "@0n"    in LTsv_tf else LTsv_tf.replace("@0n"   ,"{0:0>2}".format(LTsv_meridian_miNute))
    LTsv_tf=LTsv_tf if not "@_n"    in LTsv_tf else LTsv_tf.replace("@_n"   ,"{0: >2}".format(LTsv_meridian_miNute))
    LTsv_tf=LTsv_tf if not "@nz"    in LTsv_tf else LTsv_tf.replace("@nz"   ,"０１２３４５６７８９"[LTsv_meridian_miNute]) if LTsv_meridian_miNute <= 9 else LTsv_tf.replace("@nz","{0}".format(LTsv_meridian_miNute))
    LTsv_tf=LTsv_tf if not "@n"     in LTsv_tf else LTsv_tf.replace("@n"    ,"{0}".format(LTsv_meridian_miNute))
    LTsv_tf=LTsv_tf if not "@0N"    in LTsv_tf else LTsv_tf.replace("@0N"   ,"{0:0>2}".format(LTsv_allnight_miNute))
    LTsv_tf=LTsv_tf if not "@_N"    in LTsv_tf else LTsv_tf.replace("@_N"   ,"{0: >2}".format(LTsv_allnight_miNute))
    LTsv_tf=LTsv_tf if not "@Nz"    in LTsv_tf else LTsv_tf.replace("@Nz"   ,"０１２３４５６７８９"[LTsv_allnight_miNute]) if LTsv_allnight_miNute <= 9 else LTsv_tf.replace("@Nz","{0}".format(LTsv_allnight_miNute))
    LTsv_tf=LTsv_tf if not "@N"     in LTsv_tf else LTsv_tf.replace("@N"    ,"{0}".format(LTsv_allnight_miNute))

    LTsv_tf=LTsv_tf if not "@0s"    in LTsv_tf else LTsv_tf.replace("@0s"   ,"{0:0>2}".format(LTsv_meridian_Second))
    LTsv_tf=LTsv_tf if not "@_s"    in LTsv_tf else LTsv_tf.replace("@_s"   ,"{0: >2}".format(LTsv_meridian_Second))
    LTsv_tf=LTsv_tf if not "@sz"    in LTsv_tf else LTsv_tf.replace("@sz"   ,"０１２３４５６７８９"[LTsv_meridian_Second]) if LTsv_allnight_Second <= 9 else LTsv_tf.replace("@sz","{0}".format(LTsv_meridian_Second))
    LTsv_tf=LTsv_tf if not "@s"     in LTsv_tf else LTsv_tf.replace("@s"    ,"{0}".format(LTsv_meridian_Second))
    LTsv_tf=LTsv_tf if not "@0S"    in LTsv_tf else LTsv_tf.replace("@0S"   ,"{0:0>2}".format(LTsv_allnight_Second))
    LTsv_tf=LTsv_tf if not "@_S"    in LTsv_tf else LTsv_tf.replace("@_S"   ,"{0: >2}".format(LTsv_allnight_Second))
    LTsv_tf=LTsv_tf if not "@Sz"    in LTsv_tf else LTsv_tf.replace("@Sz"   ,"０１２３４５６７８９"[LTsv_allnight_Second]) if LTsv_allnight_Second <= 9 else LTsv_tf.replace("@Sz","{0}".format(LTsv_allnight_Second))
    LTsv_tf=LTsv_tf if not "@S"     in LTsv_tf else LTsv_tf.replace("@S"    ,"{0}".format(LTsv_allnight_Second))

    LTsv_tf=LTsv_tf if not "@0ls"   in LTsv_tf else LTsv_tf.replace("@0ls"  ,"{0:0>3}".format(LTsv_meridian_miLliSecond))
    LTsv_tf=LTsv_tf if not "@_ls"   in LTsv_tf else LTsv_tf.replace("@_ls"  ,"{0: >3}".format(LTsv_meridian_miLliSecond))
    LTsv_tf=LTsv_tf if not "@ls"    in LTsv_tf else LTsv_tf.replace("@ls"   ,"{0}".format(LTsv_meridian_miLliSecond))
    LTsv_tf=LTsv_tf if not "@0rs"   in LTsv_tf else LTsv_tf.replace("@0rs"  ,"{0:0>6}".format(LTsv_meridian_micRoSecond))
    LTsv_tf=LTsv_tf if not "@_rs"   in LTsv_tf else LTsv_tf.replace("@_rs"  ,"{0: >6}".format(LTsv_meridian_micRoSecond))
    LTsv_tf=LTsv_tf if not "@rs"    in LTsv_tf else LTsv_tf.replace("@rs"   ,"{0}".format(LTsv_meridian_micRoSecond))
    LTsv_tf=LTsv_tf if not "@0Ls"   in LTsv_tf else LTsv_tf.replace("@0Ls"  ,"{0:0>3}".format(LTsv_allnight_miLliSecond))
    LTsv_tf=LTsv_tf if not "@_Ls"   in LTsv_tf else LTsv_tf.replace("@_Ls"  ,"{0: >3}".format(LTsv_allnight_miLliSecond))
    LTsv_tf=LTsv_tf if not "@Ls"    in LTsv_tf else LTsv_tf.replace("@Ls"   ,"{0}".format(LTsv_allnight_miLliSecond))
    LTsv_tf=LTsv_tf if not "@0Rs"   in LTsv_tf else LTsv_tf.replace("@0Rs"  ,"{0:0>6}".format(LTsv_allnight_micRoSecond))
    LTsv_tf=LTsv_tf if not "@_Rs"   in LTsv_tf else LTsv_tf.replace("@_Rs"  ,"{0: >6}".format(LTsv_allnight_micRoSecond))
    LTsv_tf=LTsv_tf if not "@Rs"    in LTsv_tf else LTsv_tf.replace("@Rs"   ,"{0}".format(LTsv_allnight_micRoSecond))

    LTsv_tf=LTsv_tf if not "@0bti"  in LTsv_tf else LTsv_tf.replace("@0bti" ,"{0:0>3}".format(LTsv_meridian_BeatInteger))
    LTsv_tf=LTsv_tf if not "@_bti"  in LTsv_tf else LTsv_tf.replace("@_bti" ,"{0: >3}".format(LTsv_meridian_BeatInteger))
    LTsv_tf=LTsv_tf if not "@bti"   in LTsv_tf else LTsv_tf.replace("@bti"  ,"{0}".format(LTsv_meridian_BeatInteger))
    LTsv_tf=LTsv_tf if not "@0btp"  in LTsv_tf else LTsv_tf.replace("@0btp" ,"{0:0>3}".format(LTsv_meridian_BeatPoint))
    LTsv_tf=LTsv_tf if not "@_btp"  in LTsv_tf else LTsv_tf.replace("@_btp" ,"{0: >3}".format(LTsv_meridian_BeatPoint))
    LTsv_tf=LTsv_tf if not "@btp"   in LTsv_tf else LTsv_tf.replace("@btp"  ,"{0}".format(LTsv_meridian_BeatPoint))
    LTsv_tf=LTsv_tf if not "@0bt"   in LTsv_tf else LTsv_tf.replace("@0bt"  ,"{0:0>5}".format(LTsv_meridian_Beat))
    LTsv_tf=LTsv_tf if not "@_bt"   in LTsv_tf else LTsv_tf.replace("@_bt"  ,"{0: >5}".format(LTsv_meridian_Beat))
    LTsv_tf=LTsv_tf if not "@bt"    in LTsv_tf else LTsv_tf.replace("@bt"   ,"{0:}".format(LTsv_meridian_Beat))

    LTsv_tf=LTsv_tf if not "@0fpk"  in LTsv_tf else LTsv_tf.replace("@0fpk" ,"{0:0>3}".format(LTsv_FPS_fPsK))
    LTsv_tf=LTsv_tf if not "@_fpk"  in LTsv_tf else LTsv_tf.replace("@_fpk" ,"{0: >3}".format(LTsv_FPS_fPsK))
    LTsv_tf=LTsv_tf if not "@fpk"   in LTsv_tf else LTsv_tf.replace("@fpk"  ,"{0}".format(LTsv_FPS_fPsK))
    LTsv_tf=LTsv_tf if not "@0fpc"  in LTsv_tf else LTsv_tf.replace("@0fpc" ,"{0:0>2}".format(LTsv_FPS_fPsC))
    LTsv_tf=LTsv_tf if not "@_fpc"  in LTsv_tf else LTsv_tf.replace("@_fpc" ,"{0: >2}".format(LTsv_FPS_fPsC))
    LTsv_tf=LTsv_tf if not "@fpc"   in LTsv_tf else LTsv_tf.replace("@fpc"  ,"{0}".format(LTsv_FPS_fPsC))

    LTsv_tf=LTsv_tf if not "\t"     in LTsv_tf else LTsv_tf.replace("\t","@")
    return LTsv_tf

#timer
def LTsv_settimershift():
    global LTsv_start_now,LTsv_lap_now,LTsv_goal_now,LTsv_passed_TotalSeconds,LTsv_timeleft_TotalSeconds,LTsv_limit_TotalSeconds
    global LTsv_passed_micRoSecond,LTsv_passed_miLliSecond,LTsv_passed_Second,LTsv_passed_miNute,LTsv_passed_Hour,LTsv_passed_DayHour,LTsv_passed_Day
    global LTsv_passed_Beat,LTsv_passed_BeatInteger,LTsv_passed_BeatPoint
    LTsv_passed_TotalSeconds=(LTsv_lap_now-LTsv_start_now).total_seconds()
    LTsv_passed_micRoSecond=int(LTsv_passed_TotalSeconds*1000000)%1000000
    LTsv_passed_miLliSecond=int(LTsv_passed_TotalSeconds*1000)%1000
    LTsv_passed_Second=int(LTsv_passed_TotalSeconds)%60
    LTsv_passed_miNute=int(LTsv_passed_TotalSeconds/60)%60
    LTsv_passed_Hour=int(LTsv_passed_TotalSeconds/3600)%24
    LTsv_passed_DayHour=int(LTsv_passed_TotalSeconds/3600)
    LTsv_passed_Day=int(LTsv_passed_TotalSeconds/86400)
    LTsv_passed_Beat,LTsv_passed_BeatInteger,LTsv_passed_BeatPoint=LTsv_beat864(LTsv_passed_Hour,LTsv_passed_miNute,LTsv_passed_Second)
    global LTsv_timeleft_micRoSecond,LTsv_timeleft_miLliSecond,LTsv_timeleft_Second,LTsv_timeleft_miNute,LTsv_timeleft_Hour,LTsv_timeleft_DayHour,LTsv_timeleft_Day
    global LTsv_timeleft_Beat,LTsv_timeleft_BeatInteger,LTsv_timeleft_BeatPoint
    LTsv_timeleft_TotalSeconds=(LTsv_goal_now-LTsv_lap_now).total_seconds()
    LTsv_timeleft_micRoSecond=int(LTsv_timeleft_TotalSeconds*1000000)%1000000 if LTsv_timeleft_TotalSeconds>=0 else int(-LTsv_timeleft_TotalSeconds*1000000)%1000000
    LTsv_timeleft_miLliSecond=int(LTsv_timeleft_TotalSeconds*1000)%1000 if LTsv_timeleft_TotalSeconds>=0 else int(-LTsv_timeleft_TotalSeconds*1000)%1000
    LTsv_timeleft_Second=int(LTsv_timeleft_TotalSeconds)%60 if LTsv_timeleft_TotalSeconds>0 else int(-LTsv_timeleft_TotalSeconds)%60
    LTsv_timeleft_miNute=int(LTsv_timeleft_TotalSeconds/60)%60 if LTsv_timeleft_TotalSeconds>0 else int(-LTsv_timeleft_TotalSeconds/60)%60
    LTsv_timeleft_Hour=int(LTsv_timeleft_TotalSeconds/3600)%24 if LTsv_timeleft_TotalSeconds>0 else int(-LTsv_timeleft_TotalSeconds/3600)%24
    LTsv_timeleft_DayHour=int(LTsv_timeleft_TotalSeconds/3600) if LTsv_timeleft_TotalSeconds>0 else int(-LTsv_timeleft_TotalSeconds/3600)
    LTsv_timeleft_Day=int(LTsv_timeleft_TotalSeconds/86400) if LTsv_timeleft_TotalSeconds>0 else int(-LTsv_timeleft_TotalSeconds/86400)
    LTsv_timeleft_Beat,LTsv_timeleft_BeatInteger,LTsv_timeleft_BeatPoint=LTsv_beat864(LTsv_timeleft_Hour,LTsv_timeleft_miNute,LTsv_timeleft_Second)

def LTsv_settimershiftoption():
    global LTsv_start_now,LTsv_lap_now,LTsv_goal_now,LTsv_passed_TotalSeconds,LTsv_timeleft_TotalSeconds,LTsv_limit_TotalSeconds
    global LTsv_limit_micRoSecond,LTsv_limit_miLliSecond,LTsv_limit_Second,LTsv_limit_miNute,LTsv_limit_Hour,LTsv_limit_DayHour,LTsv_limit_Day
    global LTsv_limit_Beat,LTsv_limit_BeatInteger,LTsv_limit_BeatPoint
    LTsv_limit_TotalSeconds=(LTsv_goal_now-LTsv_start_now).total_seconds()
    LTsv_limit_micRoSecond=int(LTsv_limit_TotalSeconds*1000000)%1000000
    LTsv_limit_miLliSecond=int(LTsv_limit_TotalSeconds*1000)%1000
    LTsv_limit_Second=int(LTsv_limit_TotalSeconds)%60
    LTsv_limit_miNute=int(LTsv_limit_TotalSeconds/60)%60
    LTsv_limit_Hour=int(LTsv_limit_TotalSeconds/3600)%24
    LTsv_limit_DayHour=int(LTsv_limit_TotalSeconds/3600)
    LTsv_limit_Day=int(LTsv_limit_TotalSeconds/86400)
    LTsv_limit_Beat,LTsv_limit_BeatInteger,LTsv_limit_BeatPoint=LTsv_beat864(LTsv_limit_Hour,LTsv_limit_miNute,LTsv_limit_Second)

def LTsv_puttimerstartgoal(microsecond=None,millisecond=None,seconds=None,minute=None,hour=None,day=None):
    LTsv_microsecond=0
    LTsv_microsecond=LTsv_microsecond if day         is None else day*86400*1000000
    LTsv_microsecond=LTsv_microsecond if hour        is None else hour*3600*1000000
    LTsv_microsecond=LTsv_microsecond if minute      is None else minute*60*1000000
    LTsv_microsecond=LTsv_microsecond if seconds     is None else seconds*1000000
    LTsv_microsecond=LTsv_microsecond if millisecond is None else millisecond*1000
    LTsv_microsecond=LTsv_microsecond if microsecond is None else microsecond
    global LTsv_start_now,LTsv_lap_now,LTsv_goal_now,LTsv_passed_TotalSeconds,LTsv_timeleft_TotalSeconds,LTsv_limit_TotalSeconds
    LTsv_start_now=datetime.datetime.now()
    LTsv_lap_now=LTsv_start_now
    LTsv_goal_now=LTsv_start_now+datetime.timedelta(microseconds=LTsv_microsecond)
    LTsv_passed_TotalSeconds=(LTsv_lap_now-LTsv_start_now).total_seconds()
    LTsv_timeleft_TotalSeconds=(LTsv_goal_now-LTsv_lap_now).total_seconds()
    LTsv_limit_TotalSeconds=(LTsv_goal_now-LTsv_start_now).total_seconds()
    LTsv_settimershift()
    LTsv_settimershiftoption()
    return LTsv_limit_TotalSeconds

def LTsv_puttimerspecify(LTsv_toyear,LTsv_tomonth,LTsv_today,LTsv_tohour,LTsv_tominute,LTsv_tosecond,LTsv_tomicrosecond):
    global LTsv_start_now,LTsv_lap_now,LTsv_goal_now,LTsv_passed_TotalSeconds,LTsv_timeleft_TotalSeconds,LTsv_limit_TotalSeconds
    LTsv_year=min(max(LTsv_toyear,datetime.MINYEAR),datetime.MAXYEAR)
    LTsv_month=min(max(LTsv_tomonth,1),12)
    LTsv_day=min(max(LTsv_today,1),LTsv_monthleap(LTsv_year,LTsv_month))
    LTsv_hour=min(max(LTsv_tohour,0),23)
    LTsv_minute=min(max(LTsv_tominute,0),59)
    LTsv_second=min(max(LTsv_tosecond,0),59)
    LTsv_microsecond=min(max(LTsv_tomicrosecond,0),999999)
    LTsv_goal_now=datetime.datetime(LTsv_year,LTsv_month,LTsv_day,LTsv_hour,LTsv_minute,LTsv_second,LTsv_microsecond)
    LTsv_start_now=datetime.datetime.now()
    LTsv_lap_now=LTsv_start_now
    LTsv_passed_TotalSeconds=(LTsv_lap_now-LTsv_start_now).total_seconds()
    LTsv_timeleft_TotalSeconds=(LTsv_goal_now-LTsv_lap_now).total_seconds()
    LTsv_limit_TotalSeconds=(LTsv_goal_now-LTsv_start_now).total_seconds()
    LTsv_settimershift()
    LTsv_settimershiftoption()

def LTsv_puttimerlap():
    global LTsv_start_now,LTsv_lap_now,LTsv_goal_now,LTsv_passed_TotalSeconds,LTsv_timeleft_TotalSeconds,LTsv_limit_TotalSeconds
    LTsv_lap_now=datetime.datetime.now()
    LTsv_passed_TotalSeconds=(LTsv_lap_now-LTsv_start_now).total_seconds()
    LTsv_timeleft_TotalSeconds=(LTsv_goal_now-LTsv_lap_now).total_seconds()
    LTsv_settimershift()
    return LTsv_passed_TotalSeconds

def LTsv_gettimerstr(timeformat=None):
    LTsv_tf="@0h@0n@0s.0Rs" if timeformat is None else timeformat
    LTsv_tf=LTsv_tf if not "@@"     in LTsv_tf else LTsv_tf.replace("@@","\t")

    global LTsv_passed_micRoSecond,LTsv_passed_miLliSecond,LTsv_passed_Second,LTsv_passed_miNute,LTsv_passed_Hour,LTsv_passed_DayHour,LTsv_passed_Day
    global LTsv_timeleft_micRoSecond,LTsv_timeleft_miLliSecond,LTsv_timeleft_Second,LTsv_timeleft_miNute,LTsv_timeleft_Hour,LTsv_timeleft_DayHour,LTsv_timeleft_Day
    global LTsv_limit_micRoSecond,LTsv_limit_miLliSecond,LTsv_limit_Second,LTsv_limit_miNute,LTsv_limit_Hour,LTsv_limit_DayHour,LTsv_limit_Day
    global LTsv_timeleft_Beat,LTsv_timeleft_BeatInteger,LTsv_timeleft_BeatPoint
    global LTsv_passed_Beat,LTsv_passed_BeatInteger,LTsv_passed_BeatPoint
    global LTsv_limit_Beat,LTsv_limit_BeatInteger,LTsv_limit_BeatPoint
    global LTsv_FPS_now,LTsv_FPS_earlier,LTsv_FPS_TotalSeconds,LTsv_FPS_fPsK,LTsv_FPS_fPsC
    LTsv_tf=LTsv_tf if not "@000d"  in LTsv_tf else LTsv_tf.replace("@000d" ,"{0:0>4}".format(LTsv_passed_Day))
    LTsv_tf=LTsv_tf if not "@___d"  in LTsv_tf else LTsv_tf.replace("@___d" ,"{0: >4}".format(LTsv_passed_Day))
    LTsv_tf=LTsv_tf if not "@00d"   in LTsv_tf else LTsv_tf.replace("@00d"  ,"{0:0>3}".format(LTsv_passed_Day))
    LTsv_tf=LTsv_tf if not "@__d"   in LTsv_tf else LTsv_tf.replace("@__d"  ,"{0: >3}".format(LTsv_passed_Day))
    LTsv_tf=LTsv_tf if not "@0d"    in LTsv_tf else LTsv_tf.replace("@0d"   ,"{0:0>2}".format(LTsv_passed_Day))
    LTsv_tf=LTsv_tf if not "@_d"    in LTsv_tf else LTsv_tf.replace("@_d"   ,"{0: >2}".format(LTsv_passed_Day))
    LTsv_tf=LTsv_tf if not "@d"     in LTsv_tf else LTsv_tf.replace("@d"    ,"{0}".format(LTsv_passed_Day))
    LTsv_tf=LTsv_tf if not "@-000d" in LTsv_tf else LTsv_tf.replace("@-000d","{0:0>4}".format(LTsv_timeleft_Day))
    LTsv_tf=LTsv_tf if not "@-___d" in LTsv_tf else LTsv_tf.replace("@-___d","{0: >4}".format(LTsv_timeleft_Day))
    LTsv_tf=LTsv_tf if not "@-00d"  in LTsv_tf else LTsv_tf.replace("@-00d" ,"{0:0>3}".format(LTsv_timeleft_Day))
    LTsv_tf=LTsv_tf if not "@-__d"  in LTsv_tf else LTsv_tf.replace("@-__d" ,"{0: >3}".format(LTsv_timeleft_Day))
    LTsv_tf=LTsv_tf if not "@-0d"   in LTsv_tf else LTsv_tf.replace("@-0d"  ,"{0:0>2}".format(LTsv_timeleft_Day))
    LTsv_tf=LTsv_tf if not "@-_d"   in LTsv_tf else LTsv_tf.replace("@-_d"  ,"{0: >2}".format(LTsv_timeleft_Day))
    LTsv_tf=LTsv_tf if not "@-d"    in LTsv_tf else LTsv_tf.replace("@-d"   ,"{0}".format(LTsv_timeleft_Day))
    LTsv_tf=LTsv_tf if not "@000D"  in LTsv_tf else LTsv_tf.replace("@000D" ,"{0:0>4}".format(LTsv_limit_Day))
    LTsv_tf=LTsv_tf if not "@___D"  in LTsv_tf else LTsv_tf.replace("@___D" ,"{0: >4}".format(LTsv_limit_Day))
    LTsv_tf=LTsv_tf if not "@00D"   in LTsv_tf else LTsv_tf.replace("@00D"  ,"{0:0>3}".format(LTsv_limit_Day))
    LTsv_tf=LTsv_tf if not "@__D"   in LTsv_tf else LTsv_tf.replace("@__D"  ,"{0: >3}".format(LTsv_limit_Day))
    LTsv_tf=LTsv_tf if not "@0D"    in LTsv_tf else LTsv_tf.replace("@0D"   ,"{0:0>2}".format(LTsv_limit_Day))
    LTsv_tf=LTsv_tf if not "@_D"    in LTsv_tf else LTsv_tf.replace("@_D"   ,"{0: >2}".format(LTsv_limit_Day))
    LTsv_tf=LTsv_tf if not "@D"     in LTsv_tf else LTsv_tf.replace("@D"    ,"{0}".format(LTsv_limit_Day))

    LTsv_tf=LTsv_tf if not "@0dh"   in LTsv_tf else LTsv_tf.replace("@0dh"  ,"{0:0>3}".format(LTsv_passed_DayHour))
    LTsv_tf=LTsv_tf if not "@_dh"   in LTsv_tf else LTsv_tf.replace("@_dh"  ,"{0: >3}".format(LTsv_passed_DayHour))
    LTsv_tf=LTsv_tf if not "@dh"    in LTsv_tf else LTsv_tf.replace("@dh"   ,"{0}".format(LTsv_passed_DayHour))
    LTsv_tf=LTsv_tf if not "@-0dh"  in LTsv_tf else LTsv_tf.replace("@-0dh" ,"{0:0>3}".format(LTsv_timeleft_DayHour))
    LTsv_tf=LTsv_tf if not "@-_dh"  in LTsv_tf else LTsv_tf.replace("@-_dh" ,"{0: >3}".format(LTsv_timeleft_DayHour))
    LTsv_tf=LTsv_tf if not "@-dh"   in LTsv_tf else LTsv_tf.replace("@-dh"  ,"{0}".format(LTsv_timeleft_DayHour))
    LTsv_tf=LTsv_tf if not "@0Dh"   in LTsv_tf else LTsv_tf.replace("@0Dh"  ,"{0:0>3}".format(LTsv_limit_DayHour))
    LTsv_tf=LTsv_tf if not "@_Dh"   in LTsv_tf else LTsv_tf.replace("@_Dh"  ,"{0: >3}".format(LTsv_limit_DayHour))
    LTsv_tf=LTsv_tf if not "@Dh"    in LTsv_tf else LTsv_tf.replace("@Dh"   ,"{0}".format(LTsv_limit_DayHour))
    LTsv_tf=LTsv_tf if not "@0h"    in LTsv_tf else LTsv_tf.replace("@0h"   ,"{0:0>2}".format(LTsv_passed_Hour))
    LTsv_tf=LTsv_tf if not "@_h"    in LTsv_tf else LTsv_tf.replace("@_h"   ,"{0: >2}".format(LTsv_passed_Hour))
    LTsv_tf=LTsv_tf if not "@h"     in LTsv_tf else LTsv_tf.replace("@h"    ,"{0}".format(LTsv_passed_Hour))
    LTsv_tf=LTsv_tf if not "@-0h"   in LTsv_tf else LTsv_tf.replace("@-0h"  ,"{0:0>2}".format(LTsv_timeleft_Hour))
    LTsv_tf=LTsv_tf if not "@-_h"   in LTsv_tf else LTsv_tf.replace("@-_h"  ,"{0: >2}".format(LTsv_timeleft_Hour))
    LTsv_tf=LTsv_tf if not "@-h"    in LTsv_tf else LTsv_tf.replace("@-h"   ,"{0}".format(LTsv_timeleft_Hour))
    LTsv_tf=LTsv_tf if not "@0H"    in LTsv_tf else LTsv_tf.replace("@0H"   ,"{0:0>2}".format(LTsv_limit_Hour))
    LTsv_tf=LTsv_tf if not "@_H"    in LTsv_tf else LTsv_tf.replace("@_H"   ,"{0: >2}".format(LTsv_limit_Hour))
    LTsv_tf=LTsv_tf if not "@H"     in LTsv_tf else LTsv_tf.replace("@H"    ,"{0}".format(LTsv_limit_Hour))

    LTsv_tf=LTsv_tf if not "@0n"    in LTsv_tf else LTsv_tf.replace("@0n"   ,"{0:0>2}".format(LTsv_passed_miNute))
    LTsv_tf=LTsv_tf if not "@_n"    in LTsv_tf else LTsv_tf.replace("@_n"   ,"{0: >2}".format(LTsv_passed_miNute))
    LTsv_tf=LTsv_tf if not "@n"     in LTsv_tf else LTsv_tf.replace("@n"    ,"{0}".format(LTsv_passed_miNute))
    LTsv_tf=LTsv_tf if not "@-0n"   in LTsv_tf else LTsv_tf.replace("@-0n"  ,"{0:0>2}".format(LTsv_timeleft_miNute))
    LTsv_tf=LTsv_tf if not "@-_n"   in LTsv_tf else LTsv_tf.replace("@-_n"  ,"{0: >2}".format(LTsv_timeleft_miNute))
    LTsv_tf=LTsv_tf if not "@-n"    in LTsv_tf else LTsv_tf.replace("@-n"   ,"{0}".format(LTsv_timeleft_miNute))
    LTsv_tf=LTsv_tf if not "@0N"    in LTsv_tf else LTsv_tf.replace("@0N"   ,"{0:0>2}".format(LTsv_limit_miNute))
    LTsv_tf=LTsv_tf if not "@_N"    in LTsv_tf else LTsv_tf.replace("@_N"   ,"{0: >2}".format(LTsv_limit_miNute))
    LTsv_tf=LTsv_tf if not "@N"     in LTsv_tf else LTsv_tf.replace("@N"    ,"{0}".format(LTsv_limit_miNute))

    LTsv_tf=LTsv_tf if not "@0s"    in LTsv_tf else LTsv_tf.replace("@0s"   ,"{0:0>2}".format(LTsv_passed_Second))
    LTsv_tf=LTsv_tf if not "@_s"    in LTsv_tf else LTsv_tf.replace("@_s"   ,"{0: >2}".format(LTsv_passed_Second))
    LTsv_tf=LTsv_tf if not "@s"     in LTsv_tf else LTsv_tf.replace("@s"    ,"{0}".format(LTsv_passed_Second))
    LTsv_tf=LTsv_tf if not "@-0s"   in LTsv_tf else LTsv_tf.replace("@-0s"  ,"{0:0>2}".format(LTsv_timeleft_Second))
    LTsv_tf=LTsv_tf if not "@-_s"   in LTsv_tf else LTsv_tf.replace("@-_s"  ,"{0: >2}".format(LTsv_timeleft_Second))
    LTsv_tf=LTsv_tf if not "@-s"    in LTsv_tf else LTsv_tf.replace("@-s"   ,"{0}".format(LTsv_timeleft_Second))
    LTsv_tf=LTsv_tf if not "@0S"    in LTsv_tf else LTsv_tf.replace("@0S"   ,"{0:0>2}".format(LTsv_limit_Second))
    LTsv_tf=LTsv_tf if not "@_S"    in LTsv_tf else LTsv_tf.replace("@_S"   ,"{0: >2}".format(LTsv_limit_Second))
    LTsv_tf=LTsv_tf if not "@S"     in LTsv_tf else LTsv_tf.replace("@S"    ,"{0}".format(LTsv_limit_Second))

    LTsv_tf=LTsv_tf if not "@0ls"   in LTsv_tf else LTsv_tf.replace("@0ls"  ,"{0:0>3}".format(LTsv_passed_miLliSecond))
    LTsv_tf=LTsv_tf if not "@_ls"   in LTsv_tf else LTsv_tf.replace("@_ls"  ,"{0: >3}".format(LTsv_passed_miLliSecond))
    LTsv_tf=LTsv_tf if not "@ls"    in LTsv_tf else LTsv_tf.replace("@ls"   ,"{0}".format(LTsv_passed_miLliSecond))
    LTsv_tf=LTsv_tf if not "@-0ls"  in LTsv_tf else LTsv_tf.replace("@-0ls" ,"{0:0>3}".format(LTsv_timeleft_miLliSecond))
    LTsv_tf=LTsv_tf if not "@-_ls"  in LTsv_tf else LTsv_tf.replace("@-_ls" ,"{0: >3}".format(LTsv_timeleft_miLliSecond))
    LTsv_tf=LTsv_tf if not "@-ls"   in LTsv_tf else LTsv_tf.replace("@-ls"  ,"{0}".format(LTsv_timeleft_miLliSecond))
    LTsv_tf=LTsv_tf if not "@0Ls"   in LTsv_tf else LTsv_tf.replace("@0Ls"  ,"{0:0>3}".format(LTsv_limit_miLliSecond))
    LTsv_tf=LTsv_tf if not "@_Ls"   in LTsv_tf else LTsv_tf.replace("@_Ls"  ,"{0: >3}".format(LTsv_limit_miLliSecond))
    LTsv_tf=LTsv_tf if not "@Ls"    in LTsv_tf else LTsv_tf.replace("@Ls"   ,"{0}".format(LTsv_limit_miLliSecond))
    LTsv_tf=LTsv_tf if not "@0rs"   in LTsv_tf else LTsv_tf.replace("@0rs"  ,"{0:0>6}".format(LTsv_passed_micRoSecond))
    LTsv_tf=LTsv_tf if not "@_rs"   in LTsv_tf else LTsv_tf.replace("@_rs"  ,"{0: >6}".format(LTsv_passed_micRoSecond))
    LTsv_tf=LTsv_tf if not "@rs"    in LTsv_tf else LTsv_tf.replace("@rs"   ,"{0}".format(LTsv_passed_micRoSecond))
    LTsv_tf=LTsv_tf if not "@-0rs"  in LTsv_tf else LTsv_tf.replace("@-0rs" ,"{0:0>6}".format(LTsv_timeleft_micRoSecond))
    LTsv_tf=LTsv_tf if not "@-_rs"  in LTsv_tf else LTsv_tf.replace("@-_rs" ,"{0: >6}".format(LTsv_timeleft_micRoSecond))
    LTsv_tf=LTsv_tf if not "@-rs"   in LTsv_tf else LTsv_tf.replace("@-rs"  ,"{0}".format(LTsv_timeleft_micRoSecond))
    LTsv_tf=LTsv_tf if not "@0Rs"   in LTsv_tf else LTsv_tf.replace("@0Rs"  ,"{0:0>6}".format(LTsv_limit_micRoSecond))
    LTsv_tf=LTsv_tf if not "@_Rs"   in LTsv_tf else LTsv_tf.replace("@_Rs"  ,"{0: >6}".format(LTsv_limit_micRoSecond))
    LTsv_tf=LTsv_tf if not "@Rs"    in LTsv_tf else LTsv_tf.replace("@Rs"   ,"{0}".format(LTsv_limit_micRoSecond))

    LTsv_tf=LTsv_tf if not "@0bti"  in LTsv_tf else LTsv_tf.replace("@0bti" ,"{0:0>3}".format(LTsv_passed_BeatInteger))
    LTsv_tf=LTsv_tf if not "@_bti"  in LTsv_tf else LTsv_tf.replace("@_bti" ,"{0: >3}".format(LTsv_passed_BeatInteger))
    LTsv_tf=LTsv_tf if not "@bti"   in LTsv_tf else LTsv_tf.replace("@bti"  ,"{0}".format(LTsv_passed_BeatInteger))
    LTsv_tf=LTsv_tf if not "@0btp"  in LTsv_tf else LTsv_tf.replace("@0btp" ,"{0:0>3}".format(LTsv_passed_BeatPoint))
    LTsv_tf=LTsv_tf if not "@_btp"  in LTsv_tf else LTsv_tf.replace("@_btp" ,"{0: >3}".format(LTsv_passed_BeatPoint))
    LTsv_tf=LTsv_tf if not "@btp"   in LTsv_tf else LTsv_tf.replace("@btp"  ,"{0}".format(LTsv_passed_BeatPoint))
    LTsv_tf=LTsv_tf if not "@0bt"   in LTsv_tf else LTsv_tf.replace("@0bt"  ,"{0:0>5}".format(LTsv_passed_Beat))
    LTsv_tf=LTsv_tf if not "@_bt"   in LTsv_tf else LTsv_tf.replace("@_bt"  ,"{0: >5}".format(LTsv_passed_Beat))
    LTsv_tf=LTsv_tf if not "@bt"    in LTsv_tf else LTsv_tf.replace("@bt"   ,"{0:}".format(LTsv_passed_Beat))
    LTsv_tf=LTsv_tf if not "@-0bti" in LTsv_tf else LTsv_tf.replace("@-0bti","{0:0>3}".format(LTsv_timeleft_BeatInteger))
    LTsv_tf=LTsv_tf if not "@-_bti" in LTsv_tf else LTsv_tf.replace("@-_bti","{0: >3}".format(LTsv_timeleft_BeatInteger))
    LTsv_tf=LTsv_tf if not "@-bti"  in LTsv_tf else LTsv_tf.replace("@-bti" ,"{0}".format(LTsv_timeleft_BeatInteger))
    LTsv_tf=LTsv_tf if not "@-0btp" in LTsv_tf else LTsv_tf.replace("@-0btp","{0:0>3}".format(LTsv_timeleft_BeatPoint))
    LTsv_tf=LTsv_tf if not "@-_btp" in LTsv_tf else LTsv_tf.replace("@-_btp","{0: >3}".format(LTsv_timeleft_BeatPoint))
    LTsv_tf=LTsv_tf if not "@-btp"  in LTsv_tf else LTsv_tf.replace("@-btp" ,"{0}".format(LTsv_timeleft_BeatPoint))
    LTsv_tf=LTsv_tf if not "@-0bt"  in LTsv_tf else LTsv_tf.replace("@-0bt" ,"{0:0>5}".format(LTsv_timeleft_Beat))
    LTsv_tf=LTsv_tf if not "@-_bt"  in LTsv_tf else LTsv_tf.replace("@-_bt" ,"{0: >5}".format(LTsv_timeleft_Beat))
    LTsv_tf=LTsv_tf if not "@-bt"   in LTsv_tf else LTsv_tf.replace("@-bt"  ,"{0:}".format(LTsv_timeleft_Beat))
    LTsv_tf=LTsv_tf if not "@0Bti"  in LTsv_tf else LTsv_tf.replace("@0Bti" ,"{0:0>3}".format(LTsv_limit_BeatInteger))
    LTsv_tf=LTsv_tf if not "@_Bti"  in LTsv_tf else LTsv_tf.replace("@_Bti" ,"{0: >3}".format(LTsv_limit_BeatInteger))
    LTsv_tf=LTsv_tf if not "@Bti"   in LTsv_tf else LTsv_tf.replace("@Bti"  ,"{0}".format(LTsv_limit_BeatInteger))
    LTsv_tf=LTsv_tf if not "@0Btp"  in LTsv_tf else LTsv_tf.replace("@0Btp" ,"{0:0>3}".format(LTsv_limit_BeatPoint))
    LTsv_tf=LTsv_tf if not "@_Btp"  in LTsv_tf else LTsv_tf.replace("@_Btp" ,"{0: >3}".format(LTsv_limit_BeatPoint))
    LTsv_tf=LTsv_tf if not "@Btp"   in LTsv_tf else LTsv_tf.replace("@Btp"  ,"{0}".format(LTsv_limit_BeatPoint))
    LTsv_tf=LTsv_tf if not "@0Bt"   in LTsv_tf else LTsv_tf.replace("@0Bt"  ,"{0:0>5}".format(LTsv_limit_Beat))
    LTsv_tf=LTsv_tf if not "@_Bt"   in LTsv_tf else LTsv_tf.replace("@_Bt"  ,"{0: >5}".format(LTsv_limit_Beat))
    LTsv_tf=LTsv_tf if not "@Bt"    in LTsv_tf else LTsv_tf.replace("@Bt"   ,"{0:}".format(LTsv_limit_Beat))

    LTsv_tf=LTsv_tf if not "@+-"    in LTsv_tf else LTsv_tf.replace("@+-"   ,"+") if LTsv_timeleft_TotalSeconds >= 0 else LTsv_tf.replace("@+-","-")
    LTsv_tf=LTsv_tf if not "@_-"    in LTsv_tf else LTsv_tf.replace("@_-"   ," ") if LTsv_timeleft_TotalSeconds >= 0 else LTsv_tf.replace("@_-","-")
    LTsv_tf=LTsv_tf if not "@--"    in LTsv_tf else LTsv_tf.replace("@--"   ,"") if LTsv_timeleft_TotalSeconds >= 0 else LTsv_tf.replace("@--","-")

    LTsv_tf=LTsv_tf if not "@0fpk"  in LTsv_tf else LTsv_tf.replace("@0fpk" ,"{0:0>3}".format(LTsv_FPS_fPsK))
    LTsv_tf=LTsv_tf if not "@_fpk"  in LTsv_tf else LTsv_tf.replace("@_fpk" ,"{0: >3}".format(LTsv_FPS_fPsK))
    LTsv_tf=LTsv_tf if not "@fpk"   in LTsv_tf else LTsv_tf.replace("@fpk"  ,"{0}".format(LTsv_FPS_fPsK))
    LTsv_tf=LTsv_tf if not "@0fpc"  in LTsv_tf else LTsv_tf.replace("@0fpc" ,"{0:0>2}".format(LTsv_FPS_fPsC))
    LTsv_tf=LTsv_tf if not "@_fpc"  in LTsv_tf else LTsv_tf.replace("@_fpc" ,"{0: >2}".format(LTsv_FPS_fPsC))
    LTsv_tf=LTsv_tf if not "@fpc"   in LTsv_tf else LTsv_tf.replace("@fpc"  ,"{0}".format(LTsv_FPS_fPsC))

    LTsv_tf=LTsv_tf if not "\t"     in LTsv_tf else LTsv_tf.replace("\t","@")
    return LTsv_tf


if __name__=="__main__":
    from LTsv_printf import *
    from LTsv_file   import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_checkFPS()
    timeformat24="@yzj年@000y-@0m-@0dm@mes(@0dy/@0yd日@0wnyi/@ywi週@wdes第@wnm@wdj曜@apj@hap時)@0h:@0n:@0s.@0rs"
    timeformat30="@Yzj年@000Y-@Mz-@Dmz@Mes(@0Dy/@0Yd日@Wnyiz/@Ywi週@Wdes第@Wnmz@Wdj曜@Apj@Hz時)@Hz:@Nz:@Sz.@0Rs"
    timeformatBT="@000y-@0m-@0dm@mes(@0dy/@0yd,@0wn/@yw.@wdes)@bt:@@@0bti.@0btp"
    timeformatsec="@0h:@0n:@0s.@0rs(@+-@-0h:@-0n:@-0s.@-0rs)@@@0bti.@0btp(@+-@-0bti.@-0btp)/@0H:@0N:@0S.@0Rs FPS:@0fpk"
    timeformatday="2020年東京オリンピックまで@000D日"
    LTsv_libc_printf("LTsv_getdaytimestr()→{0}".format(LTsv_getdaytimestr()))
    print("")
    LTsv_putdaytimespecify(2011,3,11,14,46,18,0,overhour=24,diffminute=0)
    LTsv_libc_printf("LTsv_putdaytimespecify(2011,3,11,14,46,18,0,overhour=24,diffminute=0),LTsv_meridian_now→{0}".format(LTsv_meridian_now))
    LTsv_libc_printf("LTsv_getdaytimestr('{0}')↓\n{1}".format(timeformat24,LTsv_getdaytimestr(timeformat24)))
    print("")
    LTsv_putdaytimever(LTsv_file_ver())
    LTsv_libc_printf("LTsv_putdaytimever(LTsv_time_ver()),LTsv_meridian_now→{0}".format(LTsv_meridian_now))
    LTsv_libc_printf("LTsv_getdaytimestr('{0}')↓\n{1}".format(timeformat24,LTsv_getdaytimestr(timeformat24)))
    print("")
    LTsv_putdaytimenow(overhour=24,diffminute=-9*60)
    LTsv_libc_printf("LTsv_putdaytimenow(overhour=24,diffminute=-9*60),LTsv_meridian_now→{0}".format(LTsv_meridian_now))
    LTsv_libc_printf("LTsv_getdaytimestr('{0}')↓\n{1}".format(timeformat24,LTsv_getdaytimestr(timeformat24)))
    LTsv_putdaytimeearlier(overhour=48,diffminute=0);
    LTsv_libc_printf("LTsv_putdaytimeearlier(overhour=48,diffminute=0),LTsv_meridian_now→{0}".format(LTsv_meridian_now))
    LTsv_libc_printf("LTsv_getdaytimestr('{0}')↓\n{1}".format(timeformat24,LTsv_getdaytimestr(timeformat24)))
    LTsv_libc_printf("LTsv_getdaytimestr('{0}')↓\n{1}".format(timeformat30,LTsv_getdaytimestr(timeformat30)))
    print("")
    LTsv_putdaytimeearlier(overhour=24,diffminute=-8*60)
    LTsv_libc_printf("LTsv_putdaytimeearlier(overhour=24,diffminute=-8*60),LTsv_meridian_now→{0}".format(LTsv_meridian_now))
    LTsv_libc_printf("LTsv_getdaytimestr('{0}')↓\n{1}".format(timeformatBT,LTsv_getdaytimestr(timeformatBT)))
    print("")
    LTsv_puttimerstartgoal(seconds=3)
    count=5
    while count >= 0:
        LTsv_checkFPS()
        LTsv_libc_printf("count {0}:{1:3.6f}".format(count,LTsv_puttimerlap()))
        LTsv_libc_printf("LTsv_gettimerstr('{0}')↓\n{1}".format(timeformatsec,LTsv_gettimerstr(timeformatsec)))
        count-=1
        if count >= 0:
            time.sleep(1.0)
    print("")
    LTsv_puttimerspecify(2020,7,24,0,0,0,0)
    LTsv_libc_printf("LTsv_gettimerstr('{0}')↓\n{1}".format(timeformatday,LTsv_gettimerstr(timeformatday)))
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv10kanedit/blob/master/LICENSE
