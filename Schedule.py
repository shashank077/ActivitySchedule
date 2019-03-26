import time
import webbrowser
i=0
print("start time="+time.ctime())
while i<3:
 time.sleep(5)
 print("time now=" + time.ctime())
 webbrowser.open("https://www.youtube.com/watch?v=V15BYnSr0P8")
 i+=1
