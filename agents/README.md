# Agent-Definitionen

Unter `agents/` liegen fachliche Rollen. Eine Agent-Definition erklärt, wofür ein Agent zuständig ist und woran ein gutes Ergebnis erkennbar ist.

## Wann eine neue Definition sinnvoll ist

Eine neue Definition ist sinnvoll, wenn eine Rolle:

- einen wiederkehrenden Auftrag hat,
- eigene Eingaben, Entscheidungen oder Ausgaben besitzt,
- von anderen Rollen getrennt getestet oder ersetzt werden kann.

Für eine einzelne einmalige Aufgabe genügt meist ein Workflow-Schritt oder eine kurze Aufgabenbeschreibung.

## Mindestinhalt

Jede Agent-Definition sollte enthalten:

- Name und Zweck,
- Verantwortungsbereich und klare Nicht-Zuständigkeiten,
- erwartete Eingaben,
- erwartete Ausgaben,
- Arbeitsablauf,
- verfügbare Werkzeuge oder Quellen,
- Sicherheits- und Berechtigungsgrenzen,
- Erfolgskriterien und Eskalationsfälle.

Nutze [agent-template.md](agent-template.md) als Ausgangspunkt.

## Namenskonvention

Dateien werden in Kleinbuchstaben mit Bindestrichen benannt, zum Beispiel `research-agent.md` oder `review-agent.md`. Der Dateiname beschreibt die Rolle, nicht das verwendete Modell oder den Anbieter.

## Abgrenzung

Agenten sind Rollen. Wiederverwendbare Fähigkeiten gehören nach [../skills/README.md](../skills/README.md). Die Verbindung mehrerer Rollen gehört nach [../workflows/README.md](../workflows/README.md).
