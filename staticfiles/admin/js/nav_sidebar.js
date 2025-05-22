// Add shadow to navbar on scroll
window.addEventListener('scroll', function () {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 20) {
    navbar.classList.add('shadow');
  } else {
    navbar.classList.remove('shadow');
  }
});

// Collapse mobile menu after clicking a nav link
document.addEventListener('DOMContentLoaded', function () {
  const navLinks = document.querySelectorAll('.navbar-collapse .nav-link');
  const navbarCollapse = document.querySelector('.navbar-collapse');

  navLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      const isExpanded = navbarCollapse.classList.contains('show');
      if (isExpanded) {
        new bootstrap.Collapse(navbarCollapse).hide();
      }
    });
  });
});

