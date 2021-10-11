import toggl
import timelogger
import sys
from datetime import datetime


def main():
    args = sys.argv
    if len(args) > 1:
        try:
            date = args[1]
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Please ensure the date entered is in the format 'yyyy-mm-dd'.")
            print(f"Got: {args}")
    else:
        date = datetime.now().strftime("%Y-%m-%d")

    print(f"Exporting Toggl entries occuring on {date}...")
    timelogger.log_entry(toggl.get_formatted_data(date))
    print("Done.")


if __name__ == "__main__":
    main()
