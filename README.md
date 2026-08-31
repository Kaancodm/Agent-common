# Agent Common

Eine schlanke, framework-unabhängige Grundlage für die Entwicklung, Dokumentation und Orchestrierung von Agenten.

## Ziel

Agent Common stellt gemeinsame Konventionen bereit, damit Agenten:

- klar abgegrenzte Aufgaben und Verantwortlichkeiten haben,
- wiederverwendbare Skills nutzen,
- in nachvollziehbaren Workflows zusammenspielen,
- Annahmen, Quellen und Ergebnisse transparent dokumentieren,
- sicher und mit möglichst wenig unnötiger Komplexität arbeiten.

Das Repository enthält bewusst noch keine Bindung an ein bestimmtes Modell, SDK oder Laufzeitsystem. Konkrete Integrationen können später ergänzt werden, ohne die fachlichen Definitionen neu zu strukturieren.

## Struktur

```text
.
├── AGENTS.md                    # Arbeitsregeln für Agenten im Repository
├── agents/
│   ├── README.md                # Konventionen für Agent-Definitionen
│   └── agent-template.md        # Kopierbare Vorlage für neue Agenten
├── skills/
│   ├── README.md                # Konventionen für wiederverwendbare Skills
│   ├── agent-common/            # Allgemeiner End-to-End-Arbeits-Skill
│   └── host-workspace-operator/ # Sichere host-native Workspace-Arbeit
├── workflows/
│   └── README.md                # Konventionen für Agent-Workflows
├── prompts/
│   └── agent-common.md          # Direkt nutzbarer Projektprompt
├── templates/
│   └── task-brief.md            # Vorlage für konkrete Aufgaben
├── .codex-plugin/
│   └── plugin.json              # Manifest des skills-only Plugins
└── docs/
    ├── architecture.md          # Architektur, Lebenszyklus und Erweiterungspunkte
    └── plugin-experience.md     # Produktgrenze und Plugin-Entscheidungen
```

## Schnellstart

1. Lies [AGENTS.md](AGENTS.md), bevor du Dateien ergänzt oder änderst.
2. Lege für jede klar abgegrenzte Rolle eine Definition unter `agents/` an.
3. Beschreibe wiederkehrende Fähigkeiten unter `skills/`.
4. Komponiere mehrere Agenten und Skills erst dann in einem Workflow unter `workflows/`.
5. Prüfe vor dem Commit, ob Zweck, Eingaben, Ausgaben, Grenzen und Erfolgskriterien eindeutig sind.

Für allgemeine Projektarbeit kann der Inhalt von
[`prompts/agent-common.md`](prompts/agent-common.md) direkt als Projektanweisung
verwendet werden. Neue Aufträge beginnen mit
[`templates/task-brief.md`](templates/task-brief.md). Das enthaltene
`skills-only`-Plugin stellt denselben Ablauf in Codex-kompatibler Form bereit.

## Grundprinzipien

- **Pragmatisch:** Erst die kleinste Lösung, die den Anwendungsfall zuverlässig abdeckt.
- **Präzise:** Jede Definition benennt Zweck, Zuständigkeit, Eingaben, Ausgaben und Grenzen.
- **Eigenständig:** Agenten arbeiten innerhalb ihres Auftrags selbstständig und eskalieren nur bei echten Entscheidungs- oder Sicherheitsfragen.
- **Nachvollziehbar:** Ergebnisse enthalten relevante Annahmen, Quellen und offene Punkte.
- **Sicher:** Keine Geheimnisse, Zugangsdaten oder personenbezogenen Daten in Definitionen, Beispielen oder Commits.
- **Komponierbar:** Skills liefern Fähigkeiten; Workflows verbinden sie; Agenten übernehmen Rollen.

## Status

Das Repository enthält die Projektgrundstruktur, wiederverwendbare Agenten und
Workflows sowie ein lokal validierbares `skills-only`-Plugin. Eine öffentliche
Plugin-Einreichung ist noch nicht freigegeben; dafür fehlen insbesondere eine
verifizierte Entwickleridentität und die in
[`docs/plugin-experience.md`](docs/plugin-experience.md) genannten Listing- und
Reviewer-Nachweise.

## Beiträge

Neue Inhalte sollten:

- einem konkreten wiederkehrenden Anwendungsfall dienen,
- die bestehenden Vorlagen und Konventionen verwenden,
- keine unnötige Laufzeit- oder Anbieterabhängigkeit einführen,
- mit einem kleinen, verständlichen Commit beschrieben werden.

