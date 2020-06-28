from django.contrib import admin
from home.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/main.css',)
        }
        js = ('js/blog.js', )


admin.site.register(Blog, BlogAdmin)
admin.site.site_title = "Master-Tech786"
admin.site.site_header = "Master-Tech786"
admin.site.index_title = "Master-Tech786 Developer"