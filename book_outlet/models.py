from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Address(models.Model):
  street = models.CharField(max_length=250)
  city = models.CharField(max_length=50)
  
  def __str__(self):
    return f'{self.street}, {self.city}'
  
  class Meta:
    verbose_name_plural = "Address Entries"

class Publisher(models.Model):
  name = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  def __str__(self):
    return f'{self.name}'
  
class Author(models.Model):
  name = models.CharField(max_length=250)
  address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
  
  def __str__(self):
    return f'{self.name}'

class Book(models.Model):
	title = models.CharField(max_length=250)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	is_best_seller = models.BooleanField(default=False)
	slug = models.SlugField(default='', null=False, db_index=True)
	publisher = models.ManyToManyField(Publisher, null=True)

	def get_absolute_url(self):
		return reverse('book-detail', args=[self.slug])

	def __str__(self):
		return f'{self.title}'
