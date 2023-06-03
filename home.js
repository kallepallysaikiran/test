
const navLinks = document.querySelectorAll('nav ul li a');

navLinks.forEach(link => {
  link.addEventListener('mouseover', () => {
    link.style.color = 'white';
  });

  link.addEventListener('mouseout', () => {
    link.style.color = '#3e1d47';
  });
});



