# Voron 3D Printer

<!-- There is no prescribed structure, but here is a suggestion: -->

## Safety

### PPE
* None necessary during ordinary use.

### Risks
* Burn from heated bed or hot-end
* Fire started due to heated bed or hot-end
* Body part or clothing caught in printer mechanism
* Hazardous gasses

<!-- Usually, all of the control measures in the risk assessment should be mentioned here -->

## Startup checks
* Filament loaded is expected type
* Bed and hotend can move freely
* Bed is clean and clear
* Correct nozzle is installed and enabled in software
* Air extraction is enabled if necessary

## Usage

### Starting the machine
* The printer should be left powered on and passive. If it is not, check with tools@edinburghhacklab.com that it can be powered on safely.
* Wipe the bed down with isopropyl alcohol and blue roll. Do not touch the bed after this process has been completed.
* Upload your file to the web interface.
* If changing nozzle:
    * unload filament
    * unscrew and remove nozzle
    * load new nozzle
    * load filament
    * edit the `toolhead.cfg` file to enable the correct nozzle
* Observe the printer begin the print. The first layer should always be watched in case of defects or malfunction.
**TODO: how do we manage ventilation?**

### Stopping the machine
* The printer should stop and cool normally when the print is finished.
* If the print must be cancelled, do so using the web interface or the menu. Only cancel your own prints, or the prints of others with their express permission.

<!-- incl estops if necessary -->

### General
* Keep your hands clear of the heated bed and hotend while prints are in progress to avoid pinching and burns.
* Be aware of the door state. In general:
    * PLA, matte PLA, PLA+: open
    * TPU: open
    * PETG: either
    * ABS: closed
    * ASA: closed
    * PA: closed

### Materials
* Only use the following materials from reputable sellers:
    * PLA (including matte PLA and PLA+)
    * PETG
    * TPU
    * ABS (with external ventilation)
    * ASA (with external ventilation)
    * PA (with external ventilation)
* Do not use materials if:
    * they have inclusions, such as Glow-In-The-Dark, carbon fibre (CF), or glass fibre (GF)
    * they have previously caused clogs or jams in printers in the lab
* If in doubt, ask.

### Cleaning up
* Remove your print and any skirt or purge lines from the bed.

## Maintenance

### General
* Contact tools@edinburghhacklab.com if you encounter any of the following:
    * repeated build failures with the same file, filament and failure mode
    * loud screeching or grinding sounds

## Other
