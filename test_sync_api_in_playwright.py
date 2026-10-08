# Nature of programming language - Sync and Async.
# Sync - It will start the second task only when the first task is complete. Basically, execution of task will wait for completion.

from playwright.sync_api import Page, expect

def test_verifyPageUrl(page:Page):
    page.goto("https://www.nopcommerce.com/en")
    myUrl = page.url
    print("URL of the Application: ", myUrl)

    expect(page).to_have_url("https://www.nopcommerce.com/en")


def test_verifyPageTitle(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    myTitle = page.title()
    print("Title of the page: ", myTitle)
    expect(page).to_have_title("Automation Testing Practice")
