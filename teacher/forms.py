from django import forms

from main.models import Degree, Bid, Solution

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