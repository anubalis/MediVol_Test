import time, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  


def timestamp():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	return "[" + str(st) + "] "
	
def start_page(address, title):

	chromedriver = "./chromedriver"
	driver1 = webdriver.Chrome(chromedriver)
	
	driver1.get("http://localhost:8888/" + address +"/")
	#driver1.get("http://107.161.21.242/" + address +"/")
	print timestamp() + "Opening " + address
	assert title in driver1.title
	
	time.sleep(0.5)
	
	global driver 
	driver = driver1
	
	#assert_element("itemSelectedMessage", "Please select an item.")


def select_item_column(categories, boxname, item):
	
	elem = driver.find_element_by_id("categories")
	send_keys(categories, elem)
	time.sleep(0.2)
	elem.send_keys(Keys.ARROW_UP)
	time.sleep(0.2)
	elem.send_keys(Keys.ARROW_DOWN)
	time.sleep(1)
	
	'''
	elem = driver.find_elements_by_xpath("//option")
	for count in range(0,len(elem)):
	    if elem[count].text == categories:
	        categeory = driver.find_element_by_xpath("//*[@id=\"categories\"]/option["+ str(count + 1)+"]")
	        categeory.click
	'''         
	
	elem = driver.find_element_by_id("box_names")
	send_keys(boxname, elem)
	time.sleep(1)
	
	elem = driver.find_element_by_id("items")
	send_keys(item, elem)
	time.sleep(1)
   	
   	'''if(check_exists_by_id("itemSelectedMessage") == True):
   		elem = driver.find_element_by_id("itemSelectedMessage")
		selectedItem = elem.text
		selectedItem = selectedItem.replace("You have selected:\n", "")
		print timestamp() + "\tElement: itemSelectedMessage"
		print timestamp() + "\t\tActual:   " +  selectedItem + "\n" + timestamp() + "\t\tExpected: " + item 
		assert selectedItem.upper() == item.upper()'''
		

def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def select_item_search(item):
	
	elem = driver.find_element_by_id("itemSearch")
	send_keys(item, elem)
	time.sleep(1.5)
	elem.send_keys(Keys.ARROW_DOWN)
	time.sleep(0.1)
	elem.send_keys(Keys.ARROW_UP)
	time.sleep(0.1)
	elem.send_keys(Keys.RETURN)
	time.sleep(0.1)	
	
	'''if(check_exists_by_id("itemSelectedMessage") == True):
		elem = driver.find_element_by_id("itemSelectedMessage")
		selectedItem = elem.text
		selectedItem = selectedItem.replace("You have selected:\n", "")
		print timestamp() + "\tElement: itemSelectedMessage"
		print timestamp() + "\t\tActual:   " +  selectedItem + "\n" + timestamp() + "\t\tExpected: " + item 
		assert selectedItem.upper() == item.upper()'''

def enter_field(fieldID, content):
	elem = driver.find_element_by_id(fieldID)
	if(fieldID != "expiration"):
		elem.send_keys(content)
	elif(fieldID == "expiration"):
		month = content[0:2]
		year = content[2:6]
		
		elem.send_keys(month)
		elem.send_keys(Keys.TAB)
		elem.send_keys(year)
		
def enter_field_prince(price, row):
	row = row + 1
	elem = driver.find_element_by_xpath("//*[@id=\"boxes_added\"]/tbody/tr[" + str(row) + "]/td[4]/input")
	elem.send_keys(price)
	
	
def click_button(buttonID):
	time.sleep(0.5)
	if (buttonID == "create_order"):
		elem = driver.find_element_by_xpath("//*[@id=\"stepOne\"]/input")
	elif (buttonID == "delete_order"):
		elem = driver.find_element_by_xpath("//*[@id=\"orderInfoLeft\"]/button")
	else:
		elem = driver.find_element_by_id(buttonID)
	
	elem.click()
	time.sleep(0.5)
	
def assert_inventory_table(categories, boxname, item, expiration, count, row):
	row = row + 1
	elem = driver.find_element_by_xpath("//*[@id=\"items_added\"]/tbody/tr[" + str(row) + "]")
	selectedRow = elem.text
	selectedRow = selectedRow.replace("Remove", "")
	selectedRow = selectedRow.strip()
	assertion = categories + " " + boxname + " " + item + " " + expiration + " " + count
	print timestamp() + "\tElement: items_added"
	print timestamp() + "\t\tActual:   " +  selectedRow + "\n" + timestamp() + "\t\tExpected: " + assertion
	assert selectedRow.upper() == assertion.upper()

def assert_open_inventory_table(size, weight, content, expiration):

	elem = driver.find_element_by_xpath("//*[@id=\"boxes_body\"]/tr")
	actual =  elem.text
	
	assertion = size + " " + weight + " lbs " + content + " " + expiration
	
	print timestamp() + "\tElement: boxes_body"
	print timestamp() + "\t\tActual:   " +  actual + "\n" + timestamp() + "\t\tExpected: " + assertion
	
	if assertion not in actual:
		assert True == False
		
def open_box_in_inventory():
	elem = driver.find_element_by_xpath("//*[@id=\"boxes_body\"]/tr/td[2]/a")
	elem.click()

def add_box_in_order():
	elem = driver.find_element_by_xpath("//*[@id=\"boxes_body\"]/tr/td[8]/input")
	elem.click()
	

