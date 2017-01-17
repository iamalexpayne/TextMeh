from django.db import models

class UserLanguage(models.Model):
	user = models.ForeignKey('auth.User')
	language = models.CharField(max_length=50)

class Chat(models.Model):
	sender = models.ForeignKey('auth.User')
	receiver = models.ForeignKey('auth.User', related_name='receiver_user')
	message = models.CharField(max_length=5000)
	time = models.DateTimeField()

	def __str__(self):
		return "Sender: " + str(self.sender) + " | Receiver: " + str(self.receiver) + " | Message: " + self.message
