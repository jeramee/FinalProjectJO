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

### Run
#### This will run a server at http://127.0.0.1:8000/


```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


### Create the administrator login for the project

```
python manage.py createsuperuser 
```

### Run the Jupyter Lite Server
#### This will launch another webserver at http://127.0.0.1:8000/index.html

```
jupyter lite serve 
```

### Location of Jupyter Notebooks:

 https://github.com/jeramee/JupyterNotebookBlogPage/notebooks/

 https://github.com/jeramee/JupyterNotebookBlogPage/notebooks/mini_project_1.ipynb