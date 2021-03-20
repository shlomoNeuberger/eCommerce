
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.


class SearchListView(ListView):
    """
        A view for show all the products
    """
    template_name = 'search/view.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query:
            products = Product.objects.filter(title__icontains=query)
            if products.count() > 0:
                return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()

    def get_context_data(self, **kwargs):
        """
            This function override the defult context constractor
            we use it for adding more data to context
        """
        context = super().get_context_data(**kwargs)
        return context
