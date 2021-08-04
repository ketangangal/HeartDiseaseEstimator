from joblib import load
import pandas as pd
import numpy as np

def featureCorrection(result):
    new_dict = {}
    frame = pd.read_csv("C:\\Users\\ketan\\Desktop\\Project\\HeartDiseaseEstimator\\csvFiles\\Feature_correction.csv")
    frame = frame.drop('target', axis=1)
    data = list(result.keys())[:-1]
    for i in data:
        new_dict[i] = result[i]

    frame = frame.append(new_dict, ignore_index=True)
    frame[['age', 'resting_blood_pressure', 'cholestoral', 'Max_heart_rate']] = frame[
        ['age', 'resting_blood_pressure', 'cholestoral', 'Max_heart_rate']].astype('int64')

    frame['oldpeak'] = frame['oldpeak'].astype('float64')

    frame = pd.get_dummies(frame, drop_first=True)
    scaler = load("C:\\Users\\ketan\\Desktop\\Project\\HeartDiseaseEstimator\\pickleFiles\\featureScaler.pkl")
    result = frame.iloc[-1].values
    result = scaler.transform(np.reshape(result, (1, -1)))

    return result
