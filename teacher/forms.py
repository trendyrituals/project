from django import forms

from main.models import Degree, Bid, Solution, Teacher_profile

# New degree form
class DegreeForm(forms.ModelForm):
	class Meta:
		model = Degree
		fields = [
			"resume",
			"degree"
		]


# New bid form
class BidForm(forms.ModelForm):
	class Meta:
		model = Bid
		fields = [
			"proposal",
			"amt"
		]


# New upload solution
class SolutionForm(forms.ModelForm):
	class Meta:
		model = Solution
		fields = [
			"file"
		]



#create profile form
class CreateProfileForm(forms.ModelForm):
	class Meta:
		model = Teacher_profile
		fields = [
			"profile_picture",
			"mobile",
			"skills",
			"about",
			"paypal_email"
		]



#create profile form
class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Teacher_profile
		fields = [
			"profile_picture",
			"mobile",
			"skills",
			"about",
			"paypal_email"
		]