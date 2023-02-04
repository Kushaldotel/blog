from django.contrib import admin
from .models import Blog, Comment

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_filter = ('title', 'slug','sno')
    list_display = ('title', 'slug')
    class Media:
        css = {
            'all': ('/static/blog/css/main.css')
            # 'all': ('blog/css/main.css')
        }
        js = ['/static/blog/js/blog.js']
        # js = ['blog/js/blog.js']
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
# admin.site.register(BlogAdmin)

