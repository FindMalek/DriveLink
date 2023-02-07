# DriveLink
A command-line tool that automates the process of extracting links to specific Google Drive folders for weekly client updates.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3
- Google Drive API credentials
- Pandas library

### Installing
1. Clone the repository 
```sh
git clone https://github.com/FindMalek/DriveLink.git
```
2. Create a project on the Google Developers Console and enable the Google Drive API.
3. Create credentials for your application to use.
4. Authorize credentials for a desktop application
To authenticate as an end user and access user data in your app, you need to create one or more OAuth 2.0 Client IDs. A client ID is used to identify a single app to Google's OAuth servers. If your app runs on multiple platforms, you must create a separate client ID for each platform.
    In the Google Cloud console, go to Menu menu > APIs & Services > Credentials.
    Go to Credentials
    Click Create Credentials > OAuth client ID.
    Click Application type > Desktop app.
    In the Name field, type a name for the credential. This name is only shown in the Google Cloud console.
    Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret.
    Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
    Save the downloaded JSON file as credentials.json, and move the file to your working directory.
5. Install the Google client library
Install the Google client library for Python:

```sh
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Usage
The tool takes the client name as input and the week number as input and returns the links of the Poster Ready and Story folders.
```sh
python driveLink.py [client_name] [week_number]
```

Example:
```sh
python driveLink.py "Move U" 2
```

## Folder Structure
In order for DriveLink to work, the structure of your Google Drive Folders must be as follows:

```
Projects
└── Client Name
    └── Weekly posters
        ├── Folder name 1
        │   └── Results
        │       ├── Poster Ready
        │       ├── Story Process
        │       └── Story
        └── Folder name 2
            └── Results
                ├── Week 1
                │   ├── Poster Ready
                │   ├── Story Process
                │   └── Story
                ├── Week 2
                │   ├── Poster Ready
                │   ├── Story Process
                │   └── Story
                .
                .
                .
```

Please note that the "Folder name 1" and "Folder name 2" should be named as the course name and inside the Results folder, there should be folders named as the week numbers, and inside each folder, there should be these folders "Poster Ready", "Story Process" and "Story".

## Built With
- [Google Drive API](https://developers.google.com/drive)
- [Pandas](https://pandas.pydata.org/)

## Acknowledgments
- [Google Drive API Docs](https://developers.google.com/drive/api/guides/)
- [Stack Overflow](https://stackoverflow.com/)

This will ensure that the script is able to find the correct folders in the Google Drive and extract the links correctly.