from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

# class chat(models.Model):
#     message = models.ForeignKey(message)
#     user_ = models.ForeignKey(User, unique = True)
#     user_2 = models.ForeignKey(User, unique = True)

#     def __str__(self):
#         return '%s %s' % (self.user_, self.user_2)
        
# class message(models.Model):
#     text = models.TextField()
#     date = models.DateTimeField(auto_now_add = True)


class Serie(models.Model):
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
    (HORROR, 'Horror'),
    (COMEDY, 'Comedy'),
    (ACTION, 'Action'),
    (DRAMA, 'Drama'),
    )
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

    def __str__(self):
        return '%s %s' % (self.name, self.release_date)