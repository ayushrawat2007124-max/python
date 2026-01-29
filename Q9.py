#wap to covert given seconds into hours minutes and remaining seconds.
sec=float(input("enter the value of seconds"))
hour = sec// 3600
sec= sec%3600
minutes = sec// 60
sec = sec%60
print(hour)
print(minutes)
print(sec)