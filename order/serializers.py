from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

	'''
	Return pizza size in cm units but we only store  numbers 30 or 50
	:param instance
	:return: details of the order
	'''

	def to_representation(self, instance):
		data = super(OrderSerializer, self).to_representation(instance)
		data['pizza_size'] += ' cm'
		return data

	class Meta:
		model = Order
		fields = ('pizza_id', 'pizza_size', 'customer_name', 'customer_address')
