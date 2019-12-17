from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    
    CATEGORY = (
        ('Ekonomi', 'Ekonomi'),
        ('Teknologi', 'Teknologi'),
        ('Politik', 'Politik'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    content = models.TextField()
    cover = models.ImageField(upload_to="news_cover", blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'tb_news'