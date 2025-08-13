from django.contrib import admin
from .models import customUser, PaymentType, RechargHistory, CardState, TravelPlanState, CardCategory, Rout, Destination, Card, Plan, TravelPlan, InterchangingPoint
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = customUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active')
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('role','address','contact_no')}),)
    

admin.site.register(customUser, CustomUserAdmin)
admin.site.register(PaymentType)
admin.site.register(RechargHistory)
admin.site.register(CardState)
admin.site.register(TravelPlanState)
admin.site.register(CardCategory)
admin.site.register(Rout)
admin.site.register(Destination)
admin.site.register(Card)
admin.site.register(Plan)
admin.site.register(TravelPlan)
admin.site.register(InterchangingPoint)
