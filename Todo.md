# To-Do List for Regression & Time Series Explorer

This document outlines potential future enhancements and tasks for the project.

## General Enhancements

- [ ] **Improve UI/UX**: Refine the layout and interactivity for a more intuitive user experience.
- [ ] **Add Loading Spinners**: Implement loading indicators for computations that take longer.
- [ ] **Error Handling**: Add more robust error handling and user feedback for invalid inputs or model failures.
- [ ] **Unit Tests**: Write unit tests for core functions (data generation, model training, plotting).
- [ ] **Code Refactoring**: Further refactor the code for better modularity and readability.

## Simple Linear Regression (SLR)

- [ ] **User-defined Intercept**: Allow users to modify the intercept (`b`) in `y = ax + b`.
- [ ] **Confidence/Prediction Intervals**: Provide clearer explanations and potentially separate controls for confidence vs. prediction intervals.
- [ ] **Residual Plots**: Add a residual plot to visually assess model assumptions.

## Multiple Linear Regression (MLR)

- [ ] **More Feature Selection Methods**: Implement additional feature selection techniques (e.g., Lasso, forward/backward selection).
- [ ] **Feature Importance Plot**: Visualize the importance of selected features.
- [ ] **Interaction Terms**: Allow users to add interaction terms between features.
- [ ] **Categorical Features**: Support for handling categorical features (e.g., one-hot encoding).

## AutoRegression (AR)

- [ ] **User-defined AR Coefficients**: Allow users to define the `phi` coefficients for AR data generation.
- [ ] **ARIMA/SARIMA Support**: Extend to more complex time series models like ARIMA and SARIMA.
- [ ] **Seasonality**: Add controls for generating and modeling seasonal time series data.
- [ ] **Exogenous Variables**: Allow for the inclusion of exogenous variables in time series models.
- [ ] **Forecast Evaluation**: Add metrics for forecast accuracy (e.g., RMSE, MAE for forecasts).

## Data Handling

- [ ] **Upload Custom Data**: Allow users to upload their own CSV or Excel files for analysis.
- [ ] **Data Preprocessing Options**: Include options for scaling, normalization, or outlier handling.

## Deployment

- [ ] **Continuous Integration/Deployment (CI/CD)**: Set up automated CI/CD pipelines for Streamlit Cloud deployment.
