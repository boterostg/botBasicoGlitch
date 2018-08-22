#Importaciones
import datetime                          
import time


dt = datetime.datetime(2018, 8, 21, 16, 00) #Ejemplo de una fecha
unixTime = time.mktime(dt.timetuple())      #Conversión de esa fecha a Unix

now = datetime.datetime.now()               #Fecha de hoy

#Separamos por partes la fecha y hora de hoy 
HoyAno =  now.year                            
HoyMes = now.month
HoyDia = now.day
HoyHora = now.hour
HoyMinuto = now.minute
HoySegundo = now.second
HoyMicrosegundo = now.microsecond

#A continuación creamos nuevas variables para asignar la sanción de tiempo que queramos añadiendo el tiempo que sea a la fecha actual.

banAno = HoyAno 
banMes = HoyMes
banDia = HoyDia 
banHora = HoyHora 
banMinuto = HoyMinuto + 10
banSegundo = HoySegundo 

fechaBan = dt = datetime.datetime(banAno, banMes, banDia, banHora, banMinuto,banSegundo) # Al igual que en el ejemplo de arriba, añadimos los parametros de la feha.
unixBan = time.mktime(fechaBan.timetuple()) #Convertimos la fecha del ban a Unix para luego asignarlo como parametro al baneo que hará el bot

print("fecha ban :" + str(fechaBan)) #Printeamos el resultado de la fecha del ban para asegurar que está bien
print(unixBan)                       #Printeamos el resultado de la fecha Unix del ban para asegurar que está bien





