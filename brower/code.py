from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click text=吴谢宇庭审过程实录首次曝光
    with page.expect_popup() as popup_info:
        page.click("text=吴谢宇庭审过程实录首次曝光")
    page2 = popup_info.value

    # Click [id="9"] >> text=吴谢宇庭审过程实录首次曝光
    # with page2.expect_navigation(url="http://www.cangchou.com/10759.html"):
    with page2.expect_navigation():
        with page2.expect_popup() as popup_info:
            page2.click("[id=\"9\"] >> text=吴谢宇庭审过程实录首次曝光")
        page3 = popup_info.value

    # Close page
    page3.close()

    # Close page
    page2.close()

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
