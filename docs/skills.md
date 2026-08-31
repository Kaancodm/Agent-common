# Skills

Skills sind kleine, wiederverwendbare Fähigkeiten, die von mehreren Agenten oder Workflows genutzt werden können. Ein Skill beschreibt das Vorgehen und die Qualitätskriterien; eine konkrete Agent-Rolle beschreibt dagegen, wer den Skill in welchem Kontext einsetzt.

## Ein guter Skill

Ein guter Skill:

- hat einen klaren Namen und einen begrenzten Zweck,
- definiert Voraussetzungen und Eingaben,
- beschreibt wenige, reproduzierbare Schritte,
- nennt erwartete Ausgaben und Prüfkriterien,
- macht Risiken und Grenzen sichtbar,
- ist unabhängig von einem bestimmten Anbieter, sofern das fachlich möglich ist.

## Empfohlene Struktur

```text
skills/<skill-name>/
├── SKILL.md              # Ablauf, Grenzen und Erfolgskriterien
├── examples/             # kleine, synthetische Beispiele
└── references/           # nur benötigte Referenzmaterialien
```

Für einfache Skills reicht zunächst eine einzelne `SKILL.md`. Zusätzliche Dateien werden nur angelegt, wenn sie die Anwendung verständlicher oder verlässlicher machen.

## Abgrenzung

- **Skill:** wiederverwendbare Fähigkeit.
- **Agent:** fachliche Rolle mit Verantwortungsbereich.
- **Workflow:** orchestrierte Folge aus Agenten und Skills.

Skills dürfen keine stillen Nebenwirkungen, versteckten Telemetriepfade oder Anbieter-Geheimnisse voraussetzen.
