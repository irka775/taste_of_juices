from django.contrib import admin
from .models import Comment, JuiceRecipe, Review
from .forms import JuiceRecipeForm
from django_summernote.admin import SummernoteModelAdmin


@admin.register(JuiceRecipe)
class JuiceAdmin(SummernoteModelAdmin):
    form = JuiceRecipeForm
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "author", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = "__all__"

    class Media:
        css = {"all": ("summernote/summernote-bs4.css",)}
        js = ("summernote/summernote-bs4.js",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "post",
        "created_on",
        "approved",
        "rating",
    )  # Adăugat "rating"
    search_fields = ["author__username", "body"]
    list_filter = ("approved", "created_on")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer", "rating", "created_on")
    search_fields = ["reviewer__username"]
    list_filter = ("rating", "created_on")
