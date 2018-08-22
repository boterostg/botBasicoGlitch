import datetime
import time
dt = datetime.datetime(2018, 8, 21, 16, 00)
unixTime = time.mktime(dt.timetuple())

now = datetime.datetime.now()

HoyAno =  now.year
HoyMes = now.month
HoyDia = now.day
HoyHora = now.hour
HoyMinuto = now.minute
HoySegundo = now.second
HoyMicrosegundo = now.microsecond

#sancion 


banAno = HoyAno 
banMes = HoyMes
banDia = HoyDia 
banHora = HoyHora 
banMinuto = HoyMinuto + 10
banSegundo = HoySegundo 

fechaBan = dt = datetime.datetime(banAno, banMes, banDia, banHora, banMinuto,banSegundo)
unixBan = time.mktime(fechaBan.timetuple())

print("fecha ban :" + str(fechaBan))
print(unixBan)


print(now)
print("Unix Timestamp: ",unixTime)
print()
