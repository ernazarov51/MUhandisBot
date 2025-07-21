from datetime import datetime
import calendar

async def format_lesson_weekly(group_name: str, lessons: list) -> str:
    if not lessons:
        return f"{group_name} guruhida bu hafta uchun dars jadvali mavjud emas."

    days = {}

    for lesson in lessons:
        start_dt = datetime.fromisoformat(lesson['start'])
        weekday = calendar.day_name[start_dt.weekday()]
        if weekday not in days:
            days[weekday] = []
        days[weekday].append(lesson)

    week_day_names = [
        ("Monday", "Dushanba"),
        ("Tuesday", "Sedhanba"),
        ("Wednesday", "Chorshanba"),
        ("Thursday", "Patshanba"),
        ("Friday", "Juma"),
        ("Saturday", "Shanba"),
        ("Sunday", "Yakshansba"),
    ]

    result = f"📚 Guruh: <b>{group_name}</b>\n\n"
    for eng_day, uz_day in week_day_names:
        if eng_day not in days:
            continue

        one_day_lessons = days[eng_day]
        one_day_lessons.sort(key=lambda l: l['start'])

        date_str = datetime.fromisoformat(one_day_lessons[0]['start']).strftime("%Y-%m-%d")

        result += f"🗓 <b>{uz_day}, {date_str}</b>\n"

        for lesson in one_day_lessons:
            start = datetime.fromisoformat(lesson['start']).strftime("%H:%M")
            end = datetime.fromisoformat(lesson['end']).strftime("%H:%M")
            science = lesson['science']['name']
            room = lesson['room']['name']
            teacher = f"{lesson['teacher']['first_name']} {lesson['teacher']['last_name']}"

            result += (
                f"⏰ {start}–{end}\n"
                f"📚 {science}\n"
                f"👨‍🏫 {teacher}\n"
                f"🏫 {room}\n\n"
            )

        result += "---------------\n"

    return result.strip()


UZ_DAYS = {
    0: "Dushanba",
    1: "Seshanba",
    2: "Chorshanba",
    3: "Payshanba",
    4: "Juma",
    5: "Shanba",
    6: "Yakshanba"
}

async def format_lesson_daily(group_name: str, lessons: list) -> str:
    if not lessons:
        return f"{group_name} guruhida bugun uchun dars jadvali mavjud emas."

    today_datetime = datetime.today()
    today = today_datetime.date()
    day_name = UZ_DAYS[today.weekday()]

    today_lessons = [
        lesson for lesson in lessons
        if datetime.fromisoformat(lesson['start']).date() == today
    ]

    if not today_lessons:
        return f"{group_name} guruhida {day_name} kuni uchun dars jadvali mavjud emas."

    today_lessons.sort(key=lambda l: l['start'])

    result = f"📚 Guruh: <b>{group_name}</b>\n🗓 Sana: <b>{today.strftime('%Y-%m-%d')} ({day_name})</b>\n\n"
    for lesson in today_lessons:
        start_time = lesson['start'][11:16]
        end_time = lesson['end'][11:16]
        science_name = lesson['science']['name']
        teacher_full_name = f"{lesson['teacher']['first_name']} {lesson['teacher']['last_name']}"
        room_name = lesson['room']['name']

        result += (
            f"⏰ {start_time} – {end_time}\n"
            f"📚 {science_name}\n"
            f"👨‍🏫 {teacher_full_name}\n"
            f"🏫 {room_name}\n\n"
        )

    return result










