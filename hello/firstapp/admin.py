from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ["id", "user", "total_price", "is_approved", "is_paid"]
    readonly_fields = ["user_url"]

    def user_url(self, obj):
        if social_account := obj.user.socialaccount_set.first():
            return f"https://vk.com/id{social_account.uid}"
        return None


admin.site.register(Order, OrderAdmin)
