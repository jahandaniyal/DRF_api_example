from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer


class OrderList(APIView):
	"""
	List all orders, or create a new order.
	"""

	def get(self, request, query=None):
		orders = Order.objects.all()
		serializer = OrderSerializer(orders, many=True)
		return Response(serializer.data)

	def post(self, request, query=None):
		serializer = OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
	"""
	Retrieve, update or delete an order instance.
	"""

	def get_object(self, pk):
		try:
			return Order.objects.get(pk=pk)
		except Order.DoesNotExist:
			raise Http404

	def get(self, request, pk, query=None):
		order = self.get_object(pk)
		serializer = OrderSerializer(order)
		return Response(serializer.data)

	def put(self, request, pk, query=None):
		order = self.get_object(pk)
		serializer = OrderSerializer(order, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, query=None):
		order = self.get_object(pk)
		order.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
