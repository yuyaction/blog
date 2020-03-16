from django.contrib import admin
#markdownx関連
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from markdownx.models import MarkdownxField
#自作モデル
from .models import Home, Post, Tag
# Register your models here.

# Preview of Markdown to HTML
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }

    #タグを昇順にする
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tags":
            kwargs["queryset"] = Tag.objects.order_by('name')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

class HomeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }

admin.site.register(Home,HomeAdmin)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)

