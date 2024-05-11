from django.contrib import admin
from .models import Signup,Admission,User_login,Admin,Car_parking,Library,Fee,Repeat_course,Scholarship,Scholarship_data

# Register your models here.
admin.site.register(Signup)
admin.site.register(Admission)
admin.site.register(User_login)
admin.site.register(Admin)
admin.site.register(Car_parking)
admin.site.register(Library)
admin.site.register(Fee)
admin.site.register(Repeat_course)
admin.site.register(Scholarship)
admin.site.register(Scholarship_data)