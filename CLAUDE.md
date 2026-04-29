# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

GETT GI is a landing page for a Senegalese livestock GPS tracking, security, and identification solution. The site is a single-page static landing page targeting herders, cooperatives, and public institutions.

## Architecture

This is a **static single-file landing page** — no build system, no bundler, no framework.

- **[index.html](index.html)** — The entire site: markup, inline `<style>`, and inline `<script>`. All CSS and JS live here.
- **[contenu.md](contenu.md)** — Full project content/copy in French (business context, stats, value props). Source of truth for all text.
- **[structure.md](structure.md)** — Defines the 14 landing page sections, their purpose, and recommended copy.

### External Dependencies (CDN-loaded)

- **Tailwind CSS** via `cdn.tailwindcss.com` (utility-first styling, no config file)
- **Iconify** via `code.iconify.design` (icon system, uses `<iconify-icon>` web component with `solar:` icon set)
- **Google Fonts**: Inter (body), Plus Jakarta Sans (`.font-jakarta`, headings), Geist (`.font-geist`, UI/labels)

### Key CSS Patterns

- Custom CSS animations defined in `<style>`: hero entrance (`hero-fade-in`), scroll reveals (`stats-reveal`, `stat-item`), SVG animations (`anim-dash`, `anim-float-*`, `anim-bar-*`)
- Parallax layering via `.hero-sticky` (sticky hero) and `.stats-over` (content slides over)
- Intersection Observer-based scroll reveal in inline `<script>` (no GSAP despite git history — previous JS files were removed)
- Design tokens: monochrome palette centered on `#1a1a1a`, `max-w-[88rem]` container, `px-6 lg:px-12` horizontal padding

## Development

**No build step.** Open `index.html` directly in a browser, or use any static file server:

```bash
# Using Python
python -m http.server 8000

# Using Node
npx serve .
```

### Reference Template

A React/Vite reference template is available at `~/Downloads/AI-Intelligence-Landing-Page-Template/` for design inspiration. It uses a different stack (React + Vite + Tailwind config) — do not copy its architecture, only reference its design patterns.

## Content & Language

- Primary language is **French**. All user-facing copy should be in French.
- The git history shows a removed i18n system (FR/EN). Current state is French-only.
- Copy source of truth: [contenu.md](contenu.md). Statistics and key figures referenced in the page come from this file.
- Contact: Abdoulaye Ly, +221 77 777 85 76, theabdoulay@gmail.com
- CTA links use WhatsApp (`wa.me/221777778576`) for demo requests and `mailto:` for general contact.

## Landing Page Section Order

Defined in [structure.md](structure.md): Hero → Chiffres du problème → Défis du terrain → Solution → Produit en action → Fonctionnalités clés → Collier → Comment ça marche → Avant/Après → Pour qui → Potentiel marché → Modèle économique → Conçu pour le Sénégal → Appel à l'action final.

## Design Direction

- Minimal, monochrome, editorial aesthetic (inspired by Esper Bionics per commit history)
- Light background with subtle vertical container lines as grid overlay
- Typography-driven: large lightweight headings, small uppercase labels
- Inline SVG illustrations preferred over image assets
- Animations: subtle, physics-based easing (`cubic-bezier(0.16, 1, 0.3, 1)`), scroll-triggered reveals
