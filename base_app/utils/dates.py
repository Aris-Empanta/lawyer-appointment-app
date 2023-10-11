import math
from datetime import timedelta

class DateUtils:    

    @staticmethod
    def render_day_name(day_number):    
        match day_number:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
            
    @staticmethod
    def generate_appointments_per_interval(starting_time, ending_time, duration, breaks):
        interval_length = ending_time - starting_time
        interval_length_in_minutes = interval_length.total_seconds() / 60
        appointments_per_interval = math.floor(interval_length_in_minutes / (duration + breaks))
        #The amount in minutes of the duration and the break time combined.
        duration_and_breaks_combined = duration + breaks
        
        # Now, we will create a list with this format: index: {starting: datetime, ending: datetime} 
        # rendering each appointments starting and ending time.
        appointments = list()

        for x in range(appointments_per_interval):
            starting_ending_times_dict = dict()
            deviation_from_interval_start = duration_and_breaks_combined * (x)
            starting_ending_times_dict["starting"] = starting_time + timedelta(minutes=deviation_from_interval_start)
            starting_ending_times_dict["ending"] = starting_ending_times_dict["starting"] + timedelta(minutes=duration)
            appointments.append(starting_ending_times_dict)

        return appointments