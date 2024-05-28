from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=250)
	author = models.CharField(max_length=250, null=True)
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	is_best_seller = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.title}, {self.author}, ({self.rating})' 
