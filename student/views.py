from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.contrib.auth.models import User, Group
from main.models import Job
from django.contrib import messages


from .forms import JobForm



#######################################
#student desk main page view.
#######################################
def student_desk(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			id = request.user.id
			user = User.objects.get(username=request.user)
			group = user.groups.get()
			context = {
			"id": id,
			"group": group,
			}
			return render(request,"student/index.html", context)
		



#######################################
#create new job/post/assignment/
#######################################
def createjob(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			form = JobForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				new_job = form.save(commit=False)
				new_job.user_name = request.user
				new_job.user_id = request.user.id
				new_job.save()
				txt = "New job added successfully."
				messages.success (request, txt, extra_tags= 'text-success')
			context = {
				"form" : form,
				}
			return render(request,"student/post_job.html", context)






#######################################
#User's Active Jobs/Assignments
#######################################
def active_job(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			jobs = Job.objects.filter(user_id = request.user.id).exclude(status=2).order_by("-id")
			context = {
			"title": "Active Jobs",
			"object_list": jobs
			}
			return render(request,"student/active_job.html", context)






#######################################
#view job posts
#######################################
def view_job(request,id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			instance = get_object_or_404(Job, id=id)
			context = {
				"instance": instance,
			}
			return render(request,"student/view_job.html", context)





#######################################
#delete job posts
#######################################
def delete_job(request,id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			instance = get_object_or_404(Job, id=id)
			instance.delete()
			txt = "Job deleted by you."
			messages.success (request, txt, extra_tags= 'text-danger')
			return redirect("/student_desk/active_job/")







#######################################
#and the last user logout function 
#######################################
def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect("/")