import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Page configuration
st.set_page_config(layout="wide", page_title="Regression & Time Series Explorer")

# --- Model Functions ---

def run_simple_linear_regression():
    st.header("Simple Linear Regression (SLR)")

    # --- Sidebar Controls for SLR ---
    st.sidebar.header("SLR Controls")
    a = st.sidebar.slider("True Slope (a)", -5.0, 5.0, 2.0, 0.1)
    noise = st.sidebar.slider("Noise Level", 0.0, 20.0, 5.0, 0.5)
    n_points = st.sidebar.slider("Number of Points", 50, 1000, 200, 10)
    b = 5 # Constant intercept for this example

    # --- CRISP-DM Framework ---
    st.subheader("CRISP-DM Walkthrough")
    crisp_dm_expander = st.expander("Show CRISP-DM Steps")
    with crisp_dm_expander:
        st.markdown(f"""
        1.  **Business Understanding**: Visualize how parameters (slope, noise, data size) and model evaluation metrics are affected in a simple linear regression task. The goal is to understand the relationship between a single feature and a target variable.
        2.  **Data Understanding**: Synthetic data is generated based on user inputs. The underlying "true" model is `y = {a}x + {b}`. We expect the trained model to learn coefficients close to these true values.
        3.  **Data Preparation**: Generate `X` values (a single feature) and corresponding `y` values with added random noise. The data is then split for modeling.
        4.  **Modeling**: A `LinearRegression` model from `scikit-learn` is trained on the generated data points.
        5.  **Evaluation**: The model is evaluated using R-squared, Mean Squared Error (MSE), and Mean Absolute Error (MAE). The regression line is plotted against the data, including a 95% confidence interval (the "funnel chart") to show prediction uncertainty.
        6.  **Deployment**: This Streamlit application serves as the deployment of the model, allowing for interactive exploration.
        """)

    # --- Data Generation ---
    X = np.random.rand(n_points, 1) * 10
    y = a * X + b + np.random.randn(n_points, 1) * noise
    df = pd.DataFrame(X, columns=['X'])
    df['y'] = y

    # --- Modeling ---
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # --- Evaluation ---
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Model Evaluation")
        st.metric("R-squared", f"{r2:.4f}")
        st.metric("Mean Squared Error (MSE)", f"{mse:.4f}")
        st.metric("Mean Absolute Error (MAE)", f"{mae:.4f}")

        st.subheader("Learned Coefficients")
        st.metric("Learned Slope", f"{model.coef_[0][0]:.4f}", delta=f"{model.coef_[0][0] - a:.4f} from true slope")
        st.metric("Learned Intercept", f"{model.intercept_[0]:.4f}", delta=f"{model.intercept_[0] - b:.4f} from true intercept")

    with col2:
        st.subheader("Prediction Funnel Chart")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.regplot(x='X', y='y', data=df, ax=ax, label='Data Points & Regression Line',
                    scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
        
        # Plot the true line
        x_range = np.array([df['X'].min(), df['X'].max()])
        y_range_true = a * x_range + b
        ax.plot(x_range, y_range_true, color='green', linestyle='--', label=f'True Line')
        
        ax.set_title(f'Linear Regression (a={a}, noise={noise}, n={n_points})')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

def run_multiple_linear_regression():
    st.header("Multiple Linear Regression (MLR)")

    # --- Sidebar Controls for MLR ---
    st.sidebar.header("MLR Controls")
    n_points_mlr = st.sidebar.slider("Number of Points", 100, 2000, 500, 50)
    noise_mlr = st.sidebar.slider("Noise Level", 0.0, 50.0, 15.0, 1.0)
    n_features = 5 # Fixed number of features for this example
    
    # --- Data Generation for MLR ---
    @st.cache_data
    def generate_mlr_data(n_points, n_features, noise):
        X = pd.DataFrame(np.random.rand(n_points, n_features) * 10, 
                         columns=[f'X{i+1}' for i in range(n_features)])
        true_coeffs = np.array([i*2 for i in range(1, n_features + 1)])
        y = X @ true_coeffs + 10 + np.random.randn(n_points) * noise
        X['y'] = y
        return X, true_coeffs

    data, true_coeffs = generate_mlr_data(n_points_mlr, n_features, noise_mlr)
    X = data.drop('y', axis=1)
    y = data['y']

    # --- Feature Selection ---
    st.sidebar.subheader("Feature Selection")
    use_rfe = st.sidebar.checkbox("Use Recursive Feature Elimination (RFE)")
    
    if use_rfe:
        n_features_to_select = st.sidebar.slider("Number of features to select", 1, n_features, n_features - 1)
        estimator = LinearRegression()
        selector = RFE(estimator, n_features_to_select=n_features_to_select, step=1)
        selector = selector.fit(X, y)
        selected_features = X.columns[selector.support_]
    else:
        selected_features = st.sidebar.multiselect("Manually select features", options=X.columns.tolist(), default=X.columns.tolist())

    if not selected_features:
        st.warning("Please select at least one feature.")
        return

    X_selected = X[selected_features]

    # --- Modeling ---
    model_mlr = LinearRegression()
    model_mlr.fit(X_selected, y)
    y_pred_mlr = model_mlr.predict(X_selected)

    # --- Evaluation ---
    r2_mlr = r2_score(y, y_pred_mlr)
    mse_mlr = mean_squared_error(y, y_pred_mlr)
    mae_mlr = mean_absolute_error(y, y_pred_mlr)

    st.subheader("Feature Selection & Model Coefficients")
    st.write(f"**Selected Features**: `{list(selected_features)}`")
    
    coeffs_df = pd.DataFrame({
        'Feature': selected_features,
        'Learned Coefficient': model_mlr.coef_
    })
    st.table(coeffs_df)

    st.subheader("Model Evaluation")
    eval_col1, eval_col2, eval_col3 = st.columns(3)
    eval_col1.metric("R-squared", f"{r2_mlr:.4f}")
    eval_col2.metric("Mean Squared Error (MSE)", f"{mse_mlr:.4f}")
    eval_col3.metric("Mean Absolute Error (MAE)", f"{mae_mlr:.4f}")

    # --- Visualization ---
    st.subheader("Model Performance Visualization")
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.scatter(y, y_pred_mlr, alpha=0.6, edgecolors='k')
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Perfect Prediction')
    ax.set_xlabel("Actual Values")
    ax.set_ylabel("Predicted Values")
    ax.set_title("Actual vs. Predicted Values")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

def run_auto_regression():
    st.header("AutoRegression (AR) for Time Series")

    # --- Sidebar Controls for AR ---
    st.sidebar.header("AR Controls")
    n_points_ar = st.sidebar.slider("Number of Time Steps", 100, 500, 200, 10)
    ar_lags = st.sidebar.slider("Number of AR Lags (p)", 1, 5, 2, 1)
    noise_ar = st.sidebar.slider("Noise Level", 0.1, 5.0, 1.0, 0.1)
    forecast_steps = st.sidebar.slider("Forecast Steps", 10, 50, 20, 5)

    # --- Data Generation for AR ---
    @st.cache_data
    def generate_ar_data(n_points, lags, noise):
        # Create a simple AR(2) process: y_t = 0.6*y_{t-1} - 0.3*y_{t-2} + noise
        ar_params = np.array([0.6, -0.3])
        y = [0, 0]
        for _ in range(n_points):
            ar_term = np.dot(ar_params, y[-2:])
            y.append(ar_term + np.random.randn() * noise)
        return pd.Series(y[2:])

    ts_data = generate_ar_data(n_points_ar, ar_lags, noise_ar)

    # --- Stationarity Check ---
    st.subheader("Time Series Analysis")
    adf_test = adfuller(ts_data)
    st.write(f"**Augmented Dickey-Fuller Test for Stationarity**")
    st.write(f"ADF Statistic: `{adf_test[0]:.3f}` | p-value: `{adf_test[1]:.3f}`")
    if adf_test[1] > 0.05:
        st.warning("The generated time series may not be stationary, which can affect model performance.")
    else:
        st.success("The generated time series is likely stationary.")

    # --- ACF/PACF Plots ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    plot_acf(ts_data, ax=ax1, title="Autocorrelation (ACF)")
    plot_pacf(ts_data, ax=ax2, title="Partial Autocorrelation (PACF)")
    st.pyplot(fig)
    st.info("Use the PACF plot to help identify the appropriate number of lags for the AR model.")

    # --- Modeling ---
    model_ar = AutoReg(ts_data, lags=ar_lags).fit()
    
    st.subheader("Model Results")
    st.text(str(model_ar.summary()))

    # --- Visualization ---
    st.subheader("Model Fit and Forecast")
    fig, ax = plt.subplots(figsize=(12, 6))
    ts_data.plot(ax=ax, label="Original Data")
    model_ar.predict(start=0, end=len(ts_data)).plot(ax=ax, label="Fitted Values", linestyle='--')
    model_ar.predict(start=len(ts_data), end=len(ts_data) + forecast_steps).plot(ax=ax, label="Forecast", linestyle=':', color='red')
    ax.set_title("AutoRegression Model Fit and Forecast")
    ax.set_xlabel("Time Steps")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


# --- Main App ---
st.title("Regression & Time Series Explorer")

st.sidebar.title("Model Selection")
model_choice = st.sidebar.radio(
    "Choose a model to explore:",
    ("Simple Linear Regression", "Multiple Linear Regression", "AutoRegression")
)

if model_choice == "Simple Linear Regression":
    run_simple_linear_regression()
elif model_choice == "Multiple Linear Regression":
    run_multiple_linear_regression()
elif model_choice == "AutoRegression":
    run_auto_regression()