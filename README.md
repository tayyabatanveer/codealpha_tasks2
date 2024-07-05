# CodeAlpha - Task2 - Event Registration System

## Description
EventSphere is a comprehensive event registration system built with Django. It allows users to create an account, log in, view upcoming events, register for events, and manage their registrations.
## Prerequisites
- Python (version 3.6 or higher)
- pip (Python package installer)
- Django (version 3.x or higher)
## How to Run
1. Ensure that Python and pip are installed on your device.
2. Clone the repository
3. Navigate to the project directory
4. Set up a virtual environment : 
- pip install virtualenv
- virtualenv env
- env\Scripts\activate  # On Windows
5. Apply database migrations
- python manage.py migrate
6. Create a superuser to access the admin panel
- python manage.py createsuperuser
7. Run the development server:
- python manage.py runserver
8. Access the application:
- Open your web browser and go to http://127.0.0.1:8000/.
## Features
- User authentication (registration, login, and logout)
- View list of upcoming events
- Detailed event view with description, date, and location
- Register for events
- View and manage your event registrations
- Admin interface to manage events and registrations
## Project Structure
1) Event_Management_System/: Root directory of the project
- manage.py: Django's command-line utility for administrative tasks
2) events/: Directory containing the events app
3) templates/: Directory containing the HTML templates.
4) models.py: Contains the data models for the app
5) views.py: Contains the views for handling HTTP requests
6) urls.py: URL configuration for the events app
7) forms.py: Contains the forms used in the app
8) Event_Management_System/: Project-level configuration
- settings.py: Django settings for the project
- urls.py: URL configuration for the project
- wsgi.py: WSGI configuration for the project
## Templates 
- landing_page.html: The landing page of the application
- event_list.html: Displays a list of upcoming events
- event_detail.html: Displays detailed information about a specific event
- event_register.html: Allows users to register for an event
- login.html: User login page
- register.html: User registration page
- my_registrations.html: Displays a list of events the user is registered for






