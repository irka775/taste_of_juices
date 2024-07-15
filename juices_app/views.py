from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import JuiceRecipe, Comment, Event, Review
from .forms import CommentForm, ReviewForm
from django.contrib.auth.decorators import login_required


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
            return HttpResponseRedirect(reverse("juice_detail", args=[slug]))
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
        },
    )


@login_required
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


@login_required
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


@login_required
def review_edit(request, slug, review_id):
    if request.method == "POST":
        queryset = JuiceRecipe.objects.filter(status=1)
        juice = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.reviewer == request.user:
            review = review_form.save(commit=False)
            review.event = juice
            review.save()
            messages.add_message(request, messages.SUCCESS, "Review Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating review!")

    return HttpResponseRedirect(reverse("juice_detail", args=[slug]))


@login_required
def review_delete(request, slug, review_id):
    queryset = JuiceRecipe.objects.filter(status=1)
    juice = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, "Review deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own reviews!"
        )

    return HttpResponseRedirect(reverse("juice_detail", args=[slug]))


def home(request):
    return render(request, "juices_app/home.html")


def about(request):
    return render(request, "juices_app/about.html")


@login_required
def add_review(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.event = event
            review.reviewer = request.user
            review.save()
            return redirect("event_detail", event_id=event.id)
    else:
        form = ReviewForm()
    return render(request, "juices_app/add_review.html", {"form": form, "event": event})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    reviews = Review.objects.filter(event=event)
    return render(request, "juices_app/event_details.html", {"event": event, "reviews": reviews})
