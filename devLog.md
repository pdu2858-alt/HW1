# Development Log: Regression & Time Series Explorer

This log details the step-by-step development process of the "Regression & Time Series Explorer" project, documenting interactions, decisions, and implementations.

## 2025-09-24 - Project Genesis and Initial Setup

### 1. Initial Project Upload to GitHub
- **Action**: User requested to upload existing project files (`hw1` directory) to a new GitHub repository.
- **Implementation**: 
    - Initialized Git repository in `C:\C_projects\.vscode\hw1`.
    - Added remote origin: `https://github.com/pdu2858-alt/HW1.git`.
    - Staged all files (`git add .`).
    - User provided Git `user.name` ("Pa Du") and `user.email` ("pdu2858@gmail.com") after initial commit failure.
    - Committed files with message "Initial commit".
    - Pushed to `master` branch.

### 2. Conversion from Flask to Streamlit
- **Action**: User requested to convert the Flask web application to a Streamlit application for deployment on `streamlit.app`.
- **Implementation**: 
    - Read `app.py` (Flask), `requirements.txt`, and `templates/index.html` to understand existing structure.
    - Created `streamlit_app.py` with Streamlit-compatible code, adapting data generation, model training, and plotting logic.
    - Updated `requirements.txt` to replace `flask` with `streamlit` and other necessary libraries.
    - Deleted old `app.py` (Flask) and the `templates` directory.
    - Renamed `streamlit_app.py` to `app.py` for standard Streamlit deployment.
    - Committed changes with message "Convert Flask app to Streamlit".
    - Pushed changes to GitHub.

### 3. Initial Documentation Enhancement
- **Action**: User requested to fill in `idea.md`, `log.md`, `steps.md`, and enhance `README.md`.
- **Implementation**: 
    - Read existing markdown files.
    - Updated `README.md` to reflect Streamlit app, new instructions, and project description.
    - Expanded `idea.md` into a more descriptive project idea document.
    - Updated `log.md` (this file) with the conversion to Streamlit.
    - Created `steps.md` detailing the development process from scratch.
    - Committed changes with message "docs: Complete and update all project documentation".
    - Pushed changes to GitHub.

### 4. Streamlit Demo URL Update (First Time)
- **Action**: User provided a new Streamlit demo URL and requested to update `README.md`.
- **Implementation**: 
    - Read `README.md`.
    - Replaced placeholder URL and title with `[DEMO SIDE](https://appapppy-dg4bts84wuqhz6tfoawmwd.streamlit.app/)`.
    - Committed changes with message "docs: Update README with new demo URL".
    - Pushed changes to GitHub.

### 5. Project Expansion: MLR, AR, Enhanced Evaluation
- **Action**: User requested to expand the project to include Multiple Linear Regression (MLR), AutoRegression (AR), feature selection, enhanced model evaluation, and a "prediction funnel chart".
- **Implementation**: 
    - Rewrote `app.py` to incorporate a model selection sidebar.
    - Implemented `run_simple_linear_regression()`: Added R-squared, MSE, MAE, and confidence interval (funnel chart) using `sns.regplot`.
    - Implemented `run_multiple_linear_regression()`: Added data generation for multiple features, manual/RFE feature selection, MLR modeling, R-squared, MSE, MAE, and actual vs. predicted plot.
    - Implemented `run_auto_regression()`: Added time series data generation, stationarity test, ACF/PACF plots, `statsmodels.tsa.ar_model.AutoReg` modeling, model summary, and forecast visualization.
    - Updated `requirements.txt` to include `pandas` and `statsmodels`.
    - Committed changes with message "feat: Add MLR, AR models and enhance evaluation".
    - Pushed changes to GitHub.

### 6. Bug Fix: `AttributeError` in MLR
- **Action**: User reported `AttributeError` in MLR section when manually selecting features.
- **Implementation**: 
    - Identified the issue: `selected_features.tolist()` failed when `selected_features` was a list (from `st.multiselect`) instead of a pandas `Index` (from RFE).
    - Modified `app.py` to use `list(selected_features)` for consistent handling.
    - Committed fix with message "fix: Handle list and Index types for selected features".
    - Pushed fix to GitHub.

### 7. Streamlit Demo URL Update (Second Time)
- **Action**: User provided the *same* new Streamlit demo URL again and requested to update `README.md`.
- **Implementation**: 
    - Confirmed the URL was already updated.
    - Re-applied the `replace` command to ensure consistency (though redundant).
    - Committed changes with message "docs: Update demo site URL".
    - Pushed changes to GitHub.

### 8. `README.md` Text Refinement
- **Action**: User requested to change "DEMO SIDE" to "Demo Site" and add the raw URL below the hyperlink in `README.md`.
- **Implementation**: 
    - Read `README.md`.
    - Used `replace` to change `## DEMO SIDE\n\n[DEMO SIDE](...)` to `## Demo Site\n\n[Demo Site](...)\n<raw_url>`.
    - Committed changes with message "docs: Update demo link text and add raw URL".
    - Pushed changes to GitHub.

### 9. Add `Todo.md`
- **Action**: User requested to create `Todo.md` with a list of future tasks.
- **Implementation**: 
    - Created `Todo.md` with a comprehensive list of potential enhancements for all model types and general project aspects.
    - Committed changes with message "docs: Add Todo.md with project to-do list".
    - Pushed changes to GitHub (after resolving a `git pull` conflict due to remote changes).
