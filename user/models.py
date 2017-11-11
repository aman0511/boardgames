from django.db import models

# Create your models here.
class Blog(models.Model):
	name = models.CharField( max_length=20 )
	tagline = models.TextField()

	def __str__(self):
		return "{0} {1}".format(self.name, self.tagline)

class Author(models.Model):
	name = models.CharField( max_length= 30 )
	email = models.EmailField()

	def __str__(self):
		return "{0}".format(self.name)

class Entry(models.Model):
	blog = models.ForeignKey(Blog)
	headline = models.CharField( max_length= 30 )
	body_text = models.CharField( max_length= 100)
	put_date = models.DateField()
	mod_date = models.DateField()
	author = models.ManyToManyField(Author)
	n_comment = models.IntegerField()
	n_pingback = models.IntegerField()
	rating = models.IntegerField()

	def __str__(self):
		return "{0}".format(self.blog)