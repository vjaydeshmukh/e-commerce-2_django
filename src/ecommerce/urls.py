"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import RedirectView

from .views import HomeView, AboutView #, contact_page #, register_page, login_page, logout_page


urlpatterns = [
  url(r'^$', HomeView.as_view(), name='home'),
  url(r'^about/$', AboutView.as_view(), name='about'),
#   url(r'^account/login/$', RedirectView.as_view(url='/login')),
#   url(r'^contact/$', contact_page, name='contact'),
#   url(r'^register/$', register_page, name='register'),
#   url(r'^login/$', login_page, name='login'),
#   url(r'^logout/$', logout_page, name='logout'),
  url(r'^settings/$', RedirectView.as_view(url='/account')),
  url(r'^accounts/$', RedirectView.as_view(url='/account')),
#   url(r'^library/$', RedirectView.as_view(url='/orders/library/')),
  url(r'^account/', include('accounts.urls', namespace='accounts')),
  url(r'^accounts/', include('accounts.passwords.urls')),
  url(r'^products/', include('products.urls', namespace='products')),
  url(r'^search/', include('search.urls', namespace='search')),
  url(r'^cart/', include('carts.urls', namespace='cart')),
  url(r'^orders/', include('orders.urls', namespace='orders')),
  url(r'^billing/', include('billing.urls', namespace='billing')),
  url(r'^address/$', RedirectView.as_view(url='/addresses')),
  url(r'^addresses/', include('addresses.urls', namespace='addresses')),
  url(r'^analytics/', include('analytics.urls', namespace='analytics')),
  url(r'^marketing/', include('marketing.urls', namespace='marketing')),
  url(r'^contact/', include('contact.urls', namespace='contact')),
  url(r'^admin/', admin.site.urls),
  
  
  url(r'^cart-api/', include('carts.api.urls', namespace='cart-api')),
]

if settings.DEBUG:
  urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
