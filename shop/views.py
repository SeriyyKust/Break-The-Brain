from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView
from django.views.generic.base import View
from profiles.utils import DataMixin, get_or_none, PointManager, VisualManager
from .models import BaseBackgroundColor, TextBackgroundColor, TextTitleFont, SHOP_CATEGORIES
from .utils import get_model_or_none


class ShopCategoriesView(DataMixin, View):
    def get(self, request):
        categories = SHOP_CATEGORIES
        context = {
            "title": "Shop Categories",
            "categories": categories
        }
        context.update(self.get_user_context())
        return render(request, "shop/categories_shop.html", context=context)


class ShopBaseBackgroundColorView(DataMixin, ListView):
    model = BaseBackgroundColor
    template_name = "shop/general_shop.html"
    context_object_name = "goods"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = BaseBackgroundColor.get_verbose_name()
        return context | self.get_user_context()


class ShopTextBackgroundColorView(DataMixin, ListView):
    model = TextBackgroundColor
    template_name = "shop/general_shop.html"
    context_object_name = "goods"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = TextBackgroundColor.get_verbose_name()
        return context | self.get_user_context()


class ShopTextTitleFontView(DataMixin, ListView):
    model = TextTitleFont
    template_name = "shop/general_shop.html"
    context_object_name = "goods"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = TextTitleFont.get_verbose_name()
        return context | self.get_user_context()


class ShopVerification(DataMixin, View):
    def get(self, request):
        model = get_model_or_none(request.GET.get("model"))
        product = get_or_none(model, pk=request.GET.get("id_product"))
        if PointManager.check_enough_points(request.user, product.price):
            PointManager.minus_points(request.user, product.price)
            VisualManager.change(request.user, product)
            return render(request, "shop/verification.html", context={"info_base": "Покупка прошла успешно!",
                                                                      "title": "Verification"})
        else:
            return render(request, "shop/verification.html", context={"info_errors": "У нас недостаточно очков!",
                                                                      "title": "Verification"})
