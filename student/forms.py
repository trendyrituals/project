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