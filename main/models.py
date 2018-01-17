from __future__ import unicode_literals

from django.db import models

#################################
# Job model here.
#################################

class Job(models.Model):
	user_id = models.CharField(max_length=10)
	user_name = models.CharField(max_length=120)
	job_title = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	due_date = models.DateField(blank=False, null=True)
	file = models.FileField(blank=False, null=True)
	description = models.TextField(blank=False)
	amt = models.CharField(max_length=4, blank=False)
	status = models.CharField(max_length=1, default=0)
	got_solution = models.CharField(max_length=1, default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __unicode__(self):
		return self.job_title


################################
#Teacher degree model here.
################################

class Degree(models.Model):
	user_id = models.CharField(max_length=10)
	user_name = models.CharField(max_length=120)
	resume = models.FileField(blank=False, null=True)
	degree = models.FileField(blank=False, null=True)
	permission = models.CharField(max_length=1,default=0)


	def __unicode__(self):
		return self.user_name





################################
#Bidding model here.
################################

class Bid(models.Model):
	teacher_id = models.CharField(max_length=10)
	job_id = models.CharField(max_length=10)
	std_id = models.CharField(max_length=10)
	proposal = models.TextField(blank=False)
	amt = models.CharField(max_length=4, blank=False)
	total_amt = models.CharField(max_length=4, blank=False)
	status = models.CharField(max_length=1, default=0)
	review = models.CharField(max_length=25, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	


	def __unicode__(self):
		return self.job_id







################################
#Bidding model here.
################################

class Bid_count(models.Model):
	user_id = models.CharField(max_length=10)
	user_name = models.CharField(max_length=60)
	bid_num = models.CharField(max_length=4, blank=False)
	
	

	def __unicode__(self):
		return self.user_name






################################
#solution model here.
################################
class Solution(models.Model):
	job_id = models.CharField(max_length=10)
	std_id = models.CharField(max_length=10)
	bid_id = models.CharField(max_length=10)
	file = models.FileField(blank=False, null=True)
	status = models.CharField(max_length=1, default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)



	def __unicode__(self):
		return self.job_id



################################
#student profile model here.
################################
class Student_profile(models.Model):
	std_id = models.CharField(max_length=10)
	mobile = models.CharField(max_length=15,blank=False)
	about = models.TextField(blank=False)
	profile_picture = models.FileField(blank=False, null=True)

	def __unicode__(self):
		return self.std_id



################################
#Teacher profile model here.
################################
class Teacher_profile(models.Model):
	teacher_id = models.CharField(max_length=10)
	mobile = models.CharField(max_length=15,blank=False)
	skills = models.CharField(max_length=50,blank=False)
	about = models.TextField(blank=False)
	paypal_email = models.CharField(blank=False,max_length=50)
	profile_picture = models.FileField(blank=False, null=True)

	def __unicode__(self):
		return self.teacher_id



################################
#Messages model here.
################################
class Messages(models.Model):
	email = models.CharField(max_length=50,blank=False)
	message = models.TextField(blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	status = models.CharField(max_length=1,default=0)

	def __unicode__(self):
		return self.email