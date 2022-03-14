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

Step 2. Close and reopen terminal to have pip take effect. Then install required packages.

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

