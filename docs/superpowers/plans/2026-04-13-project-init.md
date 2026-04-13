# Project Initialization — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold the GETT GI landing page project with HTML/CSS/JS vanilla, all CDN dependencies, global styles, i18n system, navbar, and an empty section structure ready for section-by-section development.

**Architecture:** Single `index.html` page with external CSS (`css/`) and JS (`js/`) files. Translations in `i18n/` JSON files. Assets placeholders in `assets/`. GSAP + ScrollTrigger + Lottie loaded via CDN. No build step.

**Tech Stack:** HTML5, CSS3 (custom properties, flexbox, grid), vanilla JS (ES modules), GSAP 3 + ScrollTrigger (CDN), Lottie player (CDN), Space Grotesk (Google Fonts)

---

### Task 1: Create folder structure

**Files:**
- Create: `css/style.css`
- Create: `css/animations.css`
- Create: `js/main.js`
- Create: `js/i18n.js`
- Create: `js/animations.js`
- Create: `i18n/fr.json`
- Create: `i18n/en.json`
- Create: `assets/images/` (directory)
- Create: `assets/lottie/` (directory)
- Create: `index.html`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p css js i18n assets/images assets/lottie
```

- [ ] **Step 2: Create index.html with CDN dependencies and empty body**

```html
<!DOCTYPE html>
<html lang="fr" data-lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GETT GI — Le gardien du bétail sénégalais</title>
  <meta name="description" content="Solution de localisation, sécurisation et identification du bétail conçue pour le Sénégal.">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/animations.css">

  <!-- GSAP + ScrollTrigger -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>

  <!-- Lottie Player -->
  <script src="https://unpkg.com/@lottiefiles/lottie-player@2.0.8/dist/lottie-player.js" defer></script>

  <!-- App Scripts -->
  <script src="js/i18n.js" defer></script>
  <script src="js/animations.js" defer></script>
  <script src="js/main.js" defer></script>
</head>
<body>

  <!-- Navbar -->
  <nav class="navbar" id="navbar">
    <div class="navbar__container">
      <a href="#" class="navbar__logo">GETT GI</a>
      <ul class="navbar__links">
        <li><a href="#hero" data-i18n="nav.solution">Solution</a></li>
        <li><a href="#probleme" data-i18n="nav.problem">Problème</a></li>
        <li><a href="#produit" data-i18n="nav.product">Produit</a></li>
        <li><a href="#contact" data-i18n="nav.contact">Contact</a></li>
      </ul>
      <div class="navbar__actions">
        <button class="lang-switch" id="lang-switch" aria-label="Switch language">EN</button>
        <a href="https://wa.me/221777778576?text=Bonjour%2C%20je%20souhaite%20demander%20une%20d%C3%A9mo%20de%20GETT%20GI." class="btn btn--primary" data-i18n="nav.cta">Demander une démo</a>
      </div>
      <button class="navbar__burger" id="burger" aria-label="Menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>

  <!-- Sections will be added one by one -->
  <main>
    <!-- Section 1: Hero (to be built next) -->
    <!-- Section 2-14: built incrementally -->
  </main>

  <footer class="footer">
    <p>&copy; 2026 GETT GI — Abdoulaye Ly</p>
  </footer>

</body>
</html>
```

- [ ] **Step 3: Commit**

```bash
git init
git add -A
git commit -m "chore: scaffold project structure with index.html and CDN deps"
```

---

### Task 2: Global CSS styles and design tokens

**Files:**
- Create: `css/style.css`

- [ ] **Step 1: Write global styles with CSS custom properties**

```css
/* ===== RESET ===== */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* ===== DESIGN TOKENS ===== */
:root {
  /* Colors */
  --color-bg-dark: #0A0A0A;
  --color-bg-light: #FFFFFF;
  --color-text-light: #FFFFFF;
  --color-text-dark: #0A0A0A;
  --color-text-muted: #A0A0A0;
  --color-accent-red: #C8102E;
  --color-accent-green: #2D6A4F;
  --color-glass: rgba(10, 10, 10, 0.8);
  --color-border: rgba(255, 255, 255, 0.1);

  /* Typography */
  --font-main: 'Space Grotesk', sans-serif;
  --fs-hero: clamp(2.5rem, 6vw, 5rem);
  --fs-h2: clamp(1.8rem, 4vw, 3rem);
  --fs-h3: clamp(1.2rem, 2.5vw, 1.8rem);
  --fs-body: clamp(1rem, 1.2vw, 1.2rem);
  --fs-small: 0.875rem;

  /* Spacing */
  --section-padding: clamp(4rem, 10vh, 8rem) clamp(1.5rem, 5vw, 6rem);
  --gap-sm: 1rem;
  --gap-md: 2rem;
  --gap-lg: 4rem;

  /* Effects */
  --blur: 20px;
  --radius: 12px;
  --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ===== BASE ===== */
html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-main);
  background-color: var(--color-bg-dark);
  color: var(--color-text-light);
  line-height: 1.6;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

