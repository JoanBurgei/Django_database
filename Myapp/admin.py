from django.contrib import admin

from Myapp.models import Books

# Register your models here.
admin.site.site_title = 'Bookshop'
admin.site.site_header = 'Bookshop Admin'
admin.site.index_title = 'Book Management System'

# register model
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display =('title','year','cost','isbn','category')
    search_fields = ('title','year','isbn','category')
    list_filter = ('year','category')
    ordering = ('-year','title')