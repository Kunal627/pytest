This is just a dummy repo for exploring pytest and sonarqube
=============================================================

1) pytest ./testsuite.py  - for running the test cases
2) install coverage for code coverage 
   coverage run -m pytest ./testsuite.py
   coverage report -m 
   coverage html

3) Stand up a docker image of sonar cube 
4) Install Sonar scanner for windows 64 
5) set the sonar install dir/bin in syatem path
6) run sonar-scanner in the project base folder

7) go to localhost:9000  for sonar ui and use admin/admin creds