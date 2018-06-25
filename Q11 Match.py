class Match:
    'Runs and Wickets'
    runs=21
    wickets=5
    def __init__(self,run,wickets):
        self.runs=runs
        self.wickets=wickets
        print "Runs : ",runs
        print "Wickets: ",wickets

print "Test.__do__:", Match.__doc__

print "Test.__name__:", Match.__name__
        
print "Test.__module__:",Match.__module__

print "Test.__bases__:",Match.__bases__

print "Test.__dict__:",Match.__dict__
