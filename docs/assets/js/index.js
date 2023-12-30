const toggle = document.getElementById('toggle');
const label = toggle.nextElementSibling;
const body = document.body;

// Get the dark mode preference from local storage.
const darkModePreference = localStorage.getItem('darkModePreference');

// If the dark mode preference is set, apply it to the body element.
if (darkModePreference === 'true') {
  body.classList.add('dark-theme');
  toggle.checked = true;
  label.style.backgroundImage = 'url(moon.svg)';
} else if (darkModePreference === 'false') {
  body.classList.remove('dark-theme');
  toggle.checked = false;  
  label.style.backgroundImage = 'url(sun.svg)';
}

// Add a change listener to the toggle checkbox.
toggle.addEventListener('change', () => {
  const isChecked = toggle.checked;

  // Update the dark mode preference in local storage.
  localStorage.setItem('darkModePreference', isChecked);

  // Apply the dark mode preference to the body element.
  body.classList.toggle('dark-theme');
  if(isChecked) {
    label.style.backgroundImage = 'url(moon.svg)';
  } else {
    label.style.backgroundImage = 'url(sun.svg)';
  }
});


document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach( el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });

});
