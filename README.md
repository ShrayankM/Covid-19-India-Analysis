# Covid-19 India Analysis
[![Python Version](https://img.shields.io/badge/python-v3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.1-blue.svg)](https://djangoproject.com)
## Description:
The project includes a number of _Jupyter notebooks_ on Coronavirus Statistics in India and the information is also represented using a _Django website_.

## Installation: 
1. Jupyter notebooks can be directly run using [Google Colaboratory](https://colab.research.google.com/).
2. To run the website you will have to [install django](https://docs.djangoproject.com/en/3.1/topics/install/).
   * After installing django, I recommend to create a virtual environment for your project, using this command.
   ```bash
   $ python3 -m venv _virtual_enviroment_name_
   ```
   * After creating virtual environments, install all package requirements from **_requirements.txt_** present in **Coronavirus Statistics India** folder.
   ```bash
   $ pip install -r requirements.txt
   ``` 
   * Clone the project in your personal directory, and change directory to website folder.
   * Run the project using following django command 
   ```bash
   $ python manage.py runserver
   ```
   _Make sure your are in virtual environment_
   * The project will be available at **127.0.0.1:8000**.

## Credits:
   * Data avaliable at the following API documentation https://data.covid19india.org/
   * Data has been used from the following api (url = "https://api.covid19india.org/states_daily.json").
   * The website can be found live at http://s76.pythonanywhere.com/

## License: 
   * [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![covidsite_gif](Images/t2.gif)
    
