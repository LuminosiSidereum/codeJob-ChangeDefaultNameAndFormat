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
        modelist: list[str] = ["0: Bild komplett neu benennen","1: Aufnahmedatum des umbenannten Bildes ändern","2: Name des umbenannten Bildes ändern"]
        for i in modelist:
            print(i)
        mode: str = input("Modus auswählen: ")
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

def picture_rename(date:str, name:str):
    """
    Renames all pictures in the current directory.
    Args:
    date (str): The date to be added to the file name.
    name (str): The name to be added to the file name.
    """
    count:int = 0
    for os_file in os.listdir():
        file: Path = Path(os_file) 
        if file.suffix in [".jpg", ".jpeg", ".png", ".gif",".tif",".tiff", ".mov", ".mp4", ".avi"]:
            new_file_name:str = name + "-" + date + "_" + str(count) + file.suffix
            file.rename(new_file_name)
            print(f"Umbenannt: {file} -> {new_file_name}")
            count = count + 1

def file_name_proof(nameblocks:list[str])->None:
    """
    Checks if the length of the nameblocks list is less than 2.
    Parameters:
    - nameblocks (list[str]): A list of file names
    Raises:
    - ValueError: If the length of nameblocks is less than 2
    Returns:
    - None
    """
    if len(nameblocks) < 2:
        raise ValueError("Die Dateien müssen vor dem Anpassen der Dateinamen korrekt benannt werden.")
            
def picture_edit_date(date:str):
    """
    Edits the date of all pictures in the current directory.
    Args:
    date (str): The new date to be added to the file name.
    """
    count:int = 0
    for os_file in os.listdir():
        file: Path = Path(os_file)
        if file.suffix in [".jpg", ".jpeg", ".png", ".gif","tiff"]:
            file_name, file_extension = file.stem, file.suffix
            nameblocks:list[str] = file_name.split("-")
            file_name_proof(nameblocks)
            nameblocks[-1] = date
            new_file_name:str = "-".join(nameblocks)+ "_" + str(count) + file_extension
            file.rename(new_file_name)
            print(f"Umbenannt: {file} -> {new_file_name}")
            count = count + 1

def picture_edit_name(name:str):
    """
    Edits the name of all pictures in the current directory.
    Args:
    name (str): The new name to be added to the file name.
    """
    for os_file in os.listdir():
        file: Path = Path(os_file)
        if file.suffix in [".jpg", ".jpeg", ".png", ".gif","tiff"]:
            file_name, file_extension = file.stem, file.suffix
            nameblocks:list[str] = file_name.split("-")
            file_name_proof(nameblocks)
            new_file_name: str = name + "-" + nameblocks[-1] + file_extension
            file.rename(new_file_name)
            print(f"Umbenannt: {file} -> {new_file_name}")

if __name__=="__main__":
    print("Achtung: Allle Bilder im Ordner erhalten den gleichen Namen und das gleiche Aufnahmedatum!")
    modus:str = mode_selection()

    # Set storage directory of the python skript as current diretory
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)
    
    if modus == "0":
        date:str = date_input()
        name:str = file_name_input()
        picture_rename(date, name)
    if modus == "1":
        date:str = date_input()
        try:
            picture_edit_date(date)
        except ValueError as e:
            print(e)
    if modus == "2":
        name:str = file_name_input()
        try:
            picture_edit_name(name)
        except ValueError as e:
            print(e)
    input("Drücken Sie Enter zum Beenden...")
