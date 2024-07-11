import matplotlib.pyplot as plt

def roc_comparison(models, X_test, y_test):
    """Compare classic and FHE models using ROC curves.

    Args:
        models (dict): Dictionnary containing classic and FHE models
        X_test (pandas.DataFrame): Testing dataloader values
        y_test (pandas.DataFrame): Testing dataloader labels
    """
    plt.figure(figsize=(12, 10))

    for model_name, (sk_model, fhe_model) in models.items():
        if hasattr(sk_model, "predict_proba") and model_name != "K-Nearest Neighbors":
            sk_y_pred_proba = sk_model.predict_proba(X_test)[:, 1]
            fhe_y_pred_proba = fhe_model.predict_proba(X_test)[:, 1]
            
            sk_fpr, sk_tpr, _ = roc_curve(y_test, sk_y_pred_proba)
            fhe_fpr, fhe_tpr, _ = roc_curve(y_test, fhe_y_pred_proba)
            
            sk_roc_auc = auc(sk_fpr, sk_tpr)
            fhe_roc_auc = auc(fhe_fpr, fhe_tpr)
            
            plt.plot(sk_fpr, sk_tpr, label=f'{model_name} Sklearn (AUC = {sk_roc_auc:.2f})')
            plt.plot(fhe_fpr, fhe_tpr, label=f'{model_name} FHE (AUC = {fhe_roc_auc:.2f})')

    plt.plot([0, 1], [0, 1], linestyle='--', label='No Skill')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Comparison: Sklearn vs FHE Methods')
    plt.legend(loc="lower right")
    plt.show()