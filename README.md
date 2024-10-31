# SMS Management System

## Overview
This is a Full Stack SMS Management System with a frontend built using React and a backend using FastAPI.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:

- **Docker**: For containerization and orchestration of the application.
- **Node.js**: For running the frontend application. Make sure to install the latest LTS version.

### Running the Application

#### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone <repository-url>
cd sms-management-system

 2. Backend Setup
Navigate to the backend directory and install the necessary dependencies:

cd backend
pip install -r requirements.txt


3. Frontend Setup
Navigate to the frontend directory and install the necessary dependencies:

cd ../frontend
npm install

4. Running the Application
You can run the entire application (both frontend and backend) using Docker:

    1) Navigate back to the root of the project:
      cd ..

    2) Start the application with Docker Compose:
      docker-compose up --build

This command will build the Docker images and start the application. The backend will be accessible at http://localhost:8000 and the frontend at http://localhost:3000.

Stopping the Application
To stop the application, use:

docker-compose down



Features

1) User authentication
2) SMS sending and receiving
3) Real-time metrics display
4) Country-operator management


Contributing

1) Fork the repository.
2) Create your feature branch (git checkout -b feature/YourFeature).
3) Commit your changes (git commit -m 'Add some feature').
4) Push to the branch (git push origin feature/YourFeature).
5) Open a pull request.


sms-management-system/
├── backend/                    # Backend application folder
│   ├── app/
│   │   ├── main.py             # Main entry point for the FastAPI application
│   │   ├── routes/             # Folder for route definitions
│   │   │   ├── auth.py         # Authentication routes
│   │   │   ├── sms_control.py   # Routes for SMS management
│   │   │   ├── metrics.py       # Routes for metrics display
│   │   │   └── country_operator.py # Routes for country-operator management
│   │   └── models/             # Database models
│   │       └── user.py         # User model
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Backend Docker configuration
│
├── frontend/                   # Frontend application folder
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── Dashboard.js     # Real-time metrics display
│   │   │   ├── ProgramControl.js # Program start/stop/restart
│   │   │   ├── CountryOperator.js # Manage country-operator pairs
│   │   │   └── Login.js         # Login page
│   │   ├── services/           # Axios API calls
│   │   │   └── api.js          # API service file
│   │   └── App.js              # Main app component
│   ├── Dockerfile               # Frontend Docker configuration
│   └── package.json             # Frontend dependencies
│
├── docker-compose.yml           # Docker setup for orchestrating frontend, backend, and databases
├── prometheus.yml               # Prometheus configuration file for monitoring
└── README.md                    # Project documentation

