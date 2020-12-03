from datetime import datetime
from datetime import timedelta
import calendar

def p19():
  s = 0
  start = datetime.strptime("1 Jan 1901","%d %b %Y")
  end =  datetime.strptime("31 Dec 2000","%d %b %Y")
  tmp = start
  while tmp <= end:
    if tmp.day ==1 and tmp.isoweekday() == 7:
      print(tmp,tmp.strftime("%A"),calendar.isleap(tmp.year))
      s+=1
    tmp += timedelta(days=1)
  return s


print(p19())
