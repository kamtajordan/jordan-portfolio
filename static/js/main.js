// =========================================================
// KAMTA JORDAN EARTHLAB — JS PRINCIPAL
// =========================================================

document.addEventListener('DOMContentLoaded', () => {

    // ---------- MENU MOBILE ----------
    const toggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (toggle && navLinks) {
        toggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
        });

        // Ferme le menu après un clic sur un lien (mobile)
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => navLinks.classList.remove('open'));
        });
    }

    // ---------- ANIMATION AU SCROLL ----------
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.12 });

    document.querySelectorAll('.section, .card, .featured-card').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });

});
