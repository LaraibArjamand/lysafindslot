from django import forms
from .models import *

from .utils import *


class FindSlotForm(forms.Form):

  # CHOICES
  TIME_BETWEEN_CHOICES       = [('before', 'Before: 7-9am'), ('atwork', 'At Work: 9am-5pm'),
                              ('after', 'After: 5-9pm'), ('beyond', 'Beyond: 9pm-12am'),
                              ('custom', 'Customized Search')]

  DATE_BETWEEN_CHOICES       = [('todayntom', 'Today & Tomorrow'), ('thisweek', 'This Week'),
                               ('nextweek', 'Next Week'), ('next30days', 'Next 30 Days'),
                               ('custom', 'Customized Search')]

  custom_time_choices_from   =  [(i, i) for i in get_time_slots(['custom'])]
  custom_time_choices_to     =  [(i, i) for i in get_time_slots(['custom'])]
 
  custom_date_choices_from   = [(i, i) for i in get_date_slots(['custom'], True)]
  custom_date_choices_to     = [(i, i) for i in get_date_slots(['custom'], True)]

  BUFFER_CHOICES             = [('nogap', 'No Gap'), (5, '5 min'), (10, '10 min'), (15, '15 min'), (30, '30 min')]
  MEETING_LENGTH_CHOICES     = [(5,'5 min'), (10,'10 min'), (15,'15 min'), (30,'30 min'), (60, '1 hour'), (90, '1.5 hour'), 
                                (120, '2 hour'), (180, '3 hour'), (240, '4 hour'), (300, '5 hour'), (360, '6 hour'), (420, '7 hour'), (48, '8 hour')]
  
  # Form Fields
  time_between               = forms.MultipleChoiceField(label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "time-list"}), choices=TIME_BETWEEN_CHOICES, required=True)
  date_between               = forms.MultipleChoiceField(label='', widget=forms.CheckboxSelectMultiple(attrs={'class': "date-list"}), choices=DATE_BETWEEN_CHOICES, required=True)

  custom_time_search_from    = forms.ChoiceField(label='From', widget=forms.Select(attrs={'class' : 'custom-time'}), choices=custom_time_choices_from, required=True)
  custom_time_search_to      = forms.ChoiceField(label='To',   widget=forms.Select(attrs={'class' : 'custom-time'}), choices=custom_time_choices_to, required=True)
  
  custom_date_search_from    = forms.ChoiceField(label='From', widget=forms.Select(attrs={'class' : 'custom-date'}), choices=custom_date_choices_from, required=True)
  custom_date_search_to      = forms.ChoiceField(label='To',   widget=forms.Select(attrs={'class' : 'custom-date'}), choices=custom_date_choices_to, required=True)
  
  meeting_length             = forms.ChoiceField(label='Meeting Length', widget=forms.Select, choices=MEETING_LENGTH_CHOICES)
  buffer_length              = forms.ChoiceField(label='Buffer Between Meetings', widget=forms.Select, initial=1, choices=BUFFER_CHOICES)
     
  day_events                 = forms.BooleanField(label='Don\'t include All Day Events',  required=False)
  holiday                    = forms.BooleanField(label='Don\'t include Public Holidays', required=False)
     
      