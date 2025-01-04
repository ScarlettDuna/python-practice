from datetime import datetime
birthday = datetime(1991, 4, 20)
print(birthday.weekday())

date_string = datetime.strftime(datetime.now(), '%b-%d-%Y')
print(date_string)