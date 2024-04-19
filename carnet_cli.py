#!/usr/bin/python

# command line client to use the python library for volkswagen carnet by Robin Ostlund
# https://github.com/robinostlund/volkswagencarnet
# It can be used e.g. with exec node in nodered
# In addition the newest longtermstatistics data will be retrieved
# The output is given in json format
# working commands:
#   python3 carnet_cli.py <vin> update
#   python3 carnet_cli.py <vin> setrefresh
#   python3 carnet_cli.py <vin> setcharger <start/stop> 
#   python3 carnet_cli.py <vin> setchargercurrent <ampere>
#   python3 carnet_cli.py <vin> setclimatisationtemp <temperature>
#   python3 carnet_cli.py <vin> setclimatisation <electric> <temperature/auxiliary> <true/false> (true: without external power; false: with charging cable only)
#   python3 carnet_cli.py <vin> setwindowheating <start/stop>
#   python3 carnet_cli.py <vin> setlock <lock/unlock>

spin='your SPIN'
usermail='your email' 
userpw='your password'

"""Communicate with We Connect services."""
import base64
import os

"""Modified to utilize API calls derived from Android Apps instead of Web API"""
import re
import time
import logging
import asyncio
import hashlib
import jwt
import json

from sys import version_info, argv
from datetime import timedelta, datetime
from urllib.parse import urljoin, parse_qs, urlparse
from json import dumps as to_json
import aiohttp
from bs4 import BeautifulSoup
from base64 import b64encode
from vw_vehicle import Vehicle
from vw_utilities import read_config, json_loads

from aiohttp import ClientSession, ClientTimeout
from aiohttp.hdrs import METH_GET, METH_POST

from vw_const import (
    BRAND,
    COUNTRY,
    HEADERS_SESSION,
    HEADERS_AUTH,
    BASE_SESSION,
    BASE_API,
    BASE_AUTH,
    CLIENT,
    USER_AGENT,
    APP_URI,
)

import vw_connection
from vw_vehicle import Vehicle


async def main():
    """Main method."""
    if '-h' in argv:
        print(
            f"Usage:\n" +
            "python3 carnet_cli.py <vin> <action> <action parameters>\n" +
            "python3 carnet_cli.py <vin> update\n" +
            "python3 carnet_cli.py <vin> setrefresh\n" +
            "python3 carnet_cli.py <vin> setcharger <start/stop>\n" +
            "python3 carnet_cli.py <vin> setchargercurrent <#ampere>\n" +
            "python3 carnet_cli.py <vin> setclimatisationtemp <#temperature>\n" +
            "python3 carnet_cli.py <vin> setclimatisation <electric/auxiliary> <#temperature> <true/false> (true: without external power; false: with charging cable only)\n" +
            "python3 carnet_cli.py <vin> setwindowheating <start/stop>\n" +
            "python3 carnet_cli.py <vin> setlock <lock/unlock>"
        )
        return
    if len(argv)<3:
        print ("List of arguments too short! Try -h")
        return
    vin=argv[1]
    action=argv[2]
    if action == "setlock" or action == "setwindowheating" or action[0:10]== "setcharger" or action[0:16]== "setclimatisation":
        if len(argv)<4:
            print ("List of arguments too short! Try -h")
            return
        mode=argv[3]
    elif action != "setrefresh" and action != "update":
        print('action not supported')
        return
    if '-v' in argv:
        logging.basicConfig(level=logging.INFO)
    elif '-vv' in argv:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)

    async with ClientSession() as session:
        connection = vw_connection.Connection(session, usermail, userpw)
        if await connection.doLogin():
            for vehicle in connection.vehicles:
                if vehicle.vin == vin:
                    if action == "setrefresh":
                        response = await vehicle.set_refresh()
                    elif action == "setcharger":
                        response = await vehicle.set_charger(mode)
                    elif action == "setchargercurrent":
                        response = await vehicle.set_charger_current(mode)
                    elif action == "setclimatisationtemp":
                        mode=float(mode)
                        response = await vehicle.set_climatisation_temp(mode)
                    elif action == "setclimatisation":
                        if mode != "off":
                            if len(argv)<6:
                                print ("List of arguments too short! Try -h")
                                return
                            vehicle._states['climater']['settings']['targetTemperature']['content']=(float(argv[4])+273)*10
                            if argv[5]=='True' or argv[5]=='true':
                                vehicle._states['climater']['settings']['climatisationWithoutHVpower']['content']=True
                            else:
                                vehicle._states['climater']['settings']['climatisationWithoutHVpower']['content']=False
                        response = await vehicle.set_climatisation(mode,spin)
                    elif action == "setwindowheating":
                        response = await vehicle.set_window_heating(mode)
                    elif action == "setlock":
                        response = await vehicle.set_lock(mode,spin)
                    rc = await vehicle.update()
                    if action == "update":
                        response = rc
                    str_a = "{\"VIN\":\""+vin+"\",\"last_request\":\"" + action + "\",\"response\":\"" + str(response) + "\""
                    for instrument in vehicle.dashboard().instruments:
                        if instrument.name == "Position":
                            str_a +=   ",\"Pos_x\":\"" + str(instrument.str_state[0]) + "\",\"Pos_y\":\"" + str(instrument.str_state[1]) + "\",\"Pos_time\":\"" + str(instrument.str_state[2]) +  "\""
                        else: 
                            str_a +=   ",\"" + instrument.name + "\":\"" + str(instrument.str_state) + "\""                            
                    str_a += "}"
                    print(f"{str_a}")
        await connection.terminate()            

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())