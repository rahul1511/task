from django.contrib import admin
from apiapp.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['user','title','content','posted_date']

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)