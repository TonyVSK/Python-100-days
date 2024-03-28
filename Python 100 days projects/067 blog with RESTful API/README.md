# Flask Blog Application

This Flask blog application allows users to create, view, edit, and delete blog posts. It features a rich text editor for content creation, image URL embedding, and displays posts with date, author, and subtitle details. This application is built with Flask, Flask-Bootstrap for styling, Flask-SQLAlchemy for database operations, and CKEditor for rich text editing.

## Features

- **Create Posts**: Users can add new blog posts with titles, subtitles, authors, content, and images.
- **View Posts**: All blog posts are displayed on the homepage, and users can click on individual posts to view them.
- **Edit Posts**: Functionality to edit existing blog posts (To be implemented).
- **Delete Posts**: Functionality to delete blog posts from the database (To be implemented).
- **Rich Text Editing**: CKEditor is integrated to allow rich text editing of blog post content.
- **Image Embedding**: Users can embed images in their posts via URL.
- **Responsive Design**: Uses Flask-Bootstrap for a responsive web design that looks good on both desktop and mobile devices.

## Installation and Starting

Before you begin, ensure you have Python 3 installed on your system.

1. **Clone the repository**:

```bash
git clone https://github.com/TonyVSK/Python-100-days/tree/main/Python%20100%20days%20projects/067%20blog%20with%20RESTful%20API
cd path-to-this-repo-at-your-pc
```

2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install required packages:
```bash
pip install Flask Flask-Bootstrap Flask-SQLAlchemy Flask-WTF CKEditor
```

4. Initialize the database:
The application will automatically create a SQLite database (posts.db) in the project directory upon starting the application for the first time.

5. Run the application:
```bash
python main.py
```

This will start a development server on http://127.0.0.1:5003/.

## Application Structure
**Database Models**: Defined in main.py, with BlogPost as the primary model representing blog posts.

**Forms**: Uses Flask-WTF to define the CreatePostForm for submitting new blog posts.

**Templates**: HTML templates are located in the templates directory, using Jinja2 templating language for dynamic content.

**Static Files**: Static files such as CSS and images should be placed in the static directory.

## Routes
* /: The homepage that lists all blog posts.
* /post/<int:post_id>: Displays a specific blog post.
* /new-post: A form to create a new blog post. On submission, the blog post is added to the database, and the user is redirected to the homepage.
* /about: A static about page.
* /contact: A static contact page.
