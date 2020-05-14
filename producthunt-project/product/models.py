from django.db import models
# import Django's User model
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    # CASCADE means when user deletes their account, all things connected with it get deleted too
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
