"""Kursprüfung für Lektion 5: Reihen, Punkte, Level, Soft/Hard Drop.

Prüft ausschließlich den Stand von Lektion 5.
"""

from course_checks import (
    FEHLER,
    NICHT_PRUEFBAR,
    OK,
    Ergebnis,
    datei_pfad,
    modul_laden,
)

MIN_FALLZEIT = 0.05


def _neues_brett():
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


def _i_stein():
    if not datei_pfad("tetromino").is_file():
        raise RuntimeError("tetromino.py fehlt")
    modul, fehler = modul_laden("tetromino")
    if fehler:
        raise RuntimeError(fehler)
    klasse = getattr(modul, "Tetromino", None)
    if klasse is None:
        raise RuntimeError("Klasse Tetromino fehlt")
    return klasse("I")


def _eine_reihe_abschliessen(spiel):
    """Füllt die letzte Reihe bis auf die Lücke, in die der Stein fällt.

    Formunabhängig: Die frei gelassenen Spalten sind genau die Spalten,
    die der Stein in seiner untersten Reihe belegt.
    """
    brett = spiel.board
    stein = _i_stein()
    zellen = stein.cells()
    max_y = max(y for _, y in zellen)
    freie_spalten = sorted({x for x, y in zellen if y == max_y})
    for x in range(10):
        brett.grid[19][x] = (1, 1, 1)
    for x in freie_spalten:
        brett.grid[19][x] = None
    spiel.active_piece = stein
    spiel.piece_x = 0
    spiel.piece_y = 0
    spiel.hard_drop()


def check_full_lines():
    brett, fehler = _neues_brett()
    if fehler:
        return fehler
    try:
        for x in range(10):
            brett.grid[19][x] = (1, 1, 1)
        voll = brett.full_lines()
        if 19 not in voll:
            return Ergebnis(FEHLER, "Eine volle Reihe wurde nicht erkannt.")
        return Ergebnis(OK, "`full_lines` erkennt volle Reihen.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_clear_lines():
    brett, fehler = _neues_brett()
    if fehler:
        return fehler
    try:
        for y in (18, 19):
            for x in range(10):
                brett.grid[y][x] = (1, 1, 1)
        brett.grid[0][0] = (9, 9, 9)
        entfernt = brett.clear_lines([18, 19])
        if entfernt != 2:
            return Ergebnis(
                FEHLER, f"`clear_lines` meldete {entfernt} statt 2."
            )
        if brett.grid[2][0] != (9, 9, 9):
            return Ergebnis(
                FEHLER, "Der Inhalt ist nicht korrekt nachgerutscht."
            )
        if any(zelle is not None for zelle in brett.grid[19]):
            return Ergebnis(FEHLER, "Die unterste Reihe sollte leer sein.")
        return Ergebnis(OK, "`clear_lines` entfernt und lässt nachrutschen.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_spielzahlen():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    for attribut in ("score", "level", "lines_cleared"):
        if not isinstance(getattr(spiel, attribut, None), int):
            return Ergebnis(
                FEHLER, f"`{attribut}` fehlt oder ist keine ganze Zahl."
            )
    return Ergebnis(OK, "Punkte, Level und Reihen werden als Zahlen geführt.")


def check_soft_drop():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        punkte = spiel.score
        y = spiel.piece_y
        if spiel.soft_drop():
            if spiel.piece_y != y + 1:
                return Ergebnis(
                    FEHLER, "`soft_drop` bewegt den Stein nicht ein Feld nach unten."
                )
            if spiel.score != punkte + 1:
                return Ergebnis(
                    FEHLER, "Soft Drop muss 1 Punkt pro Feld geben."
                )
        return Ergebnis(OK, "Soft Drop fällt ein Feld und gibt 1 Punkt.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_hard_drop():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        punkte = spiel.score
        spiel.hard_drop()
        belegt = any(
            zelle is not None
            for reihe in spiel.board.grid
            for zelle in reihe
        )
        if not belegt:
            return Ergebnis(
                FEHLER, "Nach Hard Drop sollte der Stein fixiert sein."
            )
        if spiel.score <= punkte:
            return Ergebnis(FEHLER, "Hard Drop muss Punkte geben.")
        return Ergebnis(OK, "Hard Drop fixiert den Stein und gibt Punkte.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_reihen_und_punkte():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    if not datei_pfad("tetromino").is_file():
        return Ergebnis(NICHT_PRUEFBAR, "`tetromino.py` fehlt noch.")
    try:
        vorher = spiel.score
        _eine_reihe_abschliessen(spiel)
        if spiel.lines_cleared != 1:
            return Ergebnis(
                FEHLER, "Nach einer Reihe sollte `lines_cleared` 1 sein."
            )
        if spiel.score < vorher + 100:
            return Ergebnis(
                FEHLER, "Eine Reihe muss mindestens 100 × Level Punkte bringen."
            )
        return Ergebnis(OK, "Eine Reihe bringt Punkte und wird gezählt.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_level():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    if not datei_pfad("tetromino").is_file():
        return Ergebnis(NICHT_PRUEFBAR, "`tetromino.py` fehlt noch.")
    try:
        for _ in range(10):
            _eine_reihe_abschliessen(spiel)
        if spiel.level != 2:
            return Ergebnis(
                FEHLER, "Nach 10 entfernten Reihen sollte das Level 2 sein."
            )
        return Ergebnis(OK, "Nach 10 Reihen steigt das Level.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


def check_fallzeit():
    spiel, fehler = _neues_spiel()
    if fehler:
        return fehler
    try:
        spiel.level = 1
        langsam = spiel.fall_time()
        spiel.level = 50
        schnell = spiel.fall_time()
        if not 0 < schnell < langsam:
            return Ergebnis(
                FEHLER, "Die Fallzeit sollte mit dem Level sinken."
            )
        if schnell < MIN_FALLZEIT:
            return Ergebnis(
                FEHLER,
                f"Die Fallzeit darf {MIN_FALLZEIT} Sekunden nicht unterschreiten.",
            )
        return Ergebnis(OK, "Fallzeit sinkt mit dem Level und hat ein Minimum.")
    except Exception as fehler:
        return Ergebnis(FEHLER, f"Fehler beim Prüfen: {fehler}")


CHECKS = [
    ("Volle Reihen werden erkannt", check_full_lines),
    ("Volle Reihen werden entfernt", check_clear_lines),
    ("Punkte, Level und Reihen vorhanden", check_spielzahlen),
    ("Soft Drop mit 1 Punkt pro Feld", check_soft_drop),
    ("Hard Drop fixiert und gibt Punkte", check_hard_drop),
    ("Reihen geben Punkte", check_reihen_und_punkte),
    ("Level steigt nach 10 Reihen", check_level),
    ("Fallzeit sinkt und hat ein Minimum", check_fallzeit),
]
