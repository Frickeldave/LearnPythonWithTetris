---
description: "Regeln für Tests im Blockfall-Kurs: Die Lernenden schreiben jeden Test selbst. Copilot beschreibt Testfälle in Worten, nennt Eingaben und erwartete Ergebnisse, liefert aber keinen vollständigen Testcode."
applyTo: "lernprojekt/tests/**"
---
# Regeln für Tests

- Die lernende Person schreibt jeden Test selbst — Testcode zählt
  genauso zum selbst geschriebenen Projektcode.
- Du darfst Testfälle **in Worten** beschreiben.
- Du darfst Eingaben und erwartete Ergebnisse nennen.
- Du darfst vorhandene Tests analysieren und erklären, warum sie
  erfolgreich sind oder fehlschlagen.
- Du darfst **keinen** vollständigen Testcode liefern — auch nicht als
  „Vorlage zum Ausfüllen".
- Du darfst keine Tests für die Lernenden schreiben oder ändern.
- Empfehle `python -m unittest discover -s tests` (im Verzeichnis
  `lernprojekt/`) und erkläre, was die Ausgabe bedeutet.
- Erinnerung an die Hinweisleiter: erst Leitfrage, dann Hinweis, dann
  Pseudocode — höchstens ein allgemeines Beispiel mit fünf Zeilen.
