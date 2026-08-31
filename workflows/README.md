# Workflows

Workflows verbinden Agenten und Skills zu einem nachvollziehbaren Ablauf. Sie beschreiben nicht nur die Reihenfolge, sondern auch Übergaben, Entscheidungen und Abschlussbedingungen.

## Mindestinhalt

Jeder Workflow sollte dokumentieren:

- Ziel und Auslöser,
- beteiligte Agenten und Skills,
- Eingaben und erwartete Endausgabe,
- Schritte mit klaren Übergaben,
- Bedingungen für Rückfragen, Abbruch oder Eskalation,
- Sicherheits- und Berechtigungsgrenzen,
- Erfolgskriterien und Verifikation.

## Empfohlener Ablauf

```text
Eingabe
  -> Kontext und Berechtigungen prüfen
  -> Aufgabe in überprüfbare Schritte zerlegen
  -> passenden Agenten/Skill ausführen
  -> Ergebnis prüfen
  -> Ergebnis, Annahmen und offene Punkte ausgeben
```

## Konventionen

Workflows werden in Kleinbuchstaben mit Bindestrichen benannt. Ein Workflow darf keine Zugangsdaten voraussetzen, die nicht als sichere Laufzeitkonfiguration beschrieben sind. Externe oder irreversible Aktionen müssen explizit markiert sein und eine passende Bestätigung oder Berechtigung verlangen.

Wenn ein Workflow wiederkehrende Schritte enthält, gehören diese Schritte in einen Skill statt als Kopie in mehrere Workflows.
