"""Gemeinsame Hilfen für die Kursprüfungen.

Wichtige Regeln:
- Die Kursprüfungen lesen und führen `lernprojekt/` nur aus.
- Sie verändern dort keine Dateien (auch keine `__pycache__`-Ordner).
- Sie greifen niemals auf `referenzspiel/` zu.
"""

import importlib.util
import os
import sys
from dataclasses import dataclass
from pathlib import Path

# Keine __pycache__-Dateien im Lernprojekt erzeugen.
sys.dont_write_bytecode = True

# Falls Code der Lernenden ein pygame-Fenster öffnet, bleibt es unsichtbar.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

REPO_ROOT = Path(__file__).resolve().parent.parent
LEARNPROJECT = REPO_ROOT / "lernprojekt"

if str(LEARNPROJECT) not in sys.path:
    sys.path.insert(0, str(LEARNPROJECT))

# Statuswerte einer einzelnen Prüfung
OK = "OK"
FEHLER = "FEHLER"
NICHT_PRUEFBAR = "NICHT_PRUEFBAR"


@dataclass
class Ergebnis:
    """Das Ergebnis einer einzelnen Prüfung."""
    status: str
    meldung: str


def fuehre_aus(funktion):
    """Führt eine Prüffunktion aus und fängt unerwartete Fehler ab."""
    try:
        ergebnis = funktion()
        if isinstance(ergebnis, Ergebnis):
            return ergebnis
        return Ergebnis(FEHLER, "Die Prüffunktion hat kein Ergebnis geliefert.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"{type(fehler).__name__}: {fehler}")


def datei_pfad(name):
    """Pfad zu einer Python-Datei im Lernprojekt."""
    return LEARNPROJECT / f"{name}.py"


def datei_vorhanden(name):
    if datei_pfad(name).is_file():
        return Ergebnis(OK, f"`{name}.py` ist vorhanden.")
    return Ergebnis(NICHT_PRUEFBAR, f"`{name}.py` fehlt noch.")


def datei_enthaelt(name, begriffe, mindestens=None):
    """Prüft, ob eine Datei die Begriffe enthält (Groß/Klein egal)."""
    pfad = datei_pfad(name)
    if not pfad.is_file():
        return Ergebnis(NICHT_PRUEFBAR, f"`{name}.py` fehlt noch.")
    text = pfad.read_text(encoding="utf-8", errors="replace").lower()
    treffer = [begriff for begriff in begriffe if begriff.lower() in text]
    if mindestens is None:
        mindestens = len(begriffe)
    if len(treffer) >= mindestens:
        return Ergebnis(OK, f"In `{name}.py` gefunden: {', '.join(treffer)}.")
    fehlend = [begriff for begriff in begriffe if begriff.lower() not in text]
    return Ergebnis(
        FEHLER, f"In `{name}.py` nicht gefunden: {', '.join(fehlend)}."
    )


def irgendeine_datei_enthaelt(names, begriffe, mindestens=1):
    """Prüft, ob mindestens eine der Dateien die Begriffe enthält."""
    for name in names:
        ergebnis = datei_enthaelt(name, begriffe, mindestens)
        if ergebnis.status == OK:
            return ergebnis
    fehlende = [name for name in names if not datei_pfad(name).is_file()]
    if len(fehlende) == len(names):
        return Ergebnis(
            NICHT_PRUEFBAR,
            f"Keine der Dateien {', '.join(names)} ist vorhanden.",
        )
    return Ergebnis(
        FEHLER,
        f"In keiner der Dateien gefunden: {', '.join(begriffe)}.",
    )


def modul_laden(name):
    """Lädt ein Modul aus dem Lernprojekt.

    Gibt (Modul, Fehlertext) zurück. Fehlt die Datei, ist das Modul None
    und der Fehlertext erklärt das — der Aufrufer entscheidet dann selbst,
    ob die Prüfung FEHLER oder NICHT_PRUEFBAR meldet.
    """
    pfad = datei_pfad(name)
    if not pfad.is_file():
        return None, f"`{name}.py` fehlt noch."
    try:
        modulname = f"lernprojekt_{name}"
        spec = importlib.util.spec_from_file_location(modulname, pfad)
        modul = importlib.util.module_from_spec(spec)
        sys.modules[modulname] = modul
        spec.loader.exec_module(modul)
        return modul, ""
    except Exception as fehler:
        return (
            None,
            f"`{name}.py` ließ sich nicht laden: "
            f"{type(fehler).__name__}: {fehler}",
        )
