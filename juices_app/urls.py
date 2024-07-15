from django.urls import path, include
from .views import home, about, JuicesList, juice_detail, comment_edit, comment_delete, review_edit, review_delete, event_detail, add_review

urlpatterns = [
    path("", JuicesList.as_view(), name="home"),
    path("about/", about, name="about"),
    path("<slug:slug>/", juice_detail, name="juice_detail"),
    path("<slug:slug>/edit_comment/<int:comment_id>/", comment_edit, name="comment_edit"),
    path("<slug:slug>/delete_comment/<int:comment_id>/", comment_delete, name="comment_delete"),
    path("<slug:slug>/edit_review/<int:review_id>/", review_edit, name="review_edit"),
    path("<slug:slug>/delete_review/<int:review_id>/", review_delete, name="review_delete"),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/add_review/', add_review, name='add_review'),
]
