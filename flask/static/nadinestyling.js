// const is a keyword used to declare a constant variable (cannot be reassigned once declared)
const homelogo = document.getElementById('home-logo');
const aboutlogo = document.getElementById('about-logo');

aboutlogo.style.display = "none";

// Scroll event is added to the window to trigger the logo change when the user interacts with the window.
window.addEventListener("scroll", changeLogo)

// Function to get the position of the about-section:
function changeLogo() {
    const aboutSection = document.getElementById('about');
    const aboutSectionTop = aboutSection.offsetTop

    if (window.scrollY >= aboutSectionTop) {
        homelogo.style.display = "none";
        aboutlogo.style.display = "block";
    }
    else {
        homelogo.style.display = "block";
        aboutlogo.style.display = "none";
    }
}