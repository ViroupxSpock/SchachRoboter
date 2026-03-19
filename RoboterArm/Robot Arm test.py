#libraries
#import gpiozero
import math

#Declaration of GPIO Pins
"""
ServoBase = gpiozero.AngularServo(12) #Servo motor in base
ServoShoulder = gpiozero.AngularServo(16) #Alpha in calculations
ServoElbow = gpiozero.AngularServo(18) #Beta in calculations
ElectroMagnet = gpiozero.LED(24)"""
#Robotparameters
LenUpperArm = 14 #Length of upper arm
LenUpperArmSquared = LenUpperArm*LenUpperArm #Squared for later convinience
LenForeArm = 14 #Length of forearm
LenForeArmSquared = LenForeArm*LenForeArm #Squared for later convinience

AnglesList = [0,0] #Angles of shoulder and elbow shoulders
AngleBase = 0 #Angle of the base servo motor

#angle function
def Angle(Dist):
    if Dist == 0: 
        print ("Not Possible please choose a larger distance")
    elif Dist <= LenForeArm + LenUpperArm and Dist >= LenUpperArm - LenForeArm:
        AnglesList[0] = math.degrees(math.acos((LenUpperArmSquared-LenForeArmSquared-Dist*Dist)\
                                /(-2*LenForeArm*Dist))) #adjusted law of cosines for Alpha
        AnglesList[0] = round(AnglesList[0], 3) #Rounding for convinience, error margin is negligible
        AnglesList[1] = math.degrees(math.acos((Dist*Dist-LenUpperArmSquared-LenForeArmSquared)\
                               /(-2*LenUpperArm*LenForeArm))) #adjust law of cosines for Beta
        AnglesList[1] = round(AnglesList[1], 3) #Round for convience, error margin is negligible
    else: print("Cannot be reached plase choose a distance between " + str(LenForeArm + LenUpperArm)\
                 + " and " + str(LenUpperArm-LenForeArm))

DistToPiece = int(input("How far is the piece, in cm?: "))
Angle(DistToPiece)
AngleBase = int(input("What is the Angle of the Base in degrees?: "))


print(AnglesList)
print(AngleBase)