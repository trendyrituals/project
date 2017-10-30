from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User, Group
from main.models import Job, Bid, Solution, Degree, Bid_count
from django.contrib import messages


from .forms import DegreeForm, BidForm


#######################################
#teacher desk main page view.
#######################################
def teacher_desk(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'teacher':
			degree_check = Degree.objects.filter(user_id = request.user.id)
			if degree_check.count() >= 1:
				id = request.user.id
				user = User.objects.get(username=request.user)
				group = user.groups.get()
				context = {
				"id": id,
				"group": group,
				}
				return render(request,"teacher/index.html", context)
			else:
				return redirect("/teacher_desk/degree/")



#######################################
#teacher degree view.
#######################################
def degree_upload(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'teacher':
			form = DegreeForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				#saving form data
				new_degree = form.save(commit=False)
				new_degree.user_name = request.user
				new_degree.user_id = request.user.id
				new_degree.save()

				#adding bid count to the user account
				check = Bid_count.objects.filter(user_id=request.user.id)
				if check.count() ==1:
					pass
				else:
					name = str(request.user)
					ID = str(request.user.id)
					new_entry = Bid_count.objects.create(user_name= name,user_id=ID, bid_num=8)
					new_entry.save()
					
				txt = "Degree and resume added successfully."
				messages.success (request, txt, extra_tags= 'text-success')
			context = {
				"form" : form,
				}
			return render(request,"teacher/degree.html", context)






#######################################
#Search Job here. 
#######################################
def search_job(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'teacher':

			#with search field query
			query = request.GET.get("q")
			if query:
				queryset_list = Job.objects.filter(
					Q(job_title__icontains=query) |
					Q(description__icontains=query) |
					Q(subject__icontains=query) |
					Q(pk__icontains=query) 
					).distinct().order_by('-id')
				paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

				page = request.GET.get('page')
				try:
					queryset = paginator.page(page)
				except PageNotAnInteger:
				# If page is not an integer, deliver first page.
					queryset = paginator.page(1)
				except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
					queryset = paginator.page(paginator.num_pages)

				context = {
					"object_list":queryset
				}
				return render(request,"teacher/search_job.html", context)

			#without search field query
			query_list = Job.objects.filter().distinct().order_by('-id')
			paginator = Paginator(query_list, 5) # Show 25 contacts per page

			page = request.GET.get('page')
			try:
				query_set = paginator.page(page)
			except PageNotAnInteger:
			# If page is not an integer, deliver first page.
				query_set = paginator.page(1)
			except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
				query_set = paginator.page(paginator.num_pages)

			context = {
				"object_list":query_set
			}
			return render(request,"teacher/search_job.html", context)






#######################################
#view job detail view
#######################################
def view_job(request,id=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'teacher':
			instance = get_object_or_404(Job, id=id)
			context = {
				"instance": instance,
			}
			return render(request,"teacher/view_job.html", context)






#######################################
#place bid on job view
#######################################
def bid(request,id=None,std=None):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'teacher':

			form = BidForm(request.POST or None)
			
			if form.is_valid():
				bid_num = Bid_count.objects.get(user_id= request.user.id)
				num = bid_num.bid_num
				if int(num )>=1:
					# updating Bid count
					get_num = Bid_count.objects.get(user_id= request.user.id)
					num = get_num.bid_num
					up_num = int(num)-1
					get_num.bid_num = str(up_num)
					get_num.save() 

					# saving bid form data 
					new_bid = form.save(commit=False)
					new_bid.teacher_id = request.user.id
					new_bid.job_id = id
					new_bid.std_id = std
					add_tax = (float(new_bid.amt)*10)/100
					total_add = float(new_bid.amt)+add_tax
					new_bid.total_amt = total_add
					new_bid.save()

					txt = "New bid added successfully."
					messages.success (request, txt, extra_tags= 'text-success')
				else:
					return render(request,"teacher/no_bid.html")
			context = {
				"form" : form,
				}
			return render(request,"teacher/bid.html", context)








#######################################
#bid manager here where user add bid to thire account.
#######################################
def bid_manager(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		if group.name == 'teacher':
			
			context = {
				"title": "Bid manager",
			}
			return render(request,"teacher/bid_manager.html", context)










#######################################
#and the last user logout function 
#######################################
def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect("/")