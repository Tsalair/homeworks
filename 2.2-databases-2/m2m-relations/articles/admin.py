from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormSet(BaseInlineFormSet):
     def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main'] == True:
                count += 1
            print(count)
            
        if count == 0:
            raise ValidationError('Отметьте главный тег')
        elif count > 1:
            raise ValidationError('Главный тег может быть только один!')
        return super().clean() 


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

admin.site.register(Tag)


