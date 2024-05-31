import pandas as pd
from catboost import CatBoostClassifier

def make_pred(data, path_to_file):
    
    model = CatBoostClassifier()
    model.load_model('./models/catboost_model.cbm')
    
    threshold = 0.51

    submission = pd.DataFrame({
        'client_id': pd.read_csv(path_to_file)['client_id'],
        'preds': (model.predict_proba(data)[:, 1] > threshold) * 1
    })

    return submission