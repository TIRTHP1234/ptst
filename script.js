const menuButton = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('.mobile-nav');

function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Open menu');
  mobileMenu.hidden = true;
  document.body.classList.remove('menu-open');
}

menuButton.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  menuButton.setAttribute('aria-label', isOpen ? 'Open menu' : 'Close menu');
  mobileMenu.hidden = isOpen;
  document.body.classList.toggle('menu-open', !isOpen);
});

mobileMenu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
document.querySelector('#year').textContent = new Date().getFullYear();

const reflection = document.querySelector('#daily-reflection');
if (reflection) {
  const prompts = [
    'What can I understand more clearly today?',
    'Where can I practise greater care in my actions?',
    'What might I learn by pausing before I respond?',
    'How can I bring more awareness to an ordinary moment?',
    'What can I release to make room for understanding?'
  ];
  const day = Math.floor(Date.now() / 86400000);
  reflection.textContent = prompts[day % prompts.length];
}
