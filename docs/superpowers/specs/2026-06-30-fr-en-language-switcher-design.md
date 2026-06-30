# FR/EN Language Switcher — Design

**Date:** 2026-06-30
**Scope:** Add a French/English language switcher to the GETT GI single-file static landing page (`index.html`). Selecting English translates all visible content; selecting French reverts. No build step, no new dependencies, no structural/SVG changes.

## Goals

- A minimal **"FR / EN"** text toggle in the navbar: active language solid, the other dimmed and clickable.
- Toggle inherits the nav's light/dark color per section and **stays visible when the nav condenses to the burger**. Also present in the mobile fullscreen menu.
- Clicking **EN** translates the entire visible page to English; **FR** reverts. Covers headings, paragraphs, cards, workflow steps, SVG `<text>` labels, nav, mobile menu, footer, `<title>`, meta description, and animated stat counters.
- **First visit:** auto-detect via `navigator.language` — English-language browsers open in English, otherwise French. The manual choice is then persisted to `localStorage` and wins on later visits.
- **Not translated:** brand "GETT GI", email, phone, "LinkedIn", "Dakar", "FCFA", local language names (Wolof, Pulaar, …), CEO name.

## Approach — text-node translation (no markup edits)

Chosen over `data-i18n`-per-element (≈170 elements, error-prone) and textContent-swap (drops `<br>`/spans).

On load, a script walks every **text node** under `<body>` (plus `<title>` and the meta description), snapshots its original French value, and looks up a normalized key in an inline **FR → EN dictionary**. Because only text-node values change — never tags — all line breaks, nested spans, SVG structure, and animations stay intact.

### Normalization (robust matching)

`normalize(s)` = replace `U+2019 (') → '`, `U+2011 (non-breaking hyphen) → -`, collapse internal whitespace, trim. Both the runtime text nodes and the dictionary keys are normalized before lookup, so curly apostrophes and special hyphens in the source can't cause silent misses.

### Switching

- Snapshot per text node: `{ node, fr: node.nodeValue, frTrim: fr.trim() }`.
- To EN: if `dict[normalize(frTrim)]` exists, `node.nodeValue = node.nodeValue.split(frTrim).join(en)` (preserves surrounding whitespace; literal split/join avoids regex `$` issues). Otherwise leave French (graceful fallback).
- To FR: restore stored `fr`.
- Also update `<html lang>`, `<title>`, and `<meta name="description">`.

### Counters & figures

- Animated counters (`.counter`) are generated in JS. `animateCounter` reads the active language: French uses `toLocaleString('fr-FR')` + `,` decimal; English uses `en-US` + `.` decimal. Suffix map `{ "Md FCFA": "Bn FCFA" }`; `%`, `M`, `FCFA` unchanged.
- Already-animated counters re-render their final value (no re-animation) on language switch.
- Static impact figures (`18,4 M`, `38,3 %`, `≈ 2 Md`, `60 %`) are plain text nodes translated via the dictionary (`18.4 M`, `38.3 %`, `≈ 2 Bn`, `60 %`).

## Toggle UI

- Element `.nav-lang`: two buttons `FR` and `EN` separated by `/`, using `currentColor` so it adapts to the existing nav color logic. Always visible (not hidden by `.is-condensed`). Sits at top-right near the burger/CTA; a second instance in `#mobileMenu`.
- Active language `opacity: 1`, inactive `opacity: 0.4`, hover raises opacity. No layout shift between sections.

## Out of scope / guarantees

- No change to existing SVGs, animations, layout, fonts, or section order.
- No new files, no bundler, no CDN additions — everything stays in `index.html`.
- Quality gate: an automated verification pass reviews the EN dictionary for naturalness, terminology consistency, and completeness (no untranslated user-facing French) before finalizing.
