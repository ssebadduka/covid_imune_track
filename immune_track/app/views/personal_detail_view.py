from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


from app.forms.personal_form import PersonalForm
from app.selectors.personal_selector import get_personal_detail,get_personal_details


def index_page(request):
    return render(request, "index.html")

def manage_details(request):
    persons = get_personal_details()
    return render(request, 'personal_details/personal_list.html', {"persons": persons})

