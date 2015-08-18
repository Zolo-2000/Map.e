from django.contrib import admin
from profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'charter', 'birthday', 'image')
	list_filter = ('user',)
	search_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)
