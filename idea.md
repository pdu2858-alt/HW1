# Project Idea: Interactive Linear Regression Visualizer

## 1. Core Concept

The primary idea is to build an educational web application that helps users understand the fundamentals of simple linear regression (`y = ax + b`). Instead of a static demonstration, the application will be interactive, allowing users to manipulate key parameters and observe their impact on the model in real-time. This hands-on approach makes abstract concepts more tangible.

## 2. Key Objectives

- **Visualize Core Concepts**: Clearly show the relationship between data points, the true underlying function, and the model's fitted line.
- **Demonstrate CRISP-DM**: Structure the application and its explanation around the Cross-Industry Standard Process for Data Mining (CRISP-DM) to provide a methodological context.
- **Interactive Learning**: Allow users to modify parameters and see immediate results, fostering a deeper understanding of cause and effect in modeling.
- **Easy Deployment**: The application should be built using a modern web framework like Streamlit or Flask to ensure it can be easily deployed and shared.

## 3. User-Modifiable Parameters

The application must provide controls for users to adjust the following:

1.  **Slope (`a`)**: The coefficient of `x` in the true underlying model (`y = ax + 5`). This allows users to see how the model adapts to different underlying slopes.
2.  **Noise**: The amount of random variation added to the `y` values. This simulates the messiness of real-world data and demonstrates the model's robustness.
3.  **Number of Points**: The size of the synthetic dataset. This helps illustrate how sample size can affect the model's accuracy and stability.

## 4. Technical Framework

- **Language**: Python
- **Web Framework**: Streamlit was chosen for its simplicity and speed in developing data-focused applications.
- **Core Libraries**:
    - `scikit-learn`: For the `LinearRegression` model.
    - `numpy`: For generating the synthetic data.
    - `matplotlib`/`seaborn`: For creating the visualizations.

## 5. Target for Deployment

The final application is intended to be deployed on a public cloud platform like Streamlit Community Cloud, making it accessible via a public URL.

- **GitHub Repository**: [https://github.com/pdu2858-alt/HW1.git](https://github.com/pdu2858-alt/HW1.git)
- **Target Demo URL**: [https://aiotda.streamlit.app/](https://aiotda.streamlit.app/)
