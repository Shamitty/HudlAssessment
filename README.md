# Python-HudlProject

## Prerequisites

1. Install a code editor of your choice VSCode or Pycharm

```
https://code.visualstudio.com/download
```

2. Next we need to download Python and Pip

```
Python download: https://www.python.org/downloads/ 
py -m ensurepip --upgrade
```

## Steps to Run your First Test

Step 1. Clone the HudlProject Selenium Repository.

```
git clone https://github.com/Shamitty/HudlAssessment
```

Step 2. Download Chromedriver. You will download the version of your Chrome Instance.
```
https://chromedriver.chromium.org/downloads
```
<b>Where you downloaded your chromedriver instance, that is where you'll need to specify in the code on line 19 of HudlLoginSteps</b>
```
 context.driver = webdriver.Chrome("<Change it here>")
```

Step 3. Close and reopen terminal to have pip take effect. Then install required packages.

```
pip install -r requirements.txt
```

Step 3.  Close and reopen terminal to have requirements take effect. Inside the HudlProject folder, put your credentials in the .env file. This will allow you to login to Hudl

<p align="center">
   <b>For Windows:</b>
   
```
.env
USER=<Some email>
PASS=<Some password>
```

Step 4. Running tests via terminal or command line

##### Running with tags
```
behave -f allure_behave.formatter:AllureFormatter -o "C:\Git\PythonScripts\HudlProject\TestReports" --tags="hudlLogin"
```

##### Running all test cases
```
behave -f allure_behave.formatter:AllureFormatter -o "C:\Git\PythonScripts\HudlProject\TestReports"
```

##### See html reports
```
allure serve "C:\Git\PythonScripts\HudlProject\TestReports"
```
 <b>You may have to install allure manually or add it to your system path variables</b>
 <p align="center">
  <b>For Mac:</b>
  ```brew install allure
  ```

