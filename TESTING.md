# Project Testing

Return to [README](README.md)

In line with coding best practice I have tested throughout the development of my project and tracked this file contains details of the testing carried out and any relevant screen shots. To track any bugs found during development I use GitHub Issues, I like to use Issues as I feel it is good practice for working in a team and helps to keep me organised while I work. I have also used commit messages to document minor bugs that were easily fixed and do not worth mentioning below.

## Project Setup

During the setup of my project I tested each step by running the project locally using 'python3 manage.py runserver' in the CLI. Below is a table summarising the testing carried out during the setup of the project. 

Step | Test | Result
--- | --- | ---
Project Start / Admin | After checking there are no error messages I tested the admin page had been setup correctly by adding `\admin` to the end of the browser URL. | No issues
Allauth | To test Allauth had been setup correctly I first verified the superuser email address via the admin page, returned to the landing page and then added `\accounts` to the end of the browser URL and logged in using the superuser credentials. | No issues
Home app | To test my templates, views and urls were working for the home app I added `<h1>Test</h1>` to [index.html](home/templates/home/index.html) (seen in this [commit](https://github.com/Tiff-C/outreach-rms/commit/bb2877e72390fbc3321cad2bfe5d615c3a5e7da0) and checked this displayed when running the project locally. | No issues
Navigation | To test the navigation was functioning as expected I used [Chrome DevTools](https://developer.chrome.com/docs/devtools/) in the browser and tested the nav collapsed at the correct breakpoints, checked the burger icon displayed the collapsed nav when clicked. I added links to the navbar as they were created throughout the project, I tested each of these worked as they were added. | 1 issue on deployment (see [ReadMe](README.md) - Deployment Issues). No other issues
Models | To check each of my models were functioning correctly after making initial migrations I went to the `admin` page and added a couple of items to each model to test they were functioning as expected. Once I had set up forms and their views I used the forms to test any updates to the models were functioning as expected.