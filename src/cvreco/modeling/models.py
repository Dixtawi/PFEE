from sklearn.ensemble import RandomForestClassifier as SkRandomForestClassifier
from sklearn.linear_model import LogisticRegression as SkLogisticRegression
from sklearn.svm import LinearSVC as SkLinearSVC
from sklearn.neighbors import KNeighborsClassifier as SkKNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier as SkDecisionTreeClassifier
from xgboost import XGBClassifier as SkXGBClassifier

from concrete.ml.sklearn.rf import RandomForestClassifier
from concrete.ml.sklearn.linear_model import LogisticRegression
from concrete.ml.sklearn.svm import LinearSVC
from concrete.ml.sklearn.neighbors import KNeighborsClassifier
from concrete.ml.sklearn.tree import DecisionTreeClassifier
from concrete.ml.sklearn.xgb import XGBClassifier

models = {
    "Random Forest": (SkRandomForestClassifier(n_estimators=100, random_state=42), RandomForestClassifier(n_estimators=100, random_state=42)),
    "Logistic Regression": (SkLogisticRegression(max_iter=1000, random_state=42), LogisticRegression(max_iter=1000, random_state=42)),
    "K-Nearest Neighbors": (SkKNeighborsClassifier(), KNeighborsClassifier()),
    "Decision Tree": (SkDecisionTreeClassifier(random_state=42), DecisionTreeClassifier(random_state=42)),
    "Linear SVC": (SkLinearSVC(random_state=42, max_iter=10000), LinearSVC(random_state=42, max_iter=10000)),
    "XGBoost Classifier": (SkXGBClassifier(random_state=42, use_label_encoder=False), XGBClassifier(random_state=42, use_label_encoder=False))
}