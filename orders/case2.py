import driver

'''
Case 2: Add item to a box with multiple content and add the created box into the Order
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

driver.enter_field("item_input", "Automated Plastic")

driver.click_button("add_new_item")

driver.assert_element("changeMessage","Automated Plastic has been added.")

driver.quit_driver()


driver.start_page("administration", "Log In")
driver.login("admin")
driver.click_navibar("ordersNavButton")
driver.click_button("createOrder")

driver.enter_field("order_name", "Automated")
driver.enter_field("contact_name", "Automated Tester")
driver.enter_field("contact_email", "automated.tester@medivol.com")
driver.enter_field("organization_name", "MediVol")
driver.enter_field("organization_address", "Automated Testing Machine")
driver.click_button("same_as_business")

driver.click_button("create_order")

driver.click_button("create_box")

driver.select_item_search("Test Plastic")
driver.enter_field("count", "5")
driver.enter_field("expiration", "122020")
driver.click_button("add_item")
driver.assert_inventory_table("Plastic", "Other Plastics" ,"Test Plastic", "12/2020", "5", 1)

driver.select_item_column("Plastic", "Other Plastics" ,"Automated Plastic")
driver.enter_field("count", "10")
driver.click_button("add_item")
driver.assert_inventory_table("Plastic", "Other Plastics" ,"Automated Plastic", "Never", "10", 2)

driver.click_button("next")


driver.enter_field("initials", "ART")
driver.enter_field("weight", "12.6")
driver.click_button("small")

driver.click_button("submit")

driver.quit_driver()

driver.start_page("administration", "Log In")
driver.login("admin")
driver.click_navibar("ordersNavButton")


driver.enter_field_prince("10", 1)

driver.assert_element("totalPrice","10.00")

driver.click_button("submit")


driver.click_button("delete_order")

driver.warning_dialog("Are you sure you want to delete this order?", "delete_order")
driver.dialog_yes()

driver.quit_driver()

driver.start_page("administration", "Log In")
driver.login("admin")
driver.click_navibar("inventoryNavButton")

driver.select_item_column("Plastic", "Other Plastics" ,"Automated Plastic")
driver.assert_open_inventory_table("Small", "12.60", "Test Plastic x 5, Automated Plastic x 10", "December, 2020")
driver.open_box_in_inventory()

driver.click_button("delete_box")
driver.warning_dialog("Are you sure you want to delete this box?", "remove_box")
driver.dialog_yes()

driver.quit_driver()

driver.start_page("administration", "Log In")
driver.login("admin")
driver.click_navibar("catalogNavButton")

driver.select_item_column("Plastic", "Other Plastics" ,"Test Plastic")


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

driver.switch_tab()

driver.select_item_search("Automated Plastic")

driver.click_button("item_details")

driver.switch_tab()

driver.assert_element("itemNameValue", "Automated Plastic")
driver.assert_element("boxNameValue", "Other Plastics")
driver.assert_element("descriptionValue", "no description")

driver.click_button("editItem")

driver.click_button("deleteItem")

driver.warning_dialog("Are you sure you want to delete this item from the catalog?", "remove_item")

driver.dialog_yes()

driver.close_tab()

driver.quit_driver()




