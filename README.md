# Music Web App Backend

This is the backend system for a music web application, developed using Flask. The backend provides various features such as user authentication, music upload, streaming, playlist management, and music recommendation. It exposes a RESTful API for the frontend to interact with, and uses Swagger for API documentation.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles using JWT tokens for secure access.
- **Music Upload**: Artists can upload music files (MP3, WAV, etc.), and the system automatically extracts metadata.
- **Music Streaming**: Users can stream music directly from the backend, with options for different audio qualities.
- **Playlist Management**: Users can create, manage, and share playlists.
- **Music Recommendations**: Personalized music recommendations based on user activity.
- **File Storage**: Music files are stored securely on AWS S3 (or another cloud storage provider).
- **Search**: Users can search for songs, artists, albums, and playlists.
- **Social Features**: Users can follow other users, comment on playlists, and share tracks.
- **Subscription**: Premium users can access high-quality streams and additional features.
- **Real-Time Notifications**: Users receive real-time updates about their playlists, new music releases, and recommendations.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/music-app-backend.git
   cd music-app-backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and configure environment variables (like database URI, secret keys, etc.):

   ```bash
   touch .env
   ```

   Example `.env` content:
   ```bash
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/musicdb
   JWT_SECRET_KEY=your-jwt-secret-key
   AWS_ACCESS_KEY_ID=your-aws-access-key
   AWS_SECRET_ACCESS_KEY=your-aws-secret-key
   ```

5. Set up the database and run migrations:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the Flask development server:

   ```bash
   flask run
   ```

---

## API Endpoints

The backend exposes a RESTful API for interaction with the frontend. The API documentation is generated using **Swagger** and can be accessed at:

**Swagger Documentation**: `http://localhost:5000/api/docs`

Here are the main API endpoints:

### **Authentication**
- `POST /auth/signup`: Register a new user.
- `POST /auth/login`: Log in and get a JWT token.
- `GET /auth/profile`: Get the logged-in user's profile.

### **Tracks**
- `GET /tracks`: Get a list of all music tracks.
- `GET /tracks/{track_id}`: Get details of a specific track.
- `POST /tracks`: Upload a new music track (artists only).
- `DELETE /tracks/{track_id}`: Delete a track.

### **Playlists**
- `GET /playlists`: Get the list of playlists for the current user.
- `GET /playlists/{playlist_id}`: Get details of a specific playlist.
- `POST /playlists`: Create a new playlist.
- `PUT /playlists/{playlist_id}`: Update a playlist (add/remove tracks).
- `DELETE /playlists/{playlist_id}`: Delete a playlist.

### **Streaming**
- `GET /stream/{track_id}`: Stream a specific track.
- **Note**: The backend uses adaptive bitrate streaming for different quality levels.

### **Recommendations**
- `GET /recommendations`: Get personalized song recommendations.

### **Search**
- `GET /search`: Search for songs, albums, or artists.

### **Social**
- `GET /users/{user_id}`: Get a user’s public profile.
- `POST /follow/{user_id}`: Follow a user.
- `POST /comments`: Post a comment on a track or playlist.

---

## Running Tests

To run unit and integration tests, use the following command:

```bash
pytest
```

The test suite covers API endpoints, authentication, file uploads, and database models.

---

## Configuration

The application is configured using environment variables. Some key configuration settings are:

- `FLASK_ENV`: Flask environment mode (development, production).
- `SECRET_KEY`: A secret key for encrypting session data.
- `SQLALCHEMY_DATABASE_URI`: Database connection URI.
- `JWT_SECRET_KEY`: JWT secret key for encoding tokens.
- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`: AWS credentials for S3 storage.

---

## Deployment

The backend can be deployed to a production environment using a WSGI server like **Gunicorn**. Below is an example of how to deploy with Gunicorn:

1. Install Gunicorn:

   ```bash
   pip install gunicorn
   ```

2. Run Gunicorn with your Flask app:

   ```bash
   gunicorn --bind 0.0.0.0:8000 wsgi:app
   ```

3. You can also deploy this app on cloud platforms like AWS, Heroku, or Google Cloud using Docker or other deployment tools.

---

## Swagger API Documentation

To generate and expose the API documentation, Swagger is integrated with Flask. The Swagger UI will automatically generate API documentation based on your API routes.

To set up Swagger:
1. Install `Flask-Swagger`:
   ```bash
   pip install flask-swagger
   ```

2. Set up Swagger documentation in your `routes.py`:

   ```python
   from flask import jsonify
   from flask_swagger import swagger

   @app.route("/api/docs")
   def api_docs():
       """
       Swagger API documentation
       ---
       """
       return jsonify(swagger(app))
   ```

3. Access the Swagger docs at `http://localhost:5000/api/docs`.

---

## Future Enhancements

- **Real-time chat**: Add real-time communication features for users.
- **Offline listening**: Allow premium users to download tracks for offline listening.
- **Analytics**: Provide detailed analytics for artists on track performance and user demographics.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

We welcome contributions! Please read our [CONTRIBUTING](CONTRIBUTING.md) guidelines for more details.

---

### Contact

If you have any questions, feel free to reach out to:

- **Email**: okedieugine@gmail.com
- **GitHub**: eugineokedi(https://github.com/eugineokedi)