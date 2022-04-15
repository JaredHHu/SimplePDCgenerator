from datetime import datetime
from pyperclip import copy

available_airport = ("ZBAA","ZBAD","ZBSJ",
                     "ZGGG","ZGKL","ZGOW","ZGSZ",
                     "ZHCC","ZHHH",
                     "ZJHK","ZJSY","ZLLL","ZLXN","ZLXY",
                     "ZPPP",
                     "ZSAM","ZSHC","ZSJN","ZSOF","ZSPD","ZSQD","ZSWZ","ZSSS",
                     "ZUCK","ZUUU","ZUTF",
                     "ZWWW",
                     "ZYCC","ZYHB","ZYTL","ZYTX")
atis_code = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

print("PDC简易生成器")
print("-"*15)
print("当前版本：0.5")
print("-"*15)
print("更新日志：")
print("0.1  新增：全手动输入参数生成PDC")
print("0.2  新增：自动获取UTC时间")
print("0.3  新增：自动将生成的PDC复制到剪贴板")
print("     新增：自动判断当前机场是否具备提供DCL服务的能力")
print("     新增：版本号、更新日志")
print("     优化：支持小写字母输入")
print("0.4  新增：半自动更新ATIS编码")
print("     优化：标明时间为世界协调时")
print("     优化：润色文本")
print("0.5  新增：无需重启程序即可更新基础设置")
print("-"*15)
print("当前内置机场数据：AIRAC2106")
print("-"*15)
print("© 2021 Jared Hu/1549223. All rights reserved.")
print("-"*15)

judge = True
print("请进行基础设置。")
airport = input("机场：")
airport = airport.upper()
if airport not in available_airport:
    judge = False
    print("该机场目前不具备提供DCL服务的能力。程序运行结束，祝您管制愉快！")
    input('使用 <Enter> 键以关闭程序。')
else:
    nextfreq = input("下一频率：")
    depfreq = input("离场频率：")
    currentfreq = input("请输入当前频率：")
    atis = input("请输入当前ATIS编码：")
    atis = atis.upper()
    while atis not in atis_code:
        atis = input("输入有误，请输入正确的ATIS编码：")
        atis = atis.upper()
    print("设置完成，祝您管制愉快！")
    print("-" * 15)
    print("如需更新机场，请在[呼号]处输入“.apt”")
    print("如需更新下一频率，请在[呼号]处输入“.nextfreq”")
    print("如需更新离场频率，请在[呼号]处输入“.depfreq”")
    print("如需更新当前频率，请在[呼号]处输入“.freq”")
    print("如需更新ATIS编码，请在[呼号]处输入“.atis”")
    print("如需查看基础设置，请在[呼号]处输入“.show”")

while judge:
    print("-" * 15)
    callsign = input("呼号：")
    callsign = callsign.upper()
    if callsign == ".APT":
        airport = input("机场：")
        airport = airport.upper()
        if airport not in available_airport:
            print("该机场目前不具备提供DCL服务的能力。程序运行结束，祝您管制愉快！")
            input('使用 <Enter> 键以关闭程序。')
            break
        else:
            print("当前机场已更新为{}".format(airport))
            continue
    elif callsign == ".NEXTFREQ":
        nextfreq = input("下一频率：")
        print("下一频率已更新为{}".format(nextfreq))
        continue
    elif callsign == ".DEPFREQ":
        depfreq = input("离场频率：")
        print("离场频率已更新为{}".format(depfreq))
        continue
    elif callsign == ".FREQ":
        currentfreq = input("当前频率：")
        print("当前频率已更新为{}".format(currentfreq))
        continue
    elif callsign == ".ATIS":
        atis = atis_code[atis_code.index(atis)+1]
        print("当前ATIS编码已更新为{}".format(atis))
        continue
    elif callsign == ".SHOW":
        print("机场：{}，下一频率：{}，离场频率：{}，当前频率：{}，ATIS编码：{}。".format(airport,nextfreq,depfreq,currentfreq,atis))
        continue
    dest = input("目的地：")
    rwy = input("跑道：")
    sid = input("SID：")
    sq = input("应答机：")
    inialt = input("起始高度：")
    crzalt = input("巡航高度：")
    dest = dest.upper()
    rwy = rwy.upper()
    sid = sid.upper()
    now_time = datetime.utcnow().strftime('%H%MZ %g%m%d')
    print("{} {} PDC {} CLRD TO {} OFF {} VIA {} SQUAWK {} NEXT FREQ {} ATIS {} INITIAL ALT {}M FL {}M DEP FREQ {} "
          "|| YOU DO NOT NEED TO REPLY THIS MESSAGE PLEASE READBACK RWY DESIGNATOR AND INITIAL CLIMB ALTITUDE ON FREQ {}"
         .format(now_time, airport, callsign, dest, rwy, sid, sq, nextfreq, atis, inialt, crzalt, depfreq, currentfreq))
    copy("{} {} PDC {} CLRD TO {} OFF {} VIA {} SQUAWK {} NEXT FREQ {} ATIS {} INITIAL ALT {}M FL {}M DEP FREQ {} "
         "|| YOU DO NOT NEED TO REPLY THIS MESSAGE PLEASE READBACK RWY DESIGNATOR AND INITIAL CLIMB ALTITUDE ON FREQ {}"
        .format(now_time, airport, callsign, dest, rwy, sid, sq, nextfreq, atis, inialt, crzalt, depfreq, currentfreq))
    print("本次生成的PDC信息已自动复制到剪贴板，可直接粘贴使用。如需结束使用请直接关闭本程序，感谢您的使用！")