# THE GAME OF THINGS

Play a version of *The Game of Things* with your friends via screenshare on video chat! Share your screen with your friends on a video communications app (Zoom, Microsoft Teams, etc) and have them submit answers via text. Simple to learn, easy to play.

![game of things title screen](https://i.imgur.com/fqA5Ze6.png)

*written for and tested on Windows OS only*

## Background
I created this project as a way to play *The Game of Things* online with friends during quarentine (Spring 2020). When I couldn't find a playable version online, I decided to make my own using Python. I have been working with Python for a little under a year as a hobbyist and it seemed like a solid way to apply my working knowledge of the language and learn some new skills along the way. 

I tracked down a list of prompts and started doing some research on how to allow the players to text in their answers, considering a smooth user experience first and foremost. From there I built out an environment and landed on using csv and text documents for data storage. Once I pinned down the logic and mechanics of the game, I set out to make it a fun game to look at, hence the colors and limited animation. Likewise, variation in the display (block textures, colors, animations, and flavor text) was something I kept in mind from the very beginning as it is keeps users engaged. 

## SETTING UP THE GAME

When running the game, I use Windows Powershell to display the game for screenshare. For how it is set up, you will also need two other terminals running simultaniously. To acheive this I use [ConEmu](https://conemu.github.io/), a free and open-source tabbed terminal emulator for Windows. 

#### 1. Sign up for a phone number on TWILIO

[Twilio](https://www.twilio.com/) allows you to send and receive text messages using its web service APIs. Make sure that any number you choose has SMS capabilites. 

At the time I am writing this, you can purchase and use a number for the purpose of this game using their free trial. You get a $15 trial credit upon signing up, which is more than enough for our purposes. The SMS enabled phone numbers are $1.00/month and all inbound texts are $0.0075 each. As long as you cancel your account before you spend the trial credit, you shouldn't be charged.

#### 2. Create a tunnel to your localhost with NGROK

Download and install [ngrok](https://ngrok.com/) to create a tunnel to your localhost. Use ConEmu (or some similiar tabbed terminal emulator) to run ngrok. Do not use Windows Powershell as that will be used to run the game display (see step 6).

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

![Twilio Example](https://i.imgur.com/oOF76Ss.png)

The ngrok terminal session must stay open for the entire gaming session. Additionally, every time you initiate ngrok, you must update your ngrok http Forwarding url on Twilio. The url you get through ngrok is randomly generated and changes every time.

#### 3. Download the repository to a folder on your computer

#### 4. Use PIP to install the necessary Python modules

- colored
- flask
- pathlib
- twilio

#### 5. Activate the Flask web application

Using a new tab alongside your ngrok terminal, run `app.py` from the repository on your computer.

At this point your computer is all setup to accept text messages through your Twilio number.

#### 6. Configure display

Before running the game, you will want to configure your display settings in Windows Powershell (see **Display Settings** section below), and screenshare your Windows Powershell terminal.

#### 7. Run the game

Once you are ready to start, run `things.py` from the repository on your computer.

## GAME RULES

*The Game of Things* starts with a prompt for each player to answer. Once the prompt is announced, the player will write a short response to the answer and submit it anonymously. Once all of the responses are received, they are read aloud and one by one the players will take turns trying to guess who wrote which response. When one player successfully pairs another player with their response, the outed player is no longer able to make guesses for the rest of the round. Once there is only one player left in the round, that player is the winner and a new round begins. When a new round begins, all players are back in the game and greeted with a new prompt. This cycle continues until players agree to end the game.

For the sake of simplicity, players in this version of the game only get recognition if they win a round. For the standard *The Game of Things*, players receive a point for each correct guess. 

![names sample](https://i.imgur.com/OEOyVOO.png)
![prompt sample](https://i.imgur.com/FOEcNLH.png)
![answers sample](https://i.imgur.com/AJIArA9.png)
![answers sample 2](https://i.imgur.com/p19FIeL.png)
![drew wins](https://i.imgur.com/IUalro0.png)

## HOW TO FACILITATE THE GAME

The person running the game natively on their PC will be the player responsible for removing answers from the screen during each round of the game as they are the player with access to the command line. 

## Display Settings
The visible display works within a 72w x 22h grid. In order for the game to display as intended, Windows Powershell must not 

![display properties](https://i.imgur.com/x9sj5PM.png)
![display 36](https://i.imgur.com/8X12aFd.png)
![display 24](https://i.imgur.com/awuy90d.png)
![display 40](https://i.imgur.com/aiL8ykx.png)
