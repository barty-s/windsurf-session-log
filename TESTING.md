# Windsurfer - Training Session Log App - Testing

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

### CSS

The app was tested with https://jigsaw.w3.org/css-validator.

| Tested         | Result    | View Result                                                                                                 | Pass |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------------- | ---- |
| CSS file       | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-css.png"> </details>     | ✔    |
| Entire webpage | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-css-app.png"> </details> | ✔    |

### Python - PEP8

The app was tested with https://pep8ci.herokuapp.com/

| Tested                 | Result    | View Result                                                                                                             | Pass |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------- | ---- |
| windsurfer/settings.py | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-windsurfer-settings.png"> </details> | ✔    |
| windsurfer/urls.py     | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-windsurfer-urls.png"> </details>     | ✔    |
| session_log/models.py  | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-session-log-models.png"> </details>  | ✔    |
| session_log/views.py   | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-session-log-views.png"> </details>   | ✔    |
| session_log/forms.py   | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-session-log-forms.png"> </details>   | ✔    |
| session_log/urls.py    | No errors | <details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-session-log-urls.png"> </details>    | ✔    |

## Accessibility

### Wave

The app was tested with https://wave.webaim.org/ - no errors or contrast warnings were detected.

<details> <summary>View result</summary> <img src="docs/testing/code_validation/cv-wave.png"> </details>

## Performance

### Lighthouse

The app was tested with Google Chrome's Lighthouse tool to analyse performance. It was tested in incognito mode.

| Tested              | Performance Score | View Result                                                                                                            |
| ------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| index.html          | 94                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-index.png> </details>       |
| about.html          | 94                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-about.png"> </details>      |
| signup.hmtl         | 95                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-signup.png"> </details>     |
| login.html          | 93                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-login.png"> </details>      |
| logout.html         | 96                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-logout.png"> </details>     |
| create_session.html | 94                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-create.png"> </details>     |
| my_sessions.html    | 95                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-mysessions.png"> </details> |
| session_detail.html | 95                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-read.png"> </details>       |
| update_session.html | 94                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-update.png"> </details>     |
| delete_session.html | 92                | <details> <summary>View result</summary> <img src="docs/testing/code_validation/lighthouse-delete.png"> </details>     |

## Test Cases (user story based with screenshots)

## Fixed Bugs

- On clicking the 'create session'/'update session'/'delete session' buttons in quick succession, multiple sessions were logged, updated and tried to be deleted. Put block on buttons once they've been clicked.
- Delete Success Message wasn't displaying - found tutorial on how to create a Delete Message

## Supported Screens and Browsers

- Using the Google Chrome Simulateur-Mobile extension, the app was tested on the following devices:

  - Samsung Galaxy Fold
  - Xiaomi 12
  - iPhone X
  - iPad Air 4 (showed issues with responsiveness of the main image on index.html)
  - MacBook Air

- The app was tested on the following browsers:

  - Safari
  - Chrome
  - Firefox
  - Edge
