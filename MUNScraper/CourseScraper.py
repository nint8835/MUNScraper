from typing import List

import requests
from bs4 import BeautifulSoup

PREFIXES = {
    "MATH": "Mathematics",
    "STAT": "Statistics",
    "COMP": "Computer Science",
    "ENGL": "English",
    "BIOL": "Biology",
    "BIOC": "Biochemistry",
    "ENGI": "Engineering"
}

class Course(object):

    prefix: str = None
    name: str = None
    number: str = None
    requirements: List[str] = []

    def __repr__(self):
        return f"{self.prefix}{self.number}: {self.name}"

def _process_basic_tag(tag) -> str:
    return tag.contents[0].replace("\n", "").replace("\t", "")

def scrape_courses(url: str, prefix: str) -> List[Course]:
    courses = {}

    content = requests.get(url).text
    soup = BeautifulSoup(content)

    divs = soup.find_all("div", class_="course")
    for div in divs:
        children = div.find_all("p")
        c = Course()
        c.prefix = prefix
        c.number = _process_basic_tag(children[0])
        c.name = _process_basic_tag(children[1])

        for tag in div.find_all("p", class_="courseAttrs"):
            if "PR: " not in tag.contents[0]:
                continue
            pr = tag.text.replace("\n", "").replace("\t", "").replace(", and ", ", ").replace(" and ", ", ").replace("; ", ", ")
            pr = pr.replace(";,", ",").replace(", or ", ", ").replace(" or ", ", ").replace("the former ", "")
            pr = pr.replace(" (or equivalent)", "")

            for k, v in PREFIXES.items():
                pr = pr.replace(v, k)
            print(pr)

        courses[c.number] = c
    return courses