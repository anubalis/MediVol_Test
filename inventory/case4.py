import driver

'''
Case 4: Creating a box without entering the required field would fail
'''

driver.start_page("inventory/create", "Box")

#No count, No expire
driver.select_item_column("Personal Care", "Oral Care" ,"Catheters")
driver.click_button("add_item")
driver.assert_inventory_table("Personal Care", "Oral Care" ,"Catheters", "Never", "No count", 1)

driver.click_button("next")

driver.click_button("submit")

driver.assert_element("requiredFieldsMessage","Please fill out the required fields.")


driver.quit_driver()

