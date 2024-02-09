import time
import datetime

def print_unix_time() :
    unix_time = time.time()
    formatted_unix_time = "{:,}".format(unix_time)
    scientific_notation_time = "{:.2e}".format(unix_time)
    print("Seconds since January 1, 1970: ", formatted_unix_time , " or ", scientific_notation_time, " in scientific notation", sep="")

def print_today_date() :
    now = datetime.datetime.now()
    formatted_date = now.strftime("%b %d %Y")
    print(formatted_date)

def format_ft_time() :
    print_unix_time()
    print_today_date()

format_ft_time()