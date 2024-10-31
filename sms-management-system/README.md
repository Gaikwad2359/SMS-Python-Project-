# SMS Management System

## Overview
This is a Full Stack SMS Management System with a frontend built using React and a backend using FastAPI.

## Getting Started

### Prerequisites
- Docker
- Node.js

### Running the Application
1. Clone the repository.
2. Navigate to the `frontend` directory and run:
   ```bash
   docker-compose up --build


# Project Structure

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


### Backend Setup 
 Navigate to the backend directory and install the necessary dependencies:
 ```bash
   cd backend
   pip install -r requirements.txt


### Frontend Setup 
 Navigate to the frontend directory and install the necessary dependencies:
   ```bash
   cd ../frontend
   npm install


## Running the Application

1) Navigate back to the root of the project:
   ```bash
   cd ...

2) Start the application with Docker Compose:
   ```bash
   docker-compose up --build


This command will build the Docker images and start the application. The backend will be accessible at http://localhost:8000 and the frontend at http://localhost:3000.


##Features

1) User authentication
2) SMS sending and receiving
3) Real-time metrics display
4) Country-operator management


## Contributing

Fork the repository.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.



