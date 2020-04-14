from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()

class Author(models.Model):
	name          = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
	profile_image = models.ImageField()
	about         = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name.username



class  Contact(models.Model):
	author_id    = models.ForeignKey(Author, on_delete=models.CASCADE)
	message      = models.TextField()

	def __str__(self):
		return self.author_id.name.username


				