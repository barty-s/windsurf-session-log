# Windsurfer - Windsurfing Training Log App - Testing

## Code Validation

### HTML

The pages were tested with https://validator.w3.org/nu/ - using the "address" feature, and the "text-input" feature to test pages that have user authentication blocking general access.

|       Tested        |                                                                                      Result                                                                                       | View                                                                                                           | Passed |
| :-----------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------- | ------ |
|     index.html      |                 No errors. Warning about "lang" in <head> - has been resolved. Info messages about trailing "/" which are present due to the local IDE settings.                  | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-index.png"> </details>      | ✔      |
|     about.html      |                                                                                     No errors                                                                                     | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-about.png"> </details>      | ✔      |
|     signup.html     |                                                   4 errors detected but they are false errors due to Django template variables                                                    | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-signup.png"> </details>     | ✔      |
|  my_sessions.html   | Using code from "Source Code" option on right clicking the page - no errors found. Avoids issues arising when testing the page address due to Django authentication requirements. | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-mysessions.png"> </details> | ✔      |
|     login.html      |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-login.png"> </details>      | ✔      |
|     logout.html     |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-logout.png"> </details>     | ✔      |
| create_session.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-create.png"> </details>     | ✔      |
| session_detail.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-read.png"> </details>       | ✔      |
| update_session.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-update.png"> </details>     | ✔      |
| delete_session.html |                                                Using code from "Source Code" option on right clicking the page - no errors found.                                                 | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-delete.png"> </details>     | ✔      |

- ### Test Cases (user story based with screenshots)

- ### Fixed Bugs
- On clicking the 'create session'/'update session'/'delete session' buttons in quick succession, multiple sessions were logged, updated and tried to be deleted. Put block on buttons once they've been clicked.
- Delete Success Message wasn't displaying - found tutorial on how to create a Delete Message

- ### Supported Screens and Browsers