from django.db import models
from django.shortcuts import reverse
from Authorapp.models import Author

class Article(models.Model):
	author_id   = models.ForeignKey(Author, on_delete=models.CASCADE)
	title       = models.CharField(max_length=120)
	image       = models.ImageField()
	description = models.TextField()
	category_name = models.ForeignKey('Category', on_delete=models.CASCADE)

	def __str__(self):
		return self.title
    


class Category(models.Model):
    category_name= models.CharField(max_length=120)
    def __str__(self):
    	return self.category_name


class Comment(models.Model):
	article     = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
	name        = models.CharField(max_length=20)
	comment     = models.TextField()
	active      = models.BooleanField(default=True)
	created     = models.DateTimeField(auto_now_add=True)
	parent      = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

	class Meta:
        # sort comments in chronological order by default
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {}'.format(self.name)

	def get_absolute_url(self):
		return reverse('post_page', kwargs={
			id:article.id
    		})

	
				


		