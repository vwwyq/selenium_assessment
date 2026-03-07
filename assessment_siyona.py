'''
Write a script to:
Open https://www.demowebshop.tricentis.com
Navigate to Books
Add first book to cart
Click Shopping Cart
Verify the product is present in the cart.
'''
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# wait = WebDriverWait(driver, 10)
# books = driver.find_element('xpath', '(//a[contains(text(),"Books")])[1]')
# wait.until(EC.element_to_be_clickable(books)).click()
# time.sleep(1)
# add_cart = driver.find_element('xpath', '(//input[@value="Add to cart"])[1]')
# wait.until(EC.element_to_be_clickable(add_cart)).click()
# time.sleep(1)
# cart = driver.find_element('xpath', '//span[text()="Shopping cart"]')
# wait.until(EC.element_to_be_clickable(cart)).click()
# time.sleep(1)
# try:
#     cart_table = driver.find_element('xpath', '//table[@class="cart"]//tr')
#     wait.until(EC.visibility_of(cart_table))
#     print("Product added to cart.")
# except:
#     print("Product not added to cart.")
'''
Write a Selenium script to:
Open https://www.demowebshop.tricentis.com
Navigate to Electronics
Use XPath contains() to locate the Cell Phones category
Click it.
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# wait = WebDriverWait(driver, 10)
#
# electronics = driver.find_element('xpath', '(//a[contains(text(),"Electronics")])[1]')
# wait.until(EC.element_to_be_clickable(electronics)).click()
# time.sleep(2)
#
# cellphones = driver.find_element('xpath', '(//a[contains(text(),"Cell phones")])[1]')
# wait.until(EC.element_to_be_clickable(cellphones)).click()
#

'''
Write a Selenium script to:
Open https://the-internet.herokuapp.com/dynamic_loading/1
Click Start
Wait until the Hello World text appears
Print the text.
'''

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# wait = WebDriverWait(driver, 10)
#
# start_btn = driver.find_element('xpath', '//button[text()="Start"]')
# wait.until(EC.element_to_be_clickable(start_btn)).click()
#
# hello_text = driver.find_element('xpath', '//div[@id="finish"]/h4')
# wait.until(EC.visibility_of(hello_text))
#
# print(hello_text.text)

'''
Write a script to:
Open https://the-internet.herokuapp.com/dynamic_controls
Click Remove
Wait until Add button becomes clickable
Click Add
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
#
# wait = WebDriverWait(driver, 10)
#
# remove_btn = driver.find_element('xpath', '//button[text()="Remove"]')
# remove_btn.click()
#
# wait.until(EC.presence_of_element_located(('xpath', '//button[text()="Add"]')))
# add_btn = driver.find_element('xpath', '//button[text()="Add"]')
#
# wait.until(EC.element_to_be_clickable(add_btn)).click()
#

'''
Write a Selenium script to:
Open https://demoqa.com/select-menu
Select "Group 2, option 1" from the Select Value dropdown
Verify the selected value.
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demoqa.com/select-menu")
#
# wait = WebDriverWait(driver, 10)
#
# dropdown = driver.find_element('xpath', '//div[@id="withOptGroup"]')
# driver.execute_script("arguments[0].scrollIntoView();", dropdown)
#
# wait.until(EC.element_to_be_clickable(dropdown)).click()
#
# option = driver.find_element('xpath', '//div[text()="Group 2, option 1"]')
# wait.until(EC.element_to_be_clickable(option)).click()
#
# selected = driver.find_element('xpath', '//div[contains(@class,"singleValue")]')
# wait.until(EC.visibility_of(selected))
#
# print("Selected value:", selected.text)


'''
Write a Selenium script to:
Open https://demoqa.com/select-menu
Scroll to Standard multi select
Select Volvo, Saab, and Opel
Print all selected options.
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait, Select
#
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demoqa.com/select-menu")
#
# wait = WebDriverWait(driver, 10)
#
# multi_select = driver.find_element('xpath', '//select[@id="cars"]')
#
# driver.execute_script("arguments[0].scrollIntoView();", multi_select)
#
# select_obj = Select(multi_select)
#
# select_obj.select_by_visible_text("Volvo")
# select_obj.select_by_visible_text("Saab")
# select_obj.select_by_visible_text("Opel")
#
# selected_options = select_obj.all_selected_options
#
# for option in selected_options:
#     print(option.text)

