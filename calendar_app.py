import importlib.util
import sys
import sysconfig
import os
import datetime

stdlib_dir = sysconfig.get_paths().get("stdlib")
calendar_path = os.path.join(stdlib_dir, "calendar.py")
spec = importlib.util.spec_from_file_location("calendar", calendar_path)
cal = importlib.util.module_from_spec(spec)

sys.modules['calendar'] = cal
spec.loader.exec_module(cal)

year = 2026

cal.setfirstweekday(cal.SUNDAY)

def print_months(year):
    for month in range(1, 13):
        print(f"{cal.month_name[month]} {year}".center(28))
        print("Su Mo Tu We Th Fr Sa")

        for week in cal.monthcalendar(year, month):
            days = " ".join(f"{day:>2}" if day != 0 else "  " for day in week)
            print(days)
        print()

if __name__ == "__main__":
    print_months(year)


# Purpose: Print each month's calendar for `year`.
# Avoid shadowing: the script loads the stdlib `calendar` directly so a local
# `calendar.py` won't override it.
# Run: `python calendar_app.py`
# Quick fix: rename/remove local `calendar.py`, then use `import calendar as cal`.
# Extensible: accept a CLI `year` or print ISO week numbers if desired.



