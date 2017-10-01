from django.db import models

class blogpost(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	publication=models.DateField(blank=True)
	category=models.CharField(max_length=100)
	hero=models.ImageField(upload_to="images/")
	image=models.ImageField(upload_to="images/")
	body=models.TextField(blank=True)
	def __str__(self):
		return self.title