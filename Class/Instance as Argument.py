class Time:
    def __init__(self,h=0,m=0):
        self.hours=h
        self.minutes=m
    def increment(self,inc):
        self.hours+=inc
        return self
    def later(self,time2):
        result=1
        if self.hours>time2.hours:
            result=1
        elif self.hours<time2.hours:
            result=0
        elif self.minutes>time2.minutes:
            result=1
        elif self.minutes<time2.minutes:
            result=2
        if result==1:
            return self
        else:
            return time2
    def __str__(self):
        return '['+str(self.hours)+':'+str(self.minutes)+']'+' hrs'


        
t1=Time(12,04)
print t1

t2=Time(13,13)
print t2

t3=t1.increment(2)
print t3

print t1
