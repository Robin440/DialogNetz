from django.contrib import admin
from organization.models import Organization,Role,Department

# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    """class for organization"""
    list_display = ('id','name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('created_at', 'updated_at')
                }),
                )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'description')
            }),
            )
    filter_horizontal = ()
    filter_vertical = ()
    # change_list_template = 'admin/organization_change_list.html'
    # change_form_template = 'admin/organization_change_form.html'
    # add_form_template = 'admin/organization_add_form.html'
    # delete_confirmation_template = 'admin/organization_delete_confirmation.html'
    # delete_selected_confirmation_template = 'admin/organization_delete_selected_confirmation.html'
    # object_history_template = 'admin/organization_object_history.html'
  
    radio_fields = {}

admin.site.register(Organization,OrganizationAdmin)


class RoleAdmin(admin.ModelAdmin):
    """class for role"""
    list_display = ('id','name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    # change_list_template = 'admin/organization_change_list.html'
    # change_form_template = 'admin/organization_change_form.html'
    # add_form_template = 'admin/organization_add_form.html'
    # delete_confirmation_template = 'admin/organization_delete_confirmation.html'
    # delete_selected_confirmation_template = 'admin/organization_delete_selected_confirmation.html'
    # object_history_template = 'admin/organization_object_history.html'


admin.site.register(Role,RoleAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    """class for department"""
    list_display = ('id','name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    # change_list_template = 'admin/organization_change_list.html'
    # change_form_template = 'admin/organization_change_form.html'
    # add_form_template = 'admin/organization_add_form.html'
    # delete_confirmation_template = 'admin/organization_delete_confirmation.html'
    # delete_selected_confirmation_template = 'admin/organization_delete_selected_confirmation.html'
    # object_history_template = 'admin/organization_object_history.html'


admin.site.register(Department,DepartmentAdmin)