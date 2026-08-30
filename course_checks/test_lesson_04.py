"""Kursprüfung für Lektion 4: Schwerkraft, Fixieren, Rotation, Wall Kick.

Prüft ausschließlich den Stand von Lektion 4.
"""

from course_checks import (
    FEHLER,
    NICHT_PRUEFBAR,
    OK,
    Ergebnis,
    datei_pfad,
    datei_vorhanden,
    modul_laden,
)


def _lade_game():
    if not datei_pfad("game").is_file():
        return None, Ergebnis(NICHT_PRUEFBAR, "`game.py` fehlt noch.")
    modul, fehler = modul_laden("game")
    if fehler:
        return None, Ergebnis(FEHLER, fehler)
    return modul, None


def _neues_spiel():
    modul, fehler = _lade_game()
    if fehler:
        return None, fehler
    klasse = getattr(modul, "Game", None)
    if klasse is None:
        return None, Ergebnis(FEHLER, "Klasse `Game` wurde nicht gefunden.")
    try:
        return klasse(), None
    except Exception as fehler:
        return None, Ergebnis(
            FEHLER, f"`Game()` ließ sich nicht erzeugen: {fehler}"
        )


def check_game_vorhanden():
    return datei_vorhanden("game")


def check_game_klasse():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    return Ergebnis(OK, "`Game()` lässt sich erzeugen.")


def check_schwerkraft_und_fixieren():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        brett = spiel.board
        for _ in range(60):
            spiel.tick()
        belegt = any(
            zelle is not None for reihe in brett.grid for zelle in reihe
        )
        if not belegt:
            return Ergebnis(
                FEHLER, "Nach 60 `tick()`-Aufrufen sollte ein Stein fixiert sein."
            )
        if spiel.active_piece is None:
            return Ergebnis(
                FEHLER, "Nach dem Fixieren sollte ein neuer Stein aktiv sein."
            )
        return Ergebnis(OK, "Schwerkraft und Fixieren funktionieren.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_bewegung_im_spiel():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        start_x = spiel.piece_x
        spiel.move(-1)
        if spiel.piece_x != start_x - 1:
            return Ergebnis(
                FEHLER, "`move(-1)` verschiebt den Stein nicht um eine Spalte."
            )
        return Ergebnis(OK, "`move(-1)` verschiebt den Stein nach links.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_rotation_tetromino():
    if not datei_pfad("tetromino").is_file():
        return Ergebnis(
            NICHT_PRUEFBAR, "Für die Rotationsprüfung fehlt `tetromino.py`."
        )
    modul, fehler = modul_laden("tetromino")
    if fehler:
        return Ergebnis(FEHLER, fehler)
    klasse = getattr(modul, "Tetromino", None)
    if klasse is None:
        return Ergebnis(FEHLER, "Klasse `Tetromino` wurde nicht gefunden.")
    try:
        stein = klasse("T")
        vorher = sorted(stein.cells())
        stein.rotate_cw()
        if sorted(stein.cells()) == vorher:
            return Ergebnis(
                FEHLER, "`rotate_cw` verändert die Form des T-Steins nicht."
            )
        stein.rotate_ccw()
        if sorted(stein.cells()) != vorher:
            return Ergebnis(
                FEHLER, "`rotate_ccw` hebt die Drehung nicht wieder auf."
            )
        return Ergebnis(OK, "Rotation in beide Richtungen funktioniert.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_wall_kick():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        for _ in range(10):
            spiel.move(-1)
        spiel.rotate_cw()
        min_x = min(x for x, _ in spiel.active_piece.cells())
        if spiel.piece_x + min_x < 0:
            return Ergebnis(
                FEHLER,
                "Nach der Drehung ragt der Stein links aus dem Feld — "
                "der Wall Kick fehlt oder greift nicht.",
            )
        return Ergebnis(OK, "Drehen an der Wand bleibt im Feld (Wall Kick).")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


CHECKS = [
    ("Datei game.py ist vorhanden", check_game_vorhanden),
    ("Klasse Game lässt sich erzeugen", check_game_klasse),
    ("Schwerkraft und Fixieren", check_schwerkraft_und_fixieren),
    ("Bewegung im Spiel", check_bewegung_im_spiel),
    ("Rotation in beide Richtungen", check_rotation_tetromino),
    ("Wall Kick an der Wand", check_wall_kick),
]
