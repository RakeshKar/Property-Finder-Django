# Property Finder Website

This is a website made using Django for the backend and React for the frontend. It is for locating houses for buy/sell/rent. It was inspired and done exactly from this course: https://www.udemy.com/course/django-react-build-a-location-based-real-estate-website/

## Features

- **Frontend:** Built with React and styled using Material UI.
- **Backend:** Django with Django Rest Framework (DRF) for APIs.
- **Maps:** Leaflet with React-Leaflet.
- **Database:** PostgreSQL with the PostGIS.
- **Authentication:** Djoser library.
- **Deployment:** Windows.

## Tech Stack

- **Frontend:**
  - React 17
  - Material UI 5
  - React-Leaflet
  
- **Backend:**
  - Django 4.0
  - Django Rest Framework (DRF)
  - Djoser for authentication
  
- **Database:**
  - PostgreSQL with PostGIS
  
## Setup

### Prerequisites

- **Python 3.9** for the backend
- **Node.js** and **npm** for the frontend
- python -m venv venv
- venv\Scripts\activate  # For Windows
- pip install -r backend/requirements.txt
- python manage.py migrate
- python manage.py runserver
- cd frontend
- npm install
- npm start
