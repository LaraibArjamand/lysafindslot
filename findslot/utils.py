import datetime as dt
from datetime import datetime


DAYS = {
	0 : 'Mon',
	1 : 'Tues',
	2 : 'Wed',
	3 : 'Thurs',
	4 : 'Fri',
	5 : 'Sat',
	6 : 'Sun'
}


def get_time_slots(timerange):

	""" Function to get time slots based on the time range preference."""

	time_slots = []

	for t in timerange:
		start, end, interval, mode = get_time_range(t)
		# hours
		for h in range(start, end+1):
			# minutes
			for m in (0, interval):
				if (mode == 'to' and m == interval and (h == end or h == 0)):
					pass
				else:
					if h == 24:
						h = 0
					time = dt.time(h, m).strftime('%H:%M')
					time_slots.append(time)

			if (mode == 'from' and h == end - 1): break
	return time_slots
				

def get_date_slots(daterange, custom=False):

	""" Function to return date slots based on the date range preference."""

	date_slots = []
	for d in daterange:
		start, end = get_date_range(d)
		for x in range(start, end):
			date = (dt.datetime.now() + dt.timedelta(days=x)).date()

			if custom:
				date_slots.append(f"{datetime.strftime(date, '%b. %d, %y')} ({DAYS[date.weekday()]})")
			else:
				date_slots.append(datetime.strftime(date, '%b. %d, %y'))

	return date_slots

def get_time_slot(timerange, custom_from=None, custom_to=None):
    
    time = []

    for t in timerange:
        if t == 'before':
            time.append([dt.time(7,0), dt.time(9,0)])
        if t == 'atwork':
            time.append([dt.time(9,0), dt.time(17,0)])
        if t == 'after':
            time.append([ dt.time(17,0), dt.time(21,0)])
        if t == 'beyond':
            time.append([ dt.time(21,0), dt.time(23,59)])
        if t == 'custom':
            time.append([datetime.strptime(custom_from,'%H:%M').time(), datetime.strptime(custom_to,'%H:%M').time()])

    return time

def get_time_range(timerange):

	""" Function to return the start, end and time interval
		based on time range preference """

	if timerange == 'before':
		return (7,9,30,'to')
	if timerange == 'atwork':
		return (9,17,30,'to')
	if timerange == 'after':
		return (17,21,30,'to')
	if timerange == 'beyond':
		return (21,24,30,'to')
	if timerange == 'custom':
		return (9,21,30,'to')


def get_date_range(daterange):

	""" Function to return the number of days
		based on date range preference """

	if daterange == 'todayntom': return (0,2)

	if daterange == 'thisweek':  return (0, 6 - dt.datetime.now().weekday())
		
	if daterange == 'nextweek':
		x = 6 - dt.datetime.now().weekday()
		return (x, x+7)

	if daterange == 'next30days': return (0, 30)
		
	if daterange == 'custom':	  return (0, 30)
		
