import driver

'''
Case 1: Add 2 times using both options and create the box
'''

driver.start_page("inventory/create", "Box")

driver.select_item_search("Mouth Swabs")
driver.enter_field("count", "5")
driver.enter_field("expiration", "12012020")
driver.click_button("add_item")
driver.assert_inventory_table("Personal Care", "Oral Care" ,"Mouth Swabs", "12/01/2020", "5", 1)

driver.select_item_column("Mother and Child", "Pediatric Supplies" ,"Breathing Circuits")
driver.enter_field("count", "10")
driver.click_button("add_item")
driver.assert_inventory_table("Mother and Child", "Pediatric Supplies" ,"Breathing Circuits", "Never", "10", 2)

driver.click_button("next")

driver.enter_field("initials", "ART")
driver.enter_field("weight", "12.6")
driver.click_button("small")

driver.click_button("submit")


driver.quit_driver()

