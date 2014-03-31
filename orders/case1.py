import driver

'''
Case 1: Add item to a box with single content and add the created book into the Order
'''


driver.start_page("inventory/create", "Box")

driver.select_item_search("Irrigation Tray")
driver.enter_field("count", "5")
driver.enter_field("expiration", "12012020")
driver.click_button("add_item")
driver.assert_inventory_table("Cautery", "Irrigation" ,"Irrigation Tray", "12/01/2020", "5", 1)

driver.click_button("next")

driver.enter_field("initials", "ART")
driver.enter_field("weight", "11.1")
driver.click_button("small")

driver.click_button("submit")

driver.quit_driver()


driver.start_page("orders/create", "Orders")


driver.select_box_column("Cautery", "Irrigation" ,"Irrigation Tray")
driver.assert_box_infomation("boxDetails", "Small", "11.10", "Irrigation Tray x 5", "12/01/2020")
driver.click_button("add_box")
#driver.assert_orders_table("", "Small" ,"11.10", 1)

driver.click_button("next")

driver.quit_driver()



