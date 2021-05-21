
This app uses [FastApi](https://fastapi.tiangolo.com/) and a simple Dockerfile.

You can run this app in four ways. 


1. The easiest is to run cli.py from the parent directory:

`>> python cli.py 1 2`

with two args, where the options are in the set [1,2,3] for the three samples, or are two strings. Additional strings could be added to cli.py as well.



2. The second option is to use the Dockerfile. Assuming Docker is installed, navigate to the parent directory (containing the Dockerfile), and type:

`docker build -t simtextimage .`

Then run the container as:

`docker run -d --name simtextcontainer -p 80:80 simtextimage`

To run using Docker, go to this address in browser:

`http://127.0.0.1/similarity/?s1=string1&s2=string2`

where `string1` and `string2` are the two strings you intend to compare.

Or, using the index of the phrase (1-indexed), use:

`http://127.0.0.1/sim_by_id/?id1=2&id2=2`

The above would compare the first and second sample, should give a value around .7.

`http://127.0.0.1/sim_by_id/?id1=2&id2=3`

This would compare first and third sample, should give a value ~ .22.



3. A third way is to install [uvicorn](https://pypi.org/project/uvicorn/)), navigate to the parent directory, and type:

`uvicorn app.main:app --reload --port 8080`

After running the server, navigate to:

`http://127.0.0.1:8080/similarity/?s1=string1&s2=string2`

or:

`http://127.0.0.1:8080/sim_by_id/?id1=1&id2=2`

or:

`http://127.0.0.1:8080/sim_by_id/?id1=1&id2=3`




4. A fourth option is to use the jupyter notebook included in the repo, which is what was used to build this.