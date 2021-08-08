from django.db import models
from django.contrib.auth.models import User
import os
# Additional function to deal with images names


def renameImagesFiles(instance, filename):

    directoryToUpload = 'Images/'
    splitedFilename = filename.split('.')[-1]

    if instance.user.username:
        newFilename = 'UserProfilePictures/{}.{}'.format(
            instance.user.username, splitedFilename)

    return(os.path.join(directoryToUpload, newFilename))


# Create your models here.


class userProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    #profilePic = models.ImageField(
    #    upload_to=renameImagesFiles, verbose_name='Profile picture', blank=True)

    student = 'student'
    userTypes = [(student, 'student')]

    userType = models.CharField(
        max_length=10, choices=userTypes, default=student)

    def __str__(self):
        return self.user.username
