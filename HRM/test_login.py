import time

from playwright.sync_api import Page, Playwright, expect


def test_loginpage(browserInstance):
    page = browserInstance



    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name = "Login").click()


    page.locator("a.oxd-main-menu-item", has_text="Admin").click()

    # page.locator(
    #     "//label[normalize-space()='Username']/ancestor::div[contains(@class, 'oxd-input-group')]//input").fill("Admin")

    page.locator("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").fill("Admin") #selector hub

    #check the profi pic whether it is visible or not
    profile = page.get_by_alt_text("profile picture")
    expect(profile).to_be_visible()
    time.sleep(7)

    #check with text
    expect(page.get_by_role("heading", name="User Management")).to_be_visible()
    #




    # Step 1: Open the dropdown (User Role)
    page.locator("div.oxd-select-text").nth(0).click()

    # Step 2: Click the ESS option (appears only after dropdown is open)
    page.locator("div.oxd-select-option").filter(has_text="ESS").click()

    # Step 3: Verify ESS is displayed in the input box

    expect(page.locator("div.oxd-select-text-input").nth(0)).to_have_text("ESS")

    page.get_by_placeholder("Type for hints...").fill("Andrew osama Hisham")

    # Open the Status dropdown and select Enabled.
    page.locator("div.oxd-select-text").nth(1).click()
    page.locator("div.oxd-select-option").filter(has_text="Enabled").click()

    expect(page.locator("div.oxd-select-text-input").nth(1)).to_have_text("Enabled")

    











