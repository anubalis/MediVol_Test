import driver

'''
General Case 1: Items, Box names, and categories are in the system
'''

driver.start_page("administration", "Log In")
driver.login("admin")

driver.click_navibar("administrationNavButton")

driver.click_button("manageUsersButton")
driver.click_navibar("administrationNavButton")

driver.click_button("manageBackupsButton")
driver.click_navibar("administrationNavButton")

driver.click_button("manageWarehousesButton")
driver.click_navibar("administrationNavButton")

driver.click_button("manageCategoriesButton")
driver.click_navibar("administrationNavButton")

driver.click_button("manageBoxNamesButton")
driver.click_navibar("administrationNavButton")

driver.click_navibar("settingsNavButton")

driver.click_navibar("catalogNavButton")

driver.click_navibar("inventoryNavButton")

driver.click_button("createNewBox")
driver.click_navibar("inventoryNavButton")

driver.click_button("boxTransfer")
driver.click_navibar("inventoryNavButton")

driver.click_navibar("ordersNavButton")

driver.click_button("createOrder")
driver.click_navibar("ordersNavButton")

driver.quit_driver()

