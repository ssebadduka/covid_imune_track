from app.models.personel_details import Personal_Data


def get_personal_details():
    return Personal_Data.objects.all()


def get_personal_detail(request_id):
    return Personal_Data.objects.get(pk=request_id)
