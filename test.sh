# install package in python virtualenvironment
python setup.py install
sleep 0.5

# perform test execution
python -m unittest tests/test_git.py
