pytest tests.py > result.txt

echo Result writed to result.txt

echo Start creating report process

pytest --cov=. tests.py --cov-report html

echo Coverage report created in htmlcov\/