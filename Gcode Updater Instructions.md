# Using Gcode Updater.py to modify .GCODE files
## Step 1: Download and install python (3.9 or later)
Visit https://www.python.org/downloads/ and follow the given installation instructions.
## Step 2: Download Gcode Updater.py
Download Gcode Updater.py from this repository and save it to an accessable location. (e.g. Desktop)
## Step 3: Locate your file path
If using an SD card, only the drive letter is needed. (e.g D:/ or E:/) if the files are burried in a folder, find the folder's path.
## Step 4: Running the program
Navigate to your downloaded copy of Gcode updater.py and run it.

You will be asked for the path of your folder. By default, this is D:/. Press Enter to continue.

The program will now proceede to scan your folder for any .gcode files. 

The program will ignore any files begining with "-" (hyphen). This is beacuse a hyphen is used as an inidicator of completion. 

For each file, the program will locate the first line containing G28 ; "Home all axes" and replace it with the predefined "replacement_gcode" which includes the bedleveling procedure.

Once a file is complete, the program will ammend a "-" (hyphen) onto the start of the file name as confirmation that the file has been editted.

Once all found .gcode files have been updated, the program will finish and close.

Running the program for a second time will ensure any previously missed .gcode files are updated.

## Done!
