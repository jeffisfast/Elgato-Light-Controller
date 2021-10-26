Elgato Light Controller
=======================

I'm really happy with my Elgato Key Light from an illumination perspective.  However, their control software has been glitchy for me.  When I first used the light the software worked most of the time, but over time it started having problems by only detecting the light intermittently.  

After internet searching I found:

1. Others have had the exact same experience.
2. Corsair’s technical support wasn’t particularly helpful or responsive.
3. Factory resetting the light didn’t help, in my case it made it worse.
4. Some internet threads think the issue is that the Key Light only uses 2.4 GHz Wi-Fi networks, and that newer Wi-Fi systems are trying to connect at 5.0 GHz. That wouldn’t explain why the light works sometimes, but I built a dedicated 2.4 GHz network to test this and it didn’t help.
5. Other internet threads think the issue is multicast being blocked on one’s home network.  It is true that this could explain the symptoms, but my network doesn’t block multicast and doesn’t explain the intermittent nature of the problem.

Diving in a bit deeper I discovered that my light:
1. Was staying connected to my network, even when the software couldn’t find it.
2. On port 9123 there was an API listener.
3. [Pyleglight](https://gitlab.com/obviate.io/pyleglight/) is a python3 module that implements an API wrapper for Key lights. I’ve included the latest version of Pyleglight in this repository as of October 26, 2021.  

So, I went ahead and created this program to accept all the typical commands for control of a single light.  If you have multiple lights you can either call the program repeatedly or have a fun afternoon modifying it to work with multiple lights.

Usage is as follows:
====================

`usage: elgato-light-controller [ options ]

CLI control of an Elgato light

optional arguments:
-h, --help            show this help message and exit
-on, --On             Turn light on
-off, --Off           Turn light off
-brighter, --Brighter
                      Turn light on and make it brighter
-dimmer, --Dimmer     Turn light on and make it dimmer
-warmer, --Warmer     Turn light on and make it warmer
-cooler, --Cooler     Turn light on and make it cooler
-address ADDRESS, --Address ADDRESS
                      Specify the light's IP address
-port PORT, --Port PORT
                      Specify the light's API port
-default, --Default   Set light to my default color and temperature


With no arguments the program will just toggle the state of the light.`

Installation & Setup Tips:
==========================

1. Give your light a static IP address through your network’s DHCP server. 
2. Adjust the IP address in the source code so it matches the address you’ve given it.  (Alternatively always pass it in using the -address command line argument).
3. If you have a Stream Deck you can link buttons to commands (at least on Mac OS). Use the Steam Deck's **Open** command and point to elgato-light-controller.py.  Then manually edit the path by clicking in the "App/File" field to the file it opens and appending ` "-brighter"` or any other parameters you want. Some internet posts state that one has to create an AppleScript or shell script to pass in parameters, but this method works fine for me and avoids that overhead.  I made buttons for toggle on/off, brighter, warmer, cooler, and dimmer.
4. If you're using this software you may choose to uninstall the Elgato Control Center, since it doesn't work well (at least as of this writing)

