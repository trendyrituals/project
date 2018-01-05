from django.contrib import admin

from .models import Job, Degree, Bid, Solution, Bid_count


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



admin.site.register(Job, JobAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Bid_count, Bid_countAdmin)
admin.site.register(Solution, SolutionAdmin)