# Latinum-Bot

Latinum Bot was made by @KampfZomby for a planned Discord Server. 
It is fully functional and only needs words to be added.

## Table of contents

 * [How to build](#how-to-build)
    * [Git](#git)
    * [Python](#Python)
    * [Cloning and using the bot](#cloning-and-using-the-bot)
 * [Staying Up To Date](#staying-up-to-date)
 * [Project Structure](#project-structure)
 * [Features](#features)
 
 ## How to build

Requirements:

 * [Git](#Git)
 * [Python](#Python)

If you have both of the above requirements you can skip to [cloning the git repo and use the bot](#cloning-and-using-the-bot).

### Git

If you haven't installed git on your system go and do so it is **REQUIRED** for setting up a working build environment.

[Download Link](https://git-scm.com/download/win)

### Python

Python is the language in which the bot is written, if you haven't used it before we will need to download and install it.

[Download Link](https://www.python.org/downloads/)

### Cloning and using the bot

- Make sure that you have installed Git and Python.

- Clone the repository:
  ```bash
  git clone https://github.com/Latinum-App/Latinum-Bot.git
  ```
  
 ## Staying Up To Date

Pull the latest changes from this repository.

With a command line it is as easy as:

```bash
git pull
``` 
 
  ## Features

Below is an list of feature.

- with the command challenge you can start the game in the dm's of the bot.
- with addvocabulary you can add words to the given database of the bot.

## Project Structure

- main.py is the file which contains the code for the bot. In there you have to insert your discord bot token and the prefix you want the bot to use.
- vocabulary.db is the file that contains the latin word and the translation (currently in german). You can edit it using the bot's addvocabulary command or a database editing program.

## Contributing
