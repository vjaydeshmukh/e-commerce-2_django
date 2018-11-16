from django.http import JsonResponse

from carts.models import Cart

# Create your views here.

def cart_home(request):
  cart_obj, new_obj = Cart.objects.new_or_get(request)
  products = [{"name": x.name, "price": x.price} for x in cart_obj.products.all()]
  cart_data = {"products": products, "subtotal": cart_obj.subtotal, "total": cart_obj.total}
  return JsonResponse(cart_data)
