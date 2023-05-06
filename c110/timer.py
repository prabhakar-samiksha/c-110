import time
def countdowntimer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        sec=int(seconds%60)
        timer=f"{mins}:{sec}"
        print (timer)
        seconds-=1
    print("timer")   
seconds=input("enter the time in number of seconds: ")    
countdowntimer(int(seconds)) 
