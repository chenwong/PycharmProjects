from django.db import models

# Create your models here.
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class Project(models.Model):

    name = models.CharField(max_length=256, unique=True)
    content = models.TextField()
    progress = models.IntegerField(blank=True, default=0)
    c_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'User',    # 注意这里
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
