from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_bub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):# название соглашение django
        """Возвращает ссылку на конкретный объект.
           Конкретный экземпляр класса Post.
        """
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.id: # Теперь он делает тоже сохранение но через проверку if
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)



    def __str__(self):
        """Специальный метод класса."""
        return self.title




class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self): 
        return reverse('tag_update_url', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.title)
