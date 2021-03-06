import os
import sys
import time
import requests
import json


def geo_command(socket, argv):
    """
    Display geo location from an IP address

    :param socket: socket from cnc
    :param argv: arguments from cmd
    """
    if len(argv) == 2:
        jsonResp = (requests.get(
            "https://api.hackertarget.com/geoip/?q=" + argv[1]).text)
        fix = jsonResp.replace("\",\"", "\r\n")
        fix = fix.replace("\"", "").replace("{", "").replace("}", "")
        socket.send(f"{fix}\r\n".encode(""))
    else:
        socket.send("[x] Error, Invalid Arugment\r\nUsage: geo <ip>\r\n".encode())
