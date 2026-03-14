from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(browser):

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox" :
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



######### HTML REPORT ##########

# def pytest_configure(config):
#     if hasattr(config, "_metadata"):
#         config._metadata["Project Name"] = "NOP COMMERCE"
#         config._metadata["Module"] = "LOGIN MODULE"
#         config._metadata["Tester"] = "PARTHIBAN C"


# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)



