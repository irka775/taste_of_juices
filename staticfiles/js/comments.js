document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll(".btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.querySelectorAll(".btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            const slug = window.location.pathname.split('/')[1];
            commentForm.setAttribute("action", `/${slug}/edit_comment/${commentId}/`); // Adăugat slash la sfârșit
        });
    }

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            const slug = window.location.pathname.split('/')[1];
            deleteConfirm.href = `/${slug}/delete_comment/${commentId}/`; // Adăugat slash la sfârșit
            deleteModal.show();
        });
    }

    const starInputs = document.querySelectorAll('.rating input[type="radio"]');
    starInputs.forEach(input => {
        input.addEventListener('change', function() {
            const value = this.value;
            starInputs.forEach(star => {
                if (star.value <= value) {
                    star.nextElementSibling.classList.add('checked');
                } else {
                    star.nextElementSibling.classList.remove('checked');
                }
            });
        });
    });
});
