"""Kursprüfung für Lektion 2: Tetrominos, aktiver Stein, 7-Bag, Vorschau.

Prüft ausschließlich den Stand von Lektion 2.
"""

from course_checks import (
    FEHLER,
    NICHT_PRUEFBAR,
    OK,
    Ergebnis,
    datei_enthaelt,
    datei_pfad,
    datei_vorhanden,
    irgendeine_datei_enthaelt,
    modul_laden,
)

ERWARTETE_ARTEN = {"I", "O", "T", "S", "Z", "J", "L"}


def _lade_tetromino():
    if not datei_pfad("tetromino").is_file():
        return None, Ergebnis(NICHT_PRUEFBAR, "`tetromino.py` fehlt noch.")
    modul, fehler = modul_laden("tetromino")
    if fehler:
        return None, Ergebnis(FEHLER, fehler)
    return modul, None


def check_tetromino_vorhanden():
    return datei_vorhanden("tetromino")


def check_shapes_woerterbuch():
    modul, fehler = _lade_tetromino()
    if fehler:
        return fehler
    shapes = getattr(modul, "SHAPES", None)
    if not isinstance(shapes, dict):
        return Ergebnis(
            FEHLER, "`SHAPES` fehlt oder ist kein Wörterbuch."
        )
    if set(shapes.keys()) == ERWARTETE_ARTEN:
        return Ergebnis(
            OK, "`SHAPES` enthält genau die sieben Arten I, O, T, S, Z, J, L."
        )
    return Ergebnis(
        FEHLER,
        f"`SHAPES` enthält {sorted(shapes.keys())} statt der sieben Arten.",
    )


def check_tetromino_klasse():
    modul, fehler = _lade_tetromino()
    if fehler:
        return fehler
    klasse = getattr(modul, "Tetromino", None)
    if klasse is None:
        return Ergebnis(FEHLER, "Klasse `Tetromino` wurde nicht gefunden.")
    try:
        for art in ERWARTETE_ARTEN:
            stein = klasse(art)
            if len(stein.cells()) != 4:
                return Ergebnis(
                    FEHLER, f"Der {art}-Stein hat nicht 4 Zellen."
                )
        return Ergebnis(OK, "Jede Art lässt sich erzeugen und hat 4 Zellen.")
    except Exception as fehler:
        return Ergebnis(
            FEHLER, f"Fehler beim Erzeugen der Steine: {fehler}"
        )


def check_farben_eindeutig():
    modul, fehler = _lade_tetromino()
    if fehler:
        return fehler
    klasse = getattr(modul, "Tetromino", None)
    if klasse is None:
        return Ergebnis(FEHLER, "Klasse `Tetromino` wurde nicht gefunden.")
    try:
        farben = {klasse(art).color for art in ERWARTETE_ARTEN}
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Lesen der Farben: {fehler}")
    if len(farben) == 7:
        return Ergebnis(OK, "Alle sieben Arten haben verschiedene Farben.")
    return Ergebnis(
        FEHLER, "Die sieben Arten haben nicht sieben verschiedene Farben."
    )


def check_stein_wird_benutzt():
    return datei_enthaelt("main", ["Tetromino", "tetromino"], mindestens=1)


def check_seven_bag():
    return irgendeine_datei_enthaelt(
        ["main", "game"], ["shuffle", "sample"], mindestens=1
    )


def check_vorschau():
    return datei_enthaelt(
        "main", ["next", "vorschau", "naechst"], mindestens=1
    )


CHECKS = [
    ("Datei tetromino.py ist vorhanden", check_tetromino_vorhanden),
    ("SHAPES enthält alle sieben Arten", check_shapes_woerterbuch),
    ("Klasse Tetromino mit 4 Zellen je Art", check_tetromino_klasse),
    ("Sieben verschiedene Farben", check_farben_eindeutig),
    ("main.py erzeugt einen Stein", check_stein_wird_benutzt),
    ("7-Bag (faire Zufallsreihenfolge)", check_seven_bag),
    ("Vorschau des nächsten Steins", check_vorschau),
]
