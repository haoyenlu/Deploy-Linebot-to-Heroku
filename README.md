# deploy-test-linebot-to-heroku
Deploy test line bot, python line-bot-sdk, on heroku
#### Step1: create heroku account and line developer account
- you can reffer to this youtube video to learn how to create line developer account and create massaging API
https://www.youtube.com/watch?v=eGTldX8zpA0
- also create line bot provide and channel beforehand
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
- click reveal config vars <br>
![image](https://user-images.githubusercontent.com/74141558/224833735-8a8eb940-5c47-4ba6-8d70-48ca7acf84cf.png)
- add CHANNEL_ACCESS_TOKEN of your line bot to the variables <br>
![image](https://user-images.githubusercontent.com/74141558/224834133-5a180b4a-50ff-40df-a086-8199b56af439.png)
- and add CHANNEL_SECRET of your line bot to the variable <br>
![螢幕擷取畫面 2023-03-13 172231](https://user-images.githubusercontent.com/74141558/224835526-4fea07ce-488f-4049-ad4a-b92d53173dd8.png)
---
#### Step8: add webhook url to your line bot 
- go to your line bot channel and click messaging API
- you will see a webhook url, click edit
- copy your application address and add "/callback" after the address
![image](https://user-images.githubusercontent.com/74141558/224835889-a17b0bc9-c5d4-4624-ad66-721f1b3a6ee6.png)
- click verify to check whether it is succeed
---
#### Step9: add chatbot to your line friend using QR code
- add the chatbot to your line friend with the QR code
- you can now talk to the chatbot
- If it works, it will only reply the message you sent to you.






