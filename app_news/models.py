from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Ник'
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название'
    )
    url = models.URLField(
        verbose_name='Ссылка на новость'
    )
    rate = models.FloatField(
        default=0,
        verbose_name='Рейтинг'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        Author,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self):
        return self.text
