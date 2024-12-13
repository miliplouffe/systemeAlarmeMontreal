# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Simple demo of reading and writing the digital I/O of the MCP2300xx as if
# they were native CircuitPython digital inputs/outputs.
# Author: Tony DiCola
import time

import board
import busio
import digitalio
from dataclasses import dataclass
from datetime import datetime, timedelta
import gpiozero
from time import sleep
import systemeArrosageDataClass as dc

led = gpiozero.LED(17)
led.on()


class const:
    pinChambrePrincipale=0
    pinChambreSecondaire=1
    pinBureau=2
    pinSalon=3
    pinSousSol=4
    pinSalleVernis=5
    pinPorteAvant=6
    pinPorteArriere=7
    pinPorteSousSol=8
    pinSensorFumeeSalleBillard = 9
    pinEauAtelier=10
    pinSensorFumeeAtelier=11
    pinSensorPluie = 12
    pinGicleur1 = 23
    pinGicleur2 = 24
    pinGicleur3 = 25
    pinGicleur4 = 26


from adafruit_mcp230xx.mcp23017 import MCP23017

# Initialize the I2C bus:
i2c = busio.I2C(board.SCL, board.SDA)

# Create an instance of either the MCP23008 or MCP23017 class depending on
# which chip you're using:
# mcp = MCP23008(i2c)  # MCP23008
mcp = MCP23017(i2c, address=0x20)  # MCP23017

# Optionally change the address of the device if you set any of the A0, A1, A2
# pins.  Specify the new address with a keyword parameter:
# mcp = MCP23017(i2c, address=0x21)  # MCP23017 w/ A0 set

# Now call the get_pin function to get an instance of a pin on the chip.
# This instance will act just like a digitalio.DigitalInOut class instance
# and has all the same properties and methods (except you can't set pull-down
# resistors, only pull-up!).  For the MCP23008 you specify a pin number from 0
# to 7 for the GP0...GP7 pins.  For the MCP23017 you specify a pin number from
# 0 to 15 for the GPIOA0...GPIOA7, GPIOB0...GPIOB7 pins (i.e. pin 12 is GPIOB4).
# pin0 = mcp.get_pin(0)

# pin1 = mcp.get_pin(7)

pinChambrePrincipale = mcp.get_pin(const.pinChambrePrincipale)
pinChambreSecondaire = mcp.get_pin(const.pinChambreSecondaire)
pinBureau = mcp.get_pin(const.pinBureau)
pinSalon = mcp.get_pin(const.pinSalon)
pinSousSol = mcp.get_pin(const.pinSousSol)
pinSalleVernis = mcp.get_pin(const.pinSalleVernis)
pinPorteAvant = mcp.get_pin(const.pinPorteAvant)
pinPorteArriere = mcp.get_pin(const.pinPorteArriere)
pinPorteSousSol = mcp.get_pin(const.pinPorteSousSol)
pinSensorFumeeSalleBillard = mcp.get_pin(const.pinSensorFumeeSalleBillard)
pinEauAtelier = mcp.get_pin(const.pinEauAtelier)
pinSensorFumeeAtelier = mcp.get_pin(const.pinSensorFumeeAtelier)
pinSensorPluie = mcp.get_pin(const.pinSensorPluie)

gicleur1 = LED(const.pinGicleur1)
gicleur2 = LED(const.pinGicleur2)
gicleur3 = LED(const.pinGicleur3)
gicleur4 = LED(const.pinGicleur4)
    
