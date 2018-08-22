#Importaciones.
import datetime                          
import time

############ EJEMPLO PARA ENTENDER COMO SE TRANSFORMA UNA FECHA A FECHA TIPO UNIX ##########################################
##                                                                                                                        ##
## dt = datetime.datetime(2018, 8, 21, 16, 00)  #Ejemplo de una fecha.                                                    ##
## unixTime = time.mktime(dt.timetuple())       #Conversión de esa fecha a Unix.                                          ##
##                                                                                                                        ##
############################################################################################################################

#Función que recoge los parametros del tiempo asignado a un baneo y lo combierte al tiempo de sanción tiempo en formato Unix.
def setTempBan(secB,minB,hourB,dayB,monthB,yearB):

  now = datetime.datetime.now()               #Fecha de hoy.

  #Separamos por partes la fecha y LA hora de hoy 
  HoyAno =  now.year                            
  HoyMes = now.month
  HoyDia = now.day
  HoyHora = now.hour
  HoyMinuto = now.minute
  HoySegundo = now.second
  HoyMicrosegundo = now.microsecond
  
  #A continuación creamos nuevas variables para asignar la sanción de tiempo que queramos añadiendo los parámetros recogidos al principio de la función.
  banAno = HoyAno + yearB
  banMes = HoyMes + monthB
  banDia = HoyDia + dayB
  banHora = HoyHora + hourB
  banMinuto = HoyMinuto + minB     
  banSegundo = HoySegundo + secB

  fechaBan = dt = datetime.datetime(banAno, banMes, banDia, banHora, banMinuto,banSegundo) # Al igual que en el ejemplo de arriba, añadimos los parametros de la feha.
  unixBan = time.mktime(fechaBan.timetuple()) #Convertimos la fecha del ban a Unix para luego asignarlo como parametro al baneo que hará el bot.

  print("fecha ban :" + str(fechaBan)) #Printeamos el resultado de la fecha del ban para asegurar que está bien.
  print(unixBan)                       #Printeamos el resultado de la fecha Unix del ban para asegurar que está bien.
  
  return unixBan        #Devolvemos el valor del tiempo de la sanción del baneado en Unix.


#Función para definir el tipo de muteo.
def setTypeMute(typeMute):
  
    sendMessages = False
    sendMedia = False
    sendOtherMessages = False
    sendWebPage = False
    
    typeBanList = [["sendMessages",sendMessages],["sendMedia",sendMedia],["sendOtherMessages",sendOtherMessages],["sendWebPage",sendWebPage]]
    
    print(typeBanList)
    
    if typeMute == "all":
        print("Entramos en all")
        typeBanList = [ [x[0],True] if x[1] == False else x for x in typeBanList ]
        
    elif typeMute == "media":
        print("Entramos en media")
        
        typeBanList = [ [x[0],True] if x[0] == "sendMedia" else x for x in typeBanList ]
        
    elif typeMute == "other":
        print("Entramos en media")
        
        typeBanList = [ [x[0],True] if x[0] == "sendOtherMessages" else x for x in typeBanList ]
        
    elif typeMute == "web":
        print("Entramos en media")
        
        typeBanList = [ [x[0],True] if x[0] == "sendWebPage" else x for x in typeBanList ]
        
    elif typeMute == "message":
        print("Entramos en media")
        
        typeBanList = [ [x[0],True] if x[0] == "sendMessages" else x for x in typeBanList ]
 
    print(typeBanList)
    
    return typeBanList
    
typeBan = setTypeMute("message")


def banlevel(idChatGroup,idUser,level,typeMute):
    
    cid = idChatGroup
    idUsuario =idUser
    
    if level == 1 :
        
        typeMuteo = setTypeMute(typeMute)
        tiempoban = setTempBan(0,30,0,0,0,0)
        
        print("El usuario tiene un ban de nivel 1 " + str(idUsuario)  + "estara baneado de: " + str(typeMuteo) + "con este tiempo: " + str(tiempoban) )
        
    if level == 2 :
    
        typeMuteo = setTypeMute(typeMute)
        tiempoban = setTempBan(0,0,8,0,0,0)
    
        print("El usuario tiene un ban de nivel 2 " + str(idUsuario)  + "estara baneado de: " + str(typeMuteo) + "con este tiempo: " + str(tiempoban) )
    
    if level == 3 :
    
        typeMuteo = setTypeMute(typeMute)
        tiempoban = setTempBan(0,0,0,1,0,0)
    
        print("El usuario tiene un ban de nivel 3 " + str(idUsuario)  + "estara baneado de: " + str(typeMuteo) + "con este tiempo: " + str(tiempoban) )
    
    if level == 4 :
    
        typeMuteo = setTypeMute(typeMute)
        tiempoban = setTempBan(0,0,0,7,0,0)
    
        print("El usuario tiene un ban de nivel 4 " + str(idUsuario)  + "estara baneado de: " + str(typeMuteo) + "con este tiempo: " + str(tiempoban) )
    
    if level == 5 :
    
        typeMuteo = setTypeMute(typeMute)
        tiempoban = setTempBan(0,0,0,0,1,0)
    
        print("El usuario tiene un ban de nivel 5 " + str(idUsuario)  + "estara baneado de: " + str(typeMuteo) + "con este tiempo: " + str(tiempoban) )
    
    if level == 6 :
    
        typeMuteo = setTypeMute(typeMute)
        tiempoban = setTempBan(0,0,0,0,3,0)
    
        print("El usuario tiene un ban de nivel 6 " + str(idUsuario)  + "estara baneado de: " + str(typeMuteo) + "con este tiempo: " + str(tiempoban) )
    
    if level == 7 :
    
        typeMuteo = setTypeMute(typeMute)
        tiempoban = setTempBan(0,0,0,0,0,1)
    
        print("El usuario tiene un ban de nivel 7 " + str(idUsuario)  + "estara baneado de: " + str(typeMuteo) + "con este tiempo: " + str(tiempoban) )
    

#Funcion para configurar el flood de cada grupo
def antiFloodConfig(idChatGroup,numMessages,typeMute,timeBan):
  
  db_config = read_db_config()
 
    # prepare query and data
    query = """ UPDATE Group
                SET maxMessages = %s, mute = typeMute
                WHERE id = %s """
 
    data = (title, book_id)
 
    try:
        conn = MySQLConnection(**db_config)
 
        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)
 
        # accept the changes
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()



