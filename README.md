# FinalProjectJO

INF601 - Jupyter Blog
Jeramee Oliver
<br>Final Project

## Description
A small personal blog that includes jupyter functionality. This project is a practical application of computer science and data science in real-time. The design remains minimalistic, functional, and aligned with the basic requirements, offering a straightforward yet insightful experience. In my programming journey, I exceled in data science and micro-controller domains. Acknowledging my weakness in web development, I am actively working to strengthen this area, emphasizing a commitment to addressing and improving my proficiency in all facets of programming.  

## Installing FinalProjectJO:

### Pip install instructions
### Please run the following:
```
pip install -r requirements.txt
````

### Run the following series of commands:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 5000
```
#### This will run a server at http://127.0.0.1:5000/


### Create the administrator login for the project

```
python manage.py createsuperuser 
```

### Run the Jupyter Lite Server

#### Open up another terminal and type in the following command:

```
jupyter lite serve 
```
#### This will launch another webserver at http://127.0.0.1:8000/index.html which can be safely ignored because this server only runs the Interactive Jupyter Lite Notebook which can be accessed from the parent site.

You may receive error at the command prompt but the server should still work. 
The Jupyter Lite server is prebuilt, and it is unable to delete some files upon 
launch because of lack of admin priviledges.
This saves the trouble of dealing with micropip installations.


#### Jupyter Lite does not work because of lack of SSL within micropip installation on Pyrodine

Failed to get ticker 'AAPL' reason: Expecting value: line 1 column 1 (char 0)
AAPL: No price data found, symbol may be delisted (period=10d)
Failed to get ticker 'AAPL' reason: Expecting value: line 1 column 1 (char 0)
AAPL: No price data found, symbol may be delisted (period=10d)
Failed to get ticker 'AAPL' reason: Expecting value: line 1 column 1 (char 0)
AAPL: No price data found, symbol may be delisted (period=10d)

#### There is a recent release or patch to request that should solve this, but I haven't solved it yet

https://github.com/koenvo/pyodide-http/tree/main

#### Google Colab and Binder that allow interactive environments do not allow for embedding because of security polices.

### Location of Jupyter Notebooks:

 https://github.com/jeramee/JupyterNotebookBlogPage/notebooks/

 https://github.com/jeramee/JupyterNotebookBlogPage/notebooks/mini_project_1.ipynb