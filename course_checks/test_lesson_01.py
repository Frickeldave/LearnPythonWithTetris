"""Kursprüfung für Lektion 1: Fenster, Event-Loop und Spielfeld.

Prüft ausschließlich den Stand von Lektion 1. Jede Prüffunktion gibt
ein Ergebnis mit Status OK, FEHLER oder NICHT_PRUEFBAR zurück.
"""

from course_checks import (
    FEHLER,
    NICHT_PRUEFBAR,
    Ergebnis,
    datei_enthaelt,
    datei_pfad,
    datei_vorhanden,
    modul_laden,
)


def check_main_vorhanden():
    return datei_vorhanden("main")


def check_pygame_initialisiert():
    return datei_enthaelt("main", ["pygame.init"])


def check_fenster_geoeffnet():
    return datei_enthaelt("main", ["set_mode", "set_caption"])


def check_event_loop():
    return datei_enthaelt(
        "main", ["pygame.QUIT", "pygame.event.get"], mindestens=1
    )


def check_zeichnung():
    return datei_enthaelt(
        "main",
        ["pygame.display.flip", "pygame.display.update", "pygame.draw"],
        mindestens=2,
    )


def check_settings_vorhanden():
    return datei_vorhanden("settings")


def check_spielfeldgroesse():
    if not datei_pfad("settings").is_file():
        return Ergebnis(NICHT_PRUEFBAR, "`settings.py` fehlt noch.")
    settings, fehler = modul_laden("settings")
    if fehler:
        return Ergebnis(FEHLER, fehler)
    breite = getattr(settings, "BOARD_WIDTH", None)
    hoehe = getattr(settings, "BOARD_HEIGHT", None)
    if breite == 10 and hoehe == 20:
        return Ergebnis(
            OK, "`BOARD_WIDTH` = 10 und `BOARD_HEIGHT` = 20 gefunden."
        )
    return Ergebnis(
        FEHLER, "`BOARD_WIDTH` muss 10 und `BOARD_HEIGHT` muss 20 sein."
    )


CHECKS = [
    ("Datei main.py ist vorhanden", check_main_vorhanden),
    ("pygame wird initialisiert", check_pygame_initialisiert),
    ("Ein Fenster wird geöffnet", check_fenster_geoeffnet),
    ("Eine Event-Schleife läuft", check_event_loop),
    ("Es wird sichtbar gezeichnet", check_zeichnung),
    ("Datei settings.py ist vorhanden", check_settings_vorhanden),
    ("Spielfeldgröße 10 × 20", check_spielfeldgroesse),
]
