"""Module for discovery of Elgato devices on the local network"""

from zeroconf import ServiceBrowser, Zeroconf
from time import sleep, time
import socket
from typing import cast
from . import LegLight
import logging


def discover(timeout: int = 5) -> list:
    """ 
    Return a list of Elgato lights on the network
    
    Parameters
    ----------
    timeout
       The number of seconds to wait for zeroconf discovery
    """

    lights = []

    class thelistener:
        def remove_service(self, zeroconf, type, name):
            pass

        def add_service(self, zeroconf, type, name):
            # Get the info from mDNS and shove it into a LegLight object
            info = zeroconf.get_service_info(type, name)
            ip = socket.inet_ntoa(info.addresses[0])
            port = cast(int, info.port)
            lname = info.name
            server = info.server
            logging.debug("Found light @ {}:{}".format(ip, port))
            lights.append(LegLight(address=ip, port=port, name=lname, server=server))

    zeroconf = Zeroconf()
    listener = thelistener()
    browser = ServiceBrowser(zeroconf, "_elg._tcp.local.", listener)  # type: ignore

    try:
        # We're gonna loop for a bit waiting for discovery
        # Depending on your network, you may need more/less timeout
        start = time()
        while True and (time() - start) < timeout:
            sleep(0.1)
    finally:
        # This sometimes takes a litteral second or two
        zeroconf.close()
    return lights
