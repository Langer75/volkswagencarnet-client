# volkswagen-carnet-client
Commandline script to interact with [volkswagencarnet](https://github.com/robinostlund/volkswagencarnet) library

## Table of Contents
* [General Info](#general-information)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Project Status](#project-status)
 
## General Information
The volkswagencarnet library (by robinostlund) retrieves statistics about your Volkswagen from the Volkswagen Carnet online service. Also some actions can be requested via this library. This simple python script allows to use the library via command line and parameter lists. In that way it can be used in an easy way e.g. in nodered with the exec node.

## Setup
* Just install the [volkswagencarnet](https://github.com/robinostlund/volkswagencarnet) library
* copy/download the script and put it whereever you want to use it from the command line
* edit the credentials (user email, user password, SPIN) for your volkswagen account in the script

## Usage
start from command line: 
```
python3 carnet_cli.py <vin> <action> <action parameters>
e.g.
python3 carnet_cli.py <vin> update
python3 carnet_cli.py <vin> setrefresh
python3 carnet_cli.py <vin> setcharger <start/stop>
python3 carnet_cli.py <vin> setchargercurrent <#ampere>
python3 carnet_cli.py <vin> setclimatisationtemp <#temperature>
python3 carnet_cli.py <vin> setclimatisation <electric/auxiliary> <#temperature> <true/false>
python3 carnet_cli.py <vin> setwindowheating <start/stop>
python3 carnet_cli.py <vin> setlock <lock/unlock>"
```
(vin: Vehicle ID, true: without external power; false: with charging cable only)

## Features
Currently the following actions are implemented:
* update               - get all available data of the car identified by te VIN (from the VW backend only)
* setrefresh           - force the vehicle data update directly from the car
* setcharger           - start or stop charging
* setchargercurrent    - set the chargingcurrent
* setclimatisationtemp - set the targettemperature for climatisation
* setclimatisation     - start or stop climatisation (for auxiliary heater SPIN needed)
* setwindowheating     - start or stop the window heating
* setlock              - lock or unlock your car (only when activated, SPIN needed)

## Acknowledgements
- This project was inspired by [volkswagencarnet](https://github.com/robinostlund/volkswagencarnet) library
- Many thanks to [robinostlund](https://github.com/robinostlund) and all people that contribute to the library
  
## Project Status
It was developed to use the [volkswagencarnet](https://github.com/robinostlund/volkswagencarnet) library in nodered. All basic (from my point of view) functions are implemented. However I have tested it only with an eGolf. Feel free to use it or improve it for combustion cars or other functionalities available in the volkswagencarnet library. No licence, public domain, no guarantees.  
  
