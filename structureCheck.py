import os
from googleapiclient.discovery import build

def check_folder_exists(folder_id, folder_name):
    """
    Check if a specific folder exists within a parent folder, specified by its id.
    """
    folder = drive_service.files().list(q=f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and name='{folder_name}'", fields='nextPageToken, files(id, name)').execute()
    if not folder.get('files'):
        raise ValueError(f"The folder {folder_id} doesn't have a {folder_name} folder.")

def check_folder_structure():
    """
    Check if the folder structure is correct for the DriveLink app to function properly.
    """
    try:
        client_folder = drive_service.files().list(q=f"mimeType='application/vnd.google-apps.folder' and name='{client_name}'", fields='nextPageToken, files(id, name)').execute()
        if not client_folder.get('files'):
            raise ValueError(f"The client folder {client_name} doesn't exist.")
        
        client_folder_id = client_folder.get('files')[0].get('id')
        check_folder_exists(client_folder_id, "Weekly posters")
        
        weekly_posters_folder = drive_service.files().list(q=f"'{client_folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and name='Weekly posters'", fields='nextPageToken, files(id, name)').execute()
        weekly_posters_folder_id = weekly_posters_folder.get('files')[0].get('id')
        courses_folders = drive_service.files().list(q=f"'{weekly_posters_folder_id}' in parents and mimeType='application/vnd.google-apps.folder'", fields='nextPageToken, files(id, name)').execute()
        courses_folders_id = [folder.get('id') for folder in courses_folders.get('files')]
        for course_folder_id in courses_folders_id:
            check_folder_exists(course_folder_id, "Results")
            results_folder = drive_service.files().list(q=f"'{course_folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and name='Results'", fields='nextPageToken, files(id, name)').execute()
            results_folder_id = results_folder.get('files')[0].get('id')
            week_folders = drive_service.files().list(q=f"'{results_folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and name contains 'Week'", fields='nextPageToken, files(id, name)').execute()
            week_folders_id = [folder.get('id') for folder in week_folders.get('files')]
            week_folders_id = [folder.get('id') for folder in week_folders.get('files')]
            for week_folder_id in week_folders_id:
                check_folder_exists(week_folder_id, "Poster Ready")
                check_folder_exists(week_folder_id, "Story Process")
                check_folder_exists(week_folder_id, "Story")
                return True
            
    except HttpError as error:
        print(F'An error occurred: {error}')
        return False
    
    except ValueError as error:
        print(error)
        print("The structure of the folders is not correct. Please correct the structure and try again...")
        return False