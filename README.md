# Smart Traffic Flow Prediction AI

A Flask-based web application that predicts traffic congestion levels using Machine Learning. This project helps users evaluate traffic conditions based on real-time factors like time, weather, vehicle volume, and signal status.

## 🚀 Features

-   **Real-time Prediction**: Inputs flow through a trained ML model to predict traffic volume and status (Lancar, Padat Merayap, Macet Total).
-   **Interactive Guide**: A dedicated "Panduan Pengisian" page with detailed tips and specific example scenarios to help users input accurate data.
-   **User-Friendly UI**: Modern interface built with Bootstrap 5 and Google Fonts (Plus Jakarta Sans).
-   **Scenario Simulation**: Visual cards in the guide showing exact inputs for different traffic conditions.

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **Frontend**: HTML5, Bootstrap 5.3, CSS3, FontAwesome
-   **Machine Learning**: Scikit-learn (Random Forest/Linear Regression context), Joblib, Pandas, NumPy

## 📂 Project Structure

```
Traffic_App/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment instruction (for Heroku/Render)
├── traffic_model_final.pkl # Trained ML Model
├── scaler.pkl              # Data Scaler
├── templates/
│   ├── index.html          # Main Dashboard/Form
│   └── guide.html          # Guide/Manual Page
└── README.md               # Project Documentation
```

## ⚙️ Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/Traffic_App.git
    cd Traffic_App
    ```

2.  **Create Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    python app.py
    ```

5.  **Access the App**
    Open your browser and go to `http://127.0.0.1:5001/`

## 📖 How to Use the Guide

1.  Click the **"Panduan"** button in the top navigation bar.
2.  Review the 5 categories (Time, Speed, Weather, Volume, Signal).
3.  Scroll to the bottom to see **"Contoh Skenario Lengkap"**.
4.  Use these example values to test the model (e.g., input the "Macet Total" scenario to see the Red result).

## ☁️ Deployment

To deploy this app to platforms like **Render**, **Railway**, or **Heroku**:

1.  Ensure `requirements.txt` and `Procfile` are present (included).
2.  Push this code to your GitHub repository.
3.  Connect your repo to the hosting service.
4.  The service will automatically detect the Python app and run it using the command in `Procfile`.

---
*Created for Traffic Flow Optimization Project*
