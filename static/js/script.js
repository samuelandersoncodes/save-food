// Injects real world date into copyright date of footer
document.getElementById('copyright-date').innerHTML = (new Date().getFullYear());

// set timeout for message alert displays
setTimeout(function () {
    let messages = document.getElementById('message')
    let alertEl = new bootstrap.Alert(messages);
    alertEl.close();
}, 3000);

// Listens to nav activities and asigns its activeness respectively 
document.addEventListener("DOMContentLoaded", function (event) {

    // This method activates nav elements upon click
    const navItems = document.getElementsByClassName("nav-item");
    const removeActiveAll = () => {
        for (let item of navItems) {
            if (item.classList.contains("active"))
                item.classList.remove("active");
        }
    };

    if (window.location.pathname == '/') {
        // Keep home nav active
        const homeNav = document.getElementById('home-nav');
        removeActiveAll();
        homeNav.classList.add("active");
    }

    if (window.location.pathname.includes('/about/')) {
        // makes about nav link active
        const aboutNav = document.getElementById('about-nav');
        removeActiveAll();
        aboutNav.classList.add("active");
    }

});