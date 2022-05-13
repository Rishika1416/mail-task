from decouple import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
from requests import Session
import sys
from retry import retry
from Date import Date_
from selenium.common.exceptions import (
    ElementNotInteractableException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotVisibleException,
)
class Shopify:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\H P\.wdm\drivers\chromedriver\win32\100.0.4896.60\chromedriver.exe", chrome_options=options)
    def open_login_window(self):
        website=config('SHOPIFY_WEBSITE')
        self.driver.get("https://partners.shopify.com/organizations")
        #driver = webdriver.Chrome(ChromeDriverManager().install())
    @retry((ElementNotInteractableException,ElementNotVisibleException,ElementClickInterceptedException),3,3)
    def submit(self):
        submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'commit')))
        submit.click()
    def login(self):
        self.username=config('SHOPIFY_USERNAME')
        self.password=config('SHOPIFY_PASSWORD')
        self.driver.refresh()
        #time.sleep(5)
        self.driver.find_element_by_id("account_email").send_keys(self.username)
        #time.sleep(5)
        self.submit()
        print("entered email id")
        self.driver.switch_to.frame(0)
        print("switched frame")
        #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next']"))).click()
        #button = self.driver.find_element_by_name("commit")
        #ActionChains(self.driver).move_to_element(button).click(button).perform()
        #self.driver.find_element_by_xpath("//button[text()='Next']").click()
        #Next.click()

        #self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "myXpath"))).click()
        #self.driver.find_element_by_name("commit").click()
        time.sleep(3)
        self.driver.find_element_by_id("account_password").send_keys(self.password)
        self.submit()
        self.driver.switch_to.default_content()
        #time.sleep(3000)
        return
    @retry((ElementNotInteractableException,ElementNotVisibleException,ElementClickInterceptedException),3,3)
    def click_link(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,"PicAmaze Animate Images, Gifs"))).click()
        #self.driver.find_element_by_class_name("FeTD8").click()
        time.sleep(5)
    def view_history(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,"View all history"))).click()
    # def get_email(self):
    #     #r = requests.get('https://partners.shopify.com/1451076/apps/3932647/history')
    #     #soup = BeautifulSoup(r.text, "html.parser")
    #     with Session() as s:
    #         site = s.get("https://partners.shopify.com/1451076/apps/3932647/history")
    #         print("this is a site")
    #         print(site)
    #         bs_content = BeautifulSoup(site.content, "html.parser")
    #         print("site captured successfully!")
    #         print(bs_content)
    #         token = bs_content.find("input", {"name":"csrf_token"})["value"]
    #         login_data = {"username":self.username,"password":self.password, "csrf_token":token}
    #         s.post("https://partners.shopify.com/1451076/apps/3932647/history", login_data)
    #         home_page = s.get("https://partners.shopify.com/1451076/apps/3932647/history")
    #         print(home_page.content)
        #table = soup.find('table', class_='Polaris-DataTable__Table_2qj3m')
        #print(table)
        # for row in table.tbody.find_all('tr'):
        #     # Find all data for each column
        #     columns = row.find_all('td')
        #     print(columns)

    def get_email(self):
        time.sleep(5)
        print("in get_email.....")
        rows = self.driver.find_elements_by_xpath("//table/tbody/tr")
        list_activity={}
        list_activity['Closed Store']=[]
        list_activity['Uninstalled']=[]
        list_activity['Installed']=[]
        list_activity['Uninstalled']=[]
        list_activity['Recurring charge cancelled']=[]
        # Iterate over the rows
        finish=False
        temps=[]
        for row in rows:
            # Get all the columns for each row. 
            # cols = row.find_elements_by_xpath("./*")
            cols = row.find_elements_by_xpath("./*[name()='th' or name()='td']")
            temp = [] # Temproary list
            for col in cols:
                temp.append(col.text)
            print(temp)
            temps.append(temp)
        print("newline",temps,sep='\n')  
        for r in temps:
            date_inword=r[0]
            date_=Date_(date_inword)
            date_.convert_date_in_numbers()
            if date_.match_date() == True:
                activity=r[2].split('\n')[1]
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,r[1]))).click()
                #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATHT,'//*[@id="AppFrameMain"]/div/div/div[2]/div/section[1]/div[3]/p[1]/a'))).click()
                element=self.driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div[2]/div/section[1]/div[3]/p[1]/a')
                list_activity[activity].append(element.text)
                self.driver.execute_script("window.history.go(-1)")
                time.sleep(1)
            else:
                finish=True
                break 
        print(list_activity)
        return list_activity
        # print("hi")
        # aftertd_XPath = "]/td["
        # aftertr_XPath = "]"
        # before_XPath = ".//table[@class='Polaris-DataTable__TableRow_1a85o']/tbody/tr["
        # rows = len(self.driver.find_elements_by_xpath("//table/tbody/tr[2]/td"))
        # # print (rows)
        # columns = len(self.driver.find_elements_by_xpath(".//table[@class='Polaris-DataTable__TableRow_1a85o']/tbody/tr[2]/td"))
        # # print(columns)
        
        # # print("Company"+"               "+"Contact"+"               "+"Country")
        # print(rows,columns)
        # for t_row in range(2, (rows + 1)):
        #     for t_column in range(1, (columns + 1)):
        #         FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
        #         print("hello")
        #         cell_text = self.driver.find_element_by_xpath(FinalXPath).text
        #         # print(cell_text, end = '               ')
        #         print(cell_text)
        #     print()  



        # time.sleep(5)
        # table_id = self.driver.find_element(By.XPATH, '//table[@class="Polaris-DataTable__Table_2qj3m"]')
        # rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
        # print(rows)
        # for row in rows:
        #     # Get the columns (all the column 2)        
        #     col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
        #     print(col.text)#prints text from the element
    def open_workplace(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Propero')]").click()
        time.sleep(5)
        self.click_link()
        self.view_history()
        email_pair=self.get_email()
        return email_pair
        #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "identity-card identity-card--clickable"))).click()
        #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "FeTD8"))).click()
    '''
    def login(self):
        self.driver.execute_script("window.promptResponse=prompt('Enter username','smth')")
        a = self.driver.execute_script("var win = this.browserbot.getUserWindow(); return win.promptResponse")
        self.driver.find_element_by_id("account_email").send_keys(a)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next']"))).click()
    '''