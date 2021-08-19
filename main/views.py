# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now
import datetime

def home(request):
    today = datetime.date.today()
    return render(request, "index.html", {'today': today, 'now': now()})