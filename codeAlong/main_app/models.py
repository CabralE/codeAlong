from django.db import models
from django.urls import reverse
from datetime import date
# Importing for User Authentication and Authorization
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class Leetcode(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=30)
    video_solution = models.CharField(max_length=30)
    code = models.CharField(max_length=200)
    study_solution = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return self.name
        

sample = [
    Leetcode('Contains Duplicate','https://leetcode.com/problems/contains-duplicate/','easy','https://wwwyoutube.com/watch?v=3OamzN90kPg','code solution', 'study solution', 'Arrays & Hashing'),
    Leetcode('Valid Anagram','https://leetcode.com/problems/valid-anagram/','easy','https://www.youtube.comwatch?v=9UtInBqnCgA', 'code solution', 'study solution', 'Arrays & Hashing'),
    Leetcode('Two Sum','https://leetcode.com/problems/two-sum/','easy','https://www.youtube.com/watchv=KLlXCFG5TnA', 'code solution', 'study solution', 'Arrays & Hashing')
]

'''
l = Leetcode(name="Contains Duplicate", link='https://leetcode.com/problems/contains-duplicate/',
difficulty='easy', video_solution='code solution', code="code", study_solution='study solution', category='Arrays & Hashing')
l.__dict__
{..., 'id': None, 'name':"Contains Duplicate", "link":'https://leetcode.com/problems/contains-duplicate/',
'difficulty':'easy', 'video_solution':'code solution', 'code':"code", 'study_solution':'study solution', 'category':'Arrays & Hashing'}
'''