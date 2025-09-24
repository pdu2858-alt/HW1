# Simple Linear Regression Visualizer

This project is an interactive web application built with Streamlit that demonstrates the principles of simple linear regression. It allows users to dynamically adjust parameters like slope, noise, and the number of data points to see how they affect the model's fit. The application is structured around the CRISP-DM methodology.

## Demo Site

[Demo Site](https://appapppy-dg4bts84wuqhz6tfoawmwd.streamlit.app/)
https://appapppy-dg4bts84wuqhz6tfoawmwd.streamlit.app/

## 📋 Features

- **Interactive Controls**: Use sliders to adjust the true slope (`a`), noise level, and number of data points.
- **Real-time Visualization**: The plot instantly updates to show the new data points, the "true" underlying line, and the fitted regression line.
- **Model Evaluation**: The learned slope and intercept from the `scikit-learn` model are displayed and updated in real-time.
- **CRISP-DM Framework**: The interface explains how each step of the CRISP-DM process applies to this modeling task.

## 🛠️ Technologies Used

- **Python**: The core programming language.
- **Streamlit**: For creating the interactive web application.
- **Scikit-learn**: For training the linear regression model.
- **NumPy**: For numerical operations and data generation.
- **Matplotlib & Seaborn**: For data visualization.

## ⚙️ How to Run the Application Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/pdu2858-alt/HW1.git
    cd HW1
    ```

2.  **Install dependencies:**
    Make sure you have Python installed. Then, install the required packages using pip.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

4.  **Open your web browser:**
    The application should automatically open in a new tab. If not, navigate to the local URL provided in your terminal (usually `http://localhost:8501`).

