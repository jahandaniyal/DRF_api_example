# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateTestCases(APITestCase):
	url = reverse("order:order_list")

	def setUp(self):
		self.customer_name = "danny"
		self.customer_address = "5 Lynarstr."
		self.pizza_size = "30"

	def test_create_order(self):
		"""
		Test to create a new order
		"""
		response = self.client.post(self.url, {"pizza_size": "30", "customer_name": "John Cramer", "customer_address": "156b Mullerstr."})
		dataFromDb = OrderSerializer(Order.objects.get()).data
		self.assertEqual(201, response.status_code)
		self.assertEqual(response.data, dataFromDb)

	def test_get_order(self):
		"""
		Test to verify order retrieval
		"""
		Order.objects.create(customer_name='danny', customer_address="5 Lynarstr.", pizza_size='50')
		response = self.client.get(self.url)
		self.assertTrue(len(json.loads(response.content)) == Order.objects.count())


class OrderGetUpdateDeleteTestCases(APITestCase):

	def setUp(self):
		self.order = Order.objects.create(customer_name='danny', customer_address="5 Lynarstr.", pizza_size='50')
		self.url = reverse("order:order_detail", kwargs={"pk": self.order.pizza_id})

	def test_order_update(self):
		"""
		Test to verify order update
		"""
		response = self.client.put(self.url, {"pizza_size": "50", "customer_name": "Darth Vader", "customer_address": "Coruscant"})
		response_data = json.loads(response.content)
		order = Order.objects.get(pizza_id=self.order.pizza_id)
		self.assertEqual(response_data.get("customer_name"), order.customer_name)

	def test_order_partial_update(self):
		"""
		Test to verify order partial update. Only customer_name is updated
		"""
		response = self.client.put(self.url, {"customer_name": 'Batman'})
		response_data = json.loads(response.content)
		order = Order.objects.get(pizza_id=self.order.pizza_id)
		self.assertEqual(response_data.get("customer_name"), order.customer_name)

	def test_order_delete(self):
		"""
		Test to verify order deletion
		"""
		response = self.client.delete(self.url)
		self.assertEqual(204, response.status_code)