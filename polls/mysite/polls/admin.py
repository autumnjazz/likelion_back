from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date','question_text'] #필드 순서변경
#
# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Votes', {'fields': ['votes']}),
#         ('Choice Text', {'fields': ['choice_text']})
#     ]

class ChoiceInline(admin.TabularInline): #StackedInline
    model = Choice
    extra =2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}) #숨기기
    ]
    inlines = [ChoiceInline] #여기까지 choice 모델 한번에 보기
    list_display = ('question_text', 'pub_date') #테이블 레코드 칼럼
    list_filter = ['pub_date'] #정렬
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)