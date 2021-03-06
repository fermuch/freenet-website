#License: GFDL
from pages.index import *
from pages.help import *
from pages.download import *
from pages.news import *
from pages.about import *
from pages.documentation import *
from pages.donate import *
from pages.contribute import *
from pages.ngrouting import *

languages = ["en", "nl"]
title = "Freenet"
def create_menu():
    return [
        IndexPage(),
        NewsPage(),
        DownloadPage(),
        AboutPage(),
        DocumentationPage(),
        HelpPage(),
        DonatePage(),
        ContributePage(),
        NGRoutingPage(),
        ]
