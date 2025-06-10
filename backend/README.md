# Backend API Documentation

## Overview
This backend is built using FastAPI and connects to a MongoDB Atlas database. It serves as the API layer for the fullstack application, providing endpoints for data interaction.

## Project Structure
- `app/main.py`: Entry point of the FastAPI application.
- `app/models.py`: Defines data models using Pydantic and MongoDB ODM.
- `app/routes.py`: Contains API route definitions and request handlers.
- `app/database.py`: Manages the connection to MongoDB Atlas.

## Setup Instructions

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd my-fullstack-app/backend
   ```

2. **Create a virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Set up MongoDB Atlas**
   - Create a MongoDB Atlas account and cluster.
   - Obtain the connection string and update it in `app/database.py`.

5. **Run the application**
   ```
   uvicorn app.main:app --reload
   ```

## API Usage
- The API endpoints are defined in `app/routes.py`. Refer to this file for available routes and their usage.

## Additional Notes
- Ensure that your MongoDB Atlas cluster is accessible from your application.
- For further customization, modify the models and routes as needed.