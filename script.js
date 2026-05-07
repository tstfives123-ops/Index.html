/**
 * HAMZA BLOG — script.js
 * Smooth interactions, animations, and dynamic behaviour
 */

/* ============================================================
   1. LOADER
============================================================ */
window.addEventListener('load', () => {
  const loader = document.getElementById('loader');
  // Wait for loader animation to complete, then hide
  setTimeout(() => {
    loader.classList.add('hidden');
    document.body.style.overflow = '';
    // Trigger initial reveal animations
    checkReveal();
  }, 2000);
});

// Prevent scroll during load
document.body.style.overflow = 'hidden';


/* ============================================================
   2. CUSTOM CURSOR GLOW
============================================================ */
const cursorGlow = document.getElementById('cursorGlow');

document.addEventListener('mousemove', (e) => {
  // Smooth cursor follow with slight lag
  requestAnimationFrame(() => {
    cursorGlow.style.left = e.clientX + 'px';
    cursorGlow.style.top  = e.clientY + 'px';
  });
});

// Hide cursor glow on touch devices
document.addEventListener('touchstart', () => {
  cursorGlow.style.display = 'none';
});


/* ============================================================
   3. NAVIGATION — blur on scroll + active links
============================================================ */
const nav       = document.getElementById('mainNav');
const navLinks  = document.querySelectorAll('.nav__link');
const sections  = document.querySelectorAll('section[id]');

let lastScroll = 0;

window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;

  // Add blur class once scrolled past 60px
  if (scrollY > 60) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }

  lastScroll = scrollY;

  // Active nav link
  updateActiveLink();

  // Reveal animations on scroll
  checkReveal();

  // Counter animation trigger
  triggerCounters();
});

function updateActiveLink() {
  let current = '';

  sections.forEach(section => {
    const sectionTop    = section.offsetTop - 120;
    const sectionBottom = sectionTop + section.offsetHeight;
    if (window.scrollY >= sectionTop && window.scrollY < sectionBottom) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('data-section') === current) {
      link.classList.add('active');
    }
  });
}


/* ============================================================
   4. MOBILE HAMBURGER MENU
============================================================ */
const hamburger  = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger.addEventListener('click', () => {
  const isOpen = mobileMenu.classList.toggle('open');
  hamburger.classList.toggle('open', isOpen);
  hamburger.setAttribute('aria-expanded', isOpen);
  mobileMenu.setAttribute('aria-hidden', !isOpen);
});

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav__mobile-link').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', false);
    mobileMenu.setAttribute('aria-hidden', true);
  });
});

// Close menu on outside click
document.addEventListener('click', (e) => {
  if (!nav.contains(e.target)) {
    mobileMenu.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', false);
    mobileMenu.setAttribute('aria-hidden', true);
  }
});


/* ============================================================
   5. SMOOTH SCROLLING (anchor links)
============================================================ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (!target) return;

    e.preventDefault();

    const navHeight = nav.offsetHeight;
    const targetTop = target.getBoundingClientRect().top + window.scrollY - navHeight;

    window.scrollTo({
      top: targetTop,
      behavior: 'smooth'
    });
  });
});


/* ============================================================
   6. TYPING EFFECT — Hero headline
============================================================ */
const typedEl   = document.getElementById('typedText');
const phrases   = [
  'ORDINARY',
  'POSSIBLE',
  'THINKING',
  'EXPECTED',
  'LIMITS'
];

let phraseIndex = 0;
let charIndex   = 0;
let isDeleting  = false;
let typingTimeout;

function type() {
  const currentPhrase = phrases[phraseIndex];
  const displayText   = isDeleting
    ? currentPhrase.substring(0, charIndex - 1)
    : currentPhrase.substring(0, charIndex + 1);

  typedEl.textContent = displayText;

  if (!isDeleting) charIndex++;
  else             charIndex--;

  let delay = isDeleting ? 60 : 100;

  if (!isDeleting && charIndex === currentPhrase.length) {
    // Pause at end of phrase
    delay = 2000;
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting  = false;
    phraseIndex = (phraseIndex + 1) % phrases.length;
    delay = 400;
  }

  typingTimeout = setTimeout(type, delay);
}

// Start typing after loader
setTimeout(type, 2200);


/* ============================================================
   7. SCROLL REVEAL ANIMATIONS
============================================================ */
const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');

function checkReveal() {
  const windowHeight = window.innerHeight;

  revealElements.forEach(el => {
    const rect = el.getBoundingClientRect();
    const triggerPoint = windowHeight * 0.88;

    if (rect.top < triggerPoint) {
      el.classList.add('visible');
    }
  });
}

// Initial check (for elements in view on load)
setTimeout(checkReveal, 100);


/* ============================================================
   8. ANIMATED COUNTERS — Hero stats
============================================================ */
const counterEls   = document.querySelectorAll('.hero__stat-num[data-target]');
let countersStarted = false;

function animateCounter(el) {
  const target   = parseInt(el.getAttribute('data-target'), 10);
  const duration = 1800;
  const start    = performance.now();

  function update(now) {
    const elapsed  = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(eased * target);

    el.textContent = current >= 1000
      ? current.toLocaleString()
      : current;

    if (progress < 1) requestAnimationFrame(update);
    else el.textContent = target >= 1000 ? target.toLocaleString() : target;
  }

  requestAnimationFrame(update);
}

