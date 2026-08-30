"""Kursprüfung für Lektion 3: Bewegung, Grenzen, belegte Zellen.

Prüft ausschließlich den Stand von Lektion 3.
"""

from course_checks import (
    FEHLER,
    NICHT_PRUEFBAR,
    OK,
    Ergebnis,
    datei_enthaelt,
    datei_pfad,
    datei_vorhanden,
    modul_laden,
)


def _neues_brett():
    """Lädt board.py und erzeugt ein Board(10, 20)."""
    if not datei_pfad("board").is_file():
        return None, Ergebnis(NICHT_PRUEFBAR, "`board.py` fehlt noch.")
    modul, fehler = modul_laden("board")
    if fehler:
        return None, Ergebnis(FEHLER, fehler)
    klasse = getattr(modul, "Board", None)
    if klasse is None:
        return None, Ergebnis(FEHLER, "Klasse `Board` wurde nicht gefunden.")
    try:
        return klasse(10, 20), None
    except Exception as fehler:
        return None, Ergebnis(
            FEHLER, f"`Board(10, 20)` ließ sich nicht erzeugen: {fehler}"
        )


def check_board_vorhanden():
    return datei_vorhanden("board")


def check_board_klasse():
    brett, fehler = _neues_brett()
    if fehler:
        return fehler
    breite = getattr(brett, "width", None)
    hoehe = getattr(brett, "height", None)
    if breite == 10 and hoehe == 20:
        return Ergebnis(OK, "`Board(10, 20)` erzeugt ein 10 × 20-Feld.")
    return Ergebnis(
        FEHLER, f"Das Feld hat width={breite} und height={hoehe} statt 10 und 20."
    )


def check_is_inside():
    brett, fehler = _neues_brett()
    if fehler:
        return fehler
    try:
        ok = (
            brett.is_inside(0, 0) is True
            and brett.is_inside(9, 19) is True
            and brett.is_inside(-1, 0) is False
            and brett.is_inside(10, 0) is False
            and brett.is_inside(0, 20) is False
        )
    except Exception as fehler:
        return Ergebnis(FEHLER, f"`is_inside` brach ab: {fehler}")
    if ok:
        return Ergebnis(OK, "`is_inside` erkennt Feldgrenzen korrekt.")
    return Ergebnis(FEHLER, "`is_inside` beurteilt die Grenzen nicht korrekt.")


def check_cell_is_free():
    brett, fehler = _neues_brett()
    if fehler:
        return fehler
    try:
        ok = (
            brett.cell_is_free(5, 5) is True
            and brett.cell_is_free(0, -1) is True
            and brett.cell_is_free(-1, 0) is False
            and brett.cell_is_free(10, 0) is False
        )
    except Exception as fehler:
        return Ergebnis(FEHLER, f"`cell_is_free` brach ab: {fehler}")
    if ok:
        return Ergebnis(
            OK,
            "`cell_is_free` meldet freie und belegte Zellen korrekt "
            "(über dem Feld ist frei).",
        )
    return Ergebnis(
        FEHLER, "`cell_is_free` meldet die Zellen nicht korrekt."
    )


def check_can_place_und_lock():
    brett, fehler = _neues_brett()
    if fehler:
        return fehler
    zellen = [(0, 0), (1, 0)]
    farbe = (1, 2, 3)
    try:
        if not brett.can_place(zellen, 0, 0):
            return Ergebnis(
                FEHLER, "Auf einem leeren Feld muss `can_place` True liefern."
            )
        brett.lock(zellen, 0, 0, farbe)
        if brett.can_place(zellen, 0, 0):
            return Ergebnis(
                FEHLER, "Nach `lock` müssen die Zellen belegt sein."
            )
        if not brett.can_place(zellen, 0, 1):
            return Ergebnis(
                FEHLER, "Die Zellen darunter müssen frei bleiben."
            )
        gitter = getattr(brett, "grid", None)
        if gitter is None or gitter[0][0] != farbe:
            return Ergebnis(
                FEHLER, "Nach `lock` speichert das Gitter die Farbe nicht."
            )
        return Ergebnis(OK, "`can_place` und `lock` arbeiten korrekt.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_bewegungstasten():
    return datei_enthaelt("main", ["K_LEFT", "K_RIGHT"])


CHECKS = [
    ("Datei board.py ist vorhanden", check_board_vorhanden),
    ("Klasse Board mit 10 × 20 Feldern", check_board_klasse),
    ("Feldgrenzen werden erkannt (is_inside)", check_is_inside),
    ("Freie Zellen werden erkannt (cell_is_free)", check_cell_is_free),
    ("Belegte Zellen blockieren (can_place, lock)", check_can_place_und_lock),
    ("Bewegung über Pfeiltasten", check_bewegungstasten),
]
