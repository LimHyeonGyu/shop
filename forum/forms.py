from django import forms

from forum.models import Forum


class forumcreateForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['fo_title', 'fo_desc']