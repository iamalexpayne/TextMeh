from django.db import models

class UserLanguage(models.Model):
	user = models.ForeignKey('auth.User')
	language = models.CharField(max_length=50)

	
