from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.contrib.auth.models import User, Group

#form include here
from .forms import UserLoginForm, UserRegisterForm, UserRegisterFormTeacher


# Create your views here.
#Index view here Home page.
def index(request):
    return render(request,"index.html")





#contact us  view here contact page.  
def contact(request):
	return render(request,"contact page here user can send a message to admin or query somthing about.")





#login view where option displays student login or teacher login 
def sign_in(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user= authenticate(username=username, password=password)
		login(request, user)
		return redirect("/sign_check")
	context = {
	"form": form,
	"title": title,
	}
	return render(request,"sign_in.html",context)





#login separator for users
def sign_check(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		group = user.groups.get()
		gr = 'student'
		tr = 'teacher'
		if gr == group.name:
			return redirect("/student_desk/")
		if tr == group.name:
			return redirect("/teacher_desk/")
		#return render(request,"test.html",{"user": group})





#registration options here.
def register_here(request):
	return render(request,"registration_page.html")





#student registration form here.
def register_student(request):
	title = "Register Student"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		group = Group.objects.get(name='student')
		user.groups.add(group)
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect("/sign_check")
	context = {
	"form": form,
	"title": title,
	}
	return render(request,"register_student.html", context)





#teacher registration form here.
def register_teacher(request):
	title = "Register Teacher"
	form = UserRegisterFormTeacher(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		group = Group.objects.get(name='teacher')
		user.groups.add(group)
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect("/sign_check")
	context = {
	"form": form,
	"title": title,
	}
	return render(request,"register_teacher.html", context)

