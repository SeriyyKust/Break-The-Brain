from django.urls import path
from .views import ProfilesListView, ProfilesDetailView, RegistrationProfilesView, LoginProfilesView, logout_profiles, \
    ProfilesMyPage


urlpatterns = [
    path('all/', ProfilesListView.as_view(), name="all_profiles"),
    path('<int:user_id>/', ProfilesDetailView.as_view(), name="detail_profiles"),
    path('my-page/', ProfilesMyPage.as_view(), name="my_page"),
    path('registration/', RegistrationProfilesView.as_view(), name="registration_profiles"),
    path('login/', LoginProfilesView.as_view(), name="login_profiles"),
    path('logout/', logout_profiles, name="logout_profiles"),
]