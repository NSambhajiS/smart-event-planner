# My Fullstack App

This project is a fullstack application built using React for the frontend, FastAPI for the backend, and MongoDB Atlas for the database. 

## Technologies Used
- **Frontend**: React
- **Backend**: FastAPI
- **Database**: MongoDB Atlas

## Project Structure
```
my-fullstack-app
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── database.py
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── public
│   ├── src
│   │   ├── App.jsx
│   │   ├── components
│   │   └── index.js
│   ├── package.json
│   └── README.md
└── README.md
```

## Getting Started

### Backend Setup
1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## API Documentation
Refer to the `backend/README.md` for detailed API usage and endpoints.

## Frontend Documentation
Refer to the `frontend/README.md` for detailed usage and component structure.

## License
This project is licensed under the MIT License.