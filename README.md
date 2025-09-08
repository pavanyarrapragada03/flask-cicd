Flask CI/CD with GitHub Actions & Docker

This project demonstrates a CI/CD pipeline for a simple Flask app using Docker, GitHub Actions, and Pytest.
The pipeline automatically:
✅ Runs tests
✅ Builds a Docker image
✅ Pushes the image to Docker Hub
✅ Deploys locally using Docker Compose

Project Structure
flask-cicd/
│── app.py                 # Main Flask application
│── requirements.txt       # Python dependencies
│── Dockerfile             # Docker image definition
│── docker-compose.yml     # Local deployment config
│── tests/
│    └── test_app.py       # Unit tests with pytest
│── .github/
│    └── workflows/
│         └── docker.yml   # GitHub Actions workflow
│── README.md              # Project documentation


2️⃣ Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run tests
pytest -q

5️⃣ Run locally
python app.py


Visit: 👉 http://127.0.0.1:5000/

🐳 Docker Setup
1️⃣ Build the image
docker build -t dockerusername/flask-cicd:dev .

2️⃣ Run the container
docker run -p 5000:5000 dockerusername/flask-cicd:dev

3️⃣ Using Docker Compose
docker-compose up --build

🔄 CI/CD Pipeline (GitHub Actions)

The GitHub Actions workflow (.github/workflows/docker.yml) does the following:

Checkout repository

Set up Python environment

Install dependencies & run tests

Log in to Docker Hub

Build & push Docker image
