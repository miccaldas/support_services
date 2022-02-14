"""The goal is to have a python page generator that, if needed, can easily redo all pages on site or make alterations on their structure.
    This way all changes to the structure can be done on the templates or through the information that is sent to these python files."""
import subprocess

import isort  # noqa: F401
import snoop
from jinja2 import Environment, FileSystemLoader, Template  # noqa: F401
from loguru import logger

from inputs import Inputs

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def head_and_header_builder():
    """We collect the information from the Inputs file and put them in the templates."""
    inp = Inputs()
    head_pages = inp.head()
    header_title = inp.headertitle()

    titles = []
    new_titles = []
    for page in head_pages:
        titles.append(head_pages[page]["title"])
    for title in titles:
        new_titles.append(title.lower() + ".php")

    listoflists = [list(d.values()) for d in head_pages.values()]
    print(len(listoflists))

    env = Environment(loader=FileSystemLoader("/usr/share/nginx/html/support_services/templates"))
    template = env.get_template("base.tpl")
    for i in range(len(new_titles)):
        with open(f"/usr/share/nginx/html/support_services/teste/{new_titles[i]}", "w") as f:
            f.write(
                template.render(
                    title=listoflists[i][0],
                    description=listoflists[i][1],
                    page_url=listoflists[i][2],
                    project=listoflists[i][3],
                    refresh=listoflists[i][4],
                    lists=listoflists,
                )
            )

    env = Environment(loader=FileSystemLoader("/usr/share/nginx/html/support_services/templates"))
    template = env.get_template("header.tpl")
    for i in range(len(new_titles)):
        with open("/usr/share/nginx/html/support_services/partials/header.php", "w") as f:
            f.write(
                template.render(
                    title=listoflists[i][0],
                    description=listoflists[i][1],
                    page_url=listoflists[i][2],
                    project=listoflists[i][3],
                    refresh=listoflists[i][4],
                    lists=listoflists,
                    header_title=header_title,
                )
            )


if __name__ == "__main__":
    head_and_header_builder()
