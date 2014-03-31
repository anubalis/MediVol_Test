import driver

'''
General Case 1: Items, Box names, and categories are in the system
'''

driver.start_page("inventory/create", "Box")

driver.quit_driver()

driver.start_page("orders/create", "Orders")

driver.quit_driver()

driver.start_page("administration", "Log In")
driver.login("admin")

driver.click_button("manageUsersButton")
driver.click_navibar("administrationNavButton")

driver.click_button("manageBackupsButton")
driver.click_navibar("administrationNavButton")

driver.click_button("manageWarehousesButton")
driver.click_navibar("administrationNavButton")

driver.click_navibar("settingsNavButton")

driver.click_navibar("catalogNavButton")


driver.quit_driver()

