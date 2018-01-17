from django import forms

from main.models import Job, Student_profile

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
    


#create profile form
class CreateProfileForm(forms.ModelForm):
	class Meta:
		model = Student_profile
		fields = [
			"profile_picture",
			"mobile",
			"about",
		]



#create profile form
class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Student_profile
		fields = [
			"profile_picture",
			"mobile",
			"about",
		]