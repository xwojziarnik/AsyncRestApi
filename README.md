🇬🇧

# AsyncRestApi

## Table of contents:

- [The aim of the project](#the-aim-of-the-project)
- [What is my motivation?](#what-is-my-motivation)
- [Features](#features)
- [Technologies & Documentation](#technologies--documentation)
- [Installation](#installation)
- [Run](#run)


## The aim of the project

REST API application where user is adding books into MongoDB using POST request. Next user can see all books using GET request.

## What is my motivation?

I want to:
- Get to know Sanic framework,
- Create an app using Sanic framework instead of Django or Flask,
- Write an app using API,
- Get to know with Docker

## Features

- [x] Created homepage where user can see what to do,
- [x] Created one endpoint using two request methods (to list / add books),
- [x] MongoDB database in Docker file .yml,

## Technologies & Documentation

- [Python 3](https://docs.python.org/3/)
- [Sanic](https://sanic.dev/en/)
- [MongoDB](https://www.mongodb.com/docs/)
- [Docker](https://www.docker.com/)

## Installation

<details>
<summary>Python:</summary>

Visit https://www.python.org/downloads/ and type which installing package you prefer (by your operating system) and download the package.

After download, go through installation process.

After above, let's check if Python is installed on your computer. To do this, open your terminal or command prompt and type:

For MacOS/Linux:
```
python3 --version
```

For Windows:
```
python --version
```
</details>

<details>
<summary>Virtual environment:</summary>

[More info about venv](https://docs.python.org/3/library/venv.html)

Open terminal/command prompt and create directory where you will create a django project using commands below:

```
ls                                                   # to check content of your domain directory
mkdir <directory_name>                               # to create a separated directory for project
cd <directory_name>                                  # just to go into new directory
python3 -m venv <virtualenv_name>                    # to create virtualenv using MacOS terminal
python -m venv <virtualenv_name>                     # to create virtualenv on Windows
source <virtualenv_name>/bin/activate                # to activate virtualenv on MacOS
<virtualenv_name>\Scripts\activate                   # to activate virtualenv on Windows

(<virtualenv_name>) <username>@<actual_directory> %  # after above you should see the (<virtualenv_name>). This line appears on MacOS.
```
</details>

<details>
<summary>Sanic:</summary>

If you did above tutorials, now you should have schema of your files like:

```
Desktop/
    <directory_name>/
        <virtualenv_name>
```

Now we can install Sanic framework. Simply type in your terminal/command prompt:

```
pip3 install sanic     # on MacOS
pip install sanic      # on Windows
```

</details>

<details>
<summary>All packages included in requirements.txt:</summary>

<details>
<summary>First option (prefered):</summary>

After clone this repo, type command:
```
pip3 install -r requirements.txt        # on MacOS
pip install -r requirements.txt         # on Windows
```

</details>

<details>
<summary>Second option:</summary>

Open file ```requirements.txt``` and type command with every package name:
```
pip3 install <package_name>     # on MacOS
pip install <package_name>      # on Windows
```

</details>

</details>

Perfect! Now, it's time to last episode.

##  Run

We've seen how to run venv. Keep that running!


<details>
<summary>Now we can simply clone this repo, and see if it's working on our machine (in case we did everything above count creating virtualenv):</summary>

```
git init                                                # to initialize repository
git clone https://github.com/xwojziarnik/cepik_app      # to clone this repository into your local machine

python3 main.py     # using MacOS
python main.py      # using Windows
```
</details>

And that's it! Great job!
