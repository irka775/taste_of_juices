from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import JuiceRecipe, Comment, Event, Review
from .forms import CommentForm, ReviewForm

class JuicesList(generic.ListView):
    queryset = JuiceRecipe.objects.filter(status=1)
    template_name = "juices_app/home.html"
    paginate_by = 4

def juice_detail(request, slug):
    queryset = JuiceRecipe.objects.filter(status=1)
    juice = get_object_or_404(queryset, slug=slug)
    comments = juice.comments.all().order_by("-created_on")
    comment_count = juice.comments.filter(approved=True).count()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = juice  
            new_comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )
            return HttpResponseRedirect(reverse('juice_detail', args=[slug]))
    else:
        comment_form = CommentForm()
    
    return render(
        request,
        "juices_app/juice_details.html",
        {
            "juice": juice,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "new_comment": new_comment,
        },
    )

def home(request):
    return render(request, "juices_app/home.html")

def about(request):
    return render(request, "juices_app/about.html")

def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = JuiceRecipe.objects.filter(status=1)
        juice = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = juice
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("juice_detail", args=[slug]))

def comment_delete(request, slug, comment_id):
    queryset = JuiceRecipe.objects.filter(status=1)
    juice = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("juice_detail", args=[slug]))
