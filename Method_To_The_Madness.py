class Time(object):
 def __init__(self, hour, minute, second):
     self.hour = hour
     self.minute = minute
     self.second = second
 def __str__(self):
    return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

 def __add__(self, other):
     return str(self.hour + other.hour) + ":" + str(self.minute + other.minute) + ":" +str(self.second + other.second)


time1 = Time(6,18,0)
time2 = Time(3,16,0)
time3 = Time(8,41,0)
print time1
print time2
print time3
print " "
print time1 + time2
print time1 + time3
print time2 + time3
