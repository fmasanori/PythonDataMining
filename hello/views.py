from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import io
import requests
import urllib, pybase64
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
    # Pega o diretório atual então recupera o CSV a partir
    script_dir = os.path.dirname(__file__)  # Script directory
    full_path = os.path.join(script_dir, '../Datafiles/Respiradores_em_2019.csv')

    df = pd.read_csv(full_path, delimiter=',',error_bad_lines=False)
    table_result = df.to_html()

    return HttpResponse(table_result)


def Partidos(request):
    # Pega o diretório atual então recupera o CSV a partir
    script_dir = os.path.dirname(__file__)  # Script directory
    full_path = os.path.join(script_dir, '../Datafiles/detalhe_votacao_secao_2020_SP.csv')

    df = pd.read_csv(full_path, delimiter=',',error_bad_lines=False)
    table_result = df.to_html()

    return HttpResponse(table_result)

def Analises(request):
    # Pega o diretório atual então recupera o CSV a partir
    script_dir = os.path.dirname(__file__)  # Script directory
    full_path = os.path.join(script_dir, '../Datafiles/detalhe_votacao_secao_2020_SP.csv')

    df = pd.read_csv(full_path, delimiter=',',error_bad_lines=False)
    df = df.groupby('NR_ZONA')['QT_APTOS'].max().sort_values().tail(10).plot(kind='barh')


    fig = df.get_figure()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = pybase64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request,'analises.html',{'data': uri})

def Analises2(request):
    # Pega o diretório atual então recupera o CSV a partir
    script_dir = os.path.dirname(__file__)  # Script directory
    full_path = os.path.join(script_dir, '../Datafiles/detalhe_votacao_secao_2020_SP.csv')

    df = pd.read_csv(full_path, delimiter=',',error_bad_lines=False)
    df = df.groupby('NR_ZONA')['QT_VOTOS_NULOS'].max().sort_values().tail(20).plot(kind='barh')


    fig = df.get_figure()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = pybase64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request,'analises2.html',{'data': uri})  
