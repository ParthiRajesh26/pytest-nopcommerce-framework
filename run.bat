rem pytest -s -v .\testCases\test_DDT_login.py --browser firefox

rem pytest -s -v ./testCases/test_login.py --browser chrome
rem pytest -s -v ./testCases/test_login.py --browser firefox
rem pytest -s -v ./testCases/test_DDT_login.py --browser chrome
rem pytest -s -v -m "sanity"
rem pytest -s -v -m "regression"
pytest -s -v -m "sanity and regression"


