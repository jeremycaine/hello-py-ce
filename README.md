# hello-py-ce
Hello World in Python on IBM Code Engine

## Application Setup

```
cd [source dir]
python3 -m venv env
source activate
cd src
pip install -r requirements.txt
python main.py
```

## IBM Cloud Engine
Project setup
```
ibmcloud login --sso ...

ibmcloud target -r eu-gb
ibmcloud target -g ceh-group

ibmcloud ce project list
ibmcloud ce project select --name ml-ce

ibmcloud ce app create --name hello-py-ce --src https://github.com/jeremycaine/hello-py-ce --bcdr src --str buildpacks

```
