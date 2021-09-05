from datetime import date, datetime, timedelta
import sys

MONDAY = 0
FIRST_WIN = ("I decided to take control of my Python journey "
             "and joined the PyBites Developer Mindset Program")
WINS_HEADER = """# Wins of the Week
Once a week, come back to this file and document your "wins of the week".
Anything you consider a win counts but even better if it's a result of your progress in the Program.
"""  # noqa E501
WEEKLY_WINS = """## {week_h2}
- {first_win}
-
-
"""


def get_week_dates(start_date, num_weeks=10):
    for i in range(num_weeks):
        start = start_date + timedelta(days=i*7)
        end = start + timedelta(days=6)
        yield start, end


def generate_wins_md(dates):
    print(WINS_HEADER)
    for week, (start, end) in enumerate(dates, 1):
        start, end = [dt.strftime('%Y-%m-%d') for dt in (start, end)]
        first_win = FIRST_WIN if week == 1 else ''
        week_h2 = f"Week {str(week).zfill(2)}: {start} - {end}"
        print(WEEKLY_WINS.format(week_h2=week_h2,
                                 first_win=first_win))


def _get_start_date():
    start_date = date.today()

    if len(sys.argv) == 1:
        print("No start date specified (YYYY-MM-DD) defaulting to today")
    else:
        try:
            start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
        except ValueError:
            print("Please enter a valid date: YYYY-MM-DD")
            sys.exit(1)

    if start_date.weekday() != MONDAY:
        print("Start date needs to be a Monday")
        sys.exit(1)

    return start_date


def main():
    start_date = _get_start_date()
    dates = get_week_dates(start_date)
    generate_wins_md(dates)


if __name__ == "__main__":
    main()
