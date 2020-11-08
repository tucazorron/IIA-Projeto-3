from sklearn.ensemble import RandomForestClassifier
import Dataset

def create():

    model = RandomForestClassifier(n_estimators = 100)
    variables = ["Patient age quantile", "Patient addmited to regular ward (1=yes, 0=no)", "Patient addmited to semi-intensive unit (1=yes, 0=no)", "Patient addmited to intensive care unit (1=yes, 0=no)"]
    x = Dataset.matrix[variables]
    x = x.fillna(0)
    y = Dataset.matrix["SARS-Cov-2 exam result"]
    model.fit(x, y)
    p = model.predict(x)
    print(p)