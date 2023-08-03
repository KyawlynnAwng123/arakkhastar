from django.contrib import admin

from base.models import About, Category, Contact, Message, Post, Social, Tag

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug',]
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Social)
admin.site.register(Message)
admin.site.register(Post)

admin.site.site_header='Arakkhastars'
admin.site.site_title='arakkhastars project'
admin.site.site_index_title='Welcome'