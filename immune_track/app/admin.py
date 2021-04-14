from django.contrib import admin
from app.models.personel_details import Personal_Data

# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = ('national_id_or_passport_no',
                    'first_name', 'last_name', 'status', 'contact', 'email',
                    'date_immunized', 'report_back_date', 'dose_status', 'photo')


admin.site.register(Personal_Data, HomeAdmin)
