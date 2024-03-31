# Post Requests With Flask and HTML Forms

This Flask application demonstrates handling POST requests with HTML forms, showcasing a simple blog where users can view posts and submit contact information through a form. The contact form submissions are sent via email using SMTP.

## Features

- **Flask Framework**: Utilizes Flask to create web routes and serve HTML templates.
- **External API for Blog Posts**: Fetches blog posts from an external API to be displayed on the index page.
- **Contact Form**: Includes a contact form that users can submit. Submissions are sent to the owner's email via SMTP.
- **HTML Template Rendering**: Dynamically renders HTML templates with blog posts and form submissions.

## Installation

Ensure you have Python and pip installed on your system. Then, follow these steps to get the application running locally:

1. **Clone the Repository**:
```bash
git clone https://your-repository-link-here.git
```

2. **Navigate to the Project Directory**:
```bash
cd path-to-your-project
```

3. **Install Dependencies**:
Install Flask and Requests with pip:
```bash
pip install flask requests
```


## Configuration

Before running the application, you'll need to configure a few items:

1. **Email Credentials**: In the `usefulkeys.py` file, provide your email address and password for SMTP email sending.
2. **SMTP Setup**: Ensure that the SMTP settings are configured correctly for your email provider in the `send_email` function.
3. **API Endpoint**: Replace the npoint API endpoint with your own, where your blog posts are stored.

## Running the Application

Start the Flask application with the following command:
```bash
flask run --port=5001
```


Or directly with Python:
```bash
python main.py
```



The application will be accessible at `http://127.0.0.1:5001/`.

## Usage

- **Viewing Blog Posts**: Visit the homepage (`/`) to view all blog posts fetched from the external API.
- **About Page**: Accessible via `/about`, providing information about the blog or its creator.
- **Contact Page**: Found at `/contact`, where users can fill out and submit the contact form.
- **View Individual Post**: Click on a post title or navigate to `/post/<post_id>` to view an individual blog post.
- **Submitting Contact Form**: Submit the contact form on the `/contact` page, which will send the submitted information to the specified email.

## Support

For any issues or questions, please open an issue on the GitHub repository.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.