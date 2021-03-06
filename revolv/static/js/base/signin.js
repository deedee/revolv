/**
 * Show the sign up component if key is "signup" and the log in component if
 * key is "login", otherwise do nothing
 * @param {string} key component to show
 */
var showComponent = function (key) {
    if (key === "signup") {
        $(".component-row.login").slideUp(function () {
            $(".component-row.signup").slideDown();
        });
    } else if (key === "login") {
        $(".component-row.signup").slideUp(function () {
            $(".component-row.login").slideDown();
        });
    }
};

$(document).ready(function () {
    // show whichever component is relevant, either sign up or log in
    if (window.SHOULD_AUTOSHOW_COMPONENT) {
        if (window.location.hash.replace("#", "") === "signup") {
            showComponent("signup");
        } else {
            showComponent("login");
        }
    }

    $(".component-link").click(function () {
        showComponent($(this).data("component"));
    });
});
