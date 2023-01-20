from django.urls import path
from breakthebrain import settings
from django.conf.urls.static import static
from .views import QuizzesListView, QuizzesDetailView


urlpatterns = [
    path('all_quizzes/', QuizzesListView.as_view(), name="all_quizzes"),
    path('detail_quizzes/<slug:task_slug>/', QuizzesDetailView.as_view(), name="detail_quizzes"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)