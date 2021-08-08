from django.db import models
from django.template.defaultfilters import slugify
import os
from django.contrib.auth.models import User
# Create your models here.


def renameImagesFiles(instance, filename):

    directoryToUpload = 'Images/'
    splitedFilename = filename.split('.')[-1]

    if instance.subject_Id:
        newFilename = 'SubjectPictures/{}.{}'.format(
            instance.subject_Id, splitedFilename)

    return(os.path.join(directoryToUpload, newFilename))


class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subject(models.Model):
    subject_Id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name='subjects')
    #image = models.ImageField(
    #    upload_to=renameImagesFiles, blank=True, verbose_name='Subject image')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_Id)
        super().save(*args, **kwargs)

def save_lesson_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]

    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, instance.lesson_id, ext)

        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, new_name, ext)
    return os.path.join(upload_to, filename)

class Lesson(models.Model):

    lesson_id = models.CharField(max_length=100, unique=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=150)
    position = models.PositiveSmallIntegerField(verbose_name='Chapter n.')
    slug = models.SlugField(null=True, blank = True)
    video = models.CharField(max_length=300, unique = True)
    ppt = models.CharField(max_length=300)
    notes = models.CharField(max_length=300)

    class Meta():
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
