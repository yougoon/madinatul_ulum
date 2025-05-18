from django import forms
class AdmissionForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    father_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    course = forms.ChoiceField(choices=[
        ('nurani', 'Nurani (Kindergarten)'),
        ('general', 'General (Nursery-Class 7)'),
        ('pre-hifz', 'Pre-Hifz'),
        ('hifz', 'Hifzul Quran'),
        ('one-hour', '1 Hour Madrasa')
    ])
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(required=False)
