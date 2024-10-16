from django.contrib import admin
# Register your models here.
from .models import doorRelease

class doorReleaseAdminn(admin.ModelAdmin):
	list_display=('userid','recdate','success')

admin.site.register(doorRelease,doorReleaseAdminn)
