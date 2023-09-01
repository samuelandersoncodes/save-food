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

});