def initialiseDetecteurAlarmes():
    global pinChambrePrincipale,pinChambreSecondaire,pinBureau,pinSalon,pinSousSol
    global pinSalleVernis,pinPorteAvant,pinPorteArriere,pinPorteSousSol,pinSensorFumeeSalleBillard
    global pinEauAtelier,pinSensorFumeeAtelier,pinSensorPluie
        
    pinChambrePrincipale.direction = digitalio.Direction.INPUT
    pinChambrePrincipale.pull = digitalio.Pull.UP
    pinChambreSecondaire.direction = digitalio.Direction.INPUT
    pinChambreSecondaire.pull = digitalio.Pull.UP
    pinBureau.direction = digitalio.Direction.INPUT
    pinBureau.pull = digitalio.Pull.UP
    pinSalon.direction = digitalio.Direction.INPUT
    pinSalon.pull = digitalio.Pull.UP
    pinSousSol.direction = digitalio.Direction.INPUT
    pinSousSol.pull = digitalio.Pull.UP
    pinSalleVernis.direction = digitalio.Direction.INPUT
    pinSalleVernis.pull = digitalio.Pull.UP
    pinPorteAvant.direction = digitalio.Direction.INPUT
    pinPorteAvant.pull = digitalio.Pull.UP
    pinPorteArriere.direction = digitalio.Direction.INPUT
    pinPorteArriere.pull = digitalio.Pull.UP
    pinPorteSousSol.direction = digitalio.Direction.INPUT
    pinPorteSousSol.pull = digitalio.Pull.UP
    pinSensorFumeeSalleBillard.direction = digitalio.Direction.INPUT
    pinSensorFumeeSalleBillard.pull = digitalio.Pull.UP
    pinEauAtelier.direction = digitalio.Direction.INPUT
    pinEauAtelier.pull = digitalio.Pull.UP
    pinSensorFumeeAtelier.direction = digitalio.Direction.INPUT
    pinSensorFumeeAtelier.pull = digitalio.Pull.UP
    pinSensorPluie.direction = digitalio.Direction.INPUT
    pinSensorPluie.pull = digitalio.Pull.UP


 


def initialiseRelaisGicleur(gicleurs):
    global gicleur1, gicleur2, gicleur3,gicleur4
    
    if gicleurs["1"].ZoneActive==True:
        gicleur1.on()
    if gicleurs["2"].ZoneActive==True:
        gicleur2.on()
    if gicleurs["3"].ZoneActive==True:
        gicleur3.on()
    if gicleurs["4"].ZoneActive==True:
        gicleur4.on()


def set_relais(nomRelais, statut):
    global relais1, relais2, relais3, relais4

    if statut==True:
        print ("statut True")
        if nomRelais =="1":
            gicleur1.off()
        if nomRelais =="2":
            gicleur2.off()        
        if nomRelais =="3":
            gicleur3.off()
        if nomRelais =="4":
            gicleur4.off()            
    else:
        gicleur1.on()
        gicleur2.on()
        gicleur3.on()
        gicleur4.on()



def getValeursAlarme(equipementsAlarmes):
    global pinChambrePrincipale,pinChambreSecondaire,pinBureau,pinSalon,pinSousSol
    global pinSalleVernis,pinPorteAvant,pinPorteArriere,pinPorteSousSol,pinSensorFumeeSalleBillard
    global pinEauAtelier,pinSensorFumeeAtelier,pinSensorPluie
    
    print ("passe 11")
    equipementsAlarmes.pinChambrePrincipale= pinChambrePrincipale.value
    print ("passe 12")
    equipementsAlarmes.pinChambreSecondaire =pinChambreSecondaire.value
    equipementsAlarmes.pinBureau= pinBureau.value
    equipementsAlarmes.pinSalon= pinSalon.value
    equipementsAlarmes.pinSousSol= pinSousSol.value
    equipementsAlarmes.pinSalleVernis= pinSalleVernis.value
    equipementsAlarmes.pinPorteAvant= pinPorteAvant.value
    equipementsAlarmes.pinPorteArriere= pinPorteArriere.value
    equipementsAlarmes.pinPorteSousSol= pinPorteSousSol.value
    equipementsAlarmes.pinSensorFumeeSalleBillard= pinSensorFumeeSalleBillard.value
    equipementsAlarmes.pinEauAtelier= pinEauAtelier.value
    equipementsAlarmes.pinSensorPluie= pinSensorPluie.value
    equipementsAlarmes.pinSensorFumeeAtelier= pinSensorFumeeAtelier.value
   
    return equipementsAlarmes

def getValeursGicleurs(gicleurs):
    equipementsGicleurs=[]
    if gicleurs["1"].ZoneActive==True:
        if gicleur1.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
    if gicleurs["2"].ZoneActive==True:
        if gicleur2.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
    if gicleurs["3"].ZoneActive==True:
        if gicleur3.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
    if gicleurs["4"].ZoneActive==True:
        if gicleur4.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
                  
   

    return equipementsGicleurs