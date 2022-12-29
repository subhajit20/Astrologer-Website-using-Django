from django import forms

LANG_CHOICES = (
    ("en", "english"),
    ("hi", "hindi"),
    ("ma", "marathi"),
    ("bn", "bengali"),
    ("ta", "tamil"),
    ("te", "telugu"),
    ("kn", "kannada"),
    ("ml", "malayalam"),
)

G_CHOICES = (
    ("male", "Male"),
    ("female", "Female")
)

class ReportForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=200)
    phone = forms.IntegerField(label='Phone')
    phonecode = forms.CharField(label='Code', max_length=100)
    gender = forms.ChoiceField(label='Gender', choices = G_CHOICES, widget=forms.RadioSelect)
    date  = forms.DateField(label='Birth date')
    time  = forms.TimeField(label='Birth time')
    place = forms.CharField(label='Place of birth', max_length=100)
    lat  = forms.DecimalField(label='Latitude')
    lon  = forms.DecimalField(label='Longitude')
    tzone = forms.CharField(label='Timezone')
    language = forms.ChoiceField(label='Choose your language', choices = LANG_CHOICES)