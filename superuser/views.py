from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.contrib.auth.models import User, Group
from main.models import Job, Bid, Solution, Student_profile, Teacher_profile, Degree
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def superuser_desk(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			job_active = Job.objects.filter(status=0)
			active_count = job_active.count()
			complete_bid = Bid.objects.filter(status=2)
			completed_count = complete_bid.count()		
			context = {		
				"active": active_count,
				"complete_bid": completed_count,	
			}
			return render(request,"superuser/index.html", context)



#active projects view here
def active_projects(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			projects = Job.objects.filter(status=0).order_by("-id")
			job_active = Job.objects.filter(status=0)
			active_count = job_active.count()
			job_under_process = Job.objects.filter(status=1)
			under_process_count = job_under_process.count()
			job_closed = Job.objects.filter(status=2)
			closed_count = job_closed.count()
			context = {
				"title":"Active Projects",
				"object": projects,
				"active": active_count,
				"under_process": under_process_count,
				"closed": closed_count,
			}
			return render(request,"superuser/active_projects.html", context)



#under_process projects view here
def under_process_projects(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			projects = Job.objects.filter(status=1).order_by("-id")
			job_active = Job.objects.filter(status=0)
			active_count = job_active.count()
			job_under_process = Job.objects.filter(status=1)
			under_process_count = job_under_process.count()
			job_closed = Job.objects.filter(status=2)
			closed_count = job_closed.count()
			context = {
				"title":"Under Process Projects",
				"object": projects,
				"active": active_count,
				"under_process": under_process_count,
				"closed": closed_count,
			}
			return render(request,"superuser/under_process_projects.html", context)




#closed projects view here
def closed_projects(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			projects = Job.objects.filter(status=2).order_by("-id")
			job_active = Job.objects.filter(status=0)
			active_count = job_active.count()
			job_under_process = Job.objects.filter(status=1)
			under_process_count = job_under_process.count()
			job_closed = Job.objects.filter(status=2)
			closed_count = job_closed.count()
			context = {
				"title":"Closed Projects",
				"object": projects,
				"active": active_count,
				"under_process": under_process_count,
				"closed": closed_count,
			}
			return render(request,"superuser/closed_projects.html", context)





#View projects view here
def view_project(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			instance = get_object_or_404(Job, id=id)
			context = {
				"instance": instance,
			}
			return render(request,"superuser/view_project.html", context)




#active bid view here
def active_bids(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			bid_list = Bid.objects.filter(status=0).order_by("-id")
			active_count = bid_list.count()
			accept_bid = Bid.objects.filter(status=1)
			accepted_count = accept_bid.count()
			complete_bid = Bid.objects.filter(status=2)
			completed_count = complete_bid.count()
			close_bid = Bid.objects.filter(status=3)
			closed_count = close_bid.count()
			context = {
				"title": "Active Bids",
				"object": bid_list,
				"active": active_count,
				"accepted": accepted_count,
				"complete": completed_count,
				"close": closed_count,
			}
			return render(request,"superuser/active_bids.html", context)



#accepted bid view here
def accepted_bids(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			bid_list = Bid.objects.filter(status=0)
			active_count = bid_list.count()
			accept_bid = Bid.objects.filter(status=1).order_by("-id")
			accepted_count = accept_bid.count()
			complete_bid = Bid.objects.filter(status=2)
			completed_count = complete_bid.count()
			close_bid = Bid.objects.filter(status=3)
			closed_count = close_bid.count()
			context = {
				"title": "Accepted Bids",
				"object": accept_bid,
				"active": active_count,
				"accepted": accepted_count,
				"complete": completed_count,
				"close": closed_count,
			}
			return render(request,"superuser/accepted_bids.html", context)



#completed bid view here
def completed_bids(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			bid_list = Bid.objects.filter(status=0)
			active_count = bid_list.count()
			accept_bid = Bid.objects.filter(status=1)
			accepted_count = accept_bid.count()
			complete_bid = Bid.objects.filter(status=2).order_by("-id")
			completed_count = complete_bid.count()
			close_bid = Bid.objects.filter(status=3)
			closed_count = close_bid.count()
			context = {
				"title": "Completed Bids",
				"object": complete_bid,
				"active": active_count,
				"accepted": accepted_count,
				"complete": completed_count,
				"close": closed_count,
			}
			return render(request,"superuser/completed_bids.html", context)






#closed bid view here
def closed_bids(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			bid_list = Bid.objects.filter(status=0)
			active_count = bid_list.count()
			accept_bid = Bid.objects.filter(status=1)
			accepted_count = accept_bid.count()
			complete_bid = Bid.objects.filter(status=2)
			completed_count = complete_bid.count()
			close_bid = Bid.objects.filter(status=3).order_by("-id")
			closed_count = close_bid.count()
			context = {
				"title": "Closed Bids",
				"object": close_bid,
				"active": active_count,
				"accepted": accepted_count,
				"complete": completed_count,
				"close": closed_count,
			}
			return render(request,"superuser/close_bids.html", context)





#View bid view here
def view_bid(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			instance = get_object_or_404(Bid, id=id)
			context = {
				"instance": instance,
			}
			return render(request,"superuser/view_bid.html", context)





#New Solution List view here
def new_solution(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			new_sol = Solution.objects.filter(status=0).order_by("-id")
			new_count = new_sol.count()
			old_sol = Solution.objects.filter(status=1)
			old_count = old_sol.count()
			context = {
				"title": "New Solutions",
				"new_count": new_count,
				"old_count": old_count,
				"object": new_sol,
			}
			return render(request,"superuser/new_solution.html", context)




#Closed Solution list view here
def closed_solution(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			new_sol = Solution.objects.filter(status=0)
			new_count = new_sol.count()
			old_sol = Solution.objects.filter(status=1).order_by("-id")
			old_count = old_sol.count()
			context = {
				"title": "Reviewed Solutions",
				"new_count": new_count,
				"old_count": old_count,
				"object": old_sol,
			}
			return render(request,"superuser/closed_solution.html", context)





#View solution view here
def view_solution(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			solution = get_object_or_404(Solution, id=id)
			job = solution.job_id
			bid = solution.bid_id
			job_info = get_object_or_404(Job, id=job)
			bid_info = get_object_or_404(Bid, id=bid)
			context = {
				"solution": solution,
				"job": job_info,
				"bid": bid_info,
			}
			return render(request,"superuser/view_solution.html", context)





#New Degrees List view here
def new_degrees(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			new_degree = Degree.objects.filter(permission=0).order_by("-id")
			new_count = new_degree.count()
			accepted_degree = Degree.objects.filter(permission=1)
			accepted_count = accepted_degree.count()
			rejected_degree = Degree.objects.filter(permission=2)
			rejected_count = rejected_degree.count()
			context = {
				"title": "New Degrees",
				"new_count": new_count,
				"accepted_count": accepted_count,
				"rejected_count": rejected_count,
				"object": new_degree,
			}
			return render(request,"superuser/new_degrees.html", context)




#Accepted Degrees List view here
def accepted_degrees(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			new_degree = Degree.objects.filter(permission=0)
			new_count = new_degree.count()
			accepted_degree = Degree.objects.filter(permission=1).order_by("-id")
			accepted_count = accepted_degree.count()
			rejected_degree = Degree.objects.filter(permission=2)
			rejected_count = rejected_degree.count()
			context = {
				"title": "Accepted Degrees",
				"new_count": new_count,
				"accepted_count": accepted_count,
				"rejected_count": rejected_count,
				"object": accepted_degree,
			}
			return render(request,"superuser/accepted_degrees.html", context)





#Accepted Degrees List view here
def rejected_degrees(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			new_degree = Degree.objects.filter(permission=0)
			new_count = new_degree.count()
			accepted_degree = Degree.objects.filter(permission=1)
			accepted_count = accepted_degree.count()
			rejected_degree = Degree.objects.filter(permission=2).order_by("-id")
			rejected_count = rejected_degree.count()
			context = {
				"title": "Rejected Degrees",
				"new_count": new_count,
				"accepted_count": accepted_count,
				"rejected_count": rejected_count,
				"object": rejected_degree,
			}
			return render(request,"superuser/rejected_degrees.html", context)						



#View bid view here
def view_degree(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			instance = get_object_or_404(Degree, id=id)
			user_info = get_object_or_404(Teacher_profile, teacher_id=instance.user_id)
			context = {
				"instance": instance,
				"user": user_info,
			}
			return render(request,"superuser/view_degree.html", context)



#View bid view here
def view_normal_degree(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			instance = get_object_or_404(Degree, id=id)
			user_info = get_object_or_404(Teacher_profile, teacher_id=instance.user_id)
			context = {
				"instance": instance,
				"user": user_info,
			}
			return render(request,"superuser/view_normal_degree.html", context)




#accept degree view here
def accept_degree(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			instance = get_object_or_404(Degree, id=id)
			instance.permission = 1
			instance.save()
			txt = "New Degree Accepted By You."
			messages.success (request, txt, extra_tags= 'text-success')
			return redirect("/superuser/new_degrees/")




#View bid view here
def reject_degree(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'superuser':
			instance = get_object_or_404(Degree, id=id)
			instance.permission = 2
			instance.save()
			txt = "New Degree Rejected By You."
			messages.success (request, txt, extra_tags= 'text-success')
			return redirect("/superuser/new_degrees/")





#logout view
def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect("/")