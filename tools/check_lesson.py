"""Kursprüfung: Prüft den Stand einer Lektion im Lernprojekt.

Verwendung (vom Wurzelverzeichnis des Repositories aus):

    python tools/check_lesson.py --lesson 1
    python tools/check_lesson.py --lesson 7
    python tools/check_lesson.py --lesson all   (vollständige Basisabnahme)

Die Kursprüfung liest und führt `lernprojekt/` nur aus. Sie verändert
dort keine Dateien und greift niemals auf `referenzspiel/` zu.

Exit-Codes:
    0  BESTANDEN
    1  NACHARBEIT ERFORDERLICH
    2  NICHT PRÜFBAR
"""

import argparse
import importlib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# Verhindert __pycache__-Dateien im Lernprojekt beim Prüfen.
sys.dont_write_bytecode = True

from course_checks import FEHLER, NICHT_PRUEFBAR, OK, fuehre_aus  # noqa: E402


def _konsole_utf8():
    """Sorgt auf Windows für eine saubere Umlaut-Ausgabe."""
    for stream in (sys.stdout, sys.stderr):
        if stream and hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def main(argv=None):
    _konsole_utf8()

    parser = argparse.ArgumentParser(
        description="Prüft eine Lektion des Blockfall-Kurses."
    )
    parser.add_argument(
        "--lesson",
        required=True,
        help="Nummer der Lektion (1 bis 7) oder 'all' für die Basisabnahme.",
    )
    args = parser.parse_args(argv)

    if args.lesson == "all":
        lektionen = [1, 2, 3, 4, 5, 6, 7]
    else:
        try:
            nummer = int(args.lesson)
        except ValueError:
            print("FEHLER: --lesson erwartet eine Zahl von 1 bis 7 oder 'all'.")
            return 2
        if not 1 <= nummer <= 7:
            print("FEHLER: --lesson erwartet eine Zahl von 1 bis 7 oder 'all'.")
            return 2
        lektionen = [nummer]

    gesamt_ok = 0
    gesamt_fehler = 0
    gesamt_nicht_pruefbar = 0

    for nummer in lektionen:
        modulname = f"course_checks.test_lesson_{nummer:02d}"
        try:
            modul = importlib.import_module(modulname)
        except ImportError:
            print(f"Lektion {nummer}: Prüfmodul `{modulname}` nicht gefunden.")
            return 2

        print(f"\n=== Lektion {nummer} ===")
        for name, funktion in modul.CHECKS:
            ergebnis = fuehre_aus(funktion)
            if ergebnis.status == OK:
                print(f"  [OK]   {name}")
                if ergebnis.meldung:
                    print(f"         {ergebnis.meldung}")
                gesamt_ok += 1
            elif ergebnis.status == NICHT_PRUEFBAR:
                print(f"  [--]   {name} (nicht prüfbar)")
                if ergebnis.meldung:
                    print(f"         {ergebnis.meldung}")
                gesamt_nicht_pruefbar += 1
            else:
                print(f"  [!!]   {name}")
                if ergebnis.meldung:
                    print(f"         {ergebnis.meldung}")
                gesamt_fehler += 1

    print()
    print(
        f"Ergebnis: {gesamt_ok} bestanden, {gesamt_fehler} fehlgeschlagen, "
        f"{gesamt_nicht_pruefbar} nicht prüfbar."
    )
    if gesamt_fehler > 0:
        print("Status: NACHARBEIT ERFORDERLICH")
        return 1
    if gesamt_nicht_pruefbar > 0:
        print("Status: NICHT PRÜFBAR")
        return 2
    print("Status: BESTANDEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
