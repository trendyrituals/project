from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.contrib.auth.models import User, Group
from main.models import Job, Bid, Solution
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
			new_bid = Bid.objects.filter(std_id = request.user.id, status=0)
			context = {
			"id": id,
			"group": group,
			"bids": new_bid,
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
#view bid
#######################################
def view_bid(request,id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			instance = get_object_or_404(Bid, id=id)
			context = {
				"instance": instance,
			}
			return render(request,"student/view_bid.html", context)






#######################################
#accept bid
#######################################
def accept_bid(request,id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			get_status = Bid.objects.get(id=id)
			get_status.status = 1
			job_id = get_status.job_id
			get_status.save()
			instance = get_object_or_404(Job, id=job_id)
			instance.status = 1
			instance.save()
			return redirect("/student_desk/")






#######################################
#delete bid
#######################################
def delete_bid(request,id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			instance = get_object_or_404(Bid, id=id)
			instance.delete()
			return redirect("/student_desk/")




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
#get solution
#######################################
def get_solution(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			solution = Solution.objects.filter(std_id= request.user.id, status=0).order_by("-id")
			context = {
				"object" : solution,
				"title" : "Solutions",
			}
			return render(request,"student/solution_list.html", context)





#######################################
#payment page solution
#######################################
def payment(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			amt = Bid.objects.get(id=id)
			price = amt.total_amt
			request.session['bid']= id
			#print request.session['bid']
			context = {
				"price" : price
			}
			return render(request,"student/payment.html", context)




#######################################
#success payment page
#######################################
def success_payment(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			solution = get_object_or_404(Solution, bid_id=request.session['bid'])
			file = solution.file
			solution.status = 1
			solution.save()
			bid = get_object_or_404(Bid, id=request.session['bid'])
			job_id = bid.job_id
			bid.status = 3
			bid.save()
			close_job = get_object_or_404(Job, id=job_id)
			close_job.status = 2
			close_job.save()
			del request.session['bid']
			context = {
				"file" : file
			}
			return render(request,"student/success_payment.html", context)





#######################################
#cancel payment page
#######################################
def cancel_payment(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			del request.session['bid']
			context = {
				"session" : request.session['bid']
			}
			return render(request,"student/cancel_payment.html", context)





#######################################
#and the last user logout function 
#######################################
def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect("/")