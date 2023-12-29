from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the headbrain.csv dataset
dataset = pd.read_csv("headbrain.csv")
X = dataset["Head Size(cm^3)"].values.reshape(-1, 1)
y = dataset["Brain Weight(grams)"].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

#model.predict(123)
# / - root
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        head_size = float(request.form["head_size"])
        # Make a prediction using the trained model
        prediction = model.predict([[head_size]])
        return render_template("index.html", prediction=f"Predicted Brain Weight: {prediction[0]:.2f} grams")

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
