# Fehlersuche

Diese Seite sammelt häufige Probleme mit Diagnosewegen und Leitfragen.
Fertige Projektlösungen gibt es hier bewusst nicht — du findest den
Fehler selbst (gern mit dem Prompt `00-debugging.prompt.md`).

## Python wird nicht gefunden

**Symptom:** `python --version` zeigt einen Fehler.

**Diagnose:**

- Auf Windows: Ist der Haken „Add Python to PATH" gesetzt? Sonst
  Python neu installieren.
- Alternativ `py --version` oder `python3 --version` probieren.
- Leitfrage: Wo ist Python installiert — und kennt dein Terminal den Pfad?

## Virtuelle Umgebung ist nicht aktiv

**Symptom:** `pygame` wird nicht gefunden, obwohl es installiert wurde;
der Prompt zeigt kein `(.venv)`.

**Diagnose:**

- Umgebung aktivieren (`docs/EINRICHTUNG.md`).
- Leitfrage: Läuft das Terminal in derselben Sitzung wie die
  Aktivierung — und im richtigen Ordner?

## pygame fehlt

**Symptom:** `ModuleNotFoundError: No module named 'pygame'`.

**Diagnose:**

- `python -m pip install -r requirements.txt` in der **aktiven**
  Umgebung ausführen.
- Leitfrage: Zeigt `python -c "import pygame"` noch immer einen Fehler?

## Fenster reagiert nicht

**Symptom:** Das Fenster lässt sich nicht schließen oder „friert ein".

**Diagnose:**

- Fehlt `pygame.event.get()` in der Hauptschleife? Ohne Event-Abfrage
  weiß pygame nichts vom X-Klick.
- Wird das Bild mit `flip()`/`update()` aktualisiert?
- Leitfrage: Welche Ereignisse holt deine Schleife ab?

## Koordinaten sind vertauscht

**Symptom:** Formen erscheinen gedreht oder gespiegelt.

**Diagnose:**

- In `grid[y][x]` ist der erste Index die **Reihe** (y), der zweite die
  **Spalte** (x).
- Leitfrage: Was bedeutet bei dir `(x, y)` — und was erwartet dein
  Zeichencode?

## Stein verlässt das Spielfeld

**Symptom:** Der Stein bewegt sich über den Rand oder bleibt halb stecken.

**Diagnose:**

- Prüfst du **alle** Zellen des Steins oder nur seine Position?
- Leitfrage: Welche Zellen der Form wären nach der Bewegung außerhalb?

## Rotation erzeugt eine Überlappung

**Symptom:** Der gedrehte Stein steckt im Stapel oder in der Wand.

**Diagnose:**

- Wird die gedrehte Form erst geprüft und nur bei Erfolg übernommen?
- Wall Kick vorhanden? (`docs/SPIELREGELN.md`)
- Leitfrage: Was passiert in deinem Code, wenn die Drehung nicht passt?

## Stein wird nicht fixiert

**Symptom:** Der Stein schwebt am Boden weiter oder fällt durch.

**Diagnose:**

- Wird beim Scheitern des Fallschritts `lock` aufgerufen?
- Leitfrage: Wo erkennst du „kann nicht mehr fallen"?

## Reihen werden nicht korrekt entfernt

**Symptom:** Volle Reihen bleiben stehen oder leere verschwinden.

**Diagnose:**

- Wird jede Reihe auf **alle** Zellen geprüft?
- Wird von unten nach oben entfernt, damit sich die Nummern nicht
  verschieben?
- Leitfrage: Welche Reihennummern haben deine vollen Reihen nach der
  ersten Entfernung?

## Tests können Module nicht importieren

**Symptom:** `ModuleNotFoundError` beim Testlauf.

**Diagnose:**

- Tests aus `lernprojekt/` heraus starten:
  `python -m unittest discover -s tests`.
- Liegt das Modul wirklich in `lernprojekt/` (nicht in einem Unterordner)?
- Leitfrage: Von wo aus läuft Python — und wo sucht es deine Module?

## Allgemeiner Ablauf bei Fehlern

1. Vollständige Fehlermeldung lesen (unterste Zeile zuerst!).
2. Erwartung und Beobachtung in einem Satz formulieren.
3. Prompt `00-debugging.prompt.md` mit Copilot durchgehen.
4. Genau **eine** Änderung machen und erneut testen.
