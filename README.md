# DEVOPS - TP1  - Docker 
### Professeur : Vincent DOMINGUES


## Objectifs :


> Créer un repository Github

>Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude (passées en variable d'environnement) en utilisant openweather API dans le langage de
programmation de votre choix (bash, python, go, nodejs, etc)

>Packager son code dans une image Docker

>Mettre à disposition son image sur DockerHub

>Mettre à disposition son code dans un repository Github


 ## Choices : 
>Language de programmation : Python 

>Recupération des données : wrapper (données météo)

>Api : Openweather API



## STEPS : 

> 0. Creating a virtual environment
> 1. Writing the wrapper (IN PYTHON)
> 2. Package the wrapper with DockerHub
  


 ### Prerequisite
 creation d'un envronnement virtuel 

``` python3 -m venv myvenv```

puis 
```bash pip freeze -> requirements.txt```
 pour installer dans les conteneurs les packages et librairies 



### Commands : 

#### Request :
```getter = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + Y + "&lon=" + X + "&appid=" + APIKEY + "&units=metric") ```
#### Build image : 
```docker build --tag mywrapper .```
#### Local run : 
```docker run -p 5000:5000 --env Y ="5.902785" --env X ="102.754175" --env APIKEY=$APIKEY --rm mywrapper```
#### Push on DockerHub
> Get id :
 ```docker images ```
> Login to DockerHub : 
```docker login --username=emilefrd```
> Push :
 ```docker push emilefrd/tp1 ```
> Get : 
```docker pull emilefrd/tp1```
> Running : 
```docker run --env Y ="5.902785" --env X ="102.754175" --env API_KEY=$APIKEY emilefrd/tp1```




## Remarks
> Keys : API, lat et lon are retrived on openwheather
> Reading of the key thanks to different functions already implemented, for exemple load_totenv() and os.environ["Clé"]