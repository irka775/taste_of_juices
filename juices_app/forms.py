from django import forms
from .models import Comment, Review, JuiceRecipe

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment',)

class JuiceRecipeForm(forms.ModelForm):
    class Meta:
        model = JuiceRecipe
        fields = ['title', 'slug', 'author', 'featured_image', 'instructions', 'ingredients', 'status']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        instance = self.instance

        if instance and instance.pk:
            # Updating an existing instance
            if JuiceRecipe.objects.filter(title=title).exclude(pk=instance.pk).exists():
                raise forms.ValidationError("A recipe with this title already exists.")
        else:
            # Creating a new instance
            if JuiceRecipe.objects.filter(title=title).exists():
                raise forms.ValidationError("A recipe with this title already exists.")
        return title
