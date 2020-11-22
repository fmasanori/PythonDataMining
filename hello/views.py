from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configs
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def Table(request):
    #filepath = os.path.expanduser('~/Datafiles/Respiradores_em_2019.csv')

    script_dir = os.path.dirname(__file__)  # Script directory
    full_path = os.path.join(script_dir, '../Datafiles/Respiradores_em_2019.csv')

    df = pd.read_csv(full_path, delimiter=',',error_bad_lines=False)
    table_result = df.to_html()

    return HttpResponse(table_result)