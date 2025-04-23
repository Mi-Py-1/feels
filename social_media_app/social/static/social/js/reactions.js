document.addEventListener("DOMContentLoaded", function () {
    const reactionButtons = document.querySelectorAll(".reaction-button");

    reactionButtons.forEach((button) => {
        button.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default form submission

            const reactionType = this.getAttribute("data-reaction");
            const postId = this.getAttribute("data-post-id");

            fetch(`/reaction/add/${postId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify({ reaction_type: reactionType }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        alert(data.message); // Show success message
                        // Optionally, update the UI dynamically
                    } else {
                        alert(data.message); // Show error message
                    }
                })
                .catch((error) => console.error("Error:", error));
        });
    });

    // Helper function to get CSRF token
    function getCSRFToken() {
        const cookies = document.cookie.split("; ");
        for (const cookie of cookies) {
            const [name, value] = cookie.split("=");
            if (name === "csrftoken") {
                return value;
            }
        }
        return "";
    }
});