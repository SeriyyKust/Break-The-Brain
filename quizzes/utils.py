from .models import Task, PhotoElementQuestion
from profiles.utils import get_or_none
from .models import BASE_ELEMENT_QUESTION_PHOTO_CATEGORY, BASE_QUESTION_TEXT_CATEGORY, BASE_QUESTION_CHOICE_CATEGORY, \
    ANSWER_TEXT_CATEGORY, ANSWER_PHOTO_CATEGORY
from .forms import TextAnswerForm, ChoiceAnswerForm, ChoiceWithPhotoAnswerForm


class FormManagerTask:
    @staticmethod
    def get_forms_list(task=None, task_slug=None):
        """
        Create forms from Task
        :param task:
        :param task_slug:
        :return: list question's forms
        """
        task = FormManagerTask.__get_task(task, task_slug)
        questions_forms_list = []
        for base_question in task.questions.all():
            questions_forms_list.append({"photo_label": FormManagerTask.__get_photo_label_from_question(base_question),
                                         "form": FormManagerTask.__get_form_from_question(base_question)})
        return questions_forms_list

    @staticmethod
    def check_forms_with_answers(answer_dict, task=None, task_slug=None):
        """
        Checks the correctness of the solved task and counts the number of points
        :param answer_dict:
        :param task:
        :param task_slug:
        :return: number of points
        """
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
        """
        Returns Task
        :param task:
        :param task_slug:
        :return: Task
        """
        if task is not None:
            return task
        elif task_slug is not None:
            task = get_or_none(Task, slug=task_slug)
            if task is None:
                raise TypeError(f"FormManagerTask: There isn't task with slug '{task_slug}'")
            return task
        else:
            raise TypeError("'task' and 'task_slug' cannot be both equals None")

    @staticmethod
    def __get_photo_label_from_question(base_question):
        """
        If base_question has a photo, returns it, otherwise returns None
        :param base_question:
        :return: photo or None
        """
        if base_question.question.category == BASE_ELEMENT_QUESTION_PHOTO_CATEGORY:
            photo_element_question = get_or_none(PhotoElementQuestion, pk=base_question.question.pk)
            if photo_element_question is None:
                raise TypeError(f"FormManagerTask: There isn't PhotoElementQuestion with pk="
                                f"'{base_question.question.pk}'")
            return photo_element_question.photo
        return None

    @staticmethod
    def __get_form_from_question(base_question, answer_dict=None):
        """
        Returns an empty form, if answer_dict isn't None then returns form with data from answer_dict
        :param base_question:
        :param answer_dict:
        :return: Forms
        """
        if base_question.category == BASE_QUESTION_TEXT_CATEGORY:
            try:
                return TextAnswerForm(base_question,
                                      {base_question.question.text: answer_dict[base_question.question.text]})
            except TypeError:
                return TextAnswerForm(base_question)
        elif base_question.category == BASE_QUESTION_CHOICE_CATEGORY:
            if base_question.correct_answer.category == ANSWER_TEXT_CATEGORY:
                try:
                    return ChoiceAnswerForm(base_question,
                                            {base_question.question.text: answer_dict[base_question.question.text]})
                except TypeError:
                    return ChoiceAnswerForm(base_question)
            elif base_question.correct_answer.category == ANSWER_PHOTO_CATEGORY:
                try:
                    return ChoiceWithPhotoAnswerForm(base_question,
                                                        {base_question.question.text: answer_dict[base_question.question.text]})
                except TypeError:
                    return ChoiceWithPhotoAnswerForm(base_question)
        else:
            raise TypeError(f"FormManagerTask: There isn't BaseQuestion with category '{base_question.category}'")