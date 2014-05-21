import driver

'''
Case 2: Create new item with duplicate name
'''

driver.start_page("administration", "Log In")
driver.login("admin")
driver.click_navibar("catalogNavButton")

driver.assert_element("boxNameField","choose a box name above")
driver.select_item_column("Plastic", "Other Plastics" ,"Funnel")
driver.assert_element("boxNameField","Other Plastics")

driver.enter_field("item_input", "Test Plastic")

driver.click_button("add_new_item")

driver.assert_element("changeMessage","Test Plastic has been added.")

driver.enter_field("item_input", "Test Plastic")

driver.click_button("add_new_item")

driver.assert_element("changeMessage","Item \"Test Plastic\" already exists")

driver.quit_driver()

driver.start_page("administration", "Log In")
driver.login("admin")
driver.click_navibar("catalogNavButton")

driver.select_item_search("Test Plastic")

driver.click_button("item_details")

driver.switch_tab()

driver.assert_element("itemNameValue", "Test Plastic")
driver.assert_element("boxNameValue", "Other Plastics")
driver.assert_element("descriptionValue", "no description")

driver.click_button("editItem")

driver.click_button("deleteItem")

driver.warning_dialog("Are you sure you want to delete this item from the catalog?", "remove_item")

driver.dialog_yes()

driver.close_tab()

driver.quit_driver()

