from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import autoit
service_obj = Service("C:\\Users\\ALAGU SUNDARI\\Downloads\\geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://dev.talentfind.io/ohr")
driver.maximize_window()
username = "alagusundarimca@gmail.com"
phoneno = "8764523189"
password = "Arun@123"
Qsubject = "Dental"
PG = "MD"
def sign():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, 'register-now'))).click()
    driver.find_element(By.XPATH, "//input[@name ='email']").send_keys(username)
    element = driver.find_element(By.XPATH,  "//button[@class = 'btn rounded-0 pl-5 pr-5 btn-primary']")
    driver.execute_script("arguments[0].click();", element)
sign()
def personal():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div[@name='title_id'] ").click()
    Title = driver.find_elements(By.XPATH , "//ul[@id ='vs1__listbox']//li['vs__dropdown-option']")
    for title in Title:
        if title.text == "Mr":

            title.click()
            break
    driver.find_element(By.XPATH, "//input[@name = 'first_name']").send_keys("Arun")
    driver.find_element(By.XPATH, "//input[@name = 'middle_name']").send_keys("Pradesh")
    driver.find_element(By.XPATH, "//input[@name = 'surname']").send_keys("E")
    driver.find_element(By.XPATH, "//div[@name ='date-dropdown-date-dob']").click()
    Days = driver.find_elements(By.XPATH, " //ul[@id = 'vs2__listbox']//li[@class = 'vs__dropdown-option']")
    for day in Days:

        if day.text == "27":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            day.click()
            break
    driver.find_element(By.XPATH, "//div[@name  = 'date-dropdown-month-dob']").click()
    Month = driver.find_elements(By.XPATH, "//ul[@id =  'vs3__listbox']//li[@class = 'vs__dropdown-option']")
    for month in Month:
        if month.text == "Dec":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            month.click()
            break
    driver.find_element(By.XPATH, " //div[@name = 'date-dropdown-year-dob']").click()
    Year = driver.find_elements(By.XPATH, "//ul[@id =  'vs4__listbox']//li[@class = 'vs__dropdown-option']")
    for year in Year:
        if year.text == "1979":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            year.click()
            break
    driver.find_element(By.XPATH, "//div[@name = 'gender']").click()
    Gender = driver.find_elements(By.XPATH, "//ul[@id ='vs5__listbox']//li[@class ='vs__dropdown-option']")
    for gender in Gender:
        if gender.text == "Male":
            gender.click()
            break
    driver.find_element(By.XPATH, " //div[@name = 'nationality']").click()
    Nation = driver.find_elements(By.XPATH, "//ul[@id = 'vs6__listbox']//li[@class ='vs__dropdown-option']")
    for nation in Nation:
        if nation.text == "Russian":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            nation.click()
            break
    driver.find_element(By.XPATH, " //div[@name ='country_id']").click()
    Work = driver.find_elements(By.XPATH, "//ul[@id = 'vs7__listbox']//li[@class ='vs__dropdown-option']")
    for work in Work:
        if work.text == "Canada":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            work.click()
            break
personal()
def contact():
    driver.find_element(By.XPATH, "//div[@name='phone-code-phone']").click()
    Code = driver.find_elements(By.XPATH, "//ul[@id = 'vs8__listbox']//li[@class ='vs__dropdown-option']")
    for code in Code:
        if code.text == "HRV +385":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            code.click()
            break

    driver.find_element(By.XPATH, "//input[@name='phone-number-phone']").send_keys(phoneno)
    contact = driver.find_element(By.XPATH, "//div[@name ='contact-information']")
    driver.execute_script("arguments[0].scrollIntoView();", contact)
    driver.find_element(By.XPATH, "//span[@class ='c-switch-slider'] ").click()
    driver.find_element(By.XPATH, "//div[@name = 'phone-code-whatsapp']").click()
    Codes = driver.find_elements(By.XPATH, "//ul[@id = 'vs20__listbox']//li[@class = 'vs__dropdown-option']")
    for codes in Codes:
        if codes.text() == "HRV +385":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            codes.click()
            break

    driver.find_element(By.XPATH, "//div[@id = 'vs9__combobox']").click()
    Option = driver.find_elements(By.XPATH,"//ul[@id = 'vs9__listbox']//li[@class = 'vs__dropdown-option']")
    for option in Option:
        if option.text == "SMS":
            option.click()
            break
    driver.find_element(By.XPATH, "//input[@name = 'alternate_email']").send_keys(username)