'''
Write a Selenium script to:
Open https://demoqa.com/menu/
Hover over Main Item 2
Hover over SUB SUB LIST
Click Sub Sub Item 1
'''

# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
# driver.get("https://demoqa.com/menu/")
# time.sleep(15)
#
# ele1=driver.find_element('xpath','//a[text()="Main Item 2"]')
# ac.move_to_element(ele1).perform()
# time.sleep(2)
# ele2=driver.find_element('xpath','//a[text()="SUB SUB LIST »"]')
# ac.move_to_element(ele2).perform()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Sub Sub Item 1"]').click()
'''
Write a Selenium script to:
Open https://demoqa.com/droppable
Drag Drag me element
Drop it on Drop here
Verify text changes to Dropped!
'''
# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
# driver.get("https://demoqa.com/droppable")
# time.sleep(15)
#
#
# draggable_ele = driver.find_element('xpath', '//div[text()="Drag Me"]')
# droppable_ele = driver.find_element('xpath', '//p[text()="Drop Here"]')
#
# ac.drag_and_drop(draggable_ele, droppable_ele).perform()

'''
Write a Selenium script to:
Open https://the-internet.herokuapp.com/javascript_alerts
Click JS Confirm
Accept the alert
Verify result text shows You clicked: Ok
'''
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
#
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(5)
#
# driver.find_element('xpath','//button[text()="Click for JS Confirm"]').click()
# time.sleep(2)
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# try:
#     wait_obj.until(EC.presence_of_element_located(('xpath', '//p[text()="You clicked: Ok"]')))
#     print("Clicked 'OK' ")
# except:
#     print("Invalid")

'''
Write a Selenium script that:
Open https://demowebshop.tricentis.com
Navigate to Books
Add all books priced below $20 to cart

'''
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com")
# driver.find_element('xpath', '//a[contains(text(),"Books")]').click()
# time.sleep(2)
# books = driver.find_elements('xpath', '//div[@class="item-box"]')
#
# for book in books:
#     price = book.find_element('xpath', './/span[@class="price actual-price"]').text
#     price = float(price.replace("$", ""))
#
#     if price < 20:
#         try:
#             button = book.find_element('xpath', './/input[@value="Add to cart"]')
#             button.click()
#             print("Added book with price:", price)
#             time.sleep(1)
#         except:
#             pass
#

'''
Write the steps to read the data from excel
'''
# import xlrd
#
# path = r'<absolute_path_of_file>.xlsx'
#
# # open the excel
# workbook = xlrd.open_workbook(path)
# # print(workbook)          ##book object
#
# ## open the worksheet
# worksheet = workbook.sheet_by_name('Sheet1')
# # print(worksheet)
#
# ## convert the sheet object to the generator object
# rows = worksheet.get_rows()
# #print(rows)
#
# #for ele in rows:
# #    print(ele)
#
# for ele in rows:
#     print(ele[0].value, ele[1].value, ele[2].value)


'''
Write the syntax for the xpath to locate the elements using
	*	attributes
	*	text
	*	group indexing
	*	contains
'''
'''

1. Using Attribute
Syntax:
//tagname[@attribute='value']

2. Using Text
Syntax:
//tagname[text()='text']

3. Using Group Indexing
Syntax:
(xpath)[index]

4. Using contains()
Syntax:
//tagname[contains(@attribute,'value')]
'''


'''
Write a Selenium script to:
Open https://the-internet.herokuapp.com/upload
Upload a file from local system
Click Upload
Verify uploaded file name.
'''
#
# from selenium import webdriver
# import time
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
#
# file = r'/Users/shubhranshuverma/Desktop/b.txt'
#
# driver.find_element('xpath', '//input[@id="file-upload"]').send_keys(file)
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="file-submit"]').click()

'''
Write a Selenium script to:
Open https://the-internet.herokuapp.com/download
Download any file
Verify the file is downloaded in the Downloads folder using Python.
'''

'''
Write a script to:
Open https://demowebshop.tricentis.com
Add any two products from Books
Navigate to Shopping Cart
Verify total number of products added is 2.
'''
