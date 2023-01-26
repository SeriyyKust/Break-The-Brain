from .models import SHOP_CATEGORIES


def get_model_or_none(model_type):
    for model in SHOP_CATEGORIES:
        if str(model) == str(model_type):
            return model
    return None
