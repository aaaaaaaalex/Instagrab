# Instagrab

This application can be used to scrape images/videos off of Instagram Posts by giving it the URL of a specific Instagram post.

How to run:
Python 3.x needs to be installed for this application to run. Open it like any other Python script.

How it works:
Instagrab uses the urllib library to request a HTML web-page from Instagram, which is then parsed using HTMLParser.
After receiving the webpage, Instagrab will look for the link to the main Image/Video, which is always held in a HTML element with the attribute "og:video" or "og:image".
Once found, Instagrab will request the data from that link, and save it to a file.

Known Issues:
-Status Icon next to Grab! button only changes once - icon stays locked after first request.
-Instagrab will throw an error if it attempts to fetch data from a post that is marked 'private', since authentication is required to view such posts.
