To install required packages run below command
   pip install -r requirements.txt

To Run Test Suite run below command
    Syntax--> pytest -v -s <suitename> --browser <browser name>(if browser is not given it will default take chrome browser.)
    Exp--> py.test -v -s testCases/test_login.py --browser chrome

To run test in parallel use below command
    Syntax--> py.test -v -s -n <no of browser instances(i.e. 1,2,3)> <suitename> --browser <browser name>
     Exp--> py.test -v -s -n 2 testCases/test_login.py --browser chrome
 
TO run test and generate pytest HTML Report   
    Syntax--> pytest -v -s <suitename> --html=<path> --browser browsername
    Exp--> pytest -v -s testCases/test_login.py --html=Reports//report.html --browser chrome