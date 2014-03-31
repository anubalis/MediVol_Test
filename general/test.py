import driver


driver.start_page("inventory/create", "Box")

driver.select_item_search("Bottles")
driver.enter_field("count", "5")
#driver.enter_field("expiration", "122020")
driver.enter_field("expiration", "012020")
#driver.click_button("add_item")
#driver.assert_inventory_table("Dressings", "Wound Care" ,"Bottles", "12/01/2020", "5", 1)


