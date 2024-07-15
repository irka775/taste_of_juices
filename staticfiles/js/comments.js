document.addEventListener("DOMContentLoaded", function () {
    // editButtons.forEach(button => {
    //     button.addEventListener("click", function() {
    //         const commentId = this.getAttribute("data-comment-id");
    //         const commentContent = document.getElementById(`comment${commentId}`).innerText.trim();
    //         commentText.value = commentContent;
    //         submitButton.innerText = "Update";
    //         const slug = window.location.pathname.split('/')[1];
    //         commentForm.setAttribute("action", `/${slug}/edit_comment/${commentId}/`);
    //     });
    // });

    // deleteButtons.forEach(button => {
    //     button.addEventListener("click", function() {
    //         const commentId = this.getAttribute("data-comment-id");
    //         const slug = window.location.pathname.split('/')[1];
    //         deleteConfirm.href = `/${slug}/delete_comment/${commentId}/`;
    //         deleteModal.show();
    //     });
    // });

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

});
