from .models import Task, PhotoElementQuestion
from .models import BASE_ELEMENT_QUESTION_PHOTO_CATEGORY, BASE_QUESTION_TEXT_CATEGORY, BASE_QUESTION_CHOICE_CATEGORY, \
    ANSWER_TEXT_CATEGORY, ANSWER_PHOTO_CATEGORY
from .forms import TextAnswerForm, ChoiceAnswerForm, ChoiceWithPhotoAnswerForm


class FormManagerTask:
    @staticmethod
    def get_forms_list(task=None, task_slug=None):
        task = FormManagerTask.__get_task(task, task_slug)
        questions_forms_list = []
        for base_question in task.questions.all():
            questions_forms_list.append({"photo_label": FormManagerTask.__get_photo_label_from_question(base_question),
                                         "form": FormManagerTask.__get_form_from_question(base_question)})
        return questions_forms_list

    @staticmethod
    def check_forms_with_answers(answer_dict, task=None, task_slug=None):
        task = FormManagerTask.__get_task(task, task_slug)
        count_point = 0
        for base_question in task.questions.all():
            form = FormManagerTask.__get_form_from_question(base_question, answer_dict=answer_dict)
            if form.is_valid():
                if base_question.check_answer(form.cleaned_data):
                    count_point += base_question.cost
        return count_point

    @staticmethod
    def __get_task(task=None, task_slug=None):
        if task is not None:
            return task
        elif task_slug is not None:
            return Task.objects.get(slug=task_slug)
        else:
            raise TypeError("'task' and 'task_slug' cannot be both equals None")

    @staticmethod
    def __get_photo_label_from_question(base_question):
        if base_question.question.category == BASE_ELEMENT_QUESTION_PHOTO_CATEGORY:
            return (PhotoElementQuestion.objects.get(pk=base_question.question.pk)).photo
        return None

    @staticmethod
    def __get_form_from_question(base_question, answer_dict=None):
        if answer_dict is None:
            if base_question.category == BASE_QUESTION_TEXT_CATEGORY:
                return TextAnswerForm(base_question)
            elif base_question.category == BASE_QUESTION_CHOICE_CATEGORY:
                if base_question.correct_answer.category == ANSWER_TEXT_CATEGORY:
                    return ChoiceAnswerForm(base_question)
                elif base_question.correct_answer.category == ANSWER_PHOTO_CATEGORY:
                    return ChoiceWithPhotoAnswerForm(base_question)
            else:
                return None
        else:
            if base_question.category == BASE_QUESTION_TEXT_CATEGORY:
                return TextAnswerForm(base_question,
                                      {base_question.question.text: answer_dict[base_question.question.text]})
            elif base_question.category == BASE_QUESTION_CHOICE_CATEGORY:
                if base_question.correct_answer.category == ANSWER_TEXT_CATEGORY:
                    return ChoiceAnswerForm(base_question,
                                            {base_question.question.text: answer_dict[base_question.question.text]})
                elif base_question.correct_answer.category == ANSWER_PHOTO_CATEGORY:
                    return ChoiceWithPhotoAnswerForm(base_question,
                                                     {base_question.question.text: answer_dict[base_question.question.text]})
            else:
                return None
