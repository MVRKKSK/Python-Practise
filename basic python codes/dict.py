import time
import webbrowser

breaks = 3
count = 1
print("This program started on "+time.ctime())
while(count<=breaks):
    time.sleep()
    webbrowser.open("https://www.youtube.com/watch?v=SAcpESN_Fk4")
    count = count+1
