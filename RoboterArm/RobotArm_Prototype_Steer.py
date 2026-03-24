#libraries
import math
import gpiozero

#Pins
ServoBase = AngularServo(12, min_angle=-90, max_angle=90)
ServoShoulder = AngularServo(16, min_angle=0, max_angle=90)
ServoElbow = AngularServo(18 , min_angle=-90, max_angle=0)

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
        print ("Not Possible please choose a larger distance") #prevents an error due to dividing by 0
    elif Dist <= LenForeArm + LenUpperArm and Dist >= LenUpperArm - LenForeArm: #Only allows inputs in a certain range to prevent errors
        AnglesList[0] = math.degrees(math.acos((LenUpperArmSquared-LenForeArmSquared-Dist*Dist)\
                                /(-2*LenForeArm*Dist))) #adjusted law of cosines for Alpha
        AnglesList[0] = round(AnglesList[0], 3) #Rounding for convinience, error margin is negligible
        AnglesList[1] = math.degrees(math.acos((Dist*Dist-LenUpperArmSquared-LenForeArmSquared)\
                               /(-2*LenUpperArm*LenForeArm))) #adjust law of cosines for Beta
        AnglesList[1] = round(AnglesList[1], 3) #Round for convience, error margin is negligible
    else: print("Cannot be reached plase choose a distance between " + str(LenForeArm + LenUpperArm)\
                 + " and " + str(LenUpperArm-LenForeArm)) #Error message when input is outside the defined range

DistToPiece = int(input("How far is the piece, in cm?: ")) #Let user choose distance to move the arm
Angle(DistToPiece) #Calculate Angles based on input
AngleBase = int(input("What is the Angle of the Base in degrees?: ")) #User chooses base angle

print(AnglesList) #Print Angles for bug fixing
print(AngleBase) #Print Angles for bug fixing

#Move robot to desired position
ServoBase.angle() = AngleBase
ServoShoulder.angle() = AnglesList[0]
ServoShoulder.angle() = -AnglesList[1]