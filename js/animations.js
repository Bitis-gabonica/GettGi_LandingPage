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
