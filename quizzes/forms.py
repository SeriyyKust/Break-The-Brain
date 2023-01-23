from django import forms
from django.utils.safestring import mark_safe
from django.forms.widgets import RadioSelect
from .models import TEXT_ANSWER_TEXT_MAX_LENGTH
from .models import ChoiceQuestion, PhotoAnswer


class TextAnswerForm(forms.Form):
    def __init__(self, question,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[question.question.text] = forms.CharField(label=question.question.text, max_length=TEXT_ANSWER_TEXT_MAX_LENGTH)


class ChoiceAnswerForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choice_question = ChoiceQuestion.objects.get(slug=question.slug)
        choice_list = ((answer, answer) for answer in choice_question.get_shuffle_answer_list())
        self.fields[question.question.text] = forms.ChoiceField(label=question.question.text, choices=choice_list, widget=RadioSelect)


class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return mark_safe("<img src='%s'/>" % obj.photo.url)


class ChoiceWithPhotoAnswerForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choice_question = ChoiceQuestion.objects.get(slug=question.slug)
        answer_list = [element.pk for element in choice_question.get_shuffle_answer_list()]
        choice_queryset = PhotoAnswer.objects.filter(pk__in=answer_list).order_by('?')
        self.fields[question.question.text] = CustomChoiceField(label=question.question.text, widget=RadioSelect,
                                                                queryset=choice_queryset)