def assert_orders_table(boxID, size, weight, row):
	if (boxID == ""):
		elem = driver.find_element_by_id("boxes")
		elem = driver.find_element_by_xpath("//*[@id=\"boxes\"]/option[1]")
		boxID = elem.text
		
	row = row + 1
	elem = driver.find_element_by_xpath("//*[@id=\"boxes_added\"]/tbody/tr[" + str(row) + "]")
	selectedRow = elem.text
	selectedRow = selectedRow.replace("Remove", "")
	selectedRow = selectedRow.strip()
	assertion = boxID + " " + size + " " + weight
	print timestamp() + "\tElement: boxes_added"
	print timestamp() + "\t\tActual:   " +  selectedRow + "\n" + timestamp() + "\t\tExpected: " + assertion
	assert selectedRow.upper() == assertion.upper()
	
def assert_warehouse_table(Abbreviation, Name, Address, row):
	
	row = row + 1
	elem = driver.find_element_by_xpath("//*[@id=\"warehouses\"]/table/tbody/tr[" + str(row) + "]")
	selectedRow = elem.text
	selectedRow = selectedRow.replace("Remove", "")
	selectedRow = selectedRow.replace("Set Default", "")
	selectedRow = selectedRow.strip()
	assertion = Abbreviation + " " + Name + " " + Address
	print timestamp() + "\tElement: warehouses"
	print timestamp() + "\t\tActual:   " +  selectedRow + "\n" + timestamp() + "\t\tExpected: " + assertion
	assert selectedRow.upper() == assertion.upper()

def select_box_column(categories, boxname, item):
	
	elem = driver.find_element_by_id("categories")
	send_keys(categories, elem)
	time.sleep(1)     
	
	elem = driver.find_element_by_id("box_names")
	send_keys(boxname, elem)
	time.sleep(1)
	
	elem = driver.find_element_by_id("items")
	send_keys(item, elem)
	time.sleep(1)

	elem = driver.find_element_by_id("boxes")
	time.sleep(1)
	
	elem = driver.find_element_by_xpath("//*[@id=\"boxes\"]/option[1]")
	boxID = elem.text
	elem = driver.find_element_by_id("boxes")
	elem.send_keys(boxID)
	
	
def quit_driver():
	driver.quit()
	
def log(message):
	print timestamp() + message

def assert_element(element, expected):
	time.sleep(0.5)
	elem = driver.find_element_by_id(element)
	elem = elem.text.strip()
	print timestamp() + "\tElement: " + element
	print timestamp() + "\t\tActual:   " +  elem.replace("\n", " ") + "\n" + timestamp() + "\t\tExpected: " + expected.replace("\n", " ")
	assert elem.upper() == expected.upper()
	
def assert_box_infomation(element, Size, Weight, Contents, Expires):
	time.sleep(0.5)
	elem = driver.find_element_by_id(element)
	actual = elem.text.replace("\n", " ")
	expected = "Size " + Size + " Weight " + Weight + " lbs Contents " + Contents + " Expires " + Expires
	print timestamp() + "\tElement: " + element
	print timestamp() + "\t\tActual:   " +  actual + "\n" + timestamp() + "\t\tExpected: " + expected
	assert actual.upper() == expected.upper()

def send_keys(text, elem):
	keysList = list(text)
	for key in keysList:
		elem.send_keys(key)
		time.sleep(0.1)
		
def login(role):
	user = ""
	pwd = ""
	if(role == "admin"):
		user = "root"
		pwd = "root"
	elif(role == "boxtransfer"):
		user = "boxtransfer"
		pwd = "boxtransfer"
	elif(role == "guest"):
		user = "guest"
		pwd = "guest"
	elif(role == "readonly"):
		user = "readonly"
		pwd = "readonly"
	
	print timestamp() + "Login as " + role
	enter_field("id_username", user)
	enter_field("id_password", pwd)
	
	time.sleep(0.5)
	elem = driver.find_element_by_xpath("//*[@id=\"loginWrapper\"]/form/input[3]")
	elem.click()
	time.sleep(0.5)
	
def click_navibar(ID):
	elem = driver.find_element_by_xpath("//*[@id=\""+ ID +"\"]/li")
	elem.click()
	
def switch_tab():
	driver.switch_to_window(driver.window_handles[-1])
	
def close_tab():
	driver.close()

def warning_dialog(expected, dialog):
	time.sleep(1)
	elem = ""
	
	if (dialog == "remove_item"):
		elem = driver.find_element_by_xpath("//*[@id=\"ui-id-2\"]/tbody/tr/td")
	elif(dialog == "remove_warehouse"):
		elem = driver.find_element_by_xpath("//*[@id=\"ui-id-1\"]/tbody/tr/td")
	elif(dialog == "remove_box"):
		elem = driver.find_element_by_xpath("//*[@id=\"ui-id-1\"]/tbody/tr/td")
	elif(dialog == "delete_order"):
		elem = driver.find_element_by_xpath("//*[@id=\"ui-id-1\"]/tbody/tr/td")
	
	elem = elem.text.strip()
	print timestamp() + "\tElement: Dialog message"
	print timestamp() + "\t\tActual:   " +  elem.replace("\n", " ") + "\n" + timestamp() + "\t\tExpected: " + expected.replace("\n", " ")
	assert elem.upper() == expected.upper()

def dialog_yes():
	elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/button[1]")
	elem.click()

def remove_from_table(row, table):
	elem = ""
	row = row +1
	if (table == "warehouse"):
		elem = driver.find_element_by_xpath("//*[@id=\"warehouses\"]/table/tbody/tr[" + str(row) + "]/td[5]/a")
	elem.click()

def logout():
	elem = driver.find_element_by_xpath("//*[@id=\"logoutWrapper\"]/a")
	elem.click()

	
