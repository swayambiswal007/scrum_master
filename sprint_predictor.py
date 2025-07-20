import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    df = pd.read_csv("sprint_data.csv")
    X = df[["team_size", "sprint_duration_days", "avg_story_points_per_member", "bugs_last_sprint"]]
    y = df["completed_story_points"]

    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "sprint_model.pkl")
    print("✅ Model trained and saved!")

def predict_next_sprint(team_size, days, avg_story_points, bugs):
    model = joblib.load("sprint_model.pkl")
    input_data = pd.DataFrame([[team_size, days, avg_story_points, bugs]],
                          columns=["team_size", "sprint_duration_days", "avg_story_points_per_member", "bugs_last_sprint"])
    prediction = model.predict(input_data)[0]
    return round(prediction, 2)

if __name__ == "__main__":
    train_model()
    result = predict_next_sprint(4, 14, 6.0, 2)
    print(f"\n📊 Predicted Story Points for Next Sprint: {result}")
