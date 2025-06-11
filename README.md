# Travel-Agency

```
travel-bot-api/
├── app/
│   ├── __init__.py
│   ├── main.py                # Main entry point for running the API
│   ├── config.py              # General configuration (environment variables, DB connections)
│   ├── routers/               # Main routes (endpoints)
│   │   ├── __init__.py
│   │   ├── destinations.py    # Endpoints related to destinations
│   │   ├── itineraries.py     # Endpoints related to itineraries
│   │   ├── transport.py       # Endpoints related to transportation
│   │   └── accommodations.py  # Endpoints related to accommodations
|   |
│   ├── auth/                  # Authenticate logic
│   │   ├── __init__.py
│   │   ├── jwt_bearer.py      # JWT Bearer dependency for FastAPI
│   │   ├── jwt_handler.py     # Creating and Validating Token 
|   |
|   |
│   ├── models/                # Definitions for data schemas (Pydantic)
│   │   ├── __init__.py
│   │   ├── destination.py
│   │   ├── itinerary.py
│   │   ├── transport.py
│   │   └── accommodation.py
│   ├── services/              # Business logic (calculations/suggestions)
│   │   ├── __init__.py
│   │   ├── destination_service.py
│   │   ├── itinerary_service.py
│   │   └── weather_service.py
│   └── db/                    # Database connection and management
│       ├── __init__.py
│       ├── database.py        # Database connection
|
|
|
├── .env                       # File containing environment variables (API keys, config)
├── .gitignore                 # List of files to be ignored in Git
├── requirements.txt           # Required libraries
├── Dockerfile                 # Docker configuration file
├── docker-compose.yml         # Docker Compose configuration file
└── README.md                  # Project description

```
