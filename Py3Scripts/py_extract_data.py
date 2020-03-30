import re
import csv
import urllib.request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import xlrd
import time

dots = []


def read_excel_file():
    loc = "dots.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(1, 5):
        dot = str(sheet.cell_value(i, 0)).replace(".0", "")
        dots.append(dot)


def crawl_data(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, "html.parser")
    bold_texts = bs.find_all("b")
    for b in bold_texts:
        try:
            date = (
                re.search(
                    "The information below reflects the content of the FMCSA management information systems as of(.*).",
                    b.get_text(strip=True, separator="  "),
                )
                .group(1)
                .strip()
            )
            if len(date) > 11:
                date = date.split(".", 1)[0]
            print(date)
        except AttributeError:
            pass

    information = bs.find("center").get_text(strip=True, separator="  ")

    operating = re.search("Operating Status:(.*)Out", information).group(1).strip()
    legal_name = re.search("Legal Name:(.*)DBA", information).group(1).strip()
    physical_address = (
        re.search("Physical Address:(.*)Phone", information).group(1).strip()
    )
    mailing_address = (
        re.search("Mailing Address:(.*)USDOT", information).group(1).strip()
    )
    usdot_address = (
        re.search("USDOT Number:(.*)State Carrier ID Number", information)
        .group(1)
        .strip()
    )
    power_units = re.search("Power Units:(.*)Drivers", information).group(1).strip()
    drivers = re.search("Drivers:(.*)MCS-150 Form Date", information).group(1).strip()

    write_csv(
        date,
        operating,
        legal_name,
        physical_address,
        mailing_address,
        usdot_address,
        power_units,
        drivers,
    )


def write_csv(
    date,
    operating,
    legal_name,
    physical_address,
    mailing_address,
    usdot_address,
    power_units,
    drivers,
):
    with open(
        usdot_address + ".csv", mode="w", newline="", encoding="utf-8"
    ) as csv_file:
        fieldnames = [
            "Date",
            "Operating Status",
            "Legal_Name",
            "Physical Address",
            "Mailing Address",
            "Power Units",
            "Drivers",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {
                "Date": date,
                "Operating Status": operating,
                "Legal_Name": legal_name,
                "Physical Address": physical_address,
                "Mailing Address": mailing_address,
                "Power Units": power_units,
                "Drivers": drivers,
            }
        )


read_excel_file()
print(dots)
for dot in dots:
    crawl_data(
        "https://safer.fmcsa.dot.gov/query.asp?searchtype=ANY&query_type=queryCarrierSnapshot&query_param=USDOT&query_string="
        + dot
    )
    time.sleep(5)
