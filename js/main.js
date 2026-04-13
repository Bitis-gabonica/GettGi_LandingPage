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
