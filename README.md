# Pi Romulus

[![Join the chat at https://gitter.im/pi_romulus/Lobby](https://badges.gitter.im/pi_romulus/Lobby.svg)](https://gitter.im/pi_romulus/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Retropie ROM downloader

Based on Romulus, the Linux Retropie ROM manager, Pi Romulus is intended to fill a gaping hole
in the Retropie functionality.
It allows you to search for games for the Retropie that you already own and then downloads it
directly to your Retropie installation, no further work required.
What makes Pi Romulus so attractive, is that there is no need for any other computer system.
You dont need to switch on your laptop to download and transfer the games. Just hook up a
keyboard to your Retropie, search for the game, select and play.

Features:
* Searching ROMs through Emuparadise
* Automatic detection of which emulator is required
* If required, it will automatically extract ROMs
* Places ROMs in the correct folder

Technical Details
-----------------
Romulus is written using Python 2.7.
For it's GUI framework it makes use of the excellent npyscreen library.

Installation
------------
Clone this app into a folder on your Retropie. If it isnt already installed, install pip: `sudo apt-get install python-pip libarchive-dev`.
After this, install all the requirements with `pip install -r requirements.txt`
Once completed, run `python romulus.py` to start the app, or create a shortcut.

Developers
----------
All code is licensed under GNU Public License 2 (GPLv2). This license allows you to copy, edit, and redistribute without restriction, as long as it retains the free GPLv2 license.

All help is appreciated, whether filing bug reports, squashing bugs, requesting features or anything else, simply clone this repo, and if you have improved it somehow, make a pull request.

Authors
-------
Arthur Moore <arthur.moore85@gmail.com>
