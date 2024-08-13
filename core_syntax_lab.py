import datetime


class TimeInterval: 
    def __init__(self, hours, minutes, seconds): 
        self.hours = self.validate_hours(hours)
        self.minutes = self.validate_minutes(minutes)
        self.seconds = self.validate_seconds(seconds) 

    def format_time_interval(self, time_interval): 
        pass 

    def __add__(self, second_time_interval): 
        pass  

    def __sub__(self, second_time_interval):
        pass 

    def __mul__(self, value): 
        if all(self.hours, self.minutes, self.seconds) == 0:
            return 0
        
        time_interval = self.hour + self.minutes + self.seconds * value
        self.hour, self.minutes, self.seconds = self.format_time_interval(
            time_interval
        )

    def __str__(self): 
        return 
    
    def validate_hours(self, hours): 
        if hours not in range(00, 23): 
            raise Exception("Hours must be between 00 and 23!")
        
        return hours * 3600
    
    def validate_minutes(self, minutes): 
        if minutes not in range(00, 59): 
            raise Exception("Minutes must be between 00 and 59!")
        
        return minutes * 60

    def validate_seconds(self, seconds): 
        if seconds not in range(00, 59): 
            raise Exception("Seconds must be between 00 and 59!")
        
        return seconds 
