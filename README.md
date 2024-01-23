# Windsurfer - Windsurfing Training Log App

## The Purpose of the Project

Most wearable tech devices have features to record various sporting activities - running, cycling, yoga etc. However, there is no feature to record windsurfing training sessions. This app can be used by windsurfers to log their training sessions which will allow them to track their progress on the water.

## User Stories

As a user, I want to be able to create a profile and log in and out.
As a user, I want to be able to create, read, update and delete training sessions from my log.

As admin, I want to be able to delete users or sessions from the database using the superuser access, if required.

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

Google Fonts:
Raleway for logo and headline
Oxygen for all other text

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

- ### Fixed Bugs
- On clicking the 'create session'/'update session'/'delete session' buttons in quick succession, multiple sessions were logged, updated and tried to be deleted. Put block on buttons once they've been clicked.
- Delete Success Message wasn't displaying - found tutorial on how to create a Delete Message mixin

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
- https://stackoverflow.com/questions/66482049/get-deleted-object-in-django-deleteview - Delete Success Message
- https://codepen.io/bramus/pen/rLovLY - for title styling text-stroke

#### CI PP4s for examples/inspiration on structure

CI Hello Django, I think therefore I blog - video tutorials
Kim Bergstroem - https://github.com/KimBergstroem/PP4/tree/main
Christian Goran - https://github.com/christiangoran/dome-restaurant-repo/tree/main

#### Media

- https://unsplash.com/ - for open-source images Photo by <a href="https://unsplash.com/@darice?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Darice de Cuba</a> on <a href="https://unsplash.com/photos/a-person-holding-a-kite-on-a-beach-nbjA7vuoUVw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
- ERD - made with LucidCharts
- Wireframes - made with Figma
