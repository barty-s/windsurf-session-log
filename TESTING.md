# Windsurfer - Windsurfing Training Log App - Testing

## Code Validation

### HTML

The pages were tested with https://validator.w3.org/nu/ - using the address feature and the text-input feature to test pages that have user authentication blocking general access.

|       Tested        |                                                                                      Result                                                                                       | View | Passed |
| :-----------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | ---- | ------ |
|     index.html      |                 No errors. Warning about "lang" in <head> - has been resolved. Info messages about trailing "/" which are present due to the local IDE settings.                  |      | ✔      |
|     about.html      |                                                                                     No errors                                                                                     |      | ✔      |
|     signup.html     |                                                   4 errors detected but they are false errors due to Django template variables                                                    |      | ✔      |
|  my_sessions.html   | Using code from "Source Code" option on right clicking the page - no errors found. Avoids issues arising when testing the page address due to Django authentication requirements. |      | ✔      |
|     login.html      |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 |      | ✔      |
|     logout.html     |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 |      | ✔      |
| create_session.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 |      | ✔      |
| session_detail.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 |      | ✔      |
| update_session.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 |      | ✔      |
| delete_session.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 |      | ✔      |

- ### Test Cases (user story based with screenshots)

- ### Fixed Bugs
- On clicking the 'create session'/'update session'/'delete session' buttons in quick succession, multiple sessions were logged, updated and tried to be deleted. Put block on buttons once they've been clicked.
- Delete Success Message wasn't displaying - found tutorial on how to create a Delete Message

- ### Supported Screens and Browsers