contact()
def professional():
    prof = driver.find_element(By.XPATH, "//div[@name ='candidate_type']")
    driver.execute_script("arguments[0].scrollIntoView();", prof)
    driver.find_element(By.XPATH, "//div[@id ='vs10__combobox']").click()
    Profession = driver.find_elements(By.XPATH,"//ul[@id = 'vs10__listbox']//li[@class = 'vs__dropdown-option']")
    for profession in Profession:
        if profession.text == "Dentist":
            profession.click()
            break
    driver.find_element(By.XPATH, "//div[@name ='main_qualification_country_id'] ").click()
    Qualification = driver.find_elements(By.XPATH, " //ul[@id = 'vs11__listbox']//li[@class ='vs__dropdown-option']")
    for qualification in Qualification:
        if qualification.text == "Nepal":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            qualification.click()
            break
    Qname = driver.find_element(By.XPATH, "//label[text() = 'Qualification Name']")
    driver.execute_script("arguments[0].scrollIntoView();", Qname)

    driver.find_element(By.XPATH, "//div[@name ='main_qualification_id']").click()
    PGcourse = driver.find_elements(By.XPATH, "//ul[@id = 'vs12__listbox']//li[@class = 'vs__dropdown-option']")
    for pgcourse in PGcourse:
        if pgcourse.text == "PG Cert":
            pgcourse.click()
            break

    driver.find_element(By.XPATH,"//input[@name = 'main_qualification_description'] ").send_keys(Qsubject)
    Mony = driver.find_element(By.XPATH, "//div[@name= 'month-and-year-awarded']")
    driver.execute_script("arguments[0].scrollIntoView();", Mony)
    driver.find_element(By.XPATH,  "//div[@name= 'date-dropdown-month-qualified_date']").click()
    Mon = driver.find_elements(By.XPATH, "//ul[@id ='vs13__listbox']//li[@class = 'vs__dropdown-option']")
    for mon in Mon:
        if mon.text == "Oct":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            mon.click()
            break
    driver.find_element(By.XPATH, "//div[@name= 'date-dropdown-year-qualified_date']").click()
    Yea = driver.find_elements(By.XPATH, "//ul[@id = 'vs14__listbox']//li[@class ='vs__dropdown-option']")
    for yea in Yea:
        if yea.text == "2008":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            yea.click()
            break
    driver.find_element(By.XPATH," //div[@name= 'speciality_id']").click()
    Specality = driver.find_elements(By.XPATH,  "//ul[@id = 'vs15__listbox']//li[@class ='vs__dropdown-option']")
    for specality in Specality:
        if specality.text == "Dental Anaesthesiology":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            specality.click()
            break
professional()
def registration():
    Reg = driver.find_element(By.XPATH, "//div[@name= 'registration-details']")
    driver.execute_script("arguments[0].scrollIntoView();", Reg)
    driver.find_element(By.XPATH, "//input[@name ='password']").send_keys(password)
    driver.find_element(By.XPATH,  "//input[@name ='confirmPassword']").send_keys(password)
registration()
def upload():
    Upload = driver.find_element(By.XPATH, "//h5[ @class= 'text-primary']")
    driver.execute_script("arguments[0].scrollIntoView();", Upload)
    driver.find_element(By.XPATH, "//div[@name ='document_type']").click()
    File = driver.find_elements(By.XPATH, "//ul[@id = 'vs16__listbox']//li[@class = 'vs__dropdown-option']")
    for file in File:
         if  file.text ==  "Cover Letter":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            file.click()
            break


    driver.find_element(By.XPATH, "//input[@class ='mr-2']").click()
    driver.find_element(By.XPATH, "//div[@name ='upload-document']//div").click()
    autoit.control_focus("File Upload", "Edit1")
    autoit.control_set_text("File Upload", "Edit1", "C:\\Users\\ALAGU SUNDARI\\OneDrive\\Desktop\\sundari.docx")
    autoit.control_click("File Upload", "Button1")
    driver.find_element(By.XPATH, "//button[@name ='registration-submit']").click()
upload()



