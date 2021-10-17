# install package in python virtualenvironment
python -m pip install .
sleep 0.5

# perform test execution
python -m unittest tests/test_git.py
