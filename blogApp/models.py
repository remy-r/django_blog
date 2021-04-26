from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Status(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status__text='Publié').order_by('-pub_date')


class DraftedManager(models.Manager):
    def get_queryset(self):
        return super(DraftedManager, self).get_queryset().filter(status__text='Brouillon').order_by('-pub_date')


class Post(models.Model):
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    drafted = DraftedManager()

    title = models.CharField(max_length=200)
    content = RichTextUploadingField(default="")
    pub_date = models.DateTimeField('date published')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

