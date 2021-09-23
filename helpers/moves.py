from adafruit_servokit import ServoKit
from mpu6050 import mpu6050
import legs
import time

pca = ServoKit(channels=16)
pca.frequency=60

def initial_position(part="whole"):
    """Restores initial position

    Args:
        part (String): Can be "back" or "front" or leave empty for restoring the whole position 
    """
    if part == "back":        
        pca.servo[legs.BL0].angle=80
        pca.servo[legs.BL2].angle=175
        pca.servo[legs.BL1].angle=180
        
        pca.servo[legs.BR0].angle=110
        pca.servo[legs.BR1].angle=35
        pca.servo[legs.BR2].angle=25
    elif part == "front":
        pca.servo[legs.FL0].angle=80
        pca.servo[legs.FL1].angle=160
        pca.servo[legs.FL2].angle=10

        pca.servo[legs.FR0].angle=110
        pca.servo[legs.FR1].angle=30
        pca.servo[legs.FR2].angle=170
    else:
        pca.servo[legs.FL0].angle=80
        pca.servo[legs.FL1].angle=160
        pca.servo[legs.FL2].angle=10
        
        pca.servo[legs.BL0].angle=80
        pca.servo[legs.BL2].angle=175
        pca.servo[legs.BL1].angle=180
        
        pca.servo[legs.FR0].angle=110
        pca.servo[legs.FR1].angle=30
        pca.servo[legs.FR2].angle=170
        
        pca.servo[legs.BR0].angle=110
        pca.servo[legs.BR1].angle=35
        pca.servo[legs.BR2].angle=25


def puntillas_position():
    
    pca.servo[legs.BR0].angle=10
    pca.servo[legs.BR1].angle=110
    pca.servo[legs.BR2].angle=25
    
    pca.servo[legs.BL0].angle=180
    pca.servo[legs.BL2].angle=175
    pca.servo[legs.BL1].angle=120
    
    time.sleep(0.25)
    
    pca.servo[legs.FL0].angle=180
    pca.servo[legs.FL1].angle=100
    pca.servo[legs.FL2].angle=10
    
    pca.servo[legs.FR0].angle=0
    pca.servo[legs.FR1].angle=100
    pca.servo[legs.FR2].angle=170
    
   
def pla_patita():
    pca.servo[legs.BL0].angle=60
    pca.servo[legs.FL0].angle=60
    time.sleep(0.1)
    pca.servo[legs.FR0].angle=130
    time.sleep(0.25)
    pca.servo[legs.FR1].angle=80
    time.sleep(0.15)
    pca.servo[legs.FR1].angle=90
    time.sleep(0.15)
    pca.servo[legs.FR0].angle=120
    time.sleep(0.25)
    pca.servo[legs.FR0].angle=130
    pca.servo[legs.FR2].angle=170
    
def baile():
       
    pca.servo[0].angle=60
    pca.servo[12].angle=140
    time.sleep(0.1)
    pca.servo[0].angle=80
    pca.servo[12].angle=110
    pca.servo[4].angle=60
    pca.servo[8].angle=140
    time.sleep(0.1)
    pca.servo[4].angle=80
    pca.servo[8].angle=110
    pca.servo[0].angle=60
    pca.servo[12].angle=140
    time.sleep(0.1)
    pca.servo[0].angle=80
    pca.servo[12].angle=110
    pca.servo[4].angle=60
    pca.servo[8].angle=140
    time.sleep(0.1)
    pca.servo[4].angle=80
    pca.servo[8].angle=110
    pca.servo[0].angle=60
    pca.servo[12].angle=140
    time.sleep(0.1)
    pca.servo[0].angle=80
    pca.servo[12].angle=100
    pca.servo[4].angle=60
    pca.servo[8].angle=140
    time.sleep(0.1)
    pca.servo[4].angle=80
    pca.servo[8].angle=110