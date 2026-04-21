import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler


# ✅ Load data (robust path handling)
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "cleaned", "EV_population_cleaned.csv")
    
    print("Loading file from:", file_path)  # debug line
    df = pd.read_csv(file_path)
    
    return df


# ✅ Convert datetime columns (if exists)
def convert_datetime(df):
    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
                
                df[f"{col}_year"] = df[col].dt.year
                df[f"{col}_month"] = df[col].dt.month
                df[f"{col}_day"] = df[col].dt.day
                df[f"{col}_weekday"] = df[col].dt.weekday
                
                df = df.drop(columns=[col])
            except:
                pass

    return df


# ✅ Encode categorical columns
def encode_categorical(df):
    le = LabelEncoder()
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col].astype(str))
    
    return df


# ✅ Scale features
def scale_features(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled


# ✅ Main feature engineering pipeline
def feature_engineering(df, target_column):
    df = convert_datetime(df)
    df = encode_categorical(df)

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = scale_features(X)

    return X, y


# ✅ Run file
if __name__ == "__main__":
    df = load_data()

    print("\nColumns in dataset:\n", df.columns)

    # ⚠️ CHANGE THIS AFTER SEEING COLUMNS
    target = df.columns[-1]  # temporary (last column as target)

    X, y = feature_engineering(df, target)

    print("\nProcessed X shape:", X.shape)
    print("Processed y shape:", y.shape)