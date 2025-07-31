Here's the updated README that reflects that the `docker-compose.yml` file is already in the root of your project:

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

You have two options to run the application: using Gunicorn or Docker.

##### Option A: Using Gunicorn

Start the app using Gunicorn:

```bash
gunicorn wsgi:app
```

Open your browser and go to `http://127.0.0.1:8000` to start playing!

---

##### Option B: Using Docker

To run the application using Docker, follow these steps:

1. **Ensure Docker and Docker Compose are installed** on your machine.

2. **Run the application** using Docker Compose:

   ```bash
   docker-compose up
   ```

3. Open your browser and go to `http://127.0.0.1` to start playing!

Now you can enjoy the Bingo App either locally with Gunicorn or through Docker!