import json
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

        # 计算未来100年的农历生日
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
    main()