img {
  max-width: 100%;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
}

/* ===== UTILITIES ===== */
.section {
  padding: var(--section-padding);
}

.section--light {
  background-color: var(--color-bg-light);
  color: var(--color-text-dark);
}

.section--dark {
  background-color: var(--color-bg-dark);
  color: var(--color-text-light);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

/* ===== BUTTONS ===== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.8rem 2rem;
  border-radius: var(--radius);
  font-family: var(--font-main);
  font-weight: 600;
  font-size: var(--fs-small);
  cursor: pointer;
  border: none;
  transition: transform var(--transition), box-shadow var(--transition);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.btn:hover {
  transform: translateY(-2px);
}

.btn--primary {
  background-color: var(--color-accent-red);
  color: var(--color-text-light);
}

.btn--primary:hover {
  box-shadow: 0 8px 30px rgba(200, 16, 46, 0.3);
}

.btn--outline {
  background: transparent;
  border: 1px solid var(--color-text-light);
  color: var(--color-text-light);
}

.btn--outline:hover {
  background: var(--color-text-light);
  color: var(--color-text-dark);
}

/* ===== NAVBAR ===== */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: var(--color-glass);
  backdrop-filter: blur(var(--blur));
  -webkit-backdrop-filter: blur(var(--blur));
  border-bottom: 1px solid var(--color-border);
}

.navbar__container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
}

.navbar__logo {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 0.1em;
}

.navbar__links {
  display: flex;
  list-style: none;
  gap: var(--gap-md);
}

.navbar__links a {
  font-size: var(--fs-small);
  font-weight: 500;
  opacity: 0.8;
  transition: opacity var(--transition);
}

.navbar__links a:hover {
  opacity: 1;
}

.navbar__actions {
  display: flex;
  align-items: center;
  gap: var(--gap-sm);
}

.lang-switch {
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text-light);
  padding: 0.4rem 0.8rem;
  border-radius: var(--radius);
  font-family: var(--font-main);
  font-size: var(--fs-small);
  font-weight: 600;
  cursor: pointer;
  transition: border-color var(--transition);
}

.lang-switch:hover {
  border-color: var(--color-text-light);
}

/* Burger menu (mobile) */
.navbar__burger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.navbar__burger span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--color-text-light);
  transition: transform var(--transition), opacity var(--transition);
}

/* ===== FOOTER ===== */
.footer {
  text-align: center;
  padding: 2rem;
  font-size: var(--fs-small);
  color: var(--color-text-muted);
  border-top: 1px solid var(--color-border);
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
  .navbar__links {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    flex-direction: column;
    background: var(--color-glass);
    backdrop-filter: blur(var(--blur));
    padding: 2rem;
    gap: 1.5rem;
    border-bottom: 1px solid var(--color-border);
  }

  .navbar__links.active {
    display: flex;
  }

  .navbar__actions .btn {
    display: none;
  }

  .navbar__burger {
    display: flex;
  }

  .navbar__burger.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }

  .navbar__burger.active span:nth-child(2) {
    opacity: 0;
  }

  .navbar__burger.active span:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -5px);
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add css/style.css
git commit -m "style: add global CSS with design tokens, navbar, and responsive layout"
```

---

### Task 3: CSS animations base

**Files:**
- Create: `css/animations.css`

- [ ] **Step 1: Write base animation classes**

```css
/* ===== SCROLL REVEAL ANIMATIONS ===== */

/* Elements start hidden, GSAP/JS will reveal them */
.reveal {
  opacity: 0;
  transform: translateY(40px);
}

.reveal--left {
  opacity: 0;
  transform: translateX(-60px);
}

.reveal--right {
  opacity: 0;
  transform: translateX(60px);
}

.reveal--scale {
  opacity: 0;
  transform: scale(0.9);
}

/* ===== BUTTON PULSE ===== */
@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(200, 16, 46, 0.4); }
  50% { box-shadow: 0 0 0 12px rgba(200, 16, 46, 0); }
}

.btn--pulse {
  animation: pulse 2.5s infinite;
}

/* ===== SMOOTH SECTION TRANSITIONS ===== */
.section {
  transition: opacity 0.6s ease;
}

