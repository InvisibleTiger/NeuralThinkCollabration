from ics import Calendar, Event
from pathlib import Path
import os
import yaml
from datetime import datetime
from dateutil.relativedelta import *
import pytz

calender_filename = 'docs/myfile.ics'
calender_datafile = 'myfile.yml'

class Calender_skill():
    c = Calendar()

    def __init__(self):
        print("")
        print("*"*50)
        print("Calender skill loaded")
        print("*"*50)

    def add_event(self, begin:str, name:str, description:str=None)->bool:
        e = Event()
        e.name = name
        e.begin = begin
        e.description = description
        try:
            self.c.events.add(e)
            return True
        except:
            print("There was a problem adding the event, sorry")
            return False

    def remove_event(self, event_name:str):
        for event in self.c.events:
            if event.name == event_name:
                self.c.events.remove(event)
                print("Removing event", event_name)
                return True

        print("Sorry could not find that event", event_name)
        return False

    def parse_to_dict(self):
        dict = []
        for event in self.c.events:
            my_event = {}   