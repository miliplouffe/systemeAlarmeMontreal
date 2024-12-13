import sys, os
sys.path.append("/home/miliplouffe/.local/lib/python3.11/site-packages/")
sys.path.append("C:\Python39\Lib")
import rpiMethodesMontreal
import RedisInOut as redisInOut

# gicleurs=redisInOut.recupereArrosageConfigurationGicleurs()

if __name__ == '__main__':

    rpiMethodesMontreal.initialiseDetecteurAlarmes()
   #  rpiMethodesMontreal.initialiseRelaisGicleur(gicleurs)