from django.contrib import admin, messages
from .models import Women, Category


# Register your models here.
class MarriedFilet(admin.SimpleListFilter):
    title = "Статус Женщин"
    parameter_name = "status"
    def lookups(self, request, model_admin):
        return [
            ('married',"Замужем"),
            ('single','Не замужем')
        ]
    def queryset(self, request, queryset):
        if self.value()=='married':
            return queryset.filter(husband__isnull=False)
        return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):


    fields = ['title','content','cat','slug','tags']
    #exclude = ['tags','is_published']
    # readonly_fields = ['slug']
    prepopulated_fields = {"slug":('title',)}#создаёт автоматически слаг по названию, даже русские буквы преобразует в латиницу
    filter_horizontal = ['tags']#более удобная менюшка для выбора тегов(то есть для отображение таблиц многие ко многим)
    # либо сделать(функционал тот же) filter_vertical
    list_display = ("title","time_create",'is_published','cat',"breif_info")
    list_display_links = ('title',)
    ordering = ['time_create','title']
    list_editable = ("is_published",)
    list_per_page = 3
    actions = ['set_published','set_draft']
    search_fields = ['title','cat__name']
    list_filter = [MarriedFilet,"cat__name","is_published"]

    @admin.display(description="Краткое описание",ordering='content')
    def breif_info(self,women: Women):
        return f"Описание {len(women.content)}"

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self,request,queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self,request,queryset):

        count=queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации.", messages.WARNING)

# admin.site.register(Women,WomenAdmin) сверху тоже самое
@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ('id', 'name')