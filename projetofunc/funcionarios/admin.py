from django.contrib import admin
from funcionarios import models

# Register your models here.

@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome_Completo', 'data_Nasc', 'apelido', 'stacks',)
    ordering = 'nome_Completo',
    search_fields = 'apelido', 'nome_Completo', 'stacks',
    list_per_page = 20
    list_max_show_all = 100