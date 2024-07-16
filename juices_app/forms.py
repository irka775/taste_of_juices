from django import forms
from .models import Comment, Review, JuiceRecipe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body", "rating")
        widgets = {
            "rating": forms.RadioSelect(
                choices=[
                    (1, "1 Star"),
                    (2, "2 Stars"),
                    (3, "3 Stars"),
                    (4, "4 Stars"),
                    (5, "5 Stars"),
                ]
            )
        }

    def save(self, commit=True):
        comment = super().save(commit=False)
        if commit:
            comment.save()
        return comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rating",)


class JuiceRecipeForm(forms.ModelForm):
    class Meta:
        model = JuiceRecipe
        fields = [
            "title",
            "slug",
            "author",
            "featured_image",
            "instructions",
            "ingredients",
            "status",
        ]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        instance = self.instance

        if instance and instance.pk:
            if JuiceRecipe.objects.filter(title=title).exclude(pk=instance.pk).exists():
                raise forms.ValidationError("A recipe with this title already exists.")
        else:
            if JuiceRecipe.objects.filter(title=title).exists():
                raise forms.ValidationError("A recipe with this title already exists.")
        return title
