from django import forms

from .models import Lesson, Comment, Reply

class LessonCreateForm(forms.ModelForm):
	class Meta:
		model = Lesson
		exclude = ['Standard', 'created_by', 'subject', 'slug']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']
		labels = {'body': 'Comment'}
		widgets = {
			'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':50, 'placeholder':'Comment here..'}),
		}


class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ['reply_body']
		labels = {'reply_body': 'Reply'}
		widgets = {
			'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':20}),
		}