from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['level', 'publishing_date']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['level', 'content']
    list_editable = ['level']
    

    class Meta:
        model = Question    
        


admin.site.register(Question)
