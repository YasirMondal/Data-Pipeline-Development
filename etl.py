# etl_pipeline.py
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import sys

DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
OUTPUT_FILE = "cleaned_data.csv"

def extract(url=DATA_URL):
    print(f"[extract] reading from {url}")
    df = pd.read_csv(url)
    return df

def preprocess(df):
    print("[preprocess] dropping duplicates and filling missing values (simple)")
    df = df.drop_duplicates().copy()
    # fill numeric NaNs with mean, categorical NaNs with mode
    df.fillna(df.mean(numeric_only=True), inplace=True)
    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col].fillna(df[col].mode().iloc[0], inplace=True)
    return df

def transform(df):
    print("[transform] building transformer and applying to features")
    numeric_features = df.select_dtypes(include=['number']).columns.tolist()
    categorical_features = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # keep target if you have a label; here we treat all cols as features for demonstration
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ],
        remainder='drop'  # drop any other columns
    )

    pipeline = Pipeline(steps=[("preprocessor", preprocessor)])
    X_transformed = pipeline.fit_transform(df)
    # create column names for transformed dataframe
    cat_cols = []
    if categorical_features:
        cat_cols = list(pipeline.named_steps['preprocessor']
                        .named_transformers_['cat']
                        .get_feature_names_out(categorical_features))
    out_cols = list(numeric_features) + cat_cols
    df_out = pd.DataFrame(X_transformed, columns=out_cols)
    return df_out

def load(df, path=OUTPUT_FILE):
    print(f"[load] saving cleaned data to {path}")
    df.to_csv(path, index=False)
    print("[load] done")

def main():
    df = extract()
    df = preprocess(df)
    df_out = transform(df)
    load(df_out)

if __name__ == "__main__":
    main()