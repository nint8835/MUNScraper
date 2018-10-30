import random

from colorutils import hsv_to_hex

from MUNScraper.TreeDrawer import draw_tree

COLOURS = {}

COURSES = [
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-1023", "COMP"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=ENGI-0504", "ENGI"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=ENGI-0517", "ENGI"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=ENGI-0534", "ENGI"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=ENGI-0554", "ENGI"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=ENGI-0578", "ENGI"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=ENGI-0605", "ENGI"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=ENGI-0643", "ENGI"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-2563", "BIOC"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-0766", "BIOL"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-0905", "CHEM"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-2273", "EASC"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-3569", "OCSC"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-1574", "PHYS"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=SCI-1702", "PSYC"),
    ("https://www.mun.ca/regoff/calendar/sectionNo=BUSI-0288", "BUSI")
]

for _, prefix in COURSES:
    random.seed(prefix)
    COLOURS[prefix] = hsv_to_hex((random.randint(0, 360), random.random(), 0.7))

draw_tree(COURSES, COLOURS)