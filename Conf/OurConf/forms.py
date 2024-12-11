from django import forms


class Posts_on_PageForm(forms.Form):
    """форма количества постов на странице"""
    posts_on_pages = forms.IntegerField(label='Постов на страницу')