from	django.db	import	models
from	django.utils	import	timezone
class	Post(models.Model):
	author	=	models.ForeignKey('auth.User')
	title	=	models.CharField(max_length=200)
	text	=	models.TextField()
	created_date	=	models.DateTimeField(
									default=timezone.now)
	published_date	=	models.DateTimeField(
									blank=True,	null=True)
	name    =  models.CharField(max_length=20, null=True)
	mail    =  models.CharField(max_length=20, null=True)
	phone_number  = models.IntegerField(null=True)

	def	publish(self):
		self.published_date	=	timezone.now()
		self.save()
	def	__str__(self):
		return	self.title
