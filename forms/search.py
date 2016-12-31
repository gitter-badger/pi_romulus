"""
:module: search.py
:description: Search form

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 31/12/16
"""
import npyscreen as npyscreen
import sys
from forms.results import ResultsForm
from scraping.scraper import Scraper

__author__ = 'arthur'


def clean_results_list(results):
    """
    Returns a clean list of results
    """
    results_list = []
    for rom in results:
        text = rom.text
        clean = text.replace('ROMSystem:', '| ')
        clean = clean.replace('ISOSystem:', '| ')
        clean = clean.replace('Size:', '')
        clean = " ".join(clean.split()[:-1])
        results_list.append(clean)
    return results_list, results


class SearchForm(npyscreen.ActionForm):
    """
    This form presents the user with a search form from where they can search for a
    ROM or other game from EmuParadise.
    """
    def create(self):
        """
        Creates form upon initialization by main app.
        """
        self.rom = self.add(npyscreen.TitleText, name='Game: ')

    def on_ok(self):
        """
        Carried out when OK button is pressed
        """
        npyscreen.notify("Please wait", "Searching...")
        self.search = Scraper(self.rom.value, parent=self)
        self.results = clean_results_list(self.search.fill_in_form())
        self.clean_results = self.results[0]
        self.parentApp.SCRAPER_OBJ = self.search
        self.parentApp.CLEAN_RESULTS = self.clean_results
        self.parentApp.RESULTS = self.results[1]

    def on_cancel(self):
        """
        Carried out when Cancel button is pressed
        """
        sys.exit()

    def afterEditing(self):
        """
        Everything here is ran after on_ok is completed.
        Note that all forms added in the parentApp are loaded with their data before
        the app formally begins. Therefore the Results form is declared here to ensure
        that the results data is loaded AFTER we have the results. Declaring the results form
        in the parentApp would load the form without the results.
        """
        self.parentApp.addForm('RESULTS', ResultsForm, name="Results")
        self.parentApp.setNextForm('RESULTS')
