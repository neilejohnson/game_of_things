Play a version of The Game of Things with your friends via screenshare on video chat! Share your screen with your friends on a video communications app (Zoom, Microsoft Teams, etc) and have them submit answers via text. Simple to learn, easy to play.

*written for and tested on Windows OS only*

## Background
I created this project as a way to play The Game of Things online with friends during quarentine (Spring 2020). When I couldn't find a playable version online, I decided to make my own using Python. I have been working with Python for a little under a year as a hobbyist and it seemed like a solid way to apply my working knowledge of the language and learn some new skills along the way. 

I tracked down a list of prompts and started doing some research on how to allow the players to text in their answers, considering a smooth user experience first and foremost. From there I built out an environment and landed on using csv and text documents for data storage. Once I pinned down the logic and mechanics of the game, I set out to make it a fun game to look at, hence the colors and limited animation. Likewise, variation in the display (block textures, colors, animations, and flavor text) was something I kept in mind from the very beginning as it is keeps users engaged. 

## SETTING UP THE GAME

When running the game I use Windows Powershell to display the game for screenshare. For how it is set up, you will also need two other terminals running simultaniously. To acheive this I use [ConEmu](https://conemu.github.io/), a free and open-source tabbed terminal emulator for Windows. 

#### 1. Use PIP to install the necessary Python modules
- colored
- flask
- pathlib
- twilio

#### 2. Sign up for a phone number on Twilio.

[Twilio](https://www.twilio.com/) allows you to send and receive text messages using its web service APIs. Make sure that any number you choose has SMS capabilites. 

At the time I am writing this, you can purchase and use a number for the purpose of this game using their free trial. You get a $15 trial credit upon signing up, which is more than enough for our purposes. The SMS enabled phone numbers are $1.00/month and all inbound texts are $0.0075 each. As long as you cancel your account before you spend the trial credit, you shouldn't be charged.

#### 3. Download the repository to a folder on your computer.

#### 4. Activate the Flask web application.

Download and install [ngrok](https://ngrok.com/) to create a tunnel to your localhost. Use ConEmu (or some similiar tabbed terminal emulator) to run ngrok. Do not use Windows Powershell as that will be used to run the game display (see step **!!!!!!!!?**).

Within your terminal, navigate to the location of the *ngrok.exe* file and type the following prompt...

```
$ ngrok http 5000
```
Once executed, you will see a variation of the following...

```
Session Status                online
Session Expires               7 hours, 59 minutes
Version                       2.3.35
Region                        United States (us)
Web Interface                 http:​//127.0.0.1:4040
Forwarding                    http:​//1df7a739.ngrok.io -> http:​//localhost:5000
Forwarding                    https:​//1df7a739.ngrok.io -> http:​//localhost:5000
```
Copy your newly active ngrok http Forwarding url ('http:​​//1df7a739.ngrok.io' in the example above), paste it within the **A MESSAGE COMES IN** section of your Twilio number's **Messaging** section, add `'/sms'` as a suffix, and click the **Save** button. Refer to the image below for proper settings.

![Twilio Example](https://i.imgur.com/EmTEbpb.png)

The ngrok terminal session must stay open for the entire gaming session. Additionally, every time you initiate ngrok, you must update your ngrok http Forwarding url on Twilio. The url you get through ngrok is randomly generated and changes every time.
