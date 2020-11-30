from django.contrib import admin
from .models import *


class AttributeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("attr_title",)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("game_title",)}


class GamerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("gamer_name",)}


class EpisodeAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("gamer_name",)}


class ScoreAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("gamer_name",)}


admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Gamer, GamerAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Score, ScoreAdmin)
