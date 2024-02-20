from datetime import datetime
from playsound import playsound

time=input("enter the time of alarm to be set:HH:MM:SS\n")
hour=time[0:2]
minute=time[3:5]
second=time[6:8]
period=time[9:11].upper()

print('setting up alarm...')
while True:
    now=datetime.now()
    chour=now.strftime("%I")
    cmin=now.strftime("%M")
    csec=now.strftime("%S")
    cpreiod=now.strftime("%p")
    if(period==cpreiod):
        if(hour==chour):
            if(minute==cmin):
                if(second==csec):
                    print('wake up')
                    playsound('audio.mp3')
                    break
