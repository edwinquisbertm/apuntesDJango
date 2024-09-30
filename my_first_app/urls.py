from django.urls import path
from .views import my_test_view, my_view, CarListView


    

urlpatterns = [
    #path("listado/", my_view),
    path("listado/", CarListView.as_view()), # se puede usar la clase en lugar de la función a traves de as_view() podemos llamar a la clase como si fuera una función
    path("detalle/<int:id>", my_test_view),
    path("marcas/<str:brand>", my_test_view),
]
