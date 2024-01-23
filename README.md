# Windsurfer - Windsurfing Training Log App

## The Purpose of the Project

Most wearable tech devices have features to record various sporting activities - running, cycling, yoga etc. However, there is no feature to record windsurfing training sessions. This app can be used by windsurfers to log their training sessions which will allow them to track their progress on the water.

## User Stories

As a user, I want to be able to create a profile and log in and out.
As a user, I want to be able to create, read, update and delete training sessions from my log.

As admin, I want to be able to delete users from the database using the superuser access, if required.

## Features

Landing page - sign up button
Sign up page - sign up form
My Sessions page - list of sessions logged by the user
Log a Session page - session log form
Session detail page - user can access the details of a selected session
Edit Session page - edit session form
Delete Session page - user can to erase a selected session from their log
Sign out page - sign out button

## Future Features

## Typography and Color Scheme

## Wireframes

## Technology

Django - allauth,
Python
HTML
CSS
JavaScript
Cloudinary

## Testing

- ### Code Validation
- ### Test Cases (user story based with screenshots)
- ### Remaining Issues

  Success Message on Session Delete: I chose to use the older version of Django to be able to follow along with the CI tutorials. The success message feature is not available with this older version on the delete view. Therefore, no success message is shown when the user chooses to delete a session from their log.

- ### Fixed Bugs
- On clicking the 'create session'/'update session'/'delete session' buttons in quick succession, multiple sessions were logged, updated and tried to be deleted. Put block on buttons once they've been clicked.

- ### Supported Screens and Browsers

## Deployment

- ### via Gitpod
- ### via GitHub Pages

## Credits

#### For Roadblock Solutions and Explanations

- https://stackoverflow.com/questions/62532910/add-a-date-or-a-number-at-the-end-of-a-slug
- https://docs.djangoproject.com/en/5.0/topics/pagination/
- https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/
- https://stackoverflow.com/questions/4941974/django-how-to-set-datefield-to-only-accept-today-future-dates
- https://stackoverflow.com/questions/61031491/can-i-limit-the-dates-possibilities-using-django-widget-dateinput-ex-between-2
- https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown

#### CI PP4s for examples/inspirations on structure

CI Hello Django, I think therefore I blog - video tutorials
Kim Bergstroem - https://github.com/KimBergstroem/PP4/tree/main
Christian Goran - https://github.com/christiangoran/dome-restaurant-repo/tree/main

#### Media

- https://unsplash.com/ - for open-source images
- ERD - made with LucidCharts
- Wireframes - made with Figma
