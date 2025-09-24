# Project Log & Changelog

## 2025-09-24

### v2.0.0: Conversion to Streamlit

- **Refactor**: The entire application was refactored from Flask to Streamlit.
- **UI/UX Overhaul**: Replaced the HTML form with interactive Streamlit widgets (`st.slider`).
- **Layout Improvement**: Implemented a two-column layout for a better user experience, separating controls and explanations from the results.
- **Dependencies**: Updated `requirements.txt` to remove `Flask` and add `Streamlit`.
- **File Cleanup**: Removed the old `app.py` (Flask) and the `templates/` directory.
- **Documentation**: Updated `README.md` with new instructions and a description of the Streamlit app.

### v1.0.0: Initial Flask Application

- **Initial Commit**: Project initialized.
- **Core Logic**: Implemented core functions for data generation (`generate_data`), model training (`train_model`), and plotting (`create_plot`).
- **Framework**: Created a basic Flask application (`app.py`) to serve the model and visualization.
- **Frontend**: Built an HTML template (`index.html`) with a form for user inputs.
- **CRISP-DM**: Structured the application flow and explanations around the CRISP-DM framework.
- **Dependencies**: Created `requirements.txt` with initial dependencies (`Flask`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`).
- **Git**: Initialized a Git repository and pushed the first version to GitHub.