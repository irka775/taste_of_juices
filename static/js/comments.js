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

    let stars =
        document.getElementsByClassName("star");
    let output =
        document.getElementById("output");

    // Funtion to update rating
    function gfg(n) {
        remove();
        for (let i = 0; i < n; i++) {
            if (n == 1) cls = "one";
            else if (n == 2) cls = "two";
            else if (n == 3) cls = "three";
            else if (n == 4) cls = "four";
            else if (n == 5) cls = "five";
            stars[i].className = "star " + cls;
        }
        output.innerText = "Rating is: " + n + "/5";
    }

    // To remove the pre-applied styling
    function remove() {
        let i = 0;
        while (i < 5) {
            stars[i].className = "star";
            i++;
        }
    }
});
