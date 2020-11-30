from django.db import models
from django.urls import reverse


class Attribute(models.Model):
    attr_title = models.CharField(blank=False, max_length=200, verbose_name='Название критерия')
    slug = models.SlugField(max_length=200, verbose_name='Url', unique=True)
    attr_meaning = models.IntegerField(default=0, verbose_name='Важность критерия')

    def __str__(self):
        return self.attr_title

    def get_absolute_url(self):
        return reverse('attr_title', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'
        ordering = ['attr_meaning']


class Game(models.Model):
    game_title = models.CharField(blank=False, max_length=100, verbose_name='Название игры')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    game_attr = models.ManyToManyField(Attribute, blank=True, related_name='attribute', verbose_name='Критерий игры')

    def __str__(self):
        return self.game_title

    def get_absolute_url(self):
        return reverse('game_title', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['game_title']


class Gamer(models.Model):
    gamer_name = models.CharField(blank=False, max_length=100, verbose_name='Имя игрока')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.gamer_name

    def get_absolute_url(self):
        return reverse('gamer_name', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        ordering = ['gamer_name']


class Episode(models.Model):
    episode_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата партии')
    episode_game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game', verbose_name='Название игры')
    episode_gamer = models.ManyToManyField(Gamer, blank=True, related_name='gamer', verbose_name='Имя игрока')

    def __str__(self):
        return self.episode_game #?

    class Meta:
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'
        ordering = ['episode_date']


class Score(models.Model):
    score_amount = models.IntegerField(default=0, verbose_name='Игровые очки')
    score_attr = models.ForeignKey(Attribute, on_delete=models.CASCADE, blank=False, verbose_name='Критерий игры')
    score_game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False, verbose_name='Название игры')
    score_gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE, blank=False, verbose_name='Имя игрока')
    score_date = models.ForeignKey(Episode, on_delete=models.CASCADE, blank=False, verbose_name='Дата партии')

    def __str__(self):
        return self.score_amount

    class Meta:
        verbose_name = 'Игровые очки'
        verbose_name_plural = 'Игровые очки'
        ordering = ['score_amount']
