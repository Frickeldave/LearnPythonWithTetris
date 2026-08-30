"""Kursprüfung für Lektion 7: Tests, Aufräumen, README, Abnahme.

Prüft ausschließlich den Stand von Lektion 7.
"""

import subprocess
import sys

from course_checks import (
    FEHLER,
    NICHT_PRUEFBAR,
    OK,
    LEARNPROJECT,
    Ergebnis,
)


def _testverzeichnis():
    return LEARNPROJECT / "tests"


def check_testverzeichnis():
    tests = _testverzeichnis()
    if not tests.is_dir():
        return Ergebnis(NICHT_PRUEFBAR, "`lernprojekt/tests/` fehlt noch.")
    dateien = sorted(tests.glob("test_*.py"))
    if not dateien:
        return Ergebnis(
            NICHT_PRUEFBAR, "In `tests/` gibt es noch keine Testdateien."
        )
    namen = ", ".join(pfad.name for pfad in dateien)
    return Ergebnis(OK, f"Testdateien gefunden: {namen}.")


def check_testanzahl():
    tests = _testverzeichnis()
    if not tests.is_dir():
        return Ergebnis(NICHT_PRUEFBAR, "`lernprojekt/tests/` fehlt noch.")
    dateien = list(tests.glob("test_*.py"))
    if not dateien:
        return Ergebnis(
            NICHT_PRUEFBAR, "In `tests/` gibt es noch keine Testdateien."
        )
    anzahl = 0
    for pfad in dateien:
        text = pfad.read_text(encoding="utf-8", errors="replace")
        anzahl += text.count("def test_")
    if anzahl < 5:
        return Ergebnis(
            FEHLER,
            f"Nur {anzahl} Testmethoden gefunden — mindestens 5 werden erwartet.",
        )
    return Ergebnis(OK, f"{anzahl} Testmethoden gefunden.")


def check_eigene_tests_laufen():
    tests = _testverzeichnis()
    if not tests.is_dir():
        return Ergebnis(NICHT_PRUEFBAR, "`lernprojekt/tests/` fehlt noch.")
    if not list(tests.glob("test_*.py")):
        return Ergebnis(
            NICHT_PRUEFBAR, "In `tests/` gibt es noch keine Testdateien."
        )
    try:
        ausfuehrung = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
            cwd=str(LEARNPROJECT),
            capture_output=True,
            text=True,
            timeout=120,
        )
        if ausfuehrung.returncode == 0:
            return Ergebnis(OK, "Die eigenen Tests laufen erfolgreich durch.")
        gesamt = (ausfuehrung.stdout + ausfuehrung.stderr).strip().splitlines()
        kurzzusammenfassung = " | ".join(gesamt[-3:]) if gesamt else ""
        return Ergebnis(
            FEHLER,
            f"Die eigenen Tests schlagen fehl: {kurzzusammenfassung}",
        )
    except Exception as fehler:
        return Ergebnis(
            FEHLER, f"Die Tests konnten nicht ausgeführt werden: {fehler}"
        )


def check_projekt_readme():
    pfad = LEARNPROJECT / "README.md"
    if not pfad.is_file():
        return Ergebnis(NICHT_PRUEFBAR, "`lernprojekt/README.md` fehlt.")
    text = pfad.read_text(encoding="utf-8", errors="replace")
    if "diese readme darfst du im laufe des kurses" in text.lower():
        return Ergebnis(
            NICHT_PRUEFBAR,
            "Die vorbereitete README wurde noch nicht durch die eigene "
            "Projektbeschreibung ersetzt.",
        )
    if len(text.strip()) < 100:
        return Ergebnis(
            FEHLER, "Die Projekt-README ist zu kurz (unter 100 Zeichen)."
        )
    return Ergebnis(OK, "Die eigene Projekt-README ist vorhanden und gefüllt.")


CHECKS = [
    ("Testverzeichnis mit Testdateien", check_testverzeichnis),
    ("Mindestens 5 eigene Testmethoden", check_testanzahl),
    ("Eigene Tests laufen grün", check_eigene_tests_laufen),
    ("Eigene Projekt-README", check_projekt_readme),
]
