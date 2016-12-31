"""
:module: romulus.py
:description: Romulus app

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 31/12/16
"""
import npyscreen as npyscreen
from forms import SearchForm

__author__ = 'arthur'


class App(npyscreen.NPSAppManaged):
    """
    Main Romulus app
    """
    # Declaring some shared variables.
    CLEAN_RESULTS = []
    RESULTS = None
    SELECTED_RESULT = None
    RESULTS_DICT = {}
    SCRAPER_OBJ = None

    def onStart(self):
        """
        Initialize the forms.
        """
        self.addForm('MAIN', SearchForm, name="Search for ROM")


if __name__ == '__main__':
    app = App()
    app.run()
