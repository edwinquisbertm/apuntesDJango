from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from products.models import Product
from .forms import ProductForm
from .serializers import ProductSerializer
from rest_framework import response


# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    template_name = "products/list_product.html"
    model = Product
    context_object_name = "products"
    paginate_by = 5


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return response.Response(serializer.data)
