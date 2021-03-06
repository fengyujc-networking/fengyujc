from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
# python_2_unicode_compatible 装饰器用于兼容 Python2


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateField(auto_now_add=True)

    post = models.ForeignKey('fengyujc_blog.Post',  on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]


class Email(models.Model):
    def __str__(self):
        return self.name

    def increase_emails(self):
        self.emails += 1
        self.save(update_fields=['emails'])

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

    emails = models.PositiveIntegerField(default=0)  # 该类型的值只允许为正整数或 0

