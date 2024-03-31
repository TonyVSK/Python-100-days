# ISS Tracker & Email Notifier with Kanye App Integration

This Python project combines two functionalities: tracking the International Space Station (ISS) for nighttime sightings and fetching random Kanye West quotes through an API. The project utilizes API requests to retrieve ISS location and sunrise-sunset data and to fetch quotes from the Kanye REST API. Additionally, it includes email notification functionality to alert users when the ISS is passing near their location during nighttime.

## About APIs and API Requests

APIs (Application Programming Interfaces) facilitate communication and data exchange between software applications. They define protocols and endpoints for accessing and manipulating data or services provided by external systems. API requests involve sending HTTP requests to API endpoints to retrieve, update, or delete data, typically in JSON or XML format.

## Project Overview

The project consists of two main components:

1. **ISS Tracker & Email Notifier**: This component tracks the International Space Station's location and determines whether it is passing near the user's location during nighttime. It utilizes the Sunrise-Sunset API to retrieve sunrise and sunset times and the Open Notify API to obtain the ISS's real-time location. If the ISS is nearby during nighttime, it sends an email notification to the user, prompting them to look up and witness the ISS passing overhead.

2. **Kanye App Integration**: The project includes an additional feature that fetches random quotes from the Kanye REST API. By making an API request to the Kanye API endpoint, the script retrieves a random quote attributed to Kanye West. This integration adds a fun and entertaining aspect to the project, allowing users to enjoy Kanye's unique insights and musings.

## Educational Purpose

The project serves as an educational tool for Python learners to explore API integration, real-time data retrieval, and email automation. By working on this project, users can enhance their understanding of API usage, JSON parsing, conditional logic, and SMTP email sending. Additionally, integrating the Kanye REST API introduces users to the concept of fetching external data and incorporating it into their applications.

### Libraries Used:

- **requests**: Used for making HTTP requests to API endpoints and fetching data.
- **datetime**: Utilized for handling date and time information, including sunrise-sunset calculations.
- **smtplib**: Enables sending email notifications using SMTP servers for ISS sightings.
- **tkinter**: Used for building the GUI (Graphical User Interface) for the Kanye App, allowing users to fetch random Kanye quotes with a click of a button.

## Instructions for Usage

1. Run the `main.py` script to initiate the ISS Tracker & Email Notifier with Kanye App Integration.
2. Ensure that the necessary libraries (`requests`, `datetime`, `smtplib`, `tkinter`) are installed.
3. Update the `MY_LAT` and `MY_LONG` variables with your latitude and longitude coordinates for accurate ISS proximity checks.
4. Enjoy receiving email notifications for ISS sightings during nighttime and fetching random Kanye quotes through the Kanye App GUI.

## Conclusion

The ISS Tracker & Email Notifier with Kanye App Integration project offers an engaging and multifaceted learning experience in API usage, real-time data retrieval, and GUI development. By combining ISS tracking functionality with Kanye quote fetching, the project combines educational content with entertainment, making it both informative and enjoyable for Python enthusiasts.
