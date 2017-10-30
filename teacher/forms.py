from django import forms

from main.models import Degree, Bid

# New Job/post form for students
class DegreeForm(forms.ModelForm):
	class Meta:
		model = Degree
		fields = [
			"resume",
			"degree"
		]


# New Job/post form for students
class BidForm(forms.ModelForm):
	class Meta:
		model = Bid
		fields = [
			"proposal",
			"amt"
		]