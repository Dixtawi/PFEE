from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split

def process_dataset(dataset, filtering_df):
    """Process the dataset and filters it to add predictions, and have a model compliant to ML models.

    Args:
        dataset (pd.DataFrame): The dataset to process
        filtering_df (pd.DataFrame): The dataframe of skills to create the predictions.

    Returns:
        pd.DataFrame: The processed dataset.
    """
    dataset['prediction'] = 0
    df_filtered = filtering_df[filtering_df['Skill'].str.contains(r'(js|javascript|java script)', case=False, na=False)]
    df_filtered = dataset[dataset['file_name'].isin(df_filtered['file_name'])]
    dataset['prediction'] = dataset['file_name'].isin(df_filtered['file_name']).astype(int)

    # Balancing the dataset
    one = dataset[dataset['prediction'] == 1]
    zero = dataset[dataset['prediction'] == 0].sample(n=len(one), random_state=42)
    dfModel = pd.concat([one, zero])
    dfModel = dfModel.sample(frac=1, random_state=42).reset_index(drop=True)

    # Preparing the final dataset
    dfModel = filtering_df[filtering_df['file_name'].isin(dfModel['file_name'])]
    dfModel = dfModel.merge(dataset[['file_name', 'prediction']], on='file_name', how='left')
    dfModel = dfModel.drop(columns=['text'])

    df_pivot = dfModel.pivot_table(index='file_name', columns='Skill', aggfunc='size', fill_value=0).astype(bool)
    df_prediction = dfModel[['file_name', 'prediction']].drop_duplicates().set_index('file_name')
    dfModel = df_pivot.join(df_prediction, lsuffix='_skill', rsuffix='_pred').reset_index()
    
    dfModel = dfModel.drop('file_name', axis=1)
    
    return dfModel

def split_scaler(dfModel):
    """Split processed dataset into train and test dataloaders.

    Args:
        dfModel (pd.DataFrame): The processed dataframe to split.

    Returns:
        (ndarray, ndarray, ndarray, ndarray): Tuple containing train and test dataloaders.
    """
    X = dfModel.drop('prediction_pred', axis=1)
    y = dfModel['prediction_pred']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Data normalization
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test