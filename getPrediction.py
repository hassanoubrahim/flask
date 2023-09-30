import warnings
warnings.filterwarnings('ignore')
import joblib
import numpy as np

#from sklearn.metrics._dist_metrics import EuclideanDistance

def predModel(data):
    user_input = np.array([[
        int(data['preg']),
        int(data['plas']),
        int(data['pres']),
        int(data['skin']),
        int(data['test']),
        int(data['mass']),
        int(data['pedi']),
        int(data['age'])
    ]])
    model = data['model']
    if model == "KNN":
        filename = 'knn_model.joblib'
    elif model == "SVM":
        filename = 'svm_model.joblib'
    elif model == "DT":
        filename = 'dt_model.joblib'
    else:
        return "Model Not Found !!!! <a href='/app1/predict'>Go back </a>"

    loaded_model = joblib.load(open(filename, 'rb'))
    res = loaded_model.predict(user_input)
    return res
