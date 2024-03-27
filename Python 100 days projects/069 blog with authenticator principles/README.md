# Blog with Authenticator Principles

This Blog Platform is a web application designed for writers to publish and manage their blog posts. Built with Flask, it features user authentication, post creation, editing, and deletion, along with a simple and intuitive interface for readers to explore and read blog entries.

## Features

- **User Authentication:** Secure login and registration system, including password hashing for safety.
- **Blog Posting:** Logged-in users can create, edit, and delete their posts.
- **Comment System:** Users can comment on posts (TODO).
- **Admin Privileges:** Special controls for admin users to manage posts more effectively (TODO).
- **Responsive Design:** Utilizes Flask-Bootstrap for a responsive layout, ensuring compatibility across various devices.

## Technologies Used

- **Python:** Programming language for backend logic.
- **Flask:** Web framework for building the web application.
- **Flask Extensions:** Several Flask extensions are used, including Flask-Login for handling user sessions, Flask-WTF for form handling, Flask-CKEditor for rich text editing, and Flask-Bootstrap for front-end design.
- **SQLAlchemy:** ORM used for database interactions.
- **SQLite:** Database for storing user and blog post information.

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

1. **Clone the repository:**
2. **Create a virtual environment (optional but recommended):**
3. **Install the required packages:**
```pip install -r requirements.txt```
4. **Set up the environment variables:**
- Create a `.env` file in the root directory.
- Add `SECRET_KEY=your_secret_key_here` to the file.

5. **Initialize the database:**
Run the application once to create the SQLite database automatically.

6. **Run the application:**
```flask run```
or
```
python main.py
```


## Usage

After starting the application, visit `http://127.0.0.1:5002/` in your web browser to see the blog platform in action. You can register a new user, log in, create, edit, and delete posts as an authenticated user.

## Contributing

Contributions are welcome, and any feedback or suggestions are greatly appreciated. To contribute:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Flask documentation and community for the comprehensive guides and support.
- SQLAlchemy for providing a powerful ORM for Python.
- Flask extensions developers for enhancing Flask's functionality.