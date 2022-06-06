from django import forms

from .models import Question, Mailing


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'employed', 'studying')


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('mailing_date',)
