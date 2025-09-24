
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import io

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
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=X.flatten(), y=y.flatten(), label='Data Points', ax=ax)
    
    # Plotting the true line
    x_range = np.array([[0], [10]])
    y_range_true = a * x_range + 5
    ax.plot(x_range, y_range_true, color='green', linestyle='--', label=f'True Line (y = {a}x + 5)')

    # Plotting the regression line
    y_range_pred = model.predict(x_range)
    ax.plot(x_range, y_range_pred, color='red', label='Regression Line')
    
    ax.set_title(f'Linear Regression (a={a}, noise={noise}, points={n_points})')
    ax.set_xlabel('X')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True)
    
    return fig

st.set_page_config(layout="wide")
st.title("Simple Linear Regression with CRISP-DM")

# Sidebar for controls
st.sidebar.header("Controls")
a = st.sidebar.slider("Slope (a)", min_value=-5.0, max_value=5.0, value=2.0, step=0.1)
noise = st.sidebar.slider("Noise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
n_points = st.sidebar.slider("Number of Points", min_value=10, max_value=500, value=100, step=10)

# Main content layout
col1, col2 = st.columns(2)

with col1:
    st.header("CRISP-DM Steps")
    st.markdown("""
    <ol>
        <li><b>Business Understanding:</b> Visualize how parameters (slope, noise, data size) affect a simple linear regression model.</li>
        <li><b>Data Understanding:</b> Synthetic data is generated based on user inputs. The underlying "true" model is y = ax + 5.</li>
        <li><b>Data Preparation:</b> Generate X values and corresponding y values with added random noise.</li>
        <li><b>Modeling:</b> A linear regression model is trained on the generated (X, y) data points.</li>
        <li><b>Evaluation:</b> The plot shows the original data, the "true" line, and the fitted regression line. We also see the learned model coefficients.</li>
        <li><b>Deployment:</b> This Streamlit application serves as the deployment of the model.</li>
    </ol>
    """, unsafe_allow_html=True)

# CRISP-DM Steps
# Data Preparation
X, y = generate_data(n_points, a, noise)

# Modeling
model = train_model(X, y)

# Evaluation
plot_fig = create_plot(X, y, model, a, n_points, noise)
model_coef = model.coef_[0][0]
model_intercept = model.intercept_[0]

with col2:
    st.header("Results")
    st.pyplot(plot_fig)
    
    st.subheader("Model Evaluation:")
    eval_col1, eval_col2 = st.columns(2)
    with eval_col1:
        st.metric(label="Learned Slope (Coefficient)", value=f"{model_coef:.4f}")
    with eval_col2:
        st.metric(label="Learned Intercept", value=f"{model_intercept:.4f}")

