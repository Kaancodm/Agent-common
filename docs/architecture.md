# Architektur

## Leitidee

Agent Common trennt fachliche Beschreibung von technischer Ausführung:

- Agenten definieren Rollen und Verantwortungsgrenzen.
- Skills definieren wiederverwendbare Fähigkeiten.
- Workflows definieren Reihenfolge und Übergaben.
- Adapter verbinden diese Definitionen später mit Modellen, Tools oder Laufzeiten.

Dadurch können fachliche Regeln unabhängig von einem einzelnen Anbieter gepflegt und getestet werden.

## Lebenszyklus

1. **Anforderung:** Ziel, Nutzerwert und Grenzen beschreiben.
2. **Definition:** Agent, Skill oder Workflow mit der passenden Vorlage anlegen.
3. **Prüfung:** Eingaben, Ausgaben, Risiken und Erfolgskriterien schärfen.
4. **Adapter:** Erst bei Bedarf eine technische Ausführung ergänzen.
5. **Verifikation:** Verhalten mit synthetischen Beispielen und realistischen Fehlerfällen prüfen.
6. **Pflege:** Änderungen an Verträgen und Abhängigkeiten nachvollziehbar dokumentieren.

## Erweiterungspunkte

Die initiale Struktur lässt spätere Ergänzungen zu:

- `adapters/` für Modell-, Tool- oder Laufzeitintegrationen,
- `tests/` für strukturierte Definitionstests,
- `examples/` für vollständige, synthetische Durchläufe,
- `config/` für nicht geheime, umgebungsunabhängige Konfiguration.

Diese Verzeichnisse werden erst eingeführt, wenn ein konkreter Bedarf besteht. Leere Platzhalterordner werden nicht versioniert.

## Sicherheitsmodell

Definitionen dürfen beschreiben, welche Berechtigungen ein Ablauf benötigt. Geheimnisse und konkrete Zugangsdaten gehören ausschließlich in die sichere Laufzeitumgebung. Aktionen mit externen oder irreversiblen Auswirkungen müssen als solche erkennbar sein; ein Agent darf die dafür nötige Berechtigung nicht stillschweigend annehmen.
