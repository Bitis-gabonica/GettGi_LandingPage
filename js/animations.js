const Animations = (() => {
  function initHero() {
    if (typeof gsap === 'undefined') return;

    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    tl.from('.hero__subtitle', { opacity: 0, y: 20, duration: 0.6, delay: 0.2 })
      .from('.hero__title', { opacity: 0, y: 40, duration: 0.8 }, '-=0.3')
      .from('.hero__description', { opacity: 0, y: 20, duration: 0.6 }, '-=0.4')
      .from('.hero__author', { opacity: 0, y: 10, duration: 0.4 }, '-=0.3')
      .from('.hero__actions', { opacity: 0, y: 20, duration: 0.5 }, '-=0.2')
      .from('.hero__visual', { opacity: 0, x: 60, duration: 1 }, '-=0.8')
      .from('.hero__line', { scaleX: 0, duration: 0.4, transformOrigin: 'right' }, '-=0.4');

    // Animate SVG circles in placeholder
    gsap.utils.toArray('.hero__illustration-placeholder circle').forEach((circle, i) => {
      gsap.from(circle, {
        scale: 0,
        opacity: 0,
        duration: 0.6,
        delay: 0.8 + i * 0.15,
        ease: 'back.out(1.7)',
        transformOrigin: 'center'
      });
    });
  }

  function init() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    // Hero entrance animation
    initHero();

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
