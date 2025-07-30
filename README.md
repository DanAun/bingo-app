## 🎉 Bingo App

Welcome to the **Bingo App**! This app is designed for you and your friends to stay connected and have fun playing bingo together, no matter where you are.

### 🚀 Getting Started

Follow these steps to run the app:

#### 1. Clone the Repository

```bash
git clone https://github.com/DanAun/bingo-app.git
cd bingo-app
```

#### 2. Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

#### 3. Run the Application

Start the app using Gunicorn:

```bash
gunicorn wsgi:app
```

Open your browser and go to `http://127.0.0.1:8000` to start playing!