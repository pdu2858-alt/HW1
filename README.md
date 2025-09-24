# Simple Linear Regression Web App

This project is a simple web application that demonstrates linear regression. It is built with Flask and follows the CRISP-DM methodology.

## Project Structure

```
hw1/
├── app.py              # Main Flask application file
├── templates/
│   └── index.html      # HTML template for the web interface
├── requirements.txt    # Python dependencies
├── idea.md             # Initial idea and requirements
├── log.md              # Log of activities
└── README.md           # This file
```

## How to Run the Application

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application:**

   ```bash
   python app.py
   ```

3. **Open your web browser and go to:**

   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Code Explanation

### `app.py`

This file contains the main Flask application. Here's a breakdown of the code:

- **Imports:** Necessary libraries like Flask, NumPy, Scikit-learn, and Matplotlib are imported.
- **`generate_data(n_points, a, noise)`:** This function generates synthetic data for the linear regression model. It creates `X` and `y` values based on the user's input for the number of points, slope `a`, and noise level.
- **`train_model(X, y)`:** This function takes the generated data and trains a simple linear regression model using Scikit-learn.
- **`create_plot(X, y, model, a, n_points, noise)`:** This function generates a plot that visualizes the data points, the true underlying line, and the fitted regression line. The plot is saved to a memory buffer and encoded in Base64 to be displayed on the web page.
- **`index()`:** This is the main view function that handles both GET and POST requests. 
    - On a GET request, it displays the page with default values.
    - On a POST request, it gets the user's input from the form, generates new data, retrains the model, and re-renders the page with the updated plot and results.
- **CRISP-DM:** The `index` function is structured to follow the CRISP-DM steps:
    - **Data Preparation:** `generate_data` is called.
    - **Modeling:** `train_model` is called.
    - **Evaluation:** `create_plot` is called, and the model's coefficients are displayed.

### `templates/index.html`

This is the HTML template for the web interface. It uses a simple layout with controls for the user to modify the parameters and a section to display the results.

- **Controls:** The form allows the user to adjust the slope `a`, noise level, and the number of data points using sliders.
- **CRISP-DM Steps:** The CRISP-DM process is explained in a list.
- **Results:** The generated plot is displayed, along with the learned slope and intercept of the regression model.