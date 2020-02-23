# Django
from django.shortcuts import render, redirect
from django.views import View

# GeoDjango
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

# Models
from .models import Restaurant

# Utils
import django_excel as excel
from django.utils import timezone

# Tasks
from .tasks import show_hello_world
# from .generate_csv import generate_csv



class HomeView(View):
    template_name = "restaurants/index.html"

    def get(self, request, x=None, y=None, *args, **kwargs):
        """
        GET
        """
        show_hello_world.delay()
        context = {}

        if x and y:
            """
            Obtenemos los restaurantes más cercanos al usuario,
            a partir de las cordenadas obtenidas...
            """
            nearby_restaurants = Restaurant.objects.get_restaurants_near_pnt(x, y, results=20)
            context['restaurants'] = nearby_restaurants
            context['latitude'] = y
            context['longitude'] = x
        
        return render(request, self.template_name, context)


def get_csv_file(request, x, y):
    """
    Generamos el archivo CSV con los restaurantes ordenados
    según su distancia al usuario, y devolvemos el archivo CSV
    para su descarga...
    """

    export = generate_csv(x, y)

    # Creamos una string para nombrar al archivo a descargar.
    today = timezone.now()
    strToday = today.strftime("%Y/%m/%d-%H:%M:%S")
    file_name = "results-"+ strToday + ".csv"

    # Generamos el archivo CSV en memoria
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "csv", file_name=file_name)
