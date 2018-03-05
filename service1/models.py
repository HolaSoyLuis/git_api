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

# http http://127.0.0.1:8000/series/1/
# $http -j POST http://127.0.0.1:8000/series/
# http -f POST http://127.0.0.1:8000/series/4 {name = 'Test', release_date = '2010-5-3', rating = 13, category = 'Test'}

# http POST http://localhost:8000/series/ name="hello world" release_date = "2010-5-3" rating = "13" category = "Test"
# http POST http://localhost:8000/series/ {name="hello world" release_date = "2010-5-3" rating = "13" category = "Test"}

# http POST http://localhost:8000/series/ name="hello world" \ release_date = "2010-5-3" \ rating = "13" \ category = "Test"
# http POST http://localhost:8000/series/ object := '{"name" : "hello world" , "release_date " : "2010-5-3" , "rating" : "13" , "category" : "Test"}'