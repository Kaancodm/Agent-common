# Plugin Experience Brief

## Produktgrenze

- Zielgruppe: Personen und Teams mit wechselnden allgemeinen Projektaufgaben.
- Wiederkehrender Job: Einen Auftrag mit vorhandenem Kontext eigenstaendig in ein nutzbares, geprueftes Ergebnis ueberfuehren.
- Architektur: `skills-only`; keine App, kein MCP-Server und keine externe Runtime erforderlich.
- Oeffentlicher Fach-Skill: `agent-common`.
- Baseline-Skill: `host-workspace-operator` fuer sichere, host-native Datei- und Repository-Arbeit.
- Ausgeschlossen: Deployment, Publikation, externe Kommunikation, Zugangsdatenverwaltung und irreversible Aktionen ohne gesonderten Auftrag.

## Kandidatenentscheidungen

| Quelle | Entscheidung | Begruendung |
| --- | --- | --- |
| `prompts/agent-common.md` | `compile_skill` | Enthaelt den wiederverwendbaren Ablauf vom Auftrag bis zur Uebergabe. |
| `AGENTS.md` | `reference_only` | Liefert Repository-Regeln, wird aber nicht als nahezu identischer zweiter Skill veroeffentlicht. |

## Host-Workspace-Profil

| Operation | Einstufung |
| --- | --- |
| read, list, search, grep | preferred fuer die Bestandsaufnahme |
| write, patch | mutation; nur bei beauftragter Aenderung |
| shell | optional; mutation bei zustandsaendernden Befehlen |
| python | optional fuer deterministische Verarbeitung und Verifikation |

Der Plugin gewaehrt diese Faehigkeiten nicht. Er nutzt sie nur, wenn der jeweilige Host sie bereitstellt.

## Discovery-Grenzen

- Direkter Trigger: Allgemeine Aufgabe strukturieren und umsetzen.
- Indirekter Trigger: Vorhandenen Projektkontext auswerten und den naechsten belastbaren Stand liefern.
- Negativer Trigger: Eine spezialisierte Sicherheits-, Rechts-, Medizin- oder Finanzaufgabe, fuer die ein engerer Fach-Workflow erforderlich ist.

## Status

Die Konfiguration ist fuer lokale Validierung vorbereitet. Als Projekt-Publisher ist der verbundene GitHub-Account `Kaancodm` hinterlegt. Eine oeffentliche Einreichung ist weiterhin nicht freigegeben und bleibt ohne erforderliche URLs, Listing-Pack, Reviewer-Evidenz und eine gegebenenfalls zusaetzlich verlangte Marketplace-Verifikation bewusst ausserhalb des Scopes.

Das lokale Brand-Pack ist vorhanden. Website-, Support-, Datenschutz- und AGB-URLs sowie Listing- und Reviewer-Evidenz fehlen weiterhin.
