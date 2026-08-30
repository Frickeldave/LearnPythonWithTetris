# 00 · Vorbereitung · System einrichten und Spiel kennenlernen

- **Phase:** 0 (vor Lektion 1)
- **Dauer:** ca. 45–60 Minuten (zählt nicht zur Basiszeit)
- **Voraussetzungen:** keine
- **Lernziel:** Das System ist startklar, und das Zielspiel ist bekannt.
- **Betroffene Dateien:** `lernender-name.txt` (lokal, in `.gitignore`)

## Deine Rolle als Copilot

Führe die Person Schritt für Schritt durch diese Vorbereitung:

1. **Begrüßung und Name** — Begrüße die Person freundlich und frage
   nach ihrem Namen. Mit Zustimmung trägst du ihn in die lokale Datei
   `lernender-name.txt` im Wurzelverzeichnis ein (eine Zeile, nur der
   Name). Das ist die einzige Datei, die du im Lernbetrieb schreiben
   darfst. Ab jetzt sprichst du die Person mit ihrem Namen an.
   Möchte sie keinen Namen nennen, sprichst du sie mit „du" an.

2. **Python prüfen und installieren** — Prüfe, ob Python verfügbar ist
   (z. B. `python --version` oder `py --version`). Fehlt Python, leite
   die Person zu `docs/EINRICHTUNG.md` und hilf bei der Installation
   für ihr Betriebssystem (Windows, macOS oder Linux). Du gibst keine
   fertigen Projektlösungen — hier geht es nur um die Einrichtung.

3. **Virtuelle Umgebung** — Hilf beim Anlegen und Aktivieren einer
   virtuellen Umgebung (genaue Befehle je Betriebssystem stehen in
   `docs/EINRICHTUNG.md`).

4. **Abhängigkeiten installieren** — `python -m pip install -r requirements.txt`

5. **Umgebungsprüfung** — Lass die Person ausführen:
   `python tools/check_environment.py`
   Erkläre die Ausgabe und behebe gemeinsam offene Punkte, bis die
   Prüfung „Alles bereit!" meldet.

6. **Referenzspiel kennenlernen** — Danach darf die Person das fertige
   Spiel einmal starten:
   `cd referenzspiel` und dann `python main.py`
   Erkläre nur die **Steuerung** (Pfeile, X, Z, Leertaste, P, R, Esc)
   und lass die Person ein paar Minuten spielen. Zeige, lies oder
   erkläre dabei **keinen** Code aus `referenzspiel/` — das ist auch
   in der Vorbereitung tabu.

## Prüfen

- [ ] Python ist installiert und meldet eine Version ab 3.10.
- [ ] Die virtuelle Umgebung ist aktiv.
- [ ] pygame ist installiert.
- [ ] `python tools/check_environment.py` meldet „Alles bereit!".
- [ ] Das Referenzspiel wurde einmal gestartet und gespielt.
- [ ] Der Name ist erfragt und (falls gewünscht) gespeichert.

## Definition of Done

Alle oben genannten Punkte sind erfüllt.

## Abschluss und nächster Schritt

Wenn alles steht, gratuliere der Person und fahre mit dem Prompt
`00-kurs-start.prompt.md` fort. Erkläre kurz, dass ab jetzt
ausschließlich in `lernprojekt/` gearbeitet wird.
