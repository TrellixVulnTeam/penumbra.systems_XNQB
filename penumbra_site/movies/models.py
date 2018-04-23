from django.db import models

class Movie(models.Model):
	def _str_(self):
		return self.title
		
	title = models.CharField(max_length=63)
	type = models.CharField(max_length=10)
	slug = models.SlugField()
	link = models.CharField(max_length=200)
	pub_date = models.DateField()
