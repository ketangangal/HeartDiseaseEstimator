from flask import Flask, request, render_template
from FeatureSetting.featureSetting import featureCorrection
from joblib import load
from FormFields.forms import SignUpForm

# flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloketan'
# connect post api call ---> predict() function


@app.route("/", methods = ['GET','POST'])
def home():
    form = SignUpForm()
    if request.method == 'POST':
        if form.is_submitted():
            result = request.form.to_dict()
            result = featureCorrection(result)
            model = load('pickleFiles/HeartDiseasePredictor.pkl')
            estimation = model.predict(result)
            if estimation == 1:
                return render_template('index.html', form=form, predict='You have a Heart Disease !')
            else:
                return render_template('index.html', form=form, predict="You Don't have a Heart Disease !")

    return render_template('index.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)

