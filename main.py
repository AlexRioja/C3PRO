from adafruit_servokit import ServoKit
from mpu6050 import mpu6050
import helpers.legs as legs
import time
import helpers.moves as moves

#c
#sensor= mpu6050(0x)
pca = ServoKit(channels=16)
pca.frequency=60

moves.initial_position()
    
while True:
    num=int(input("Subir(1)/Bajar(0)/InclinarAlante(2)/puntillitas(3)/manita(4)/baile(5)"))
    if num==1:
        moves.initial_position()
    elif num==0:
        moves.initial_position()
        pca.servo[legs.FL0].angle=20
        pca.servo[legs.FR0].angle=160
        time.sleep(0.25)
        pca.servo[legs.BR0].angle=160
        pca.servo[legs.BL0].angle=20
        
        """
        pca.servo[legs.FL0].angle=0
        pca.servo[legs.BR0].angle=180
        pca.servo[legs.FR0].angle=180
        pca.servo[legs.BL0].angle=0
        """
    elif num==2:
        moves.initial_position()
        pca.servo[0].angle=20
        pca.servo[8].angle=170
    elif num==3:
        moves.puntillas_position()
    elif num==4:
        moves.initial_position()
        moves.pla_patita()
    elif num==5:
        moves.initial_position()
        moves.baile()
            
