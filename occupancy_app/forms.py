from django import forms
from occupancy_app.models import * 

class SensorDataForm(forms.Form):
    # Populate the sensor list from the model
    data = Sensor.objects.all()
    select_sensor = forms.ChoiceField(
        # Set the key;value of the select
        choices = [(d.sensor_name, d.sensor_name) for d in data],
        required=True)
    date = forms.DateField(
        widget = forms.TextInput(attrs={'id': 'date_field', 'class': 'datepicker', 'placeholder': 'yyyy-mm-dd'}), 
        required=False)
    # Time selector
    time = forms.TimeField(
        widget = forms.TextInput(attrs={'id': 'time_field', 'class': 'timepicker', 'placeholder': 'hh:mm'}), 
        required=False)
