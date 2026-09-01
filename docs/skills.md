# Skills

Skills are small, reusable capabilities that can be used by multiple agents or workflows.
A skill describes the procedure and the quality criteria; a concrete agent role, by contrast,
describes who uses the skill in which context.

## A good skill

A good skill:

- has a clear name and a bounded purpose,
- defines preconditions and inputs,
- describes a few reproducible steps,
- names expected outputs and check criteria,
- makes risks and boundaries visible,
- is independent of a particular vendor where that is feasible.

## Recommended structure

```text
skills/<skill-name>/
├── SKILL.md              # Procedure, boundaries, and success criteria
├── examples/             # small, synthetic examples
└── references/           # only the reference material that is needed
```

For simple skills a single `SKILL.md` is enough at first. Additional files are added only
when they make the skill easier to understand or more reliable.

## Distinctions

- **Skill:** reusable capability.
- **Agent:** domain role with a responsibility area.
- **Workflow:** orchestrated sequence of agents and skills.

Skills must not assume silent side effects, hidden telemetry paths, or vendor secrets.
