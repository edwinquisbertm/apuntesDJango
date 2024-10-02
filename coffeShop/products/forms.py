from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", max_length=200, required=True)
    description = forms.CharField(label="Descripción", max_length=300)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2)
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)

    class Meta:
        model = Product
        fields = ["name", "description", "price", "available", "photo"]

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
