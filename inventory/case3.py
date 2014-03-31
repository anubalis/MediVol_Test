import driver

'''
Case 3: Add 4 items with all permutation of count and expiration
'''

driver.start_page("inventory/create", "Box")

#No count, No expire
driver.select_item_column("Personal Care", "Oral Care" ,"Catheters")
driver.click_button("add_item")
driver.assert_inventory_table("Personal Care", "Oral Care" ,"Catheters", "Never", "No count", 1)

#No count, Yes expire
driver.select_item_column("Personal Care", "Oral Care" ,"Mouth Swabs")
driver.enter_field("expiration", "122020")
driver.click_button("add_item")
driver.assert_inventory_table("Personal Care", "Oral Care" ,"Mouth Swabs", "12/2020", "No count", 2)

#Yes count, No expire
driver.select_item_column("Personal Care", "Oral Care" ,"Suction Swabs")
driver.enter_field("count", "5")
driver.click_button("add_item")
driver.assert_inventory_table("Personal Care", "Oral Care" ,"Suction Swabs", "Never", "5", 3)

#Yes count, Yes expire
driver.select_item_column("Personal Care", "Oral Care" ,"Suction Tubing")
driver.enter_field("count", "5")
driver.enter_field("expiration", "122020")
driver.click_button("add_item")
driver.assert_inventory_table("Personal Care", "Oral Care" ,"Suction Tubing", "12/2020", "5", 4)

driver.click_button("next")


driver.quit_driver()

