from django.contrib import admin

from .models import Job, Degree, Bid, Solution, Bid_count, Student_profile, Teacher_profile, Messages


################################
#Job model here.
################################
class JobAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","file","user_name","subject","timestamp"]
	list_filter = ["timestamp","subject"]
	search_fields = ["job_title", "user_name","subject","id"]
	class Meta:
		model = Job




################################
#Degree model here.
################################
class DegreeAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","user_name"]
	list_filter = ["user_name"]
	search_fields = ["user_name","user_id"]
	class Meta:
		model = Degree




################################
#Bid model here.
################################
class BidAdmin(admin.ModelAdmin):
	list_display = ["job_id","id"]
	list_filter = ["job_id","id"]
	search_fields = ["job_id","id"]
	class Meta:
		model = Bid
		



################################
#Bid_count model here.
################################
class Bid_countAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","user_name"]
	list_filter = ["user_id"]
	search_fields = ["user_id", "user_name"]
	class Meta:
		model = Bid_count



################################
#solution model here.
################################
class SolutionAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","job_id"]
	list_filter = ["job_id","bid_id"]
	search_fields = ["job_id","bid_id"]
	class Meta:
		model = Solution

################################
#student profile model here.
################################
class Student_profile_Admin(admin.ModelAdmin):
	list_display = ["__unicode__","std_id"]
	list_filter = ["std_id"]
	search_fields = ["std_id"]
	class Meta:
		model = Student_profile


################################
#Teacher profile model here.
################################
class Teacher_profile_Admin(admin.ModelAdmin):
	list_display = ["__unicode__","teacher_id"]
	list_filter = ["teacher_id"]
	search_fields = ["teacher_id"]
	class Meta:
		model = Teacher_profile


################################
#Messages model here.
################################
class Messages_Admin(admin.ModelAdmin):
	list_display = ["__unicode__"]
	list_filter = ["email"]
	search_fields = ["email"]
	class Meta:
		model = Messages



admin.site.register(Job, JobAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Bid_count, Bid_countAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Student_profile, Student_profile_Admin)
admin.site.register(Teacher_profile, Teacher_profile_Admin)
admin.site.register(Messages, Messages_Admin)