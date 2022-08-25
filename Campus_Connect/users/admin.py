from django.contrib import admin
from . models import blog, profile
from . models import tags

admin.site.register(profile)
admin.site.register(tags)
admin.site.register(blog)