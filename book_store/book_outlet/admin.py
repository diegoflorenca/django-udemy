from django.contrib import admin

from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # Prepopulated field can not be read only.
    # readonly_fields = ("slug",)
    # Populated the slug field based on the title according to the 
    # model configuration it will auto slugify the title.
    prepopulated_fields = {"slug": ("title",)} 
    # Add author and rating as filter options on the right hand-side of the books page
    list_filter = ("author", "rating",)
    # Configure the displayed columns on the books page
    list_display = ("title", "author",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
