# Bild- und Videodateien umbenennen und konvertieren

## Funktionsweise
Dieses Skript ermöglicht das automatische Umbenennen und Bearbeiten von Bild- und Videodateien im aktuellen Verzeichnis. Es bietet folgende Funktionen:
- **Modus 0:** Bilder/Videos erhalten einen neuen Namen nach dem Muster `<Projektname>-<Datum>_<Nummer>`.
- **Modus 1:** Das Aufnahmedatum von bereits umbenannten Bildern/Videos wird angepasst.
- **Modus 2:** Der Name von bereits umbenannten Bildern/Videos wird geändert.
- **Modus 3:** `.HEIC`-Dateien werden in das `.TIFF`-Format konvertiert.

## Nutzung des Skripts

### Eingabedaten
- Bilder und Videos müssen sich im selben Ordner befinden wie das Skript.
- Unterstützte Bildformate: `.jpg`, `.jpeg`, `.png`, `.gif`, `.tif`, `.tiff`, `.heic`
- Unterstützte Videoformate: `.mov`, `.mp4`, `.avi`
- `.HEIC`-Dateien können in `.TIFF` konvertiert werden.

### Ausführung
1. Das Skript starten.
2. Einen Modus auswählen:
   - `0` - Alle Dateien umbenennen (Eingabe von Datum und Projektname erforderlich).
   - `1` - Aufnahmedatum bestehender Dateien ändern (Datumseingabe erforderlich).
   - `2` - Namen bestehender Dateien ändern (Projektname erforderlich).
   - `3` - `.HEIC`-Dateien in `.TIFF` umwandeln.
3. Die geforderten Eingaben tätigen (Datum oder Projektname).
4. Das Skript führt die gewählte Aktion automatisch durch.

### Ausgabe
- Die Dateien werden entsprechend umbenannt oder konvertiert.
- `.HEIC`-Dateien werden in das `.TIFF`-Format umgewandelt und die Originaldateien in den Ordner `Orginaldateien (HEIC)` verschoben.
- Konsolenausgabe mit den jeweiligen Änderungen.

---

Falls `pillow_heif` nicht installiert ist, kann es mit folgendem Befehl nachinstalliert werden:
python -m pip install pillow-heif

Alternativ kann `requirements.bat` verwendet werden.
