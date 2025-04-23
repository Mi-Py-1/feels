// near real time notifications //
document.addEventListener("DOMContentLoaded", function () {
    function fetchNotifications() {
        fetch("/notifications/")  // Replace with your notifications endpoint
            .then(response => response.json())
            .then(data => {
                const notificationsDiv = document.getElementById("notifications");
                notificationsDiv.innerHTML = "";  // Clear existing notifications
                data.notifications.forEach(notification => {
                    const alertDiv = document.createElement("div");
                    alertDiv.className = `alert alert-${notification.tag} alert-dismissible fade show`;
                    alertDiv.role = "alert";
                    alertDiv.innerHTML = `
                        ${notification.message}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    `;
                    notificationsDiv.appendChild(alertDiv);
                });
            });
    }

    // Fetch notifications every 5 seconds
    setInterval(fetchNotifications, 5000);
});