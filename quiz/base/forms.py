from django import forms
from quiz.base.models import Aluno

class AlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = ["nome", "email"]