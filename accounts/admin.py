from django.contrib import admin
from accounts.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ()
    fieldsets = ()
    readonly_fields = ()
    inlines = []
    actions = []
    date_hierarchy = 'date_joined'
    save_on_top = True
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ()
    show_full_result_count = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    delete_confirmation_template = 'admin/delete_confirmation.html'
    delete_selected_confirmation_template = 'admin/delete_selected_confirmation.html'
    change_list_template = 'admin/change_list.html'
    change_form_template = 'admin/change_form.html'
    add_form_template = 'admin/change_form.html'
    object_history_template = 'admin/object_history.html'
    popup_response_template = 'admin/popup_response.html'
    prepopulated_fields = {}
    radio_fields = {}
    raw_id_fields = ()
    readonly_fields = ()
    search_fields = ()
    show_full_result_count = True
    view_on_site = True
    actions_on_top = True
    # actions_on_bottom = True
    actions_on_top = True
    actions_selection_counter = True
    actions = ['make_published']

admin.site.register(User,UserAdmin)


