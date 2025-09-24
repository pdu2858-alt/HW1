import io
import base64
import numpy as np
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

def generate_data(n_points, a, noise):
    """Generate synthetic data for linear regression."""
    X = np.random.rand(n_points, 1) * 10
    noise_data = np.random.randn(n_points, 1) * noise
    y = a * X + 5 + noise_data  # Assuming b=5
    return X, y

def train_model(X, y):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X, y)
    return model

def create_plot(X, y, model, a, n_points, noise):
    """Create a plot of the data and the regression line."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X.flatten(), y=y.flatten(), label='Data Points')
    
    # Plotting the true line
    x_range = np.array([[0], [10]])
    y_range_true = a * x_range + 5
    plt.plot(x_range, y_range_true, color='green', linestyle='--', label=f'True Line (y = {a}x + 5)')

    # Plotting the regression line
    y_range_pred = model.predict(x_range)
    plt.plot(x_range, y_range_pred, color='red', label='Regression Line')
    
    plt.title(f'Linear Regression (a={a}, noise={noise}, points={n_points})')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Save plot to a string
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        a = float(request.form.get('a', 2))
        noise = float(request.form.get('noise', 1))
        n_points = int(request.form.get('n_points', 100))
    else:
        # Default values
        a = 2
        noise = 1
        n_points = 100

    # CRISP-DM: Data Preparation
    X, y = generate_data(n_points, a, noise)
    
    # CRISP-DM: Modeling
    model = train_model(X, y)
    
    # CRISP-DM: Evaluation
    plot_url = create_plot(X, y, model, a, n_points, noise)
    
    model_coef = model.coef_[0][0]
    model_intercept = model.intercept_[0]

    return render_template('index.html', 
                           plot_url=plot_url,
                           a=a,
                           noise=noise,
                           n_points=n_points,
                           model_coef=model_coef,
                           model_intercept=model_intercept)

if __name__ == '__main__':
    app.run(debug=True)