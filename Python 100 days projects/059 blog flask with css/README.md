# Flask Blog With CSS

This project is a blog built with Flask, a Python microframework, showcasing blog posts retrieved from an external API. It features multiple pages, including a homepage with all posts, about and contact pages, as well as a dedicated page for each blog post.

## Features

- **Flask Integration**: Utilizes Flask to serve the blog on the web.
- **External API for Blog Posts**: Fetches blog posts from an external API to display on the blog.
- **Template Rendering**: Uses Flask's `render_template` to dynamically render HTML pages with blog content.
- **Year Dynamic Update**: Dynamically updates the year in the footer copyright notice.

## Installation

To set up this project locally, follow these steps:

1. **Clone the repository**:
```bash
git clone https://github.com/TonyVSK/Python-100-days/tree/main/Python%20100%20days%20projects/059%20blog%20flask%20with%20css
```

2. **Create a virtual environment** (Optional but recommended):
```bash
python -m venv venv
```

Activate it:
- On Windows: `venv\Scripts\activate`
- On Unix or MacOS: `source venv/bin/activate`

3. **Install the dependencies**:
```bash
pip install flask requests
```


## Running the Application

To run the application, follow these steps:

1. **Set the FLASK_APP environment variable** (Refer to Flask documentation for different operating systems):
```bash
export FLASK_APP=hello.py
```
On Windows, use `set` instead of `export`.

2. **Run Flask**:
```bash
flask run
```

Alternatively, you can use `python -m flask run`.

The application will be available at `http://127.0.0.1:5000/` by default.

## Usage

The blog is straightforward to navigate:

- **Homepage**: Displays all blog posts. Access it directly via `/` or `/index.html`.
- **About Page**: Contains information about the blog or the author. Access it via `/about.html`.
- **Contact Page**: For contacting the author. Access it via `/contact.html`.
- **Post Page**: Each post can be accessed by clicking on its title on the homepage or directly via `/post/<post_id>`, where `<post_id>` is the numerical ID of the post.

## Customization

To customize the blog, such as changing the source of the blog posts, modify the `owm_Endpoint` in the code to your desired API endpoint.

## Support

For support, please open an issue on the GitHub repository page.

## Contribution

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.