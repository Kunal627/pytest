This is just a dummy package for pytest.

1) pytest ./testsuite.py  - for running the test cases
2) install coverage for code coverage 
   coverage run -m pytest ./testsuite.py
   coverage report -m 
   coverage html

Stand up a docker image of sonar cube 
3) Install Sonar scanner for windows 64 
4) set the sonar install dir/bin in syatem path
5) run sonar-scanner in the project base folder

go to localhost:9000  for sonar ui and use admin/admin creds