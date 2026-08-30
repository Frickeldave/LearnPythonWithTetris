# L01 · E01 · Umgebung prüfen

- **Lektion:** 1
- **Übung:** 1 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Phase 0 (Vorbereitung) abgeschlossen
- **Lernziel:** Du kannst selbstständig prüfen, ob Python und pygame
  richtig funktionieren.
- **Sichtbares Ergebnis:** Das Terminal zeigt deine Python-Version und
  die pygame-Version an.
- **Betroffene Dateien:** noch keine (nur Befehle im Terminal)
- **Wichtige Begriffe:** Terminal, Python-Version, Modul, Import

## Aufgabe in kleinen Schritten

1. Öffne ein Terminal im Verzeichnis `lernprojekt/`.
2. Prüfe deine Python-Version mit einem kurzen Befehl.
3. Prüfe, ob das Modul `pygame` importiert werden kann.
4. Lass dir zusätzlich die pygame-Version anzeigen.
5. Vergleiche das Ergebnis mit `docs/EINRICHTUNG.md`.

## Unterstützung

- **Erlaubt:** Copilot erklärt dir die Befehle und ihre Ausgabe.
- **Verboten:** Es gibt hier noch keinen Projektcode — Copilot schreibt
  deshalb nichts für dich auf.

## Prüfen

**Manuell:** Das Terminal zeigt eine Python-Version ab 3.10 und eine
pygame-Version an, ohne Fehlermeldung.

## Erwartetes Ergebnis

Zwei erfolgreiche Ausgaben: Python-Version und pygame-Version.

## Definition of Done

- [ ] Python-Version (ab 3.10) wird angezeigt.
- [ ] pygame lässt sich importieren und meldet seine Version.
- [ ] Es erscheinen keine Fehlermeldungen.

## Verständnisfrage

Warum prüft man die Umgebung, bevor man mit dem Programmieren beginnt?

## Hinweisleiter

1. **Leitfrage:** Welchen Befehl benutzt du, um die Python-Version zu sehen?
2. **Konzeptueller Hinweis:** `import` lädt ein Modul; schlägt es fehl,
   ist das Modul nicht installiert.
3. **Algorithmus in Worten:** Erst Version ausgeben, dann pygame laden,
   dann dessen Version ausgeben.
4. **Pseudocode:** `python --version`, dann ein kurzer Einzeiler mit
   `import pygame` und Versionsausgabe.
5. **Beispiel (max. 5 Zeilen):** allgemeines Python-Beispiel für einen
   Import mit Versionsausgabe.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Wenn beide Versionen sichtbar sind: weiter mit `L01-E02-projekt-anlegen.prompt.md`.
