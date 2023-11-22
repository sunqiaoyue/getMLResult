import pandas as pd
import joblib


def predictResult(request):
    data = request.data
    df = pd.DataFrame([data])

    # define X and y
    feature_cols = ['Age', 'Gender', 'family_history', 'benefits', 'care_options', 'anonymity', 'leave',
                    'work_interfere', 'self_employed', 'no_employees', 'remote_work', 'tech_company',
                    'wellness_program', 'seek_help', 'mental_health_consequence', 'phys_health_consequence',
                    'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical',
                    'obs_consequence', 'age_range']
    X = df[feature_cols]
    joblib_LR_Model = joblib.load("myapi/joblib_RL_Model.pkl")
    Y_predict = joblib_LR_Model.predict(X)

    print(Y_predict)
    return {'Result': Y_predict}


if __name__ == '__main__':
    predictResult()



