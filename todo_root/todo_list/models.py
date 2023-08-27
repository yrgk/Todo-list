from django.db import models
from django.urls import reverse
from slugify import slugify



class TodoList(models.Model):
    name = models.CharField(max_length=30, blank=False)
    content = models.TextField(blank=False)
    slug = models.SlugField(max_length=30, unique=True, db_index=True)
    day_created = models.DateTimeField(auto_now_add=True)

    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        return super(TodoList, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('edit', kwargs={'post_slug':self.slug})