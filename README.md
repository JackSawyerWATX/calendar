# Calendar

Small demo script to print a month-by-month calendar for a year.

Files
- `calendar_app.py` — main runner that loads the standard-library `calendar`
  module directly (safe against a local `calendar.py` file).
- `calendar.py` — may be a local script; if present it can shadow the stdlib
  module and cause import errors.

Usage

From PowerShell in this directory run:

```powershell
python calendar_app.py
```

Change year
- Edit the `year` variable near the top of `calendar_app.py`.

Troubleshooting (import shadowing)
- If you get import errors referencing a local `calendar.py`, rename or remove
  the local file, for example:

```powershell
Rename-Item -Path .\calendar.py -NewName calendar_local.py
# or
Remove-Item -Path .\calendar.py
```

After renaming/removing the local file you can replace the manual stdlib
loading with a simple `import calendar as cal` at the top of the script.

Extending
- To accept a year from the command line, add `argparse` parsing.
- To print ISO week numbers, compute the first non-zero day in each week and
  use `datetime.date(year, month, first_day).isocalendar()[1]`.
