document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll(".btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.querySelectorAll(".btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    editButtons.forEach(button => {
        button.addEventListener("click", function() {
            const commentId = this.getAttribute("data-comment-id");
            const commentContent = document.getElementById(`comment${commentId}`).innerText.trim();
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            const slug = window.location.pathname.split('/')[1];
            commentForm.setAttribute("action", `/${slug}/edit_comment/${commentId}/`);
        });
    });

    deleteButtons.forEach(button => {
        button.addEventListener("click", function() {
            const commentId = this.getAttribute("data-comment-id");
            const slug = window.location.pathname.split('/')[1];
            deleteConfirm.href = `/${slug}/delete_comment/${commentId}/`;
            deleteModal.show();
        });
    });
});
