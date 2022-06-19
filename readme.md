# Deploying a Heart Failure Prediction ML Model on Heroku

The deployed model can be found [here](https://heart-failure-ml-deployment.herokuapp.com/). The data used to train the model (Adaboost) is found on [Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction).

The sections below document the workflow of deploying a machine learning model to the web.

## Making a Flask Application
I found this [tutorial](https://www.youtube.com/watch?v=qNF1HqBvpGE&t=3832s) particularly useful in creating a [Flask](https://flask.palletsprojects.com/en/2.1.x/quickstart/) machine learning application. The main steps are:
- Create a ML model (I have previously performed [EDA](https://www.kaggle.com/code/teoweiyi/heart-failure-dataset-eda/notebook) and [model predictions](https://www.kaggle.com/code/teoweiyi/heart-failure-prediction/notebook))
- Save the ML model as a .joblib file.
- Create a Flask instance and use the route() decorator to trigger your defined function.
- Define a function with:
  - 'GET' and 'POST' methods
  - Prediction based on user input
  - return statement typically with the render_template() function that calls a html template
  - Redirections for [error messages](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/) (e.g. when a user submits an incomplete form/ form with invalid inputs)

## HTML
Building a website with HTML is relatively straightforward. [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) was useful in maintaining the aesthetics of the page.

## Deployment to Heroku
Deployment to Heroku can be done following this [youtube tutorial](https://www.youtube.com/watch?v=OdYpNM05e9w).

To log in to heroku, type the following in the terminal and input login details:
```
heroku login
heroku container:login
```
The next step is to create a new app on heroku. Once that is done, we can push the app we made onto heroku.
```
heroku create heart-failure-ml-deployment 
git push heroku main
```

## Bonus: Dockerize A Flask Application
I also learnt how to dockerize my flask application, though it appears that a docker container is not necessary for deployment on heroku according to the tutorial I followed.

More details on docker containers can be found [here](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/). It is relatively simple to dockerize a flask application, using the code below and saving it in a file named "Dockerfile":
```
# syntax=docker/dockerfile:1

FROM python:3.7.10-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

## Other useful commands

To start a virtual environment:
```
source .env/bin/activate
```
To find out what the versions of installed modules are:
```
pip freeze
```
To run your app in development mode:
```
flask run
```
To add, commit, push changes to and check status on github:
```
git add -A
git commit -m "updates for commit"
git push
git status
```
