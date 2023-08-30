
#!/bin/bash

#activate virtual environment
source env/bin/activate

#run test
pytest test_app.py

# Capture the exit code of the pytest command
exit_code=$?

# Wrap the code

if [exit_code -eq 0]:
then
echo "Passed"
else
echo "Failed"

exit $exit_code

#to run on bash:
#$ chmod +x test.sh
#./test.sh
