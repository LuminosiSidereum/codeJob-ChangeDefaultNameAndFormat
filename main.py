import os
import sys
from pathlib import Path

def mode_selection() -> str:
    """
    Prompts the user to select a mode.
    Returns:
    str: The selected mode.
    """
    mode_selection: bool = True
    while mode_selection:
        mode: str = input("Modus auswählen: 0 um Bild umbenennen; 1 um Aufnahmedatum des umbenannten Bildes ändern; 2 um Name des umbenannten Bildes zu ändern: ")
        if mode in ["0", "1","2"]:
            mode_selection = False
        else:
            print("Ungültige Eingabe!")
    return mode

def date_input() -> str:
    """
    Prompts the user to enter a date.
    Returns:
    str: The entered date.
    """
    valid_date_input: bool = False
    while not valid_date_input:
        date: str = input("Aufnahmedatum der Bilder eingeben (Format: JJMMTT): ")
        if len(date) == 6 and date.isdigit():
            valid_date_input = True
        else:
            print("Ungültige Eingabe!")
    return date

def file_name_input() -> str:
    """
    Prompts the user to enter a file name.
    Returns:
    str: The entered file name.
    """
    valid_file_name_input: bool = False
    while not valid_file_name_input:
        name: str = input("Projektidentifizierung eingeben: ")
        if len(name) > 0:
            valid_file_name_input = True
        else:
            print("Ungültige Eingabe!")
    return name

if __name__=="__main__":
    print("Achtung: Allle Bilder im Ordner erhalten den gleichen Namen und das gleiche Aufnahmedatum!")
    modus:str = mode_selection()
    date:str = date_input()
    name:str = file_name_input()

    # Set storage directory of the python skript as current diretory
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)
    
    if modus == "0":
        picture_rename(date, name)
    if modus == "1":
        picture_edit_date(date)
    if modus == "2":
        picture_edit_name(name)
    
    input("Drücken Sie Enter zum Beenden...")
