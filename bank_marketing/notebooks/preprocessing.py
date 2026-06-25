"""
Script base para el rol B: escalamiento, codificación y construcción de pipeline.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=';')
    unknown_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan']
    for col in unknown_cols:
        if col in df.columns:
            df[col] = df[col].replace('unknown', pd.NA)
    if 'duration' in df.columns:
        df = df.drop(columns=['duration'])
    return df


def split_data(df: pd.DataFrame, target: str, test_size: float = 0.2, random_state: int = 42):
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)


def build_preprocessing_pipeline(numeric_cols, nominal_cols, ordinal_cols=None):
    numeric_transformer = Pipeline(
        steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
        ]
    )

    nominal_transformer = Pipeline(
        steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
        ]
    )

    transformers = [
        ('num', numeric_transformer, numeric_cols),
        ('nom', nominal_transformer, nominal_cols),
    ]

    if ordinal_cols:
        education_order = [
            ['illiterate', 'basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'professional.course', 'university.degree']
        ]
        ordinal_transformer = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('ordinal', OrdinalEncoder(categories=education_order)),
            ]
        )
        transformers.append(('ord', ordinal_transformer, ordinal_cols))

    return ColumnTransformer(transformers=transformers, remainder='drop')


def run_pipeline(csv_path: str, target: str):
    df = load_data(csv_path)
    X_train, X_test, y_train, y_test = split_data(df, target)

    # Definir columnas según el dataset
    numeric_cols = [
        'age', 'campaign', 'pdays', 'previous',
        'emp.var.rate', 'cons.price.idx', 'cons.conf.idx',
        'euribor3m', 'nr.employed'
    ]
    nominal_cols = [
        'job', 'marital', 'default', 'housing', 'loan',
        'contact', 'month', 'day_of_week', 'poutcome'
    ]
    ordinal_cols = ['education']

    preprocessor = build_preprocessing_pipeline(numeric_cols, nominal_cols, ordinal_cols)

    preprocessor.fit(X_train)
    X_train_transformed = preprocessor.transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)

    print('X_train shape before:', X_train.shape)
    print('X_train shape after:', X_train_transformed.shape)
    print('X_test shape before:', X_test.shape)
    print('X_test shape after:', X_test_transformed.shape)

    return {
        'preprocessor': preprocessor,
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'X_train_transformed': X_train_transformed,
        'X_test_transformed': X_test_transformed,
    }


if __name__ == '__main__':
    csv_path = '../data/raw/bank-additional-full.csv'
    target = 'y'
    result = run_pipeline(csv_path, target)
    print('Pipeline listo.')
