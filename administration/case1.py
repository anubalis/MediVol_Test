import driver

'''
General Case 1: Add 2 warehouses and remove 2 warehouses
'''


driver.start_page("administration", "Log In")
driver.login("admin")

driver.click_button("manageWarehousesButton")

driver.enter_field("warehouseName", "Warehouse1")
driver.enter_field("warehouseAbbreviation", "WRH1")
driver.enter_field("warehouseAddress", "123 ABC ST. Rochester, New York, 14623")
driver.click_button("addWarehouse")

driver.assert_warehouse_table("WRH1","Warehouse1", "123 ABC ST. Rochester, New York, 14623", 1)

driver.enter_field("warehouseName", "Warehouse2")
driver.enter_field("warehouseAbbreviation", "WRH2")
driver.enter_field("warehouseAddress", "123 ABC ST. Rochester, New York, 14623")
driver.click_button("addWarehouse")

driver.assert_warehouse_table("WRH2","Warehouse2", "123 ABC ST. Rochester, New York, 14623", 2)


#driver.quit_driver()

