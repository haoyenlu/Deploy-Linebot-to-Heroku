# deploy-test-linebot-to-heroku
Deploy test line bot, python line-bot-sdk, on heroku
#### Step1: create heroku account
---
#### Step2: download heroku sdk
- After downloading heroku sdk use the code below to test if correctly install (You may want to restart the computer)
```
heroku --version
```
- Login to your heroku account in console
```
heroku login
```
---
#### Step3: download git
- create a respository for your line bot
- initialize git 
```
git init
```
---
#### Step4: create app.py
- create a file called app.py
- copy the example code from line-bot-sdk (https://github.com/line/line-bot-sdk-python) or clone this repository
```
git clone https://github.com/haoyenlu/deploy-test-linebot-to-heroku.git
```
- create Procfile and requirements.txt (use the file in this repository for example)
  - to create requirements.txt
```
pip freeze > requirements.txt
```
  - to create Procfile
```
web gunicorn app:app
```
---
#### Step5: create heroku app
- create a heroku app by using the command in your console
```
heroku create
```
![螢幕擷取畫面 2023-03-13 170234](https://user-images.githubusercontent.com/74141558/224831612-c1c8cbbd-ecc1-4ab1-ae29-6759b8d35f34.png)




