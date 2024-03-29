from django.db import models

class Post(models.Model):
    '''данные о посте'''
    title = models.CharField('Заголовок записи', max_length=150)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    
    def __str__(self):
        return f'{self.title} ({self.author})'
    def short_text(self):
        # Ограничиваем длину текста, например, до 200 символов
        return self.description[:200]
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''комментарий'''
    email=models.EmailField()
    name=models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.post})'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация',  on_delete=models.CASCADE)
