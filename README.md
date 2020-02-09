# GradCafe-Notifier

> Using this script get notifications to your email address whenever someone posts status updates in gradcafe portal for the universities of your interest.

## Installation & usage

* Clone/ Download this repo
* Inside script.py in the pages list variable add all the URL's which you want to monitor.
```
For instance if you want to monitor status updates for Cornell university Computer Science program use the below format:
pages = ['https://www.thegradcafe.com/survey/index.php?q=cornell*+computer+science*&t=a&o=']
(You can add as many urls as you want)
```
* Also change the sender_email, sender_password and reciever_email variables accordingly.
* Turn on access for less secure apps in the sender email account (https://www.google.com/settings/security/lesssecureapps). I recommend making a new gmail account and using it as sender email ID.
* Login to Heroku and create an app 
* If you haven't already, Download and Install Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli)
* Login to add SSH keys
```
heroku login
```
* Deploy the script on heroku app
```sh
heroku git:remote -a <your-app-name>
git add .
git commit -m 'Init'
git push heroku master
```
* If your app is deployed successfully you can see logs using following command:
```
heroku logs --tail
```
* If you have no errors you will recieve email updates to reciever's mail every hour (Only if there is any updates in gradcafe)

If you have any errors feel free to raise issues. PR's are encouraged.
