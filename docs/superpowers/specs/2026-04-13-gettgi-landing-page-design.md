# GETT GI Landing Page — Design Spec

## Objectif

Landing page pour GETT GI, solution sénégalaise de localisation et sécurisation du bétail. Double cible : décrocher des contrats coopératives + convaincre investisseurs/partenaires.

## Stack technique

- **HTML / CSS / JS** : vanilla, zéro framework, zéro build
- **Style** : CSS pur (custom properties, flexbox, grid)
- **Animations** : CSS animations natives + GSAP & ScrollTrigger (CDN) pour scroll/3D
- **Illustrations** : Lottie player (CDN) pour animations vectorielles fournies par l'utilisateur
- **i18n** : script JS maison FR/EN (switch de langue sans rechargement)
- **Fonts** : Space Grotesk (Google Fonts CDN)
- **Déploiement** : Vercel / Netlify (statique)

## Design visuel

- **Palette** : Noir profond (#0A0A0A) / blanc pur, alternance entre sections
- **Accents** : Rouge premium (#C8102E) pour CTA / chiffres impactants, vert premium (#2D6A4F) pour éléments positifs
- **Style** : Minimaliste, moderne, futuriste
- **Illustrations** : Animées, minimalistes, mix de styles (line art, flat, isométrique, lottie) — assets fournis par l'utilisateur

## Navbar

- Fixe en haut, glassmorphism (noir semi-transparent + blur)
- Logo GETT GI à gauche
- Liens sections (smooth scroll)
- Sélecteur FR/EN
- Bouton CTA "Demander une démo" (accent rouge)

## Sections (14 au total, construites une par une)

Structure détaillée dans `structure.md`. Ordre :

1. Hero — titre fort, signature Abdoulaye Ly, 2 CTA, visuels app
2. Chiffres du problème — 4 stats animées (count-up)
3. Défis du terrain — 4 blocs problème (slide-in)
4. Solution — 3 piliers : Localiser, Sécuriser, Identifier (scale + fade)
5. Produit en action — screenshots app (3D tilt hover)
6. Fonctionnalités clés — 5 features (stroke animation icônes)
7. Collier — visuel collier (rotation 3D légère)
8. Comment ça marche — 3 étapes (ligne animée connectée)
9. Avant / Après — 2 colonnes (slide depuis côtés)
10. Pour qui — 3 blocs cibles (flip/reveal)
11. Potentiel marché — chiffres count-up + barres de progression
12. Modèle économique — 3 blocs (apparition progressive)
13. Conçu pour le Sénégal — fade-in doux
14. CTA final — boutons pulse, contact direct

## Animations

- **Scroll** : fade-in, slide-in, scale au défilement (GSAP ScrollTrigger + IntersectionObserver)
- **Compteurs** : count-up animé pour les chiffres (JS vanilla)
- **Transitions** : transitions fluides entre sections (CSS transitions + GSAP)
- **3D** : effets tilt légers sur certains visuels (CSS transform, pas de particules, pas d'éléments flottants)
- **Illustrations** : animations Lottie intégrées aux emplacements prévus (lottie-player CDN)

## CTAs

- "Demander une démo" → WhatsApp (+221 77 777 85 76) avec message pré-rempli
- "Contacter l'équipe" → mailto:theabdoulay@gmail.com

## Langue

- Contenu FR/EN (attributs data-i18n + fichiers JSON de traduction chargés par JS)
- Code et commentaires en anglais

## Approche de construction

Incrémentale, section par section. On commence par le scaffolding projet + Hero.
