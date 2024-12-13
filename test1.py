import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017

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

# Initialize the I2C bus:
i2c = busio.I2C(board.SCL, board.SDA)

# Create an instance of either the MCP23008 or MCP23017 class depending on
# which chip you're using:
# mcp = MCP23008(i2c)  # MCP23008
mcp = MCP23017(i2c, address=0x20)  # MCP23017

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

print ("pin salon :", mcp.get_pin(const.pinSousSol))