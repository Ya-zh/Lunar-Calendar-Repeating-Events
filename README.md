为农历的重复事件生成一个ics文件，比如我的农历生日，在谷歌日历上面想要创建农历生日就可以生成ics文件后导入。

## 1、安装 Python，安装 ics 和 LunarCalendar 库

在Python安装目录 Scripts 文件夹内运行 CMD 命令行，运行下面脚本

`pip install ics lunarcalendar`

## 2、创建配置文件 (config.json)

 ## 3、创建脚本文件 (main.py)

## 4、将 config.json 和 main.py 文件放入同一个文件夹内，运行脚本

在文件夹内运行 CMD 命令行，运行下面脚本

`python main.py -i config.json -c 50`

## 5、输出结果

运行脚本后，会生成类似以下内容，并输出一个 lunar_birthdays.ics 文件

`BEGIN:VCALENDAR
VERSION:2.0
PRODID:ics.py - http://git.io/lLljaA
BEGIN:VEVENT
DESCRIPTION:祝生日快乐，1986年出生，又长大一岁
DTSTART:20621103T000000Z
SUMMARY:小王的农历76岁生日
UID:3c377018-dac3-4284-b04b-f2cd804a49ab@3c37.org
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:祝生日快乐，2000年出生，又长大一岁
DTSTART:20310414T000000Z
SUMMARY:小李的农历31岁生日
UID:a6ca3397-f85c-4b4e-aa32-b8cd20cda974@a6ca.org
END:VEVENT
END:VCALENDAR
农历生日日历文件已生成: lunar_birthdays.ics`
