- Create environment

python3 -m venv env

- Activate env

. env/bin/activate

- install dependencies

pip install --upgrade pip

pip install -r requirements.txt

- access api folder

cd packages/ml_api

- create app

python run.py

----------------
- controller.py has the "/predict" endpoint
- Basically when giving the input in the frontend, does not return the output
- HTML = packages/ml_api/api/template/home.html




