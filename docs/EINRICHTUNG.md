# Einrichtung

So richtest du dein System für den Blockfall-Kurs ein. Der Ablauf ist
auf allen Betriebssystemen gleich:

1. Python prüfen und installieren (mindestens 3.10)
2. Repository herunterladen
3. virtuelle Umgebung erstellen
4. virtuelle Umgebung aktivieren
5. Abhängigkeiten installieren
6. pygame prüfen
7. erste Kursprüfung starten

Der Kurs braucht **keine Git-Kenntnisse**. Es gibt keine Branches und
keine Befehle, die du außerhalb dieser Anleitung ausführen musst.

## Python prüfen

Öffne ein Terminal und gib ein:

```text
python --version
```

Zeigt der Befehl nichts oder eine Version **unter 3.10**, installiere
Python von <https://www.python.org/>. Setze bei der Installation auf
Windows unbedingt den Haken „Add Python to PATH".

Auf manchen Systemen heißt der Befehl `python3` oder `py`. Probiere
notfalls:

```text
py --version
python3 --version
```

## Repository herunterladen

Ohne Git: Lade das Repository auf GitHub als ZIP herunter
(„Code" → „Download ZIP") und entpacke es in einen Ordner deiner Wahl.

Mit Git (optional):

```text
git clone <URL-des-Repositories>
```

Wechsle anschließend in den entpackten Ordner, z. B.:

```text
cd LearnPythonWithTetris
```

## Virtuelle Umgebung

### Windows (PowerShell)

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Falls PowerShell die Ausführung verweigert, starte PowerShell einmal als
Administrator und führe `Set-ExecutionPolicy RemoteSigned` aus — oder
aktiviere so:

```text
.venv\Scripts\activate.bat
```

### macOS und Linux

```text
python3 -m venv .venv
source .venv/bin/activate
```

Erkennungszeichen für eine aktive Umgebung: Der Prompt zeigt `(.venv)`.

## Abhängigkeiten installieren

```text
python -m pip install -r requirements.txt
```

Das installiert pygame.

## pygame prüfen

```text
python -c "import pygame; print(pygame.ver)"
```

Es sollte eine Versionsnummer erscheinen, ohne Fehlermeldung.

## Erste Kursprüfung starten

```text
python tools/check_environment.py
```

Meldet die Prüfung „Alles bereit!", bist du startklar. Dann geht es mit
dem Prompt `00-vorbereitung.prompt.md` in `.github/prompts/` weiter.

## Tipp: Umgebung täglich aktivieren

Die virtuelle Umgebung ist pro Terminal-Sitzung aktiv. Wenn du den Kurs
fortsetzt, öffne das Terminal im Repository-Ordner und aktiviere die
Umgebung erneut (Befehle oben).
