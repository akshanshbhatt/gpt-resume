# GPT-Resume
A basic Django and Nextjs-based Resume filtering application using OpenAI API.

GPT-Resume allows the user to upload resumes (`.pdf` files) of multiple applicants with the role and job description. It then filters out the suitable candidates for the job. The content of the resume is analysed by GPT-3.5 Turbo model by default. However, you can change the model and it's parameters to tailor your needs.

See the final report: https://github.com/akshanshbhatt/gpt-resume/blob/master/REPORT.md

## Setup
### Step 0: Pre-requisites
Make sure you have [`python`](https://www.python.org/downloads/), [`git`](https://www.git-scm.org/), [`node`](https://nodejs.org/en/download), and [`npm`](https://github.com/npm/cli?tab=readme-ov-file#installation) installed locally on your system.
```bash
$ python --version
Python 3.12.2
$ git --version
git version 2.43.2
$ node --version
v21.6.2
$ npm --version
10.4.0
```
You can run these commands to check whether you have them installed or not. The version should be close to mine; not having precisely the same version is not an issue. Just make sure you don't work with very old versions. Make sure you have [configured `git`](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) on your device.

Optional: It would be better if you have [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda) cli installed on your system for virtual environments and Python version management. This is optional since you can anyway use the native [`venv`](https://docs.python.org/3/library/venv.html) module in Python (Although I personally hate it).

### Step 1: Cloning the repository
**(Preferred Way)** If you have [ssh keys already set up on your device](https://docs.github.com/en/authentication/connecting-to-github-with-ssh), then run -
```bash
$ git clone git@github.com:akshanshbhatt/gpt-resume.git
```
on your terminal emulator of choice. Otherwise, clone using https -
```bash
$ git clone https://github.com/akshanshbhatt/gpt-resume.git
```

### Step 2: Creating Python virtual environment
After cloning the repository, move into the root directory of the project and run the following commands -
```bash
$ cd gpt-resume
$ python -m venv gpt-venv
```
```bash
$ source gpt-venv/bin/activate
```
If you get no errors, then you have just created and sourced into (activated) a new virtual environment. To make sure, just run -
```bash
$ which python
{base_path}/gpt-venv/bin/python
```
You have done everything correctly if you get the `gpt-venv` in your path.

**(Alternate/Preferred Way)** If you have `conda` cli installed on your system, just run -
```bash
$ conda create --name gpt-venv python=3.12
```
```bash
$ conda activate gpt-venv
```

After creating and sourcing in the virtual environment using any of the two ways, make sure you have the latest version of pip installed -
```bash
$ python -m pip install --upgrade pip
```

### Step 3: Installing the backend dependencies
Move inside the `gpt_resume` directory. This folder contains the backend (server-side) source code. We will be installing the external Python packages required for running the backend using `pip`.
```bash
$ cd gpt_resume
$ python -m pip install -r requirements.txt
```
**In case** any dependency causes an issue during the execution of the program, you can install the exact same versions of the dependencies with which I worked -
```bash
$ python -m pip install -r requirements.lock.txt
```

### Step 4: Setting up environment variables for the project
You will be required to create a new api key on your [OpenAI dashboard](https://platform.openai.com/) if you don't already have one and reference it before starting up the application. **DO NOT** share this api key with anyone. If you already have an existing api key, you can use that as well.
Apart from this, you will also have to generate the api key for your Django application, which is responsible for validating sessions and cookies for the backend. Run -
```bash
$ cd ..  # Move to the root of the project before running this
$ python -c 'from django.core.management.utils import get_random_secret_key; print(f"django-insecure-{get_random_secret_key()}")'
```
to generate a random api key for your Django application. Both of these keys must be referenced in the `.env` file at the root of the project. Your `.env` file should look like this -
```py
OAI_API_KEY = "<YOUR_KEY_HERE>"  # Your OpenAI API key. This is only shown once on the dashboard, so make sure you save it. Otherwise, you'll have to generate another one.
DJANGO_SECRET_KEY = "<YOUR_KEY_HERE>"  # This is the random string that you just generated in the terminal. PASTE IT AS IT IS FROM THE TERMINAL.
```

### Step 5: Installing the frontend dependencies
Change your present working directory to `gpt_resume_frontend`. This folder contains all the frontend (client-side) source code of our application. We'll be using `npm` cli to install the necessary node modules.
```bash
$ cd gpt_resume_frontend
$ npm i
```

### Step 6: Running database migration scripts
Before starting up our backend server, we have to ensure that all the data models are configured with our `sqlite` database. Move back again into the backend directory and run the migration scripts -
```bash
$ cd ../gpt_resume
$ python manage.py makemigrations
$ python manage.py migrate
```

### Step 7: Starting the backend server
To start the backend server, just run -
```bash
$ python manage.py runserver
```

Your server should now be live on `port:8000` (`http://127.0.0.1:8000/`).

### Step 8: Starting the frontend application
To start our frontend application, open **a new terminal session** and move to the `gpt_resume_frontend` directory (once again). Run -
```bash
$ cd gpt_resume_frontend  # Make sure you are inside the frontend directory
$ npm run dev
```
to host our frontend app locally (in dev setup) on `port:3000` (`http://127.0.0.1:3000`).

That's all. Now go ahead and upload as many resumes as you want for analysis!

**Important Note:** Make sure that the backend is hosted on `port:8000`. The frontend will not be able to communicate with the backend if the port is different since these are hardcoded in the frontend code.

## Project Structure

|Directory|Summary|
|--|--|
|`gpt_resume`|Contains all the backend code (Python) of the application.|
|`gpt_resume/gpt_resume`|Contains the basic configurations and settings of the Django backend.|
|`gpt_resume/api`|The main Django app that handles all the backend functionalities.|
|`gpt_resume_frontend`|Contains all the Frontend code (TS/React) of the application.|
|`gpt_resume_frontend/app`|Contains the homepage/root route (`page.tsx`) and layout (`layout.tsx`) of our fronted.|
|`gpt_resume_frontend/components`|Contains all the reusable frontend app components related to the app. Our frontend utilizes [shadcn ui components](https://ui.shadcn.com/), which is present in `gpt_resume_frontend/components/ui`.|
|`gpt_resume_frontend/pages`|Contains the pages of routes other than the root route. This app uses page-based routing using `nextjs`.|
|`sample_resume`|Contains a few sample resumes for testing the app.|

## Backend API Endpoints
You can access these endpoints in your browser since the backend uses Django Rest Framework (DRF) `views` for interactive object creation and visualization. You can also use api testing platforms like Postman or Hoppscotch if you want.
|API Endpoint|HTTP Method(s) Allowed|Purpose/Comment|
|--|--|--|
|`/api/get-applicant-list/<uuid:job_u_id>/`|GET|Gives a list of applicants for a particular job posting (referenced by its `u_id`).
|`/api/get-applicant-summary/<uuid:u_id>/`|GET|Gives the Summary of an applicant (profile, academic experience, professional experience, etc.) after extracting it from the resume. This summary is specific to a particular job posting only.|
|`/api/post-resume/`|POST|Allows the user to post multiple resumes (multiple `.pdf`s as formdata) under `files` header along with a `job_u_id` header for generating summary for all the applicants corresponding to a unique job.|
|`/api/get-job-list/`|GET|Gives a list of all the jobs (`Job` objects) posted.|
|`/api/post-job/`|POST|Allows the user to post a job using the `job_title` and `job_description` headers.|
|`/api/post-resume-with-job/`|POST|Combines the functionalities of both `/api/post-job/` and `/api/post-resume/` under a single endpoint.|

## External References

Sample Resumes Taken From: https://www.cmu.edu/career/documents/sample-resumes-cover-letters/sample-resumes_scs.pdf
