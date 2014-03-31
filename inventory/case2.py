import driver

'''
Inventory Case 2: Check for error message going to the next step with no items in the box
'''

driver.start_page("inventory/create", "Box")


driver.click_button("next")
driver.assert_element("emptyBoxMessage","Cannot create an empty box.")


driver.quit_driver()
