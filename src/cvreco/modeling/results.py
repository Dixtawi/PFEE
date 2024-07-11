import time
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score, roc_curve, auc
import pandas as pd


def get_models_metrics(models, X_train, y_train, X_test, y_test):
    """Mesures how models perform using accuracy.

    Args:
        models (dict): Dictionnary of models (normal and with FHE)
        X_train (pandas.DataFrame): Training dataloader values
        y_train (pandas.DataFrame): Training dataloader labels
        X_test (pandas.DataFrame): Testing dataloader values
        y_test (pandas.DataFrame): Testing dataloader labels

    Returns:
        pandas.DataFrame: The differents metrics calculated based on the models.
    """
    results = []

    # Training and Validation
    for model_name, (sk_model, fhe_model) in models.items():
        # Sklearn model
        start_time = time.time()
        sk_model.fit(X_train, y_train)
        sk_training_time = time.time() - start_time
        sk_y_pred = sk_model.predict(X_test)
        sk_accuracy = accuracy_score(y_test, sk_y_pred)
        
        # FHE model
        start_time = time.time()
        fhe_model.fit(X_train, y_train)
        fhe_training_time = time.time() - start_time
        fhe_y_pred = fhe_model.predict(X_test)
        fhe_accuracy = accuracy_score(y_test, fhe_y_pred)
        
        # Calculate ratios
        time_ratio = fhe_training_time / sk_training_time
        accuracy_ratio = fhe_accuracy / sk_accuracy
        
        results.append({
            "Model": model_name,
            "Sklearn Accuracy": sk_accuracy,
            "Sklearn Time": sk_training_time,
            "FHE Accuracy": fhe_accuracy,
            "FHE Time": fhe_training_time,
            "Time Ratio (FHE/Sklearn)": time_ratio,
            "Accuracy Ratio (FHE/Sklearn)": accuracy_ratio
        })

    results_df = pd.DataFrame(results)
    
    return results_df