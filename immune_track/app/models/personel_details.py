from django.db import models
from django.urls import reverse


class Personal_Data(models.Model):
    national_id_or_passport_no = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[(
        'Negative', 'Negative'), ('Positive', 'Positive')], default='Negative')
    contact = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_immunized = models.DateField()
    report_back_date = models.DateField()
    dose_status = models.CharField(max_length=20, choices=[(
        'First Dose', 'First Dose'), ('Second Dose', 'Second Dose')], default='First Dose')
    photo = models.ImageField(upload_to=None, height_field=None,
                             width_field=None, max_length=None, null=True, blank=True)


class Meta:

    verbose_name = ("Personal_Data")
    verbose_name_plural = ("Personal_Datas")


def __str__(self):
    return self.national_id_or_passport_no


def get_absolute_url(self):
    return reverse("Personal_detail", kwargs={"pk": self.pk})

    

    
