"""Validierung des Repository-Aufbaus für den Blockfall-Kurs.

Prüft Struktur, Trennung von Lernprojekt und Referenzspiel, Vollständigkeit
der Prompt-Dateien und den Zustand von `lernprojekt/` (frei von Lösungscode).

Verwendung (vom Wurzelverzeichnis des Repositories aus):

    python tools/validate_repository.py

Exit-Code: 0 = alles in Ordnung, 1 = es gibt Probleme.
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Erwartete Dateien
# ---------------------------------------------------------------------------

WURZEL_DATEIEN = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    ".editorconfig",
    "CONTRIBUTING.md",
    "LEARNING_JOURNAL.md",
    "PROGRESS.md",
]

VSCODE_DATEIEN = [".vscode/settings.json"]

GITHUB_DATEIEN = [
    ".github/copilot-instructions.md",
    ".github/workflows/ci.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/lernfrage.yml",
]

INSTRUCTIONS_DATEIEN = [
    ".github/instructions/lernmodus.instructions.md",
    ".github/instructions/lernprojekt.instructions.md",
    ".github/instructions/tests.instructions.md",
    ".github/instructions/dokumentation.instructions.md",
    ".github/instructions/referenzspiel.instructions.md",
]

ALLGEMEINE_PROMPTS = [
    "00-vorbereitung.prompt.md",
    "00-kurs-start.prompt.md",
    "00-lektions-gate.prompt.md",
    "00-debugging.prompt.md",
    "00-code-review.prompt.md",
    "00-abschlusspruefung.prompt.md",
]

UEBUNGEN = {
    "L01": [
        "E01-umgebung-pruefen", "E02-projekt-anlegen",
        "E03-fenster-oeffnen", "E04-event-loop",
        "E05-spielfeld-zeichnen", "B01-farbschema",
    ],
    "L02": [
        "E01-tetrominos-beschreiben", "E02-aktiven-stein-erzeugen",
        "E03-stein-zeichnen", "E04-seven-bag", "E05-vorschau",
        "B01-raster-umschalten",
    ],
    "L03": [
        "E01-bewegung", "E02-spielfeldgrenzen", "E03-belegte-zellen",
        "E04-kollisionstests", "B01-alternative-steuerung",
    ],
    "L04": [
        "E01-schwerkraft", "E02-fixieren", "E03-rotation",
        "E04-wall-kick", "B01-debug-anzeige",
    ],
    "L05": [
        "E01-reihen-erkennen", "E02-reihen-entfernen",
        "E03-punkte-und-level", "E04-soft-drop", "E05-hard-drop",
        "B01-ghost-piece",
    ],
    "L06": [
        "E01-statusanzeige", "E02-pause", "E03-game-over",
        "E04-neustart", "E05-steuerungshinweise", "B01-hold-funktion",
    ],
    "L07": [
        "E01-tests-vervollstaendigen", "E02-code-aufraeumen",
        "E03-readme-schreiben", "E04-abnahmetest",
        "B01-eigene-erweiterung",
    ],
}

REFERENZSPIEL_DATEIEN = [
    "referenzspiel/README.md",
    "referenzspiel/main.py",
    "referenzspiel/settings.py",
    "referenzspiel/tetromino.py",
    "referenzspiel/board.py",
    "referenzspiel/game.py",
    "referenzspiel/tests/__init__.py",
    "referenzspiel/tests/test_tetromino.py",
    "referenzspiel/tests/test_board.py",
    "referenzspiel/tests/test_game_logic.py",
]

COURSE_CHECKS_DATEIEN = [
    "course_checks/__init__.py",
] + [f"course_checks/test_lesson_{nummer:02d}.py" for nummer in range(1, 8)]

TOOLS_DATEIEN = [
    "tools/README.md",
    "tools/check_environment.py",
    "tools/check_lesson.py",
    "tools/validate_repository.py",
]

DOCS_DATEIEN = [
    "docs/KURSPLAN.md",
    "docs/EINRICHTUNG.md",
    "docs/LERNENDENLEITFADEN.md",
    "docs/KURSLEITUNGSLEITFADEN.md",
    "docs/COPILOT-NUTZUNG.md",
    "docs/SPIELREGELN.md",
    "docs/ARCHITEKTUR.md",
    "docs/TECHNISCHER-VERTRAG.md",
    "docs/TESTEN.md",
    "docs/FEHLERSUCHE.md",
    "docs/ABNAHMETEST.md",
    "docs/BONUSIDEEN.md",
    "docs/REFERENZSPIEL.md",
]


def _konsole_utf8():
    for stream in (sys.stdout, sys.stderr):
        if stream and hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def _pruefe_dateien(verzeichnis, dateien):
    fehlende = [
        datei
        for datei in dateien
        if not (verzeichnis / datei).is_file()
    ]
    return fehlende


def _alle_prompts():
    prompt_dateien = ["README.md"] + ALLGEMEINE_PROMPTS
    for lektion, uebungen in UEBUNGEN.items():
        for uebung in uebungen:
            prompt_dateien.append(f"{lektion}-{uebung}.prompt.md")
    return prompt_dateien


def _pruefe_prompts(verzeichnis):
    prompts = verzeichnis / ".github" / "prompts"
    fehlende = _pruefe_dateien(verzeichnis, [f".github/prompts/{datei}" for datei in _alle_prompts()])
    zusaetzliche = sorted(
        pfad.name
        for pfad in prompts.glob("*.md")
        if pfad.name not in _alle_prompts()
    )
    return fehlende, zusaetzliche


def _pruefe_lernprojekt(verzeichnis):
    """Das Lernprojekt muss frei von Lösungscode sein."""
    lernprojekt = verzeichnis / "lernprojekt"
    probleme = []
    if not lernprojekt.is_dir():
        return ["`lernprojekt/` fehlt."]
    if not (lernprojekt / "README.md").is_file():
        probleme.append("`lernprojekt/README.md` fehlt.")
    if not (lernprojekt / "tests" / "__init__.py").is_file():
        probleme.append("`lernprojekt/tests/__init__.py` fehlt.")

    # Keine Python-Dateien außerhalb von tests/ im Lernprojekt
    for pfad in sorted(lernprojekt.glob("*.py")):
        probleme.append(
            f"`{pfad.relative_to(verzeichnis)}` enthält Lösungscode im "
            "Ausgangszustand — das Lernprojekt muss leer sein."
        )
    tests = lernprojekt / "tests"
    if tests.is_dir():
        for pfad in sorted(tests.rglob("*.py")):
            if pfad.name != "__init__.py":
                probleme.append(
                    f"`{pfad.relative_to(verzeichnis)}` darf im "
                    "Ausgangszustand noch nicht existieren."
                )
    else:
        probleme.append("`lernprojekt/tests/` fehlt.")

    # Keine Imports aus dem Referenzspiel im Lernprojekt
    for pfad in lernprojekt.rglob("*.py"):
        try:
            text = pfad.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for zeile in text.splitlines():
            zeile = zeile.strip()
            if zeile.startswith("import") and "referenzspiel" in zeile:
                probleme.append(
                    f"`{pfad.relative_to(verzeichnis)}` importiert aus "
                    "`referenzspiel/` — das Lernprojekt muss unabhängig sein."
                )
            if zeile.startswith("from referenzspiel"):
                probleme.append(
                    f"`{pfad.relative_to(verzeichnis)}` importiert aus "
                    "`referenzspiel/` — das Lernprojekt muss unabhängig sein."
                )
    return probleme


def _pruefe_referenzspiel(verzeichnis):
    referenzspiel = verzeichnis / "referenzspiel"
    probleme = []
    for pfad in referenzspiel.rglob("*.py"):
        try:
            text = pfad.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "lernprojekt" in text.lower():
            probleme.append(
                f"`{pfad.relative_to(verzeichnis)}` verweist auf "
                "`lernprojekt/` — das Referenzspiel muss unabhängig sein."
            )
    return probleme


def _pruefe_gitignore(verzeichnis):
    gitignore = verzeichnis / ".gitignore"
    if not gitignore.is_file():
        return [".gitignore fehlt."]
    text = gitignore.read_text(encoding="utf-8", errors="replace")
    probleme = []
    for eintrag in ("lernender-name.txt", ".venv", "__pycache__"):
        if eintrag not in text:
            probleme.append(f"`.gitignore` enthält `{eintrag}` nicht.")
    return probleme


def _referenztests_ausfuehren(verzeichnis):
    """Führt die Tests des Referenzspiels aus. Gibt (ok, meldung) zurück."""
    try:
        ausfuehrung = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
            cwd=str(verzeichnis / "referenzspiel"),
            capture_output=True,
            text=True,
            timeout=180,
        )
        if ausfuehrung.returncode == 0:
            return True, "Tests des Referenzspiels laufen erfolgreich."
        zeilen = (ausfuehrung.stdout + ausfuehrung.stderr).splitlines()
        return False, " | ".join(zeilen[-5:])
    except Exception as fehler:
        return False, f"Tests konnten nicht ausgeführt werden: {fehler}"


def main():
    _konsole_utf8()
    probleme = []

    print("Blockfall — Repository-Validierung")
    print("=" * 40)

    gruppen = [
        ("Wurzelverzeichnis", WURZEL_DATEIEN),
        (".vscode", VSCODE_DATEIEN),
        (".github", GITHUB_DATEIEN),
        (".github/instructions", INSTRUCTIONS_DATEIEN),
        ("referenzspiel", REFERENZSPIEL_DATEIEN),
        ("course_checks", COURSE_CHECKS_DATEIEN),
        ("tools", TOOLS_DATEIEN),
        ("docs", DOCS_DATEIEN),
    ]
    for name, dateien in gruppen:
        fehlende = _pruefe_dateien(REPO_ROOT, dateien)
        if fehlende:
            for datei in fehlende:
                probleme.append(f"{name}: `{datei}` fehlt.")
            print(f"[!!] {name}: {len(fehlende)} Datei(en) fehlen.")
        else:
            print(f"[OK] {name}: alle {len(dateien)} Dateien vorhanden.")

    fehlende_prompts, zusaetzliche_prompts = _pruefe_prompts(REPO_ROOT)
    if fehlende_prompts:
        for datei in fehlende_prompts:
            probleme.append(f"Prompts: `{datei}` fehlt.")
        print(f"[!!] Prompts: {len(fehlende_prompts)} Datei(en) fehlen.")
    else:
        print(f"[OK] Prompts: alle {len(_alle_prompts())} Dateien vorhanden.")
    if zusaetzliche_prompts:
        print(
            f"[--] Prompts: zusätzliche Datei(en), bitte prüfen: "
            f"{', '.join(zusaetzliche_prompts)}"
        )

    lernprojekt_probleme = _pruefe_lernprojekt(REPO_ROOT)
    if lernprojekt_probleme:
        probleme.extend(lernprojekt_probleme)
        for punkt in lernprojekt_probleme:
            print(f"[!!] {punkt}")
    else:
        print("[OK] lernprojekt: leer und frei von Lösungscode.")

    referenz_probleme = _pruefe_referenzspiel(REPO_ROOT)
    if referenz_probleme:
        probleme.extend(referenz_probleme)
        for punkt in referenz_probleme:
            print(f"[!!] {punkt}")
    else:
        print("[OK] referenzspiel: unabhängig vom Lernprojekt.")

    gitignore_probleme = _pruefe_gitignore(REPO_ROOT)
    if gitignore_probleme:
        probleme.extend(gitignore_probleme)
        for punkt in gitignore_probleme:
            print(f"[!!] {punkt}")
    else:
        print("[OK] .gitignore: vollständig.")

    ok, meldung = _referenztests_ausfuehren(REPO_ROOT)
    print(f"[{'OK' if ok else '!!'}] Referenzspiel-Tests: {meldung}")
    if not ok:
        probleme.append("Referenzspiel-Tests schlagen fehl.")

    print()
    if probleme:
        print(f"Validierung fehlgeschlagen: {len(probleme)} Problem(e).")
        return 1
    print("Validierung erfolgreich: Das Repository ist vollständig vorbereitet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
