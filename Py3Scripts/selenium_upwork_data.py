import time
import datetime
import re
import xlwt
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Bolagsverket:
    def __init__(self):
        self.bot = webdriver.Firefox(
            executable_path="E:/geckodriver"
        )

    def navigate_and_crawl(self):
        bot = self.bot
        bot.get("https://poit.bolagsverket.se/poit/PublikPoitIn.do")
        time.sleep(5)
        bot.find_element_by_id("nav1-2").click()
        time.sleep(5)
        bot.find_element_by_tag_name("form").find_element_by_tag_name("a").click()
        time.sleep(5)

        search_form = bot.find_element_by_tag_name("form")
        search_form.find_element_by_xpath(
            "//select[@id='tidsperiod']/option[text()='Annan period']"
        ).click()
        wait = WebDriverWait(bot, 10)
        input_from = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='from']"))
        )
        input_from.send_keys("2019-09-23")
        # input_from.send_keys(str(datetime.date.today()-datetime.timedelta(1)))
        input_to = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='tom']"))
        )
        input_to.send_keys("2019-09-24")
        # input_to.send_keys(str(datetime.date.today()))
        time.sleep(5)

        amnesomrade = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='amnesomrade']"))
        )
        amnesomrade.find_element_by_xpath(
            "//select[@id='amnesomrade']/option[text()='Bolagsverkets registreringar']"
        ).click()
        time.sleep(5)
        kungorelserubrik = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='kungorelserubrik']"))
        )
        kungorelserubrik.find_element_by_xpath(
            "//select[@id='kungorelserubrik']/option[text()='Aktiebolagsregistret']"
        ).click()
        time.sleep(5)
        underrubrik = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='underrubrik']"))
        )
        underrubrik.find_element_by_xpath(
            "//select[@id='underrubrik']/option[text()='Nyregistreringar']"
        ).click()

        # Search Button
        button_sok = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='SokKungorelse']"))
        )
        button_sok.click()
        time.sleep(5)

        number_of_pages = bot.find_element_by_xpath(
            "//div[@class='gotopagediv']/em[@class='gotopagebuttons']"
        ).text.split("av", 1)[1]
        number_of_pages.strip().replace(" ", "")

        number_of_results = bot.find_elements_by_xpath("//table/tbody/tr")

        wb = Workbook()
        for page in range(int(number_of_pages)):
            sheet = wb.add_sheet("Sheet" + str(page))
            style = xlwt.easyxf("font: bold 1")
            sheet.write(0, 0, "Post Address", style)
            sheet.write(0, 1, "Bildat", style)
            sheet.write(0, 2, "Foretagsnamn", style)
            sheet.write(0, 3, "Email", style)

            for i in range(len(number_of_results)):
                result = bot.find_elements_by_xpath("//table/tbody/tr")[i]
                link = result.find_element_by_tag_name("a")
                bot.execute_script("arguments[0].click();", link)
                time.sleep(5)

                information = [bot.find_element_by_class_name("kungtext").text]
                try:
                    postaddress = re.search("Postadress:(.*),", information[0])
                    sheet.write(i + 1, 0, str(postaddress.group(1)))
                    bildat = re.search("Bildat:(.*)\n", information[0])
                    sheet.write(i + 1, 1, str(bildat.group(1)))
                    foretagsnamn = re.search("Företagsnamn:(.*)\n", information[0])
                    sheet.write(i + 1, 2, str(foretagsnamn.group(1)))
                    email = re.search("E-post:(.*)\n", information[0])
                    sheet.write(i + 1, 3, str(email.group(1)))
                    print(
                        postaddress.group(1),
                        bildat.group(1),
                        foretagsnamn.group(1),
                        email.group(1),
                    )
                except AttributeError as e:
                    print("Email is null")
                    sheet.write(i + 1, 3, "null")
                    pass
                bot.back()
                time.sleep(5)
                wb.save("emails.xls")
            print("Going to next page ...")
            button_next = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input/[@id='movenextTop']"))
            )
            button_next.click()
            time.sleep(5)


bot = Bolagsverket()
bot.navigate_and_crawl()
