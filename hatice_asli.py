import keyboard
import logging as log 
import time  

logger=log.getLogger("Yapılan Hareket")

with open("oyunmodu.txt","w")as dosya:
    dosya.write("Normal Mod")

print(" W \t Yukarı hareket \n A \t Sola hareket \n S \t Aşağı hareket \n D \t Sağa haraket \n C \t Stabilize Moduna Geçiş \n H \t Depth Hold isimli Moda Geçiş \n I \t Sistem durumunu görüntüleme \n Q \t Programdan çıkış  ")

while True:
    if keyboard.is_pressed("W" or "w"):
        logger.info("Yukarı") 
        time.sleep(1)
        
    elif keyboard.is_pressed("A" or "a"):
        logger.info("Sola") 
        time.sleep(1)

    elif keyboard.is_pressed("S" or "s"):
        logger.info("Aşağı")
        time.sleep(1)

    elif keyboard.is_pressed("D" or "d"):
        logger.info("Sağa")
        time.sleep(1)

    elif keyboard.is_pressed("C" or "c"):
        logger.info("Stabilize Mod")
        with open("oyunmodu.txt","w")as dosya:
            dosya.write("Stabilize Mod")
        time.sleep(1)

    elif keyboard.is_pressed("H" or "h"):
        logger.info("Depth Hold Modu")
        with open("oyunmodu.txt","w")as dosya:
            dosya.write("Depth Hold Modu")
        time.sleep(1)

    elif keyboard.is_pressed("I" or "ı"):
        with open("oyunmodu.txt","r")as dosya:
            durum=str(dosya.read())
            print(durum)
        time.sleep(1)

    elif keyboard.is_pressed("Q" or "q"):
        break

    else:
        print("Yanlış harf tuşladınız") 
        continue
    
