import driver

'''
General Case 3: Items, Box names, and categories are in the system
'''

driver.start_page("administration", "Log In")
driver.login("admin")
driver.click_navibar("inventoryNavButton")
driver.click_button("createNewBox")

driver.select_item_column("Mother and Child", "Pediatric Supplies" ,"Breathing Circuits")
driver.enter_field("count", "10")
driver.click_button("add_item")
driver.assert_inventory_table("Mother and Child", "Pediatric Supplies" ,"Breathing Circuits", "Never", "10", 1)


driver.quit_driver()

