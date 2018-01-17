from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.contrib.auth.models import User, Group
from main.models import Job, Bid, Solution, Student_profile
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


from .forms import JobForm, ReviewForm, CreateProfileForm, UpdateProfileForm



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
#Profile view here
#######################################
def profile(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			count = Student_profile.objects.filter(std_id = request.user.id)
			if count.count() == 0:
				return redirect("/student_desk/create_profile/")
			else:
				instance = get_object_or_404(Student_profile, std_id=request.user.id)
				context ={
				 "instance" : instance,
				}
				return render(request,"student/profile.html", context)


#######################################
#Create Profile view here
#######################################
def create_profile(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			form = CreateProfileForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				new_profile = form.save(commit=False)
				new_profile.std_id = request.user.id
				new_profile.save()
				txt = "Profile successfully created."
				messages.success (request, txt, extra_tags= 'text-success')
				return redirect("/student_desk/profile/")
			context = {
			 "form": form,
			}
			return render(request,"student/create_profile.html", context)


#######################################
#update Profile view here
#######################################
def update_profile(request, id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			instance = get_object_or_404(Student_profile, std_id= id)
			form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=instance)
			if form.is_valid():
				update_profile = form.save(commit=False)
				update_profile.std_id = request.user.id
				update_profile.save()
				txt = "Profile successfully updated."
				messages.success (request, txt, extra_tags= 'text-success')
				return redirect("/student_desk/profile/")
			context = {
			 "form": form,
			}
			return render(request,"student/update_profile.html", context)


	



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
#down load solution and give review
#######################################
def download_solution(request,id):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'student':
			form = ReviewForm(request.POST or None)
			solution = Solution.objects.get(bid_id= id, status=0)
			file = solution.file
			if form.is_valid():
				bid = Bid.objects.get(id=id)
				job_id = bid.job_id
				#submit review and close bid
				bid.review = form.cleaned_data['review']
				bid.status = 2
				bid.save()
				#close the solution for the review again
				sol = Solution.objects.get(job_id = job_id)
				sol.status = 1
				sol.save()
				#close project or job 
				get_job = Job.objects.get(id=job_id)
				get_job.status = 2
				get_job.save()
				return redirect("/student_desk/get_solution/")
			context = {
			"file" : file,
			"form" : form,
			}
			return render(request,"student/download_solution.html", context)





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
			#Bid accept flag update
			bid = get_object_or_404(Bid, id=request.session['bid'])
			job_id = bid.job_id
			teacher_id = bid.teacher_id
			bid.status = 1
			bid.save()
			#get teacher eamil id
			get_user = User.objects.get(id=teacher_id)
			teacher_email = get_user.email
			#Close the project from available for bid project list
			close_job = get_object_or_404(Job, id=job_id)
			close_job.status = 1
			close_job.save()
			bid_info = str(request.session['bid'])
			#send mail to student
			mail_sub = 'subject here'
			mail_message = 'payment received for bid number :' + bid_info
			sender = settings.EMAIL_HOST_USER
			to_user = [request.user.email]
			send_mail(
			    mail_sub,
			    mail_message,
			    sender,
			    to_user,
			    fail_silently=False,
			)
			#send mail to teacher
			mail_sub = 'subject here'
			mail_message = 'Bid accepted and the bid number is :' + bid_info
			sender = settings.EMAIL_HOST_USER
			to_user = [teacher_email]
			send_mail(
			    mail_sub,
			    mail_message,
			    sender,
			    to_user,
			    fail_silently=False,
			)
			del request.session['bid']
			context = {
				"text" : bid_info
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
				"session" : "request.session['bid']"
			}
			return render(request,"student/cancel_payment.html", context)





#######################################
#and the last user logout function 
#######################################
def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect("/")