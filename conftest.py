import os
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium", help="browser selection")

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    os.makedirs("test-results", exist_ok=True)
    context.tracing.stop(path=f"test-results/trace_{request.node.name}.zip")

    context.close()
    browser.close()
