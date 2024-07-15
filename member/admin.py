from django.contrib import admin

# Register your models here.
from member.models import Member,Message


class MemberAdmin(admin.ModelAdmin):
    """class for member"""
    list_display = ('id', 'name','created_at',
                    'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    inlines = []
    actions = None
    date_hierarchy = 'created_at'
    save_on_top = True
    save_as = True
    list_per_page = 20
    list_max_show_all = 200
    list_editable = ()
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {}
    # change_list_template = 'admin/organization_change_list.html'
    # change_form_template = 'admin/organization_change_form.html'
    # add_form_template = 'admin/organization_add_form.html'
    # delete_confirmation_template = 'admin/organization_delete_confirmation.html'
    # delete_selected_confirmation_template = 'admin/organization_delete_selected_confirmation.html'
    # object_history_template = 'admin/organization_object_history.html'



admin.site.register(Member,MemberAdmin)





class MessageAdmin(admin.ModelAdmin):
    """Class for customizing the admin interface for the Message model"""
    list_display = ('id', 'sender_name', 'receiver_name', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('sender_name', 'receiver_name')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)
    

    def sender_name(self, obj):
        return obj.sender.name
    sender_name.short_description = 'Sender Name'

    def receiver_name(self, obj):
        return obj.receiver.name
    receiver_name.short_description = 'Receiver Name'

admin.site.register(Message, MessageAdmin)
