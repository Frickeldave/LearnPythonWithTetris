"""Kursprüfung für Lektion 6: Anzeige, Pause, Game Over, Neustart, Hinweise.

Prüft ausschließlich den Stand von Lektion 6.
"""

from course_checks import (
    FEHLER,
    NICHT_PRUEFBAR,
    OK,
    Ergebnis,
    datei_enthaelt,
    datei_pfad,
    modul_laden,
)


def _neues_spiel():
    if not datei_pfad("game").is_file():
        return None, Ergebnis(NICHT_PRUEFBAR, "`game.py` fehlt noch.")
    modul, fehler = modul_laden("game")
    if fehler:
        return None, Ergebnis(FEHLER, fehler)
    klasse = getattr(modul, "Game", None)
    if klasse is None:
        return None, Ergebnis(FEHLER, "Klasse `Game` wurde nicht gefunden.")
    try:
        return klasse(), None
    except Exception as fehler:
        return None, Ergebnis(
            FEHLER, f"`Game()` ließ sich nicht erzeugen: {fehler}"
        )


def check_pause():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        spiel.toggle_pause()
        if not spiel.paused:
            return Ergebnis(
                FEHLER, "Nach `toggle_pause` sollte `paused` True sein."
            )
        y = spiel.piece_y
        spiel.tick()
        if spiel.piece_y != y:
            return Ergebnis(
                FEHLER, "In der Pause darf der Stein nicht fallen."
            )
        spiel.toggle_pause()
        if spiel.paused:
            return Ergebnis(
                FEHLER, "Ein zweites `toggle_pause` sollte die Pause beenden."
            )
        return Ergebnis(OK, "Pause stoppt und setzt das Spiel fort.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_game_over():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    if not datei_pfad("tetromino").is_file():
        return Ergebnis(NICHT_PRUEFBAR, "`tetromino.py` fehlt noch.")
    modul, fehler = modul_laden("tetromino")
    if fehler:
        return Ergebnis(FEHLER, fehler)
    klasse = getattr(modul, "Tetromino", None)
    if klasse is None:
        return Ergebnis(FEHLER, "Klasse `Tetromino` wurde nicht gefunden.")
    try:
        for y in range(2):
            for x in range(10):
                spiel.board.grid[y][x] = (1, 1, 1)
        spiel.next_piece = klasse("T")
        spiel.hard_drop()
        if not spiel.game_over:
            return Ergebnis(
                FEHLER,
                "Bei blockierter Startzone sollte `game_over` True werden.",
            )
        return Ergebnis(OK, "Game Over wird erkannt.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_neustart():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        spiel.soft_drop()
        spiel.reset()
        if spiel.game_over:
            return Ergebnis(
                FEHLER, "Nach `reset` sollte `game_over` False sein."
            )
        if spiel.score != 0:
            return Ergebnis(FEHLER, "Nach `reset` sollte `score` 0 sein.")
        if spiel.active_piece is None:
            return Ergebnis(
                FEHLER, "Nach `reset` sollte ein aktiver Stein existieren."
            )
        return Ergebnis(OK, "Neustart setzt das Spiel zurück.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_pause_und_neustart_tasten():
    return datei_enthaelt("main", ["K_p", "K_r"])


def check_statusanzeige():
    return datei_enthaelt("main", ["render", "font"], mindestens=1)


def check_steuerung_vollstaendig():
    return datei_enthaelt("main", ["K_SPACE", "K_ESCAPE"], mindestens=1)


CHECKS = [
    ("Pause funktioniert", check_pause),
    ("Game Over wird erkannt", check_game_over),
    ("Neustart setzt alles zurück", check_neustart),
    ("Tasten für Pause und Neustart", check_pause_und_neustart_tasten),
    ("Statusanzeige mit Text", check_statusanzeige),
    ("Vollständige Steuerung", check_steuerung_vollstaendig),
]
