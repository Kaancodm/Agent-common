# Release Preparation Workflow

## Goal

Bring the repository and the plugin listing to a consistent, verifiable state that is ready
for a public release. Steps that happen outside this repository (OpenAI Platform publisher
verification, URL registration, tag/release creation) are explicitly named so they are not
forgotten, but they cannot be automated here.

## Trigger

Use this workflow when:

- a version milestone has been reached and all intended changes are merged to `main`;
- for a public submission only: `submission/listing.json` URLs are ready (non-null).
  A beta or other internal release does not require them;
- a maintainer has decided to promote the beta to a stable release or to cut a new beta.

Do not start release preparation while open bugs or incomplete features are expected to land
in the same version.

## Roles

- Maintainer (human): decides version number, owns OpenAI Platform steps, and approves the
  final merge.
- Orchestrator agent: coordinates the in-repository preparation steps.
- Review agent: validates the prepared state before the final gated actions.

## Inputs

- Decision: target version string (e.g., `0.1.0` for stable, `0.1.0-beta.2` for a new beta).
- Current `main` ref (all changes must already be merged).
- Populated URLs for `submission/listing.json` if this is a public submission.
- OpenAI Platform publisher verification status.

## Steps

### 1. Confirm readiness

Verify:

- all intended PRs for the version are merged to `main`;
- CI is green on `main`;
- no known blocking defects remain open;
- the maintainer has confirmed the version number.

`python scripts/check_release_readiness.py` reports the mechanical part of this and of
steps 2–4 in one command. Use `--public` to also require the listing URLs.

Exit condition: version number is decided and `main` is green.

### 2. In-repository version bumps

Update the following files to the agreed version string:

| File | Field |
|---|---|
| `.codex-plugin/plugin.json` | `version` |
| `submission/reviewer-packet.json` | `source.version` |
| `CHANGELOG.md` | Add a new `## [<version>]` section with today's date |

`submission/listing.json` `version` field represents the intended public release and is
updated separately (see step 4).

Exit condition: all three files consistently name the new version.

### 3. Rebuild and update evidence

Commit the step-2 version bumps **first**, so the package is built from a clean working
tree as the security boundary below requires. Then run
`python scripts/verify_evidence.py --update` to rebuild the plugin package deterministically
and refresh `submission/reviewer-packet.json` with the current package hash and file list,
and commit that refreshed evidence as a separate commit.

The evidence file records no commit SHA (a file cannot contain the hash of the commit that
introduces it).

Exit condition: `python scripts/verify_evidence.py` passes without `--update` on a clean
working tree.

### 4. Populate listing URLs (public submission only)

If this release targets a public OpenAI plugin submission, update `submission/listing.json`:

| Field | Required content |
|---|---|
| `websiteURL` | Public product or project page |
| `customerSupportURL` | Support or contact page |
| `privacyPolicyURL` | Privacy policy (required by OpenAI) |
| `termsOfServiceURL` | Terms of service (required by OpenAI) |
| `version` | The public-facing version string |

These URLs are outside the repository. Confirm each is live and reachable before updating
the listing.

Exit condition: all required fields are non-null and all URLs are reachable.

### 5. Independent review

The review agent checks:

- version strings are consistent across all files;
- evidence matches the rebuilt package;
- CHANGELOG entry covers the changes in this version;
- listing URLs (if updated) are non-null;
- no secrets, tokens, or personal data appear in any updated file.

Disposition: `APPROVE` or `REQUEST_CHANGES`.

Exit condition: review approved.

### 6. Gated actions (human)

The following actions require maintainer execution. They are gated by `policy/approval-policy.json`
under the `production` and `external_communication` categories:

1. **Merge the release preparation into `main`.** Steps 2–4 are prepared on a branch, so
   the version, evidence, and listing changes are not on `main` until this merge lands.
   Tagging before it would point the tag at an unmerged commit while `main` still carries
   the previous release.
2. **Verify the tag target.** Check out `main`, pull, and confirm the release commit is
   present (`git log --oneline -1` shows the merged preparation) and that
   `python scripts/check_release_readiness.py` passes there.
3. **Create the Git tag on that commit**: `git tag -a v<version> -m "Release <version>"`.
4. **Push the tag**: `git push origin v<version>`. This triggers
   `.github/workflows/release.yml`, which rebuilds the package, re-verifies the evidence
   against the tag, and publishes the GitHub Release with the CHANGELOG section as notes
   and the `dist/` zip attached.
5. **OpenAI Platform publisher verification**: complete the verification flow in the OpenAI
   Platform if not already done.
6. **Submit the plugin**: upload the package attached to the GitHub Release and the listing
   metadata.
7. **Country/region selection**: choose availability in the OpenAI plugin store.

No agent acts on behalf of the publisher for these steps.

Exit condition: maintainer confirms each step is complete.

### 7. Handoff

Record the completed state:

- version released, tag name, GitHub Release URL;
- plugin submission status;
- outstanding items (e.g., review period, approval pending);
- exact next action.

## Security boundaries

- URL fields must not contain credentials, tokens, or personal data.
- The plugin package must be built from a clean working tree with no uncommitted changes.
- Gated actions in step 6 must not be delegated to an agent without explicit maintainer
  instruction.

## Success criteria

- [ ] `python scripts/check_release_readiness.py` passes (covers the three items below).
- [ ] Version strings are consistent across `plugin.json`, `reviewer-packet.json`, and `CHANGELOG.md`.
- [ ] Evidence is rebuilt and `verify_evidence.py` passes on a clean working tree.
- [ ] Listing URLs are non-null and reachable (public submission only).
- [ ] Independent review approved.
- [ ] Release preparation is merged to `main` and the tag points at that commit.
- [ ] Git tag and GitHub Release exist.
- [ ] Plugin submission completed (public submission only).
- [ ] Handoff is complete.
