# volkswagen-carnet-client
Commandline script to interact with volkswagencarnet library

## Table of Contents
* [General Info](#general-information)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
 
## General Information
The volkswagencarnet library (by robinostlund) retrieves statistics about your Volkswagen from the Volkswagen Carnet online service. Also some actions can be requested via this library. This simple python script allows to use the library via command line and parameter lists. In that way it can be used in an easy way e.g. in nodered with the exec node.

## Setup
* Just install the [volkswagencarnet](https://github.com/robinostlund/volkswagencarnet) library by robinostlund
* copy/download the script and put it whereever you want to use it from the command line

## Usage
start from th command line: 
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

## Acknowledgements
- This project was inspired by [volkswagencarnet](https://github.com/robinostlund/volkswagencarnet)
- Many thanks to [robinostlund](https://github.com/robinostlund) and all people that have contribute to the volkswagencarnet library
  
## Project Status
It was developed to use the python library in nodered. All basic (from my point of view) functions are implemented. However I have tested it with an eGolf only. Feel free to use it or improve it for combustion cars or other functionalities available in the volkswagencarnet library. No licence, public domain, no guarantees.  
  
