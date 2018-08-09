from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^orders/$', views.OrderList.as_view(), name="order_list"),
	url(r'^orders/(?P<pk>\d+)/$', views.OrderDetail.as_view(), name="order_detail")
]
