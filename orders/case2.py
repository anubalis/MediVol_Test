import driver

'''
Case 2: Add item to a box with multiple content and add the created box into the Order
'''


driver.start_page("inventory/create", "Box")

driver.select_item_search("Bottles")
driver.enter_field("count", "5")
driver.enter_field("expiration", "12012020")
driver.click_button("add_item")
driver.assert_inventory_table("Dressings", "Wound Care" ,"Bottles", "12/01/2020", "5", 1)

driver.select_item_column("Dressing", "Wound Care" ,"Unna Pack")
driver.enter_field("count", "5")
driver.enter_field("expiration", "12012020")
driver.click_button("add_item")
driver.assert_inventory_table("Dressings", "Wound Care" ,"Unna Pack", "12/01/2020", "5", 2)

driver.click_button("next")

driver.enter_field("initials", "ART")
driver.enter_field("weight", "18.1")
driver.click_button("large")

driver.click_button("submit")

driver.quit_driver()


driver.start_page("orders/create", "Orders")


driver.select_box_column("Dressing", "Wound Care" ,"Unna Pack")
driver.assert_box_infomation("boxDetails", "Large", "18.10", "Bottles x 5, Unna Pack x 5", "12/01/2020")
driver.click_button("add_box")
#driver.assert_orders_table("", "Large" ,"18.10", 1)

driver.click_button("next")

driver.quit_driver()




