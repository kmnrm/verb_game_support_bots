# Customer Support Bots

Telegram and VK customer support bots for "Verb Games" 
publishing house.

## Getting started

Bots use [DialogFlow](https://dialogflow.com/), a natural language understanding 
platform by [Google](https://google.com).

- [DialogFlow Agent training](#1-dialogflow-agent)
- [Bots](#2-bots)
    - [Telegram bot](#21-telegram-bot)
    - [VK bot](#22-vk-bot)
    - [Logging bot](#23-logging-bot)
- [Running the script](#3-running-the-script)

You can find the examples of the working bots in [Running the script](#3-running-the-script) section.

### 1. DialogFlow Agent
To setup and train a DialogFlow agent follow the steps below.

1. To use these bots, create a Google project following the 
[setup steps](https://cloud.google.com/dialogflow/docs/quick/setup). After the project is created, 
you will see [this page](https://dvmn.org/media/filer_public/95/28/95280b13-4843-47ec-bc03-2c3325ad7eac/project.png).

2. Build an agent, using the steps mentioned in 
[Create an agent](https://cloud.google.com/dialogflow/docs/quick/build-agent#create-an-agent) instructions.
Choose Russian as a default language and the project created in Step 1 as Google Project.
The result of a built agent is [this page](https://dvmn.org/media/filer_public/a4/5f/a45f0464-32f2-4b7a-9c81-4afc2ece405f/agent.png).

3. Create a [service account](https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account).
Do not forget to create and download your [service account __JSON__-key](https://console.cloud.google.com/apis/credentials/serviceaccountkey).

4. To work via DialogFlow, you need to create intents and train 
your agent. Read more about [intents](https://cloud.google.com/dialogflow/docs/intents-overview).

    1. Create and save training phrases `json` file in the project path and name it `training_phrases.json`. In the [example](https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json) of 
    `training_phrases.json` there is:
        - `Устройство на работу` for an intent name.
        - `Как устроиться к вам на работу?` for a training phrase.
        - The value of `answer` key for the training phrase response.
    
    2. Run `train intents.py` to train your agent with the training phrases from your
    `training_phrases.json` file. Check it out in the intents of your agent page.
    ![](https://sun9-11.userapi.com/c855020/v855020890/2339ca/nssJOMEr_Po.jpg)

After following the instructions above you will be having 2 configuration variables:
- Your DialogFlow `project ID`, which you
can find on your agent page.
- Your `GOOGLE_APPLICATION_CREDENTIALS` file in `json` format.

### 2. Bots
#### 2.1. Telegram Bot

Get your **Telegram chat ID** via [userinfobot](https://telegram.me/userinfobot).

Create your Telegram Bot via [BotFather](https://telegram.me/BotFather) and get a **bot token** to access the HTTP API.

Create Logging Bot via [BotFather](https://telegram.me/BotFather) and get a **logging bot token**.

Get a **logging chat ID**, if you want to use logging bot for another Telegram account.

As a result of the steps above you will have 4 config vars:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_BOT_CHAT_ID=your_chat_id
LOGGING_BOT_TOKEN=your_logging_bot_token
LOGGING_BOT_CHAT_ID=your_logging_bot_chat_id
```

##### Set your Heroku app

These are the instructions for activating your bot via Heroku app. If you want to run the script without creating an app on Heriku, go to [Running the script](#running-the-script) section.
Pay attention on how to set `GOOGLE_APPLICATION_CREDENTIALS`environment variable.

To set an app on Heroku follow the steps below.

1. Clone this repository to your [GitHub](https://github.com/) repositories.

2. Sign in or sign up on [Heroku](https://id.heroku.com/login), if you don't have a user account.

3. [Create a new app](https://dashboard.heroku.com/new-app). Add your app name and choose a region.

4. Go to `Deploy` tab and choose `Connect to GitHub` as a deployment method to connect your Heroku app to GitHub to enable code diffs and deploys.

   Add your cloned repository name to `repo-name`, click `Search` and then click `Connect`.

   Click `Deploy Branch` to deploy `master` branch to your app. 


##### Set config vars 
After your app successfully deployed go to `Settings` tab and add your `Config Vars`. 

   For **`TELEGRAM_BOT_CHAT_ID=your_chat_id`** there is `KEY` that is `TELEGRAM_BOT_CHAT_ID`, and `VALUE` that is `your_chat_id`.

   KEY  | VALUE
   ------------- | -------------
   TELEGRAM_BOT_CHAT_ID  | your_telegram_bot_token
   TELEGRAM_BOT_TOKEN  | your_chat_id
   LOGGING_BOT_CHAT_ID  | your_logging_bot_token
   LOGGING_BOT_TOKEN  | your_logging_bot_chat_id
   DIALOGFLOW_PROJECT_ID | your_dialogflow_project_id


###### Google Application Credentials

You also need one more config var named [`GOOGLE_APPLICATION_CREDENTIALS`](https://cloud.google.com/dialogflow/docs/quick/setup#auth-env).
- Declare your env variables from in Heroku dashboard like this:
![](https://i.stack.imgur.com/3gxMn.png)
The `GOOGLE_CREDENTIALS` variable is the content of service account credential `json` file as is. The `GOOGLE_APPLICATION_CREDENTIALS` env variable in the string `google-credentials.json`.
- Once variables are declared, add the buildpack from command line:
    ```commandline
    heroku buildpacks:add https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack -a your_app_name
    ```
- Deploy. The buildpack will automatically generate a `google-credentials.json` and fill it with the content of the `GOOGLE_CREDENTIALS` content.


##### Activate your bot

Go to `Resources` to open your app [Dynos](https://www.heroku.com/dynos). You will see the line from `Procfile` of your cloned repository:
   ```
   tg-bot python3 tg_bot.py
   ```
   Activate your bot by switching it on and clicking `Confirm`.


#### 2.2. VK bot
1. [Create a VK community](https://vk.com/groups?w=groups_create) with any name you want. 
Try to avoid the names that are equal to the communities' names that you've already been managing, as it may cause issues the program will be running into.
2. Go to your community settings and [enable community messages](https://vk.com/support/faq9605).
3. Open the **Manage community** tab, go to **API usage** tab and click **Create token**.

Set your `vk-bot` Heroku app following the the [steps 1 to 4](#set-your-heroku-app).

##### Set config vars 
After your app successfully deployed go to `Settings` tab and add your `Config Vars`. 

For **`VK_BOT_TOKEN=your_vk_community_token`** there is `KEY` that is `VK_BOT_TOKEN`, and `VALUE` that is `your_vk_community_token`.

   KEY  | VALUE
   ------------- | -------------
   VK_BOT_TOKEN  | your_vk_community_token
   DIALOGFLOW_PROJECT_ID  | your_dialogflow_project_id
   LOGGING_BOT_CHAT_ID  | your_logging_bot_token
   LOGGING_BOT_TOKEN  | your_logging_bot_chat_id
   
You also need one more config var named [`GOOGLE_APPLICATION_CREDENTIALS`](https://cloud.google.com/dialogflow/docs/quick/setup#auth-env).
Check [how to set](#google-application-credentials) this configuration variable.

##### Activate your bot

Go to `Resources` to open your app [Dynos](https://www.heroku.com/dynos). You will see the line from `Procfile` of your cloned repository:
   ```
   vk-bot python3 vk_bot.py
   ```
   Activate your bot by switching it on and clicking `Confirm`.
  

#### 2.3. Logging bot
Logging Telegram bot is created both for Telegram bot and for VK bot. If there is any error, the logging bot will notify user that the bot has crashed with the following error text.
![](https://sun9-55.userapi.com/c858436/v858436417/1e6735/HUyvarNzEBg.jpg)

### 3. Running the script
Install Python3 to use this program.

[Set](https://cloud.google.com/docs/authentication/getting-started#setting_the_environment_variable) the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
You will also need to set more environment variables depending on which bot you are going to use. The variables are:
- `DIALOGFLOW_PROJECT ID`
- `LOGGING_BOT_TOKEN` for _logging bot_
- `LOGGING_BOT_CHAT_ID` for _logging bot_
- `VK_BOT_TOKEN` for _VK bot_
- `TELEGRAM_BOT_TOKEN` for _Telegram bot_
- `TELEGRAM_CHAT_ID` for _Telegram bot_


Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Running `tg_bot.py` script:
```
$ python3 tg_bot.py
```
![](https://dvmn.org/media/filer_public/7a/08/7a087983-bddd-40a3-b927-a43fb0d2f906/demo_tg_bot.gif)


Running `vk_bot.py` script:
```
$ python3 tg_bot.py
```
![](https://dvmn.org/media/filer_public/1e/f6/1ef61183-56ad-4094-b3d0-21800bdb8b09/demo_vk_bot.gif)

Logging info:

```
2020-01-01 10:10:10,152 - INFO - Бот запущен
```
