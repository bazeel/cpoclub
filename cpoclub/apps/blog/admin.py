from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Record, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    

class RecordAdmin(admin.ModelAdmin):

    list_display = ['title', 'record__user', 'date', 'active', 'public']
    list_editable = ['active', 'public']
    search_fields = ['title', 'record__user']
    inlines = [CommentInline]

    def record__user(self, obj):
        return obj.user
    record__user.short_description = _('user')


class CommentAdmin(admin.ModelAdmin):

    list_display = ['__unicode__', 'comment__user', 'date', 'active', 'comment__record' ]
    list_editable = ['active']
    search_fields = ['comment', 'comment__user', 'comment__record']

    def comment__user(self, obj):
        return obj.user
    comment__user.short_description = _('user')

    def comment__record(self, obj):
        return obj.record
    comment__record.short_description = _('record')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Record, RecordAdmin)