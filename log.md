### HW1: Simple Linear Regression Web App - Project Plan

This plan outlines the steps to create a Python web application for simple linear regression, following the CRISP-DM methodology as specified in `idea.md`.

#### 1. Business Understanding
*   **Objective:** Create an interactive web application to visualize and understand simple linear regression (`y = ax + b`).
*   **Success Criteria:** The application should allow users to generate data with custom parameters (`a`, noise, number of points), train a linear regression model, and see the results visually. The entire process should be documented and clear to the user.

#### 2. Data Understanding
*   **Data Source:** The data will be synthetically generated based on user inputs.
*   **Inputs from User:**
    *   Slope (`a`)
    *   Y-intercept (`b`) - *Assumption: `b` should also be a parameter for `y=ax+b`.*
    *   Noise level (e.g., standard deviation of the random noise)
    *   Number of data points.
*   **Data Characteristics:** The data will be a set of (x, y) pairs where `y` is approximately `ax + b`.

#### 3. Data Preparation
*   **Process:**
    1.  Generate a sequence of `x` values.
    2.  Calculate the corresponding `y` values using `y = ax + b`.
    3.  Add random noise to the `y` values to simulate a real-world dataset.
    4.  Structure the data into a suitable format (e.g., a Pandas DataFrame) for modeling.

#### 4. Modeling
*   **Model Choice:** Simple Linear Regression.
*   **Library:** Use `scikit-learn`'s `LinearRegression` model.
*   **Process:**
    1.  Instantiate the model.
    2.  Train the model on the prepared dataset (`X_train`, `y_train`).
    3.  Extract the learned coefficients (slope and intercept) from the model.

#### 5. Evaluation
*   **Metrics:**
    *   Mean Squared Error (MSE) or R-squared value to quantify model performance.
    *   Visual comparison: Plot the original data points, the "true" line (from user's `a` and `b`), and the model's regression line on a single graph.
*   **Output:** Display the learned coefficients and the chosen evaluation metric to the user.

#### 6. Deployment
*   **Framework:** Choose between Streamlit or Flask. Streamlit is generally faster for data-centric apps. Let's proceed with **Streamlit**.
*   **Application Structure:**
    *   **UI Components:**
        *   Sliders/input boxes for `a`, `b`, noise, and number of points.
        *   A "Generate Data & Train Model" button.
        *   A plot area (using Matplotlib or Plotly) to display the graph.
        *   Text area to show the model's results (coefficients, MSE/R-squared).
    *   **Deployment Platform:** The final application will be deployed (e.g., on Streamlit Community Cloud) and the code pushed to GitHub.
