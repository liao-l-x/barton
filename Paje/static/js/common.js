function my$(id) {
    return document.getElementById(id);
}

my$("dl").onclick = function () {
    name();
};

function name() {
    window.location.href = "/log.html";
}