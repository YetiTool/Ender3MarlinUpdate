import glob
import os

complete_symbol = "-"

replacement_code = "\n;/////////////////////////////////////////////////////////////////////BENJI \n;Move Z and home \nG91 \nG0 Z20 \nG90 \nM300 P500 ; Beep for 500ms \nM0 Is switch loaded? \nG28 \n \n;Level bed \nG29 L25 R195 F25 B195; Perform ABL on grid 45mm inside limits \nG0 X0 Y0 Z10 S8000 \nM500; Save bed levelling to EEPROM \n \n;Eject switch \nG0 Z10 S8000 \nG0 X0 Y30 S8000 \nG0 Z-4 S8000 \nG0 Y30 S5000 \nG1 X65 S8000 \nG0 Z20 S5000 \n \n;/////////////////////////////////////////////////////////////////////BENJI \n \n"
#replacement_code = '\n Hello! \n'

def import_filenames(path):
    filenames = (glob.glob(path + "*.gcode"))
    return filenames
        
def update_gcode(file_name):
    skipped = False
    if (file_name.split(path)[1])[0] != complete_symbol:
        with open(file_name, 'r+') as file:
            content = file.readlines()  # gcode as a list where each element is a line
            line_number = 0
            complete = False
            for line in content:
                line_number += 1            
                if "G28 ; Home all axes" in line and not(complete):
                    complete = True
                    print("File:", file_name)
                    print("G28 Found!")
                    print("line number: ", line_number)
                    content[line_number-1] = replacement_code
                    file = open(file_name, "w")
                    file.writelines(content)
                    file.close()
        print("Done. \n")
    else:
        print("Skipped", file_name)
        skipped = True
    return skipped

path = input("Enter directory (e.g. D:/): ")
if path == "":
    path = "D:/"

filenames = import_filenames(path)

for file in filenames:
    skipped = update_gcode(file)
    if not(skipped):
        old_file_name = str(file)
        new_file_name = old_file_name.split("/")
        new_file_name = new_file_name[0] + "/" + complete_symbol + new_file_name[1]
        os.rename(old_file_name, new_file_name)
        print(new_file_name, "Renamed")
print("SD Complete!")


