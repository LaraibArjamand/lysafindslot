from django.db import models

# Create your models here.
class Holiday(models.Model):
    country      = models.CharField(null=False, max_length=50)
    holiday_name = models.CharField(null=False, max_length=50)
    date         = models.DateTimeField(null=False)
    Weekday      = models.CharField(null=False, max_length=25)


class CalendarList(models.Model):
    username      = models.CharField(null=False, max_length=50)
    calendar_id   = models.CharField(null=False, max_length=255)
    calendar_name = models.CharField(null=False, max_length=255)
    select_flg    = models.BooleanField(null=False, default=True)

    class Meta:
        indexes = [
            models.Index(fields=['id', 'username', 'select_flg']),
        ]

    def __str__(self):
        return self.calendar_name
        

class CalendarEvents(models.Model):
    user_event_key       = models.TextField(null=False, primary_key=True)
    calendar_info        = models.ForeignKey(CalendarList, on_delete=models.CASCADE)

    event_id             = models.TextField(null=True, blank=True)
    event_name           = models.TextField(null=True, blank=True)
    event_description    = models.TextField(null=True, blank=True)

    event_start_dt       = models.DateTimeField(null=True, blank=True)
    event_end_dt         = models.DateTimeField(null=True, blank=True)

    event_attendee       = models.TextField(null=True, blank=True)
    event_attendee_email = models.TextField(null=True, blank=True)
    event_location       = models.TextField(null=True, blank=True)

    event_start_dt_prev = models.DateTimeField(null=True, blank=True)
    event_end_dt_prev   = models.DateTimeField(null=True, blank=True)
    event_attendee_prev = models.TextField(null=True, blank=True)
    event_location_prev = models.TextField(null=True, blank=True)

    delete_flg = models.IntegerField(null=True, blank=True, default=0)
    new_flg    = models.IntegerField(null=True, blank=True, default=0)

    change_location_flg  = models.IntegerField(null=True, blank=True, default=0)
    change_start_dt_flg  = models.IntegerField(null=True, blank=True, default=0)
    change_end_dt_flg    = models.IntegerField(null=True, blank=True, default=0)
    change_attendee_flg  = models.IntegerField(null=True, blank=True, default=0)

    location_missing_flg = models.IntegerField(null=True, blank=True, default=0)

    inperson_flg = models.IntegerField(null=True, blank=True, default=0)
    zoom_flg     = models.IntegerField(null=True, blank=True, default=0)
    msteams_flg  = models.IntegerField(null=True, blank=True, default=0)
    gmeet_flg    = models.IntegerField(null=True, blank=True, default=0)
    lunch_flg    = models.IntegerField(null=True, blank=True, default=0)
    dinner_flg   = models.IntegerField(null=True, blank=True, default=0)
    oneonone_flg = models.IntegerField(null=True, blank=True, default=0)
    external_flg = models.IntegerField(null=True, blank=True, default=0)
    internal_flg = models.IntegerField(null=True, blank=True, default=0)

    all_day_flg  = models.IntegerField(null=True, blank=True, default=0)

    event_link      = models.TextField(null=True, blank=True)
    event_call_link = models.TextField(null=True, blank=True)
    num_attendees   = models.IntegerField(default=0)

    organizer_flg   = models.IntegerField(null=True, blank=True, default=0)
    creator_flg     = models.IntegerField(null=True, blank=True, default=0)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField()  # Not auto-add since we want to capture the latest updated on Google Calendar side

    class Meta:
        indexes = [
            models.Index(fields=['calendar_info', 'user_event_key'])
        ]
