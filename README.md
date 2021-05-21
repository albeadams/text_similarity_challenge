
This app uses [FastApi](https://fastapi.tiangolo.com/) and a simple Dockerfile.

You can run this app in four ways. 


1. The easiest is to navigate to the app folder and type

`>> python helper.py 1 2`

with two args, where the options are in the set [1,2,3] for the three samples, or are two strings. Long strings could be added to helper.py as well.


2. The second option is to use the Dockerfile. Assuming Docker is installed, navigate to the parent directory (contained the Dockerfile), and type:

`docker build -t simtextimage .`

Then run the container as:

`docker run -d --name simtextcontainer -p 80:80 simtextimage`


3. A third way is to install [uvicorn](https://pypi.org/project/uvicorn/)), navigate to the parent directory, and type:

`uvicorn app.main:app --reload --port 8080`

For either the Docker or server option, after running them, navigate to:

`http://127.0.0.1:8080/similarity/?1string&string2`

where string1 and string2 are the two strings you intend to compare.


4. A fourth option is to use the jupyter notebook included in the repo, which is what was used to build this.