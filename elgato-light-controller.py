#!/usr/bin/python3

import leglight
import argparse

# Initialize parser
parser = argparse.ArgumentParser(prog='elgato-light-controller', usage='%(prog)s [options]', description="CLI control of an Elgato light")
power = parser.add_mutually_exclusive_group()
power.add_argument("-on", "--On", help = "Turn light on", action="store_true")
power.add_argument("-off", "--Off", help = "Turn light off", action="store_true")
brightness = parser.add_mutually_exclusive_group()
brightness.add_argument("-brighter", "--Brighter", help = "Turn light on and make it brighter", action="store_true")
brightness.add_argument("-dimmer", "--Dimmer", help = "Turn light on and make it dimmer", action="store_true")
temperature = parser.add_mutually_exclusive_group()
temperature.add_argument("-warmer", "--Warmer", help = "Turn light on and make it warmer", action="store_true")
temperature.add_argument("-cooler", "--Cooler", help = "Turn light on and make it cooler", action="store_true")
parser.add_argument("-address", "--Address", type=str, help = "Specify the light's IP address")
parser.add_argument("-port", "--Port", type=int, help = "Specify the light's API port")
parser.add_argument("-default","--Default", help = "Set light to my default color and temperature", action="store_true")
args = parser.parse_args()

def main():
    Debug = False
    Light_IP_Address = "10.0.1.185"  # Change this to your light's IP
    Light_Port = 9123 # Elgato's default, only change if you changed this
    Light_Brightness = 23  #Change to your personal preference
    Light_Temperature = 3300 #Change to your personal preference
    Brightness_Adjustment = 10
    Color_Adjustment = 500
    Did_Something = False

    if args.Address:
        Light_IP_Address = args.Address
    
    if args.Port:
        Light_Port = args.Port

    myLight = leglight.LegLight(Light_IP_Address, Light_Port)
    myLight_config = vars(myLight) 
    
    if Debug:
        print(myLight_config)
        print(args)

    if args.Brighter:
        newbrightness = myLight_config['isBrightness'] + Brightness_Adjustment
        if newbrightness > 100:
            newbrightness = 100
        myLight.brightness(newbrightness)
        myLight.on()
        print(f"Brightness now {newbrightness}")
        Did_Something = True

    elif args.Dimmer:
        newbrightness = myLight_config['isBrightness'] - Brightness_Adjustment
        if newbrightness < 0:
            newbrightness = 0
        myLight.brightness(newbrightness)     
        myLight.on()
        print(f"Brightness now {newbrightness}")
        Did_Something = True

    if args.Cooler:
        newcolor = myLight_config['isTemperature'] + Color_Adjustment
        if newcolor > 7000:
            newcolor = 7000
        myLight.color(newcolor)
        myLight.on()
        print(f"Color now {newcolor}")
        Did_Something = True

    elif args.Warmer:
        newcolor = myLight_config['isTemperature'] - Color_Adjustment
        if newcolor < 2900:
            newcolor = 2900
        myLight.color(newcolor)
        myLight.on()
        print(f"Color now {newcolor}")
        Did_Something = True

    if args.Default:
        myLight.color(Light_Temperature)
        myLight.brightness(Light_Brightness)
        myLight.on()
        Did_Something = True

    if args.On:
        myLight.on()
        Did_Something = True
    
    if args.Off:
        myLight.off()
        Did_Something = True

    if not Did_Something:  
        if myLight_config['isOn']:
            myLight.off()
        else:
            myLight.on()

    


if __name__ == "__main__":
   main()