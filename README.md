为农历的重复事件生成一个ics文件，比如我的农历生日，在谷歌日历上面想要创建农历生日就可以生成ics文件后导入。

## 1、安装 Python，安装 ics 和 LunarCalendar 库

在Python安装目录 Scripts 文件夹内运行 CMD 命令行，运行下面脚本
`pip install ics lunarcalendar`

## 2、创建配置文件 (config.json)

`{
    "birthdays": [
        {
            "name": "小王",
            "lunar_birthday": "1986-10-03"
        },
        {
            "name": "小李",
            "lunar_birthday": "2000-03-23"
        }
    ]
}`
 ## 3、创建脚本文件 (main.py)
`import json
import sys
import argparse
from ics import Calendar, Event
from lunarcalendar import Converter, Solar, Lunar
from datetime import datetime, timedelta

def load_config(config_file):
    """加载配置文件"""
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_calendar(config, years):
    """生成日历"""
    cal = Calendar()

    for person in config['birthdays']:
        name = person['name']
        lunar_birthday = person['lunar_birthday']
        lunar_year, lunar_month, lunar_day = map(int, lunar_birthday.split('-'))

        # 计算未来50年的农历生日
        for year in range(datetime.now().year, datetime.now().year + years):
            lunar_date = Lunar(year, lunar_month, lunar_day)
            solar_date = Converter.Lunar2Solar(lunar_date)

            # 创建事件
            event = Event()
            event.name = f"{name}的农历{year - lunar_year}岁生日"
            event.begin = datetime(solar_date.year, solar_date.month, solar_date.day).date()
            event.description = f"祝生日快乐，{lunar_year}年出生，又长大一岁"
            cal.events.add(event)

    return cal

def main():
    parser = argparse.ArgumentParser(description="生成农历生日日历文件")
    parser.add_argument('-i', '--input', required=True, help="配置文件路径")
    parser.add_argument('-c', '--count', type=int, default=100, help="生成未来多少年的日历")
    args = parser.parse_args()

    # 加载配置文件
    config = load_config(args.input)

    # 生成日历
    cal = generate_calendar(config, args.count)

    # 打印日历内容
    print(cal)

    # 保存日历文件
    with open('lunar_birthdays.ics', 'w', encoding='utf-8') as f:
        f.write(str(cal))

    print("农历生日日历文件已生成: lunar_birthdays.ics")

if __name__ == '__main__':
    main()`
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
