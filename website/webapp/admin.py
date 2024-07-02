from django.contrib import admin

from .models import Category, Blog, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_enable"]
    @admin.display(
        boolean=True,
        ordering="name",
        description="is Enable?",
    )
    def is_enable(self, obj):
        return obj.enable

class CommentInline(admin.StackedInline):
# class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2

class BlogAdmin(admin.ModelAdmin):
    # fields = ["title", "content", "category"]
    fieldsets = [
        (None, {"fields": ["title", "content", "category"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [CommentInline]
    list_display = ["title", "pub_date", "category"]
    list_per_page = 10
    list_select_related = ["category"]
    list_filter = ["pub_date", "category"]
    search_fields = ["title"]
    ordering = ["-pub_date"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

