from django import forms

from main.models import Job

# New Job/post form for students
class JobForm(forms.ModelForm):
	due_date = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Job
		fields = [
			"job_title",
			"subject",
			"due_date",
			"file",
			"description",
			"amt",
		]



_Choices = (
    (5,'5 Star'),
    (4,'4 Star'),
    (3,'3 Star'),
    (2,'2 Star'),
    (1,'1 Star'),
)

class ReviewForm(forms.Form):
    review = forms.ChoiceField(label='Please choose one!', choices=_Choices, widget=forms.RadioSelect())
    