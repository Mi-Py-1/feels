document.addEventListener("DOMContentLoaded", function() {
    // Show the logout modal if redirected from the logout view
    if (window.location.search.includes("show_logout_modal=true")) {
        $('#logoutModal').modal('show');
    }
});