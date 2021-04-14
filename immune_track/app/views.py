# from django.shortcuts import render, redirect, reverse
# from django.http import HttpResponseRedirect
# from django.contrib import messages


# from app.forms.personal_form import PersonalForm
# from app.selectors.personal_selector import get_personal_detail, get_personal_details


# def index_page(request):
#     return render(request, "index.html")


# def manage_details(request):

#     personal_form = PersonalForm()
#     persons = get_personal_details()

#     if request.method == "POST":
#         personal_form = PersonalForm(request.POST, request.FILES)
#         if personal_form.is_valid():
#             personal_form.save()
#             messages.success(request, 'Personal Record saved Successfully!')
#         else:
#             messages.warning(request, 'Operation Not Successfull')

#     context = {
#         "personal_form": personal_form,
#         "persons ": persons
#     }
#     return render(request, "personal_dtails/personal_list.html", context)

# # Create your views here.
