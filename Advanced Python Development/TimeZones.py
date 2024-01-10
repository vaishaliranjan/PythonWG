#UTC Coordinated Universal Time
#naive -> that doesnt know about timezones -> it will tell us about our computer
#from datetime import datetime
#print(datetime.now())


#aware-> that knows about timezone
#from datetime import datetime, timezone
#print(datetime.now(timezone.utc))


# from datetime import datetime, timezone, timedelta
# print(datetime.now())
#
# print(datetime.now(timezone.utc))
#
# today = datetime.now(timezone.utc)
# tomorrow= today + timedelta(days=1)
# print(today)
# print(today.strftime("%d-%m-%Y %H:%M:%S"))
#
# user_input= input("Enter date in this format YYYY-MM-DD: ")
# parse_date= datetime.strptime(user_input,"%Y-%m-%d")
# print(parse_date.__class__)


import time

def powers(limit):
    return [x**2 for x in range(limit)]
start = time.time()
print(start)
powers(5000000)
end=time.time()
print(end)
print(end-start)


import timeit
print(timeit.timeit("[x**2 for x in range(10)]"))

