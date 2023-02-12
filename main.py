import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from structureCheck import check_folder_structure

from OAuth2Flow.authenticate_google_drive import authenticateGoogleDrive

def get_links(client_name, week_number):
    # Build the credentials object
    credentials = Credentials.from_authorized_user_info(info=os.environ)

    # Build the Drive API client
    drive_service = build('drive', 'v3', credentials=credentials)

    # Your code to search for the specific folder and retrieve the links goes here

    return poster_link, story_link

if __name__ == "__main__":
    authenticateGoogleDrive()
    
    # Get the client name and week number from the command line arguments
    client_name = sys.argv[1]
    week_number = sys.argv[2]
    
    if (check_folder_structure() == False):
        exit()

    # Call the get_links function and store the result in variables
    poster_link, story_link = get_links(client_name, week_number)

    # Create the output message
    message = f"Poster {client_name} (Week {week_number}): {poster_link}\nStories {client_name} (Week {week_number}): {story_link}"

    # Create the output file
    with open("output.txt", "w") as f:
        f.write(message)
    os.startfile("output.txt")