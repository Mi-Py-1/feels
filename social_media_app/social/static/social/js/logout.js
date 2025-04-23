function setupLogoutButton() {
    const logoutButton = document.getElementById("logout-button");
    if (logoutButton) {
        logoutButton.addEventListener("click", function () {
            fetch("/logout/", { method: "POST" })
                .then((response) => {
                    if (response.ok) {
                        window.location.assign("/");
                    }
                });
        });
    }
}

// Initialize the logout button functionality
document.addEventListener("DOMContentLoaded", setupLogoutButton);

// Export the function for testing
export { setupLogoutButton };