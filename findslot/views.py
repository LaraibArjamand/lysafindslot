from typing import List
from django.shortcuts import render
from django.http import HttpResponse

from .forms   import *
from .utils   import *
from .models  import *

import pprint
import datetime as dt

print = pprint.PrettyPrinter(4).pprint

# Create your views here.

def find_slot(request):

    free_slots = {}

    if request.method == 'POST':

        # meeting details
        meeting_length = int(request.POST['meeting_length'])
        buffer_length  = request.POST['buffer_length']
        try:
            buffer_length = int(buffer_length)
        except:
            buffer_length = 0

        buffer         = dt.timedelta(minutes= buffer_length)
        meeting_length = dt.timedelta(minutes=meeting_length)

        include_day_events = False if 'day_events' in request.POST else True
        include_holidays   = False if 'holiday'    in request.POST else True


        # the slot preferences
        time_slots = request.POST.getlist('time_between')
        date_slots = request.POST.getlist('date_between')


        if 'custom' in time_slots:
            time_slots: List[dt.time] = get_time_slot(time_slots, request.POST['custom_time_search_from'], request.POST['custom_time_search_to'])
        else:
            time_slots: List[dt.time] = get_time_slot(time_slots)

        dates = [ dt.datetime.strptime(str_date, '%b. %d, %y').date() for str_date in get_date_slots(date_slots) ]


        # retrieving all the scheduled events
        events   = [[
            event[0].replace(tzinfo= None) - buffer, 
            event[1].replace(tzinfo= None) + buffer 
        
        ] for event in CalendarEvents.objects.values_list('event_start_dt', 'event_end_dt') 
        ]

        # getting all holiday dates
        holidays = [ 
            holiday[0].date()  
            for holiday in Holiday.objects.values_list('date') 
        ]

        # initialize available slots dict
        free_slots = {
            date: []
            for date in dates
        }

        for date in dates:
            for start, end in time_slots:

                start   = dt.datetime.combine(date, start)
                end     = dt.datetime.combine(date, end)

                filtered_events = [ 
                    event
                    for event in events 
                    if (event[1].replace(tzinfo= None) > start
                    and event[0].replace(tzinfo= None) < end) 
                    ]

                filtered_events = sorted(filtered_events, key= lambda e: e[0])

                if not filtered_events:
                    free_slots[date].append([ start, end ])

                else:
                    if filtered_events[ 0][0] > start:  filtered_events = [[None, start]] + filtered_events
                    if filtered_events[-1][1] < end  :  filtered_events = filtered_events + [[end, None]]

                    for e1, e2 in zip(filtered_events[:-1], filtered_events[1:]):
                        if not e2[0] - e1[1] < meeting_length:
                            free_slots[date] += [[ e1[1], e2[0] ] ]
                                                
                    


            free_slots[date] = sorted(free_slots[date], key= lambda e: e[0])


        if not include_holidays:
            for date in free_slots:
                if date in holidays:
                    free_slots[date] = []

        free_slots = {
            f"{dt.datetime.strftime(date, '%b. %d, %y')} ({DAYS[date.weekday()]})": [[
            dt.datetime.strftime(time, '%H: %M')

            for time    in period
        ]   for period  in free_slots[date]
        ]   if free_slots[date] else [['Not Available', 'For This Day']]
            for date in free_slots
        }
        

        return render(request, 'findslot/results.html', {'slots' : free_slots})

    form = FindSlotForm()
    return render(request, 'findslot/find_slot.html', {'form':form})