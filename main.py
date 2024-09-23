import os
import sys
from pathlib import Path

accepted_file_extensions: dict[str,list[str]] ={
    "picture":[".jpg", ".jpeg", ".png", ".gif",".tif",".tiff",".heic"],
    "movies": [".mov", ".mp4", ".avi"]
}

forbidden_chars: list[str] = ["/", "\\", ":", "*", "?", "<", ">", "|", ".", "!", ";","#"]

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
        mode = mode.strip()
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
        date = date.strip()
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
        name = name.strip()
        if len(name) == 0 or any([char in name for char in forbidden_chars]):
            print("Ungültige Eingabe!")
            print("Verwenden Sie keine der folgenden Zeichen: / \\ : * ? < > | . ! ; # und reservierte Dateinamen")
        else:
            valid_file_name_input = True
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
        if file.suffix.lower() in accepted_file_extensions["picture"] or file.suffix.lower() in accepted_file_extensions["movies"]:
            new_file_name:str = name + "-" + date + "_" + str(count) + file.suffix.lower()
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
        if file.suffix.lower() in accepted_file_extensions["picture"] or file.suffix.lower() in accepted_file_extensions["movies"]:
            file_name, file_extension = file.stem, file.suffix.lower()
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
        if file.suffix.lower() in accepted_file_extensions["picture"] or file.suffix.lower() in accepted_file_extensions["movies"]:
            file_name, file_extension = file.stem, file.suffix.lower()
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
        date_0:str = date_input()
        name_0:str = file_name_input()
        picture_rename(date_0, name_0)
    if modus == "1":
        date_1:str = date_input()
        try:
            picture_edit_date(date_1)
        except ValueError as e:
            print(e)
    if modus == "2":
        name_2:str = file_name_input()
        try:
            picture_edit_name(name_2)
        except ValueError as e:
            print(e)
    input("Drücken Sie Enter zum Beenden...")
