# Spotify Playlist Using the Musical Time Machine

This Python script (`main.py`) utilizes web scraping techniques to retrieve the Billboard Hot 100 songs for a specific date and then creates a Spotify playlist containing these songs.

## Overview

The script performs the following tasks:
1. **Spotipy Configurations**:
   - Sets up the Spotipy client with appropriate authentication credentials.
2. **Web Scraping HTML Configurations**:
   - Requests the HTML content of the Billboard Hot 100 page for a specified date.
   - Parses the HTML content using BeautifulSoup to extract the names of the songs.
3. **Using Spotipy to Search Artist Songs by Scraping HTML List of Musics**:
   - Utilizes Spotipy to search for each song on Spotify and retrieves their URIs.
4. **Creating Spotify Playlist**:
   - Creates a new private playlist on the user's Spotify account named after the specified year.
   - Adds the songs retrieved from the Billboard Hot 100 to the created playlist on Spotify.

## Web Scraping Process

Web scraping is the process of extracting data from websites. In this script:
- The `requests` library is used to fetch the HTML content of the Billboard Hot 100 page.
- BeautifulSoup (`bs4`) is employed to parse the HTML content and extract relevant information, such as song names.
- The extracted data (song names) is then utilized to search for each song on Spotify using the Spotipy library.

## Spotipy

Spotipy is a Python library for the Spotify Web API. It allows developers to easily interact with the Spotify API to retrieve information about tracks, albums, artists, and playlists, as well as perform actions like creating playlists and adding tracks to them.

## Running the Script

To run the script:
1. Ensure you have the necessary Python packages installed, including `beautifulsoup4`, `requests`, and `spotipy`.
2. Make sure you have registered a Spotify application and obtained the required client ID and client secret.
3. Update the `clientId` and `clientSecret` variables in the `keys.py` file with your Spotify application credentials.
4. Run the `main.py` script and follow the instructions to provide the desired date for the Billboard Hot 100 songs.

## Limitations

Web scraping can sometimes be fragile and may break if the structure of the website being scraped changes. Additionally, using web scraping to access data from websites may be subject to legal and ethical considerations, so it's essential to review and adhere to the website's terms of service and scraping policies.

## Contributions

Contributions to this project, including bug fixes, feature enhancements, and documentation improvements, are welcome. If you have suggestions for improving the script or encountering any issues, feel free to open an issue or submit a pull request.