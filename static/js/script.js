// Injects real world date into copyright date of footer
document.getElementById('copyright-date').innerHTML = (new Date().getFullYear());

// set timeout for message alert displays
setTimeout(function () {
    let messages = document.getElementById('message')
    let alertEl = new bootstrap.Alert(messages);
    alertEl.close();
}, 3000);