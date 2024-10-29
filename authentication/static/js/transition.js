document.addEventListener("DOMContentLoaded", function () {
  document.body.style.visibility = "visible";

  const links = document.querySelectorAll('a');

  links.forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();  
      const href = this.getAttribute('href');
      document.body.classList.add('fade-out');

      setTimeout(() => {
        window.location.href = href;
      }, 200);  
    });
  });
});
