from django import forms

# creating a form


class CreatePostForm(forms.Form):
    title = forms.CharField(label='Post Title', required=False, widget=forms.TextInput(
        attrs={'placeholder': "Enter your title", 'class': 'form-control'}))
    subtitle = forms.CharField(label='Post Subtitle', required=False, widget=forms.TextInput(
        attrs={'placeholder': "Enter your subtitle", 'class': 'form-control'}))
        
    img = forms.ImageField(label='Choose a Image', required=False)

    desc = forms.CharField(label='Your Thoughts', required=False, widget=forms.TextInput(
        attrs={'placeholder': "Enter your thoughts", 'class': 'form-control'}))
