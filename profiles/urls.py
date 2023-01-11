from django.urls import path
from .views import ProfilesListView, ProfilesDetailView


urlpatterns = [
    path('all/', ProfilesListView.as_view(), name="all_profiles"),
    path('<int:user_id>/', ProfilesDetailView.as_view(), name="detail_profiles"),
]