from django.urls import path
from .views import ShopCategoriesView, ShopBaseBackgroundColorView, ShopTextBackgroundColorView, ShopTextTitleFontView, \
    ShopVerification


urlpatterns = [
    path('', ShopCategoriesView.as_view(), name="categories_shop"),
    path("Base-Background-Color/", ShopBaseBackgroundColorView.as_view(), name="base_background_color_shop"),
    path("Text-Background-Color/", ShopTextBackgroundColorView.as_view(), name="text_background_color_shop"),
    path("Text-Title-Font/", ShopTextTitleFontView.as_view(), name="text_title_font_shop"),
    path("Verification/", ShopVerification.as_view(), name="verification_shop"),
]

