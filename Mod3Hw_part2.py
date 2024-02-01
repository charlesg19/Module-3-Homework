def timeConversion(time, wait):
    alarm = time + wait
    diff = alarm % 24
    print("When the alarm goes off, the time on the clock will read:", diff)
   
time = int(input("Enter the current time, in hours, using a 24-hour clock:\n"))
wait = int(input("Enter the alarm duration in hours:\n"))
   
timeConversion(time,wait)
