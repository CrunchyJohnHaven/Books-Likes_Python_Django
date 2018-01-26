from __future__ import unicode_literals
import re
import bcrypt
# hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
# print "bcrypt - hash1:", hash1
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[^\W_]+(-[^\W_]+)?$', re.U)

class BeltManager(models.Manager):
    def login_validator(self,postData):
        #initiate errors as an empty list
        errors = []
        #check if email is in the system
        if len(self.filter(email=postData['email'])) > 0:
        # if it is, set 'user equal to it
            user = self.filter(email=postData['email'])[0]
        #if it isn't set errors at name equal to error message
        else:
            errors['name'] = 'email/password incorrect'
        if errors:
            return errors
        return user

    def register_validator(self,postData):
        errors = []
        # check name and last name length
        if len(postData['name']) < 2:
            errors.append("User name should be more than two characters")
        if len(postData['password']) < 8:
            errors.append("User name should be more than eight characters")
        #check email
        if not re.match(NAME_REGEX, postData['email']) > 0:
            errors.append("Password doesn't match")
        if not errors:
            # make a new user with a hashed password
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5)) 
            print "hashed pw: ", hashed
            new_belt = self.create(
                name=postData['name'],
                alias=postData['alias'],
                email=postData['email'],
                password=hashed                
            )
            return new_belt
        return errors
        
class Belt(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.URLField()
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BeltManager()

    def __unicode__(self):
        return "id: " + str(self.id) + ", name: " + str(self.name) + ", email: " + str(self.email) + ", alias: " + str(self.alias) + ", password: " + str(self.password) + ", created_at: " + str(self.created_at) + ", updated_at: " + str(self.updated_at)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BeltManager()

    def __unicode__(self):
        return "id: " + str(self.id) + ", title: " + str(self.title) + ", author: " + str(self.author) + ", created_at: " + str(self.created_at) + ", updated_at: " + str(self.updated_at)

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField(null=True)
    reviewer = models.ForeignKey(Belt, related_name='reviews', null=True)
    book_obj = models.ForeignKey(Book, related_name='book_reviews', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __repr__(self):
        return "Review: ---{}, Rate: ---{}".format(self.content, self.rating)


#  Create your models here.
# from apps.Belt.models import *
# Belt.objects.create(name="ChrisBradley", alias="Chris", email="chris@gmail.com", password="chrisbradley")
# Book.objects.create(title="For Whom The Bell Tolls", author="Ernest Hemingway")

# Book.objects.all()

# Review.objects.create(content="tells the story of Robert Jordan, a young American in the International Brigades attached to a republican guerrilla unit during the Spanish Civil War. As a dynamiter, he is assigned to blow up a bridge during an attack on the city of Segovia." book = 1, belt = 0) 

# book = Book.objects.get(id=1)
# book.belt_reviews.all()
# book.reviews.add(content="tells the story of Robert Jordan", belt_id = 0, book_id = 1)




# from __future__ import unicode_literals
# import re
# import bcrypt
# from django.db import models
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[^\W_]+(-[^\W_]+)?$', re.U)

# class UserManager(models.Manager):
#     def login_validator(self, postData):
#         errors = []
#         if len(self.filter(email=postData['email'])) > 0:
#             # check this user's password
#             user = self.filter(email=postData['email'])[0]
#             if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
#                 errors.append('email/password incorrect')
#         else:
#             errors.append('email/password incorrect')
#         if errors:
#             return errors
#         return user

#     def register_validator(self,postData):
#         errors = []
#         # check name and last name length
#         if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
#             errors.append("User name/last name should be more than 2 characters")
#         # check password
#         if len(postData['password']) < 8:
#             errors.append("Password should have more than 8 characters")    
#         #check name for character
#         if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
#             errors.append("User name/last name should contains only letters")
#         # check email 
#         if not re.match(EMAIL_REGEX, postData['email']):
#             errors.append("Invalid email format")
#         if len(User.objects.filter(email=postData['email'])) > 0:
#             errors.append("email already in use")
#         # check password
#         if postData['password'] != postData['confirm']:
#             errors.append("Password doesn't match")
#         if not errors:
#             # make our new user
#             # hash password
#             hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))
#             print "hashed code: ", hashed
#             new_user = self.create(
#                 first_name=postData['first_name'],
#                 last_name=postData['last_name'],
#                 email=postData['email'],
#                 password=hashed
#             )
#             return new_user
#         return errors


# class User(models.Model):
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     email = models.TextField(max_length=45)
#     password = models.CharField(max_length=45)
#     created_at = models.DateTimeField(auto_now_add=True)
#     objects = UserManager()
#     def __repr__(self):
#         return "User: --{}".format(self.first_name)

# class Book(models.Model):
#     name = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     uploader = models.ForeignKey(User, related_name='uploaded_books')
#     desc = models.TextField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __repr__(self):
#         return "Book: -----{}".format(self.name)

# class Review(models.Model):
#     content = models.TextField()
#     rating = models.IntegerField()
#     reviewer = models.ForeignKey(User, related_name='reviews')
#     book_obj = models.ForeignKey(Book, related_name="book_reviews", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __repr__(self):
#         return "Review: ---{}, Rate: ---{}".format(self.content, self.rating)