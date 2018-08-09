# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Order(models.Model):
	class Meta:
		db_table = 'order'
		ordering = ['customer_name']

	PIZZA_SIZES = (
		('30', '30cm'),
		('50', '50cm'),
	)
	pizza_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=50)
	customer_address = models.CharField(max_length=100)
	pizza_size = models.CharField(max_length=4, choices=PIZZA_SIZES)

	def __str__(self):
		return self.customer_name + ' - Pizza ID ' + str(self.pizza_id)
