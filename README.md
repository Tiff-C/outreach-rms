# Outreach Referral Management System

This is my fourth Milestone Project and will be based around a real world need. The goal of this project is to build a Referral Management System for the Outreach department of a local college. The RMS will help the college grow its existing Outrach department by efficiently tracking local schools the college works with, events at those schools and the referrals gained from each event. These referrals will then be tracked by the RMS as they progress to become students and eventually alumni, this conversion information and other Key Performance Indicators will be accessible via the Dashboard page. 

## Table of Contents

   1. [UX](#ux)
      - [Project Goals](#project-goals)
      - [User Goals](#user-goals)
      - [Owner Goals](#owner-goals)
      - [User Stories](#user-stories)
      - [Design Choices](#design-choices)
         - [Database Schema](#database-schema)
      - [Wireframes](#wireframes)
   2. [Features](#features)
      - [Existing Features](#existing-features)
      - [Features to implement](#features-to-impliment)
   3. [Technologies Used](#technologies-used)
   4. [Testing](#testing)
   5. [Deployment](#deployment)
      - [How to run this project locally](#how-to-run-this-project-locally)
   6. [Credits](#credits)
      - [Content](#content)
      - [Media](#media)
      - [Code](#code)
      - [Acknowledgments](#acknowledgements)

## UX

### Project Goals


### Developer and Business Goals



### User Stories



### Design Choices

#### Color Scheme

To ensure acessibility I used the [Material.io](https://material.io/) colour tool in combination with the Webaim Contrast Checker. My colour scheme can be seen [here](https://material.io/resources/color/#!/?view.left=1&view.right=1&primary.color=006152&secondary.color=f4f4f4) and the contrast checks for the [Primary colour](https://webaim.org/resources/contrastchecker/?fcolor=FFFFFF&bcolor=006152) and [Primary Dark colour](https://webaim.org/resources/contrastchecker/?fcolor=FFFFFF&bcolor=00362A)

#### Database Schema

### Wireframes




## Features

### Existing Features



### Features to Implement


## Technologies used



## Testing



## Deployment

This project has been deployed via [Heroku](https://www.heroku.com/). To prepare the app for deployment I created a `requirements.txt` file and a `Procfile`. I did this using the following commands in the terminal:

```
pip3 freeze --local > requirements.txt
```
```
echo web: gunicorn outreach_rms.wsgi > Procfile
```

When deploying the app on Heroku I used the GitHub deployment method and put the key, value pairs from the `env.py` in settings > config vars e.g `DEBUG` as the key and `False` as the value.

Once this info had been input into Heroku and the `requirements.txt` file and the `Prockfile` have been pushed to GitHub, I then went to deploy > enable automatic deployments and then selected 'deploy branch'.This method of deployment allows the app to update whenever new code is pushed to the GitHub repository.

### Issues During 

### How to run This Project Locally
When running this project locally you will need to setup an env.py file, an example of this file can be seen below. Once you have this setup run `python manage.py runserver` to run the project locally.

#### The `env.py` file
As the env.py file contains sensitive information please ensure it is not pushed to a public repository.

```python
""" import os to set env defaults """
import os

os.environ.setdefault("SECRET_KEY", "<SECRET_KEY_HERE>")
os.environ.setdefault("DEBUG", "FALSE")
os.environ.setdefault("DATABASE_URL", "<DB_URL_HERE>")
```


## Credits

### Content


### Media


  
### Code



### Acknowledgments