/* ===== 3D TILT BASE ===== */
.tilt-3d {
  transition: transform 0.4s ease;
  transform-style: preserve-3d;
  perspective: 1000px;
}
```

- [ ] **Step 2: Commit**

```bash
git add css/animations.css
git commit -m "style: add base animation classes for scroll reveals and 3D effects"
```

---

### Task 4: i18n system

**Files:**
- Create: `i18n/fr.json`
- Create: `i18n/en.json`
- Create: `js/i18n.js`

- [ ] **Step 1: Write French translations (navbar + hero placeholders)**

```json
{
  "nav": {
    "solution": "Solution",
    "problem": "Problème",
    "product": "Produit",
    "contact": "Contact",
    "cta": "Demander une démo"
  },
  "hero": {
    "title": "Le gardien du bétail sénégalais",
    "author": "Par Abdoulaye Ly",
    "description": "GETT GI est une solution de localisation, de sécurisation et d'identification du bétail conçue pour les réalités du terrain au Sénégal.",
    "cta_demo": "Demander une démo",
    "cta_contact": "Parler à l'équipe"
  }
}
```

- [ ] **Step 2: Write English translations**

```json
{
  "nav": {
    "solution": "Solution",
    "problem": "Problem",
    "product": "Product",
    "contact": "Contact",
    "cta": "Request a demo"
  },
  "hero": {
    "title": "The guardian of Senegalese livestock",
    "author": "By Abdoulaye Ly",
    "description": "GETT GI is a livestock tracking, security, and identification solution built for the realities of Senegal.",
    "cta_demo": "Request a demo",
    "cta_contact": "Talk to the team"
  }
}
```

- [ ] **Step 3: Write i18n.js — language switching without reload**

```javascript
const I18n = (() => {
  let translations = {};
  let currentLang = localStorage.getItem('gettgi-lang') || 'fr';

  async function loadLanguage(lang) {
    const response = await fetch(`i18n/${lang}.json`);
    translations = await response.json();
    currentLang = lang;
    localStorage.setItem('gettgi-lang', lang);
    document.documentElement.lang = lang;
    document.documentElement.dataset.lang = lang;
    applyTranslations();
  }

  function applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.dataset.i18n;
      const value = getNestedValue(translations, key);
      if (value) el.textContent = value;
    });
  }

  function getNestedValue(obj, path) {
    return path.split('.').reduce((o, k) => (o || {})[k], obj);
  }

  function toggle() {
    const newLang = currentLang === 'fr' ? 'en' : 'fr';
    loadLanguage(newLang);
    return newLang;
  }

  function getLang() {
    return currentLang;
  }

  return { loadLanguage, toggle, getLang };
})();
```

- [ ] **Step 4: Commit**

```bash
git add i18n/ js/i18n.js
git commit -m "feat: add i18n system with FR/EN translations and language toggle"
```

---

### Task 5: Animation controller (GSAP)

**Files:**
- Create: `js/animations.js`

- [ ] **Step 1: Write GSAP ScrollTrigger animation controller**

```javascript
const Animations = (() => {
  function init() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    // Reveal elements on scroll
    gsap.utils.toArray('.reveal').forEach(el => {
      gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          once: true
        }
      });
    });

    gsap.utils.toArray('.reveal--left').forEach(el => {
      gsap.to(el, {
        opacity: 1,
        x: 0,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          once: true
        }
      });
    });

    gsap.utils.toArray('.reveal--right').forEach(el => {
      gsap.to(el, {
        opacity: 1,
        x: 0,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          once: true
        }
      });
    });

    gsap.utils.toArray('.reveal--scale').forEach(el => {
      gsap.to(el, {
        opacity: 1,
        scale: 1,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          once: true
        }
      });
    });
  }

  // Count-up animation for stat numbers
  function countUp(el, target, duration = 2) {
    gsap.to(el, {
      textContent: target,
      duration: duration,
      ease: 'power2.out',
      snap: { textContent: 1 },
      scrollTrigger: {
        trigger: el,
        start: 'top 85%',
        once: true
      }
    });
  }

  return { init, countUp };
})();
```

- [ ] **Step 2: Commit**

```bash
git add js/animations.js
git commit -m "feat: add GSAP ScrollTrigger animation controller with reveal and count-up"
```

---

### Task 6: Main JS entry point

**Files:**
- Create: `js/main.js`

- [ ] **Step 1: Write main.js — initializes all modules**

```javascript
document.addEventListener('DOMContentLoaded', () => {
  // Initialize i18n
  I18n.loadLanguage(I18n.getLang());

  // Language switch button
  const langSwitch = document.getElementById('lang-switch');
  if (langSwitch) {
    langSwitch.addEventListener('click', () => {
      const newLang = I18n.toggle();
      langSwitch.textContent = newLang === 'fr' ? 'EN' : 'FR';
    });
  }

  // Mobile burger menu
  const burger = document.getElementById('burger');
  const navLinks = document.querySelector('.navbar__links');
  if (burger && navLinks) {
    burger.addEventListener('click', () => {
      burger.classList.toggle('active');
      navLinks.classList.toggle('active');
    });

    // Close menu on link click
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        burger.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });
  }

  // Initialize GSAP animations
  Animations.init();
});
```

- [ ] **Step 2: Commit**

```bash
git add js/main.js
git commit -m "feat: add main.js entry point with navbar, i18n, and animation init"
```

---

### Task 7: Verify everything works

- [ ] **Step 1: Open index.html in browser and verify**

- Page loads with black background, Space Grotesk font
- Navbar is visible with glassmorphism effect
- Language switch toggles FR/EN
- Burger menu works on mobile viewport
- No console errors
- GSAP and Lottie player scripts load from CDN

- [ ] **Step 2: Final commit**

```bash
git add -A
git commit -m "chore: project scaffolding complete — ready for Hero section"
```
