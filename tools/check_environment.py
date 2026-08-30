"""Prüft die Umgebung für den Blockfall-Kurs.

Dieses Werkzeug benutzt nur die Standardbibliothek und funktioniert
deshalb auch, wenn pygame noch nicht installiert ist.

Verwendung (vom Wurzelverzeichnis des Repositories aus):

    python tools/check_environment.py

Exit-Code: 0 = alles bereit, 1 = es fehlt noch etwas.
"""

import shutil
import sys


def _konsole_utf8():
    for stream in (sys.stdout, sys.stderr):
        if stream and hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def main():
    _konsole_utf8()
    fehler = []

    print("Blockfall — Umgebungsprüfung")
    print("=" * 40)

    version = sys.version_info
    print(f"Python-Version: {sys.version.split()[0]}")
    print(f"Python liegt unter: {sys.executable}")
    if version < (3, 10):
        fehler.append(
            "Python ist zu alt. Installiere Python 3.10 oder neuer "
            "von https://www.python.org/ ."
        )
    else:
        print("[OK] Python ist neu genug (mindestens 3.10).")

    if sys.prefix == sys.base_prefix:
        print("[--] Es scheint keine virtuelle Umgebung aktiv zu sein.")
        print("     Empfohlen: eine virtuelle Umgebung anlegen und aktivieren")
        print("     (siehe docs/EINRICHTUNG.md). Weiterarbeiten ist auch")
        print("     ohne virtuelle Umgebung möglich.")
    else:
        print("[OK] Eine virtuelle Umgebung ist aktiv.")

    try:
        import pygame  # noqa: F401

        print(f"[OK] pygame ist installiert (Version {pygame.ver}).")
    except ImportError:
        fehler.append(
            "pygame fehlt. Installation in der aktiven virtuellen Umgebung:\n"
            "        python -m pip install pygame\n"
            "     oder:\n"
            "        python -m pip install -r requirements.txt"
        )

    git = shutil.which("git")
    if git:
        print(f"[OK] Git ist installiert ({git}).")
    else:
        print("[--] Git wurde nicht gefunden. Für den Kurs ist Git nicht nötig.")

    print()
    if fehler:
        print("Es fehlt noch etwas:")
        for punkt in fehler:
            print("  *", punkt)
        print()
        print("Nach der Behebung diese Prüfung erneut starten.")
        return 1

    print("Alles bereit! Weiter mit dem Prompt `00-vorbereitung.prompt.md`")
    print("im Ordner `.github/prompts/`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
