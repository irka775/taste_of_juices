# =============================================================================
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# =============================================================================

STATUS = ((0, "Pending"), (1, "Approved"))

# =============================================================================


class JuiceRecipe(models.Model):
    title = models.CharField(max_length=200)  # Removed unique=True
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    featured_image = CloudinaryField("image", default="placeholder")
    instructions = models.TextField(blank=False)
    ingredients = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# =============================================================================


class Comment(models.Model):
    post = models.ForeignKey(
        JuiceRecipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)  # Adăugat câmpul de rating

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


# =============================================================================


# class Event(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateTimeField()
#     location = models.CharField(max_length=200)  # corectat
#     description = models.TextField()

#     def __str__(self):
#         return self.title


# =============================================================================


class Review(models.Model):
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer} for {self.event}"


# =============================================================================
