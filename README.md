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
- make sure to import os and change the CHANNEL_ACCESS_TOKEN and CHANNEL_SECRET to os.getenv("CHANNEL_ACCESS_TOKEN") and os.getenv("CHANNEL_SECRET")
```
import os
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
```
- create Procfile and requirements.txt (use the file in this repository for example)
* to create requirements.txt
```
pip freeze > requirements.txt
```
* to create Procfile
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
- create remote heroku for your git
```
heroku git:remote -a {your app name, in this case:sheltered-savannah-43690}
```
---
#### Step6: push the app to heroku
```
git add .
git commit -am "push app to heroku"
git remote heroku master
```
---
#### Step7: change the environment variable in your heroku app settings
- go to your heroku dashboard, and you will see the app you created display in your dashboard
![螢幕擷取畫面 2023-03-13 171208](https://user-images.githubusercontent.com/74141558/224833401-04a94a42-2f11-4a46-b8fd-a9ecb2420228.png)
- go in to the app you create and click settings
![螢幕擷取畫面 2023-03-13 171234](https://user-images.githubusercontent.com/74141558/224833638-65d643b1-175b-45d5-aad1-eb925ad67faa.png)
- click reveal config vars 
![image](https://user-images.githubusercontent.com/74141558/224833735-8a8eb940-5c47-4ba6-8d70-48ca7acf84cf.png)