function triggerCounters() {
  if (countersStarted) return;

  counterEls.forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.9) {
      countersStarted = true;
      counterEls.forEach(counter => animateCounter(counter));
    }
  });
}


/* ============================================================
   9. PARALLAX — Hero orbs on mouse move
============================================================ */
const heroSection = document.querySelector('.hero');
const orb1 = document.querySelector('.hero__orb--1');
const orb2 = document.querySelector('.hero__orb--2');
const orb3 = document.querySelector('.hero__orb--3');

if (heroSection) {
  heroSection.addEventListener('mousemove', (e) => {
    const rect = heroSection.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width  - 0.5;  // -0.5 to 0.5
    const y = (e.clientY - rect.top)  / rect.height - 0.5;

    requestAnimationFrame(() => {
      if (orb1) orb1.style.transform = `translate(${x * -30}px, ${y * -20}px)`;
      if (orb2) orb2.style.transform = `translate(${x *  20}px, ${y *  15}px)`;
      if (orb3) orb3.style.transform = `translate(${x * -15}px, ${y *  25}px)`;
    });
  });
}


/* ============================================================
   10. PARTICLE CANVAS — Hero background
============================================================ */
(function initParticles() {
  const canvas = document.getElementById('particleCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let particles = [];
  let animFrame;

  function resize() {
    canvas.width  = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }
  resize();
  window.addEventListener('resize', () => { resize(); initParticlesArray(); });

  class Particle {
    constructor() {
      this.reset();
    }
    reset() {
      this.x     = Math.random() * canvas.width;
      this.y     = Math.random() * canvas.height;
      this.size  = Math.random() * 1.5 + 0.3;
      this.speedX = (Math.random() - 0.5) * 0.4;
      this.speedY = (Math.random() - 0.5) * 0.4;
      this.alpha  = Math.random() * 0.5 + 0.1;
      this.color  = Math.random() > 0.7 ? '#e8ff3c' : '#3cffd4';
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      // Wrap around edges
      if (this.x < 0) this.x = canvas.width;
      if (this.x > canvas.width) this.x = 0;
      if (this.y < 0) this.y = canvas.height;
      if (this.y > canvas.height) this.y = 0;
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = this.color;
      ctx.globalAlpha = this.alpha;
      ctx.fill();
      ctx.globalAlpha = 1;
    }
  }

  function initParticlesArray() {
    const count = Math.min(Math.floor((canvas.width * canvas.height) / 12000), 80);
    particles = Array.from({ length: count }, () => new Particle());
  }

  function drawConnections() {
    const maxDist = 120;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx   = particles[i].x - particles[j].x;
        const dy   = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < maxDist) {
          const alpha = (1 - dist / maxDist) * 0.08;
          ctx.beginPath();
          ctx.strokeStyle = `rgba(232, 255, 60, ${alpha})`;
          ctx.lineWidth = 0.5;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    drawConnections();
    animFrame = requestAnimationFrame(animate);
  }

  initParticlesArray();
  animate();
})();


/* ============================================================
   11. NEWSLETTER FORM
============================================================ */
const newsletterForm    = document.getElementById('newsletterForm');
const emailInput        = document.getElementById('emailInput');
const newsletterSuccess = document.getElementById('newsletterSuccess');

if (newsletterForm) {
  newsletterForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const email = emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailRegex.test(email)) {
      emailInput.style.borderColor = '#ff4c3c';
      emailInput.focus();
      setTimeout(() => { emailInput.style.borderColor = ''; }, 2000);
      return;
    }

    // Simulate successful subscription
    const btn = newsletterForm.querySelector('.newsletter__btn');
    btn.textContent = 'Subscribed ✓';
    btn.style.background = '#3cffd4';
    btn.style.color = '#000';

    newsletterSuccess.textContent = '✦ Welcome to The Mind Report. First issue drops soon.';
    emailInput.value = '';

    setTimeout(() => {
      btn.innerHTML = 'Join Free <span class="btn__arrow">→</span>';
      btn.style.background = '';
      btn.style.color = '';
    }, 4000);
  });
}


/* ============================================================
   12. BLOG CARD TILT EFFECT
============================================================ */
const tiltCards = document.querySelectorAll('.blog-card, .cat-card, .editorial-card');

tiltCards.forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect   = card.getBoundingClientRect();
    const x      = (e.clientX - rect.left) / rect.width  - 0.5;
    const y      = (e.clientY - rect.top)  / rect.height - 0.5;
    const tiltX  = y * 6;
    const tiltY  = x * -6;

    card.style.transform = `perspective(600px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateY(-6px)`;
  });

  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
    card.style.transition = `transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)`;
  });

  card.addEventListener('mouseenter', () => {
    card.style.transition = `transform 0.1s ease`;
  });
});


/* ============================================================
   13. TICKER pause on hover
============================================================ */
const tickerTrack = document.querySelector('.ticker__track');
if (tickerTrack) {
  tickerTrack.addEventListener('mouseenter', () => {
    tickerTrack.style.animationPlayState = 'paused';
  });
  tickerTrack.addEventListener('mouseleave', () => {
    tickerTrack.style.animationPlayState = 'running';
  });
}


/* ============================================================
   14. KEYBOARD ACCESSIBILITY — focus visible
============================================================ */
document.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    document.body.classList.add('keyboard-nav');
  }
});

document.addEventListener('mousedown', () => {
  document.body.classList.remove('keyboard-nav');
});
