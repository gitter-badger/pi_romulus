"""
:module: download.py
:description: Downloading module

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 31/12/16
"""
from io_utils.directory_utils import Directories

__author__ = 'arthur'


class Download(object):
    """
    Downloads a ROM/Game
    """
    def __init__(self, scraper_obj):
        self.url = None
        self.dirs_obj = Directories()
        self.base_dir = '/home/pi/RetroPie/roms'
        self.scrape = scraper_obj

    def download(self, rom_url):
        """
        Downloads the ROM
        """
        platform = " ".join(rom_url.split('/')[3].replace('_', ' ').split()[:-1])
        target = self.dirs_obj.target_directory(self.base_dir, platform)
        self.scrape.download(rom_url, target)
