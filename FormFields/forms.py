from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,SelectField,validators

class SignUpForm(FlaskForm):
    genderChoice = ['Male', 'Female']
    ChestPainChoices = ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic']
    fastingSugar = ['Greater than 120 mg/ml', 'Lower than 120 mg/ml']
    angina = ['Yes', 'No']
    restEcg = ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy']
    solpeChoices = ['Upsloping', 'Flat', 'Downsloping']
    vessels = ['Zero', 'One', 'Two', 'Three', 'Four']
    thalassemiaChoices = ['No', 'Normal', 'Fixed Defect', 'Reversable Defect']

    age = IntegerField('Enter Your Age',validators=[validators.Required()])

    sex = SelectField('Select Your Gender',choices=genderChoice)

    chest_pain_type = SelectField('Select Chest Pain Type', choices= ChestPainChoices)

    resting_blood_pressure = IntegerField('Enter Blood Pressure',validators=[validators.Required()])

    cholestoral = IntegerField('Enter Cholestoral',validators=[validators.Required()])

    fasting_blood_sugar = SelectField('Select Fasting sugar',choices=fastingSugar)

    rest_ecg = SelectField('Select rest ECG',choices=restEcg)

    Max_heart_rate = IntegerField('Enter Max Heart Rate',validators=[validators.Required()])

    exercise_induced_angina = SelectField('Select induced angina',choices=angina)

    oldpeak = IntegerField('Enter Oldpeak',validators=[validators.Required()])

    slope = SelectField('Select Slope',choices=solpeChoices)

    vessels_colored_by_flourosopy = SelectField('Select Number of Colored vessels',choices=vessels)

    thalassemia = SelectField('Select Thalassemia',choices=thalassemiaChoices)

    sumbit = SubmitField('Sumbit !')
