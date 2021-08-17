# Ender3MarlinUpdate
## A Repo containing the correct files and documentation for getting Marlin firmware on a Creality Ender 3

This article is heavily inspired by https://howchoo.com/ender3/ender-3-bootloader-firmware-update-marlin
Images also from https://howchoo.com/ender3/ender-3-bootloader-firmware-update-marlin

### Burning a bootloader
In order to write Marlin to an Ender 3, we first must burn a bootloader to the mainboard. This can be done with an Arduino Uno, Mega (or knockoff)

You will need:
* An Arduino Uno or Mega
* 5x Female to female dupont jumper wires
* 1x Female to male dupont jumper wire
* A USB type B cable for your arduino
* A USB mini B cable for plugging into your printer

#### Step 1:
Download and install the Arduino IDE from https://www.arduino.cc/en/software.
#### Step 2:
Connect your Arduino to your computer with a USB type B cable.
#### Step 3:
Open the ArduinoISP sketch from the examples folder (File > Examples > 11.ArduinoISP > Arduino ISP)
#### Step 4:
Select your Arduino. Go to (Tools > Board) and select either Arduino Uno or Mega depending on which you are using.
Next, go to (Tools > Port) and select the port your arduino is on
#### Step 5:
Click upload! Your Arduino is now ready for ISP!

#### Step 6:
Powerdown your Ender 3 and use a hex key to remove the bottom panel to expose the mainboard's ICSP header

![Header pin connections](https://howchoo.com/media/mm/iy/md/ender-3-arduino-firmware-pinout.jpeg?height=900&auto=webp&quality=70)

#### Step 7:
Connect your Arduino to the Ender mainboard using 5 female to female jumper wires
* SCK to SCK
* MISO to MISO
* GND to GND
* MOSI to MOSI
* 5V to 5V
Use a female to male jumper to connect RESET to Arduino pin ~10

#### Step 8:
Install the U8glib libary. Open the libraries manager, search U8glib and install the latest version.

![](https://howchoo.com/media/yj/jm/yj/installing-the-u8glib-library.png?width=1440&auto=webp&quality=70)

#### Step 9:
Add the Sanguino board to the Arduino IDE. Open Arduino Preferences and paste the following under Additional Boards Manager URLs:

https://raw.githubusercontent.com/Lauszus/Sanguino/master/package_lauszus_sanguino_index.json

![](https://howchoo.com/media/nd/vl/yj/adding-a-custom-board-to-arduino-ide.png?width=900&auto=webp&quality=70)

Open boards manager, search for and install the "Sanguino" board.

#### Step 10:
Burn the bootloader! Under Tools, set: 
* board to "Sanguino"
* processor to "ATmega1248 or ATmega1248P (16MHz)"
* programmer to "Arduino as ISP".

With that complete, under Tools, click burn bootloader!

### Uploading Marlin!

Now that we have a bootloader on the Ender mainboard, we can write Marlin to it.

#### Step 1:
Disconnect all jumper wires from your Ender and replace the cover.

#### Step 2:
Plug a USB mini B connector into the front of your printer.

#### Step 3:
Download and extract the Marlin .Zip file from this repository

#### Step 4:
Locate and open the 

