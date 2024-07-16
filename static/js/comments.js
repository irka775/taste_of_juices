document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll(".btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.querySelectorAll(".btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    if (commentText && commentForm && submitButton) {
        editButtons.forEach(button => {
            button.addEventListener("click", function() {
                const commentId = this.getAttribute("data-comment-id");
                if (commentId) {
                    const commentContent = document.getElementById(`comment${commentId}`).innerText.trim();
                    commentText.value = commentContent;
                    submitButton.innerText = "Update";
                    const slug = window.location.pathname.split('/')[1];
                    commentForm.setAttribute("action", `/${slug}/edit_comment/${commentId}/`);
                } else {
                    console.error('commentId este undefined');
                }
            });
        });
    } else {
        console.error('Unul sau mai multe elemente nu au fost găsite: commentText, commentForm, submitButton');
    }

    if (deleteModal && deleteConfirm) {
        deleteButtons.forEach(button => {
            button.addEventListener("click", function() {
                const commentId = this.getAttribute("data-comment-id");
                if (commentId) {
                    const slug = window.location.pathname.split('/')[1];
                    deleteConfirm.href = `/${slug}/delete_comment/${commentId}/`;
                    deleteModal.show();
                } else {
                    console.error('commentId este undefined');
                }
            });
        });
    } else {
        console.error('Unul sau mai multe elemente nu au fost găsite: deleteModal, deleteConfirm');
    }

    // Adaugă funcționalitatea de rating
    const ratingStars = document.querySelectorAll(".rating span");
    ratingStars.forEach(star => {
        star.addEventListener("click", function() {
            const rating = this.getAttribute("data-value");
            const commentId = this.parentElement.getAttribute("data-comment-id");
            const slug = window.location.pathname.split('/')[1];

            fetch(`/${slug}/rate_comment/${commentId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: JSON.stringify({ rating: rating })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    updateStars(this.parentElement, rating);
                    updateAverageRating(data.average_rating);
                }
            });
        });
    });

    function updateStars(ratingElement, rating) {
        const stars = ratingElement.querySelectorAll("span");
        stars.forEach(star => {
            if (parseInt(star.getAttribute("data-value")) <= rating) {
                star.classList.add("checked");
            } else {
                star.classList.remove("checked");
            }
        });
    }

    function updateAverageRating(averageRating) {
        document.getElementById("averageRating").innerText = averageRating;
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
