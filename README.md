# hello-py-ce
Hello World in Python on IBM Code Engine

## IBM Cloud Engine
Project setup
```
pip install Flask

ibmcloud login --sso ...

ibmcloud target -r eu-gb
ibmcloud target -g ceh-group

ibmcloud ce project list
ibmcloud ce project select --name caine-code-engine

ibmcloud ce app create --name hello-py-ce --src https://github.com/jeremycaine/hello-py-ce --str buildpacks
```

