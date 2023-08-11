# Souper Mario Maker!

## What is Souper Mario Maker

Souper mario maker is a simple fun Mario themed website in where you can create your own Mario typed soups!

## Setup

The first thing you want to do is get the backend running. Our backend runs on Python Flask.

First you want to clone down the repo as normal.

Then you want to install the dependencies.

```console
pipenv install
pipenv shell
```
You can run your backend on [`localhost:5555`](http://localhost:5555) by running:

```console
python server/seed.py
```
The different routes to see the backend are as follows:

```console
/soups
/ingredients
/soup_ingredients
```

All of which with by searching for an id!

To setup up the front on all you need to run is:

```console
npm install --prefix client
```
Which will run on [`localhost:4000`](http://localhost:4000) by running the following command

```console
npm start --prefix client
```

Your frontend will run on `http://localhost:3000` You should see the Souper Mario Maker homepage!

# The database

The database should be up to date when you initially clone the repo down.

But just in case is isn't here is how to set it up.

First cd into your server directory

```console
cd server
```

Then we have to do the first flask init:

```console
flask db init
flask db upgrade head
```


After that you can seed your database:

```console
python seed.py
```

Now that all the setup is all complete you can run your app!

# What does it do?

Our app is fairly simple, for now. The main thing you can do is view soups and favorite them. 

The website is still under construction, but the plan is be able to build your own soups!

## The team

Kevin Mrozek https://github.com/5billon/
Paul Macellaro https://github.com/pmacellaro/
Zoe G https://github.com/zomeister/
Ainsley Alceme https://github.com/ainsleyalc/