"""Module Docstring"""
import subprocess

import isort  # noqa: F401
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


class Inputs:
    """"""

    def head(self):
        """"""
        page_name1 = "hp"
        title1 = "HP"
        description1 = "homepage"
        page_url1 = "http://support_services/teste/hp.php"
        project1 = "support_services/teste"
        refresh1 = "10000"

        page_name2 = "srch"
        title2 = "Search"
        description2 = "search_page"
        page_url2 = "http://support_services/teste/search.php"
        project2 = project1
        refresh2 = refresh1

        page_name3 = "abt"
        title3 = "About"
        description3 = "about"
        page_url3 = "http://support_services/teste/about.php"
        project3 = project1
        refresh3 = refresh1

        page_name4 = ""
        title4 = ""
        description4 = ""
        page_url4 = ""
        project4 = ""
        refresh4 = ""

        head_pages = {
            page_name1: {"title": title1, "description": description1, "page_url": page_url1, "project": project1, "refresh": refresh1},
            page_name2: {
                "title": title2,
                "description": description2,
                "page_url": page_url2,
                "project": project1,
                "refresh": refresh1,
            },
            page_name3: {"title": title3, "description": description3, "page_url": page_url3, "project": project1, "refresh": refresh1},
        }

        return head_pages

    def header(self):
        """"""
        descriptions = []
        page_names = []
        header_title = "TESTE"
        headdict = Inputs.head(self)
        for page in headdict:
            descriptions.append(headdict[page]["description"])
        for description in descriptions:
            page_names.append(description + "_page.php")

        return page_names

    def header_title(self):
        """"""
        header_title = "TESTE"
        return header_title


inp = Inputs()
inp.header()
