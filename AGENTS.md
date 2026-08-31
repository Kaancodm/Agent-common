# Arbeitsregeln für Agent Common

## Auftrag

Dieses Repository sammelt wiederverwendbare Agent-Definitionen, Skills und Workflows. Änderungen sollen die gemeinsame Arbeitsweise verbessern und nicht nur eine einzelne, einmalige Ausführung dokumentieren.

## Vor jeder Änderung

1. Lies die README und die relevante Bereichsdatei unter `agents/`, `skills/` oder `workflows/`.
2. Bestimme den konkreten Nutzerwert und den kleinsten sinnvollen Änderungsumfang.
3. Prüfe, ob bereits eine passende Definition existiert, bevor du eine neue anlegst.
4. Halte Annahmen sichtbar fest, wenn Anforderungen nicht vollständig spezifiziert sind.

## Regeln für Agenten und Skills

- Ein Agent hat genau eine primäre Rolle.
- Ein Skill beschreibt eine wiederverwendbare Fähigkeit, keine allgemeine Wunschliste.
- Ein Workflow benennt Reihenfolge, Übergaben, Abbruchbedingungen und Erfolgskriterien.
- Eingaben und Ausgaben müssen für einen anderen Agenten verständlich und prüfbar sein.
- Sicherheits- und Berechtigungsgrenzen gehören in die Definition, nicht nur in die Implementierung.
- Anbieter- oder modellabhängige Details werden als Adapter dokumentiert und nicht in fachliche Regeln eingebettet.
- Keine Secrets, Tokens, privaten Schlüssel oder realen personenbezogenen Daten committen.

## Arbeitsweise

- Antworte kurz, konkret und handlungsorientiert.
- Bevorzuge vorhandene Dateien, Quellen und Werkzeuge.
- Stelle nur Fragen, wenn eine falsche Annahme den Umfang, die Sicherheit oder das Ergebnis wesentlich verändern würde.
- Melde Unsicherheiten, fehlende Quellen und nicht ausgeführte Prüfungen ausdrücklich.
- Vermeide unnötige Abstraktionen, Frameworks und Abhängigkeiten.
- Ändere nur Dateien, die zum Auftrag gehören.

## Definition of Done

Eine Änderung ist fertig, wenn:

- Zweck und Nutzung in der passenden README oder Vorlage nachvollziehbar sind,
- Verantwortlichkeiten und Grenzen eindeutig sind,
- Beispiele keine sensiblen Daten enthalten,
- Querverweise und Pfade stimmen,
- die Änderung auf Inkonsistenzen oder Tippfehler geprüft wurde.
