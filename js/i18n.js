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
