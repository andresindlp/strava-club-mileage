<p align="center">
<img src="https://avatars.githubusercontent.com/u/35582438?s=400&u=db9d093e0dee75ddafa354fec2a360922e7d5961&v=4" width="128" height="128"/>
</p>
<p align="center">
<a href="#"><img title="STRAVA CLUB MILEAGE" src="https://img.shields.io/badge/STRAVA CLUB MILEAGE-green?colorA=%23ff0000&colorB=%23017e40&style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://github.com/andresindlp"><img title="Author" src="https://img.shields.io/badge/AUTHOR-ANDRESINDLP-orange.svg?style=for-the-badge&logo=github"></a>
</p>
<p align="center">
<a href="https://github.com/andresindlp/followers"><img title="Followers" src="https://img.shields.io/github/followers/andresindlp?color=blue&style=flat-square"></a>
<a href="https://github.com/andresindlp/strava-club-mileage/stargazers/"><img title="Stars" src="https://img.shields.io/github/stars/andresindlp/whatsapp-bot?color=red&style=flat-square"></a>
<a href="https://github.com/andresindlp/strava-club-mileage/watchers"><img title="Watching" src="https://img.shields.io/github/watchers/andresindlp/whatsapp-bot?label=Watchers&color=blue&style=flat-square"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FArugaZ%2Fwhatsapp-bot&count_bg=%2379C83D&title_bg=%23555555&icon=probot.svg&icon_color=%2300FF6D&title=hits&edge_flat=false"/></a>
</p>

# Strava Club Mileage

### An easy way to get the total distance all the members of a Strava club have done.
![enter image description here](https://i.ibb.co/nQdP5yH/demo.png)
### How to:
- Make sure Python works on your machine.
- Get the club code (not the name) from the URL: ![club code](https://i.ibb.co/KqVbw5M/image.png)

Keep in mind that to be able to get information from clubs, the Strava account you get the API key from needs to be in said clubs. I've found Strava limits the amount of clubs you can join in 24h to 5 currently.
- Edit the `codedb.json` file according to your needs. Make sure to set the data both on the first part of the file and on the second one as per the example file provided.

![codedb explanation](https://i.ibb.co/Yy0sLnT/codedb.png)

- Install the dependencies with `pip install -r requirements.txt`
- You need to already have a [Discord application](https://discord.com/developers/applications) and its API key, use [this](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) tutorial if you don't.
- Set the API keys by editing `discordbot.py` if running locally.
- If using Heroku set the following variables: ![heroku vars](https://i.ibb.co/bQ76zSM/heroku-configs.png)

### Usage:
|Command| Function | Scope |
|--|--|--|
| `!strava <club>`| Get the data from the specified club | Can be used by anyone |
|`!list`|List all the clubs located in the database| Can only be used a server administrator*|

*This is done to prevent hitting the API request limit by people spamming the command.





This project is licensed under the terms of the MIT license.
