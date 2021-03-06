from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('table/', hello.views.Table, name ="table"),
    path('partidos/', hello.views.Partidos, name="partidos"),
    path('analises/', hello.views.Analises, name="analises"),
    path('analises2/', hello.views.Analises2, name="analises2")
]
