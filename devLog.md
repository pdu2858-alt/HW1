# Development Log: Regression & Time Series Explorer - AI Interaction History

This log details the complete interaction history with the AI, documenting prompts, actions, decisions, and implementations that led to the creation and evolution of the "Regression & Time Series Explorer" project.

## Initial Project Conception (Prompts before AI interaction)

### User Prompt 1 (Project Core Requirements):
```
write python to solve simple linear regression problem, following CRISP-DM steps,
要有prompt and 過程, 不可只有CODE AND RESULT
1. CRISP-DM
2. allow user to modify a in ax+b, noise, number of points
3. streamlit or flask web, 框架 deployment
```

### User Prompt 2 (Project Expansion Requirements):
```
做 auto regression , multiple linear regression
1. feature selection
2. model evaluation
3. web implementation deployment
4. 預測漏斗圖
```

---

## AI-Assisted Development Process (Chronological Interaction Log)

### 2025-09-24 - Project Genesis and Initial Setup

#### User Prompt: "幫我把這些東西上傳到github，網址為https://github.com/pdu2858-alt/HW1.git。"
- **AI Action**: Initialized Git repository, added remote, staged files, committed, and pushed.
- **Note**: User provided Git credentials (name, email) during this step after initial commit failure.

#### User Prompt: "幫我把這個程式在streamlit.app上面呈現，請把他們做成那樣"
- **AI Action**: Converted the Flask application to a Streamlit application.
- **Implementation**:
    - Read existing Flask `app.py`, `requirements.txt`, `templates/index.html`.
    - Created `streamlit_app.py` with Streamlit logic.
    - Updated `requirements.txt` (removed `flask`, added `streamlit`).
    - Deleted old Flask `app.py` and `templates` directory.
    - Renamed `streamlit_app.py` to `app.py`.
    - Committed and pushed changes to GitHub.

#### User Prompt: "幫我完善這個hw1裡面所有資料，像是steps裡面要有步驟，其餘空白檔案也要寫滿與檔名應有的內容，然後再推送到github上"
- **AI Action**: Enhanced project documentation.
- **Implementation**:
    - Updated `README.md` to reflect Streamlit app and new instructions.
    - Expanded `idea.md` into a descriptive project idea document.
    - Updated `log.md` (this file's predecessor) with the Streamlit conversion.
    - Created `steps.md` detailing the development process.
    - Committed and pushed changes to GitHub.

#### User Prompt: "這是我的demo side網址，請把我的README裡面的demo side網址超連結和網址改成https://appapppy-dg4bts84wuqhz6tfoawmwd.streamlit.app/"
- **AI Action**: Updated `README.md` with the first Streamlit demo URL.
- **Implementation**:
    - Replaced placeholder URL in `README.md` with the provided link.
    - Committed and pushed changes to GitHub.

#### User Prompt: "幫我瀏覽整個專案的成果是否與上述的相符，如果有缺的幫我補上，並且推送到github，並且可以在streamlit.app上呈現"
- **AI Action**: Reviewed project against new requirements (MLR, AR, evaluation) and implemented missing features.
- **Implementation**:
    - Rewrote `app.py` to include a model selection sidebar.
    - Implemented Simple Linear Regression (SLR) with R-squared, MSE, MAE, and confidence interval ("funnel chart").
    - Implemented Multiple Linear Regression (MLR) with data generation, manual/RFE feature selection, MLR modeling, evaluation metrics, and actual vs. predicted plot.
    - Implemented AutoRegression (AR) with time series data generation, stationarity test, ACF/PACF plots, `statsmodels.tsa.ar_model.AutoReg` modeling, model summary, and forecast visualization.
    - Updated `requirements.txt` (added `pandas`, `statsmodels`).
    - Committed and pushed changes to GitHub.

#### User Prompt: "網頁呈現當中出現錯誤，幫我修正，錯誤的訊息如下..." (AttributeError in MLR)
- **AI Action**: Fixed `AttributeError` in MLR feature selection.
- **Implementation**:
    - Identified the issue: `selected_features.tolist()` failed when `selected_features` was a list (from `st.multiselect`) instead of a pandas `Index` (from RFE).
    - Modified `app.py` to use `list(selected_features)` for consistent handling.
    - Committed and pushed fix to GitHub.

#### User Prompt: "這是最新的完成的網站，幫我推送到github的README上面，修改demo side超連結以及後面的網址https://mr9k4baokapjfmrbjkbanu.streamlit.app/"
- **AI Action**: Updated `README.md` with the latest Streamlit demo URL.
- **Implementation**:
    - Replaced the previous demo URL in `README.md` with the new one.
    - Committed and pushed changes to GitHub.

#### User Prompt: "把全大寫的DEMO SIDE改成Demo Site，然後超連結以外底下再附一個原網址"
- **AI Action**: Refined `README.md` text and link format.
- **Implementation**:
    - Changed "DEMO SIDE" to "Demo Site" (heading and link text).
    - Added the raw URL below the hyperlink in `README.md`.
    - Committed and pushed changes to GitHub.

#### User Prompt: "幫我建一個Todo.md的檔案，內容為這整個專案的線性回歸實現的代辦事項列表，一樣push到github"
- **AI Action**: Created `Todo.md` with a project to-do list.
- **Implementation**:
    - Created `Todo.md` with a comprehensive list of potential enhancements.
    - Committed and pushed changes to GitHub (resolved `git pull` conflict due to remote changes).

#### User Prompt: "把你我交談的過程，也就是整個專案的生成方式，一個步驟一個步驟地寫進log.md檔案裡面，並且把log.md改名為devLog.md"
- **AI Action**: Documented the entire AI interaction process into `devLog.md`.
- **Implementation**:
    - Read existing `log.md`.
    - Generated this comprehensive log summarizing all prompts and AI actions.
    - Wrote content to `devLog.md`.
    - Deleted old `log.md`.
    - Committed and pushed changes to GitHub.

### Additional AI Interactions (Gemini CLI Setup & Related Queries)

#### User Prompt: "1.安裝gemini cli在win11系統的教學"
- **AI Action**: Provided instructions for installing Gemini CLI on Windows 11.

#### User Prompt: "2.在cmd輸入npm install -g @google/gemini-cli一直轉圈解法"
- **AI Action**: Provided troubleshooting steps for `npm install` hanging issues.

#### User Prompt: "3.給我完整cmd指令以下載gemini-cli"
- **AI Action**: Provided the complete `npm install -g @google/gemini-cli` command.

#### User Prompt: "4.如何在vscode叫出終端機與連接gemini cli"
- **AI Action**: Explained how to open the terminal in VS Code and connect/use Gemini CLI.

#### User Prompt: "5.根據我貼的需求，生成整個符合這個需求的專案，並且以網址當中的github專案為標準"
- **AI Action**: This prompt likely initiated the current project generation process, where the AI was tasked with creating a project based on user requirements and a GitHub project as a reference.

#### User Prompt: "6.如何在vscode的程式如何push到github"
- **AI Action**: Provided instructions on how to push code to GitHub from VS Code (using Git commands or VS Code's Git integration).

#### User Prompt: "7.streamlit的github URL要去哪裡取得"
- **AI Action**: Explained how to find the GitHub URL for a Streamlit app (usually the repository where the app's code resides).