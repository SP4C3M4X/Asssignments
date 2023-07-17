def simple_interest(principal,rate,time):
    return principal*(rate/100)*time
    print

def principal(simple_interest,rate,time):
    return (simple_interest*100)/rate*time

def rate(simple_interest,principal,time):
    return (simple_interest*100)/principal*time

def time(simple_interest,principal,rate):
    return (simple_interest*100)/principal*rate

