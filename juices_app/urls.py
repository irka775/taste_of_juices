from django.urls import path, include
from .views import home, about, JuicesList, juice_detail, comment_edit, comment_delete

urlpatterns = [
    path("", JuicesList.as_view(), name="home"),
    path("about/", about, name="about"),
    path("<slug:slug>/", juice_detail, name="juice_detail"),
    path("<slug:slug>/edit_comment/<int:comment_id>/", comment_edit, name="comment_edit"),
    path("<slug:slug>/delete_comment/<int:comment_id>/", comment_delete, name="comment_delete"),
]
