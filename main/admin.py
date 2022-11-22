from django.contrib import admin

from .models import *

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'surname', 'carnumber', 'date', 'email', 'status')
#     list_display_links = ('id', 'surname', 'carnumber')
#     search_fields = ('surname', 'carnumber')


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'car_number', 'birthdate', 'is_booking')
#     search_fields = ('car_number', 'user')

class ParkingPlaceTypeAdmin(admin.ModelAdmin):
    list_display = ('is_open', 'is_near_exit', 'is_for_disabled')


admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Parking)
admin.site.register(ParkingPlace)
admin.site.register(ParkingPlaceStatus)
admin.site.register(ParkingPlaceType, ParkingPlaceTypeAdmin)
admin.site.register(Preferences)
admin.site.register(Log)



