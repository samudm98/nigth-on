from django.urls import path

from nigth_on.pubs.views import ListPubs, DetailPub, CommentList

app_name = "pubs"

urlpatterns = [
    path("", view=ListPubs.as_view(), name="list_pubs"),
    path("<int:id>/", view=DetailPub.as_view(), name="detail_pubs"),
    path("comments/", view=CommentList.as_view(), name="comments")
]
