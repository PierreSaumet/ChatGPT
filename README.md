<div id="header" align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg" width="250"/>
</div>

# ChatGPT
Small program for a friend <3.

## Requirements
You need to have **Python**, **git**, **pip**,

To check if you already have it, enter these following commands in your terminal.
```bash
python --version

git --version

pip --version
```

You should see something like this:
```bash
python --version
Python 3.10.6

git --version
git version 2.34.1

pip --version
pip 22.0.2
```

**If not, follow these instructions:**

PYTHON: https://www.python.org/downloads/

GIT: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

PIP: https://www.geeksforgeeks.org/how-to-install-pip-in-macos/


## Installation

1. Clone the repo (download the projet to your laptop)
```bash
    git clone https://github.com/PierreSaumet/ChatGPT.git <FOLDER_NAME>
```
2. Install virtualenv
```bash
    python3 -m pip install virtualenv
```
3. Create an virtual environment
```bash
    python3 -m venv env
```
4. Active the virtual environment
```bash
    source env/bin/activate
```
5. Install dependencies
```bash
    pip install -r requirements.txt
```

## Usage

1. Go to your folder
```bash
    cd <FOLDER_NAME>
```

2. Rename the file .env.example to .env
```bash
    mv .env.example .env
```

3. In the new '.env' file, replace:
```bash
TOKEN_OPENAI = "INSERT_YOUR_OPENAI_TOKEN_HERE"
```
by your own token!

As I told you before, you can get it here:

https://platform.openai.com/account/api-keys

4. An then, you can use the program!
```bash
    python3 main.py "Hello, say thank you to my friend!"
```

5. **Have fun and send me a message on Whatsapp if you need help!**

<div id="header" align="center">
  <img src="https://global-img.gamergen.com/south-park-saison-10-le-personnage-jenkins-dans-l-pisode-pisode-make-love-not-warcraft_0190000000971297.jpg" width="250"/>
</div>


## Documentation
If you want to custom something, read:

https://platform.openai.com/docs/introduction

