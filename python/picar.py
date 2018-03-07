#!/usr/bin/env python
#coding=utf-8
#   Ce programme permet de contrôler  la voiture robot grasse à WebIOPi à travers une page web
#     GeoHolz : https://blog.jolos.fr


#Déclaration
from time import sleep
import webiopi
import RPi.GPIO as GPIO
from select import select   
import serial
import ossaudiodev
import wave
from threading import Thread

#Déclaration des GPIOs

#Moteur A Gauche
EnA = 4
Out1 = 17
Out2 = 22
#Moteur B Droite
EnB = 18
Out3 = 23
Out4 = 27

#Il existe 2 mode pour déclarer les GPIO, soit GPIO.BOARD soit GPIO.BCM
GPIO.setmode(GPIO.BCM)

@webiopi.macro
def Forward():
   GPIO.output(Out1,True)
   GPIO.output(Out3,True)
   GPIO.output(Out2,False)
   GPIO.output(Out4,False)
   GPIO.output(EnA,True)
   GPIO.output(EnB,True)
@webiopi.macro
def Stop():
   GPIO.output(Out1,False)
   GPIO.output(Out3,False)
   GPIO.output(Out2,False)
   GPIO.output(Out4,False)
   GPIO.output(EnA,True)
   GPIO.output(EnB,True)
@webiopi.macro
def Standby():
   GPIO.output(Out1,False)
   GPIO.output(Out3,False)
   GPIO.output(Out2,False)
   GPIO.output(Out4,False)
   GPIO.output(EnA,False)
   GPIO.output(EnB,False)
@webiopi.macro
def Reverse():
   GPIO.output(Out2,True)
   GPIO.output(Out4,True)
   GPIO.output(Out1,False)
   GPIO.output(Out3,False)
   GPIO.output(EnA,True)
   GPIO.output(EnB,True)
@webiopi.macro
def TurnRight():
   GPIO.output(Out1,True)
   GPIO.output(Out3,False)
   GPIO.output(Out2,False)
   GPIO.output(Out4,True)
   GPIO.output(EnA,True)
   GPIO.output(EnB,True)
@webiopi.macro
def TurnLeft():
   GPIO.output(Out1,False)
   GPIO.output(Out3,True)
   GPIO.output(Out2,True)
   GPIO.output(Out4,False)
   GPIO.output(EnA,True)
   GPIO.output(EnB,True)



# Called by WebIOPi at script loading
def setup():
    # Setup GPIOs
    GPIO.setup(EnA, GPIO.OUT)
    GPIO.setup(EnB, GPIO.OUT)
    GPIO.setup(Out1, GPIO.OUT)
    GPIO.setup(Out2, GPIO.OUT)
    GPIO.setup(Out3, GPIO.OUT)
    GPIO.setup(Out4, GPIO.OUT)



# Called by WebIOPi at server shutdown
def destroy():
    # Reset GPIO functions
    GPIO.cleanup()
