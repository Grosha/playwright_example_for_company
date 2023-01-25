# Test project for CV

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

Install python 3.9 via brew  ```$ brew install python@3.9```

### Installing

A step by step series of examples that tell you have to get a development env running

1. Go to the folder with project and install pipenv
    ```
    $ pip install pipenv
   ```

2. Proceed to project folder and install all needed dependencies
    ```
    $ pipenv install --dev
    ```

3. Activate pipenv
    ```
    $ pipenv shell
    ```
   
### Run UI tests:

1. Go to the project folder in terminal
2. Download playwright browsers :
    ```
    $ playwright install
    ```
3. Run command :
    ```
    $ pipenv run pytest tests
    ```
4. By default tests will run for chrome browser and if you want to add --browser type:
    ```
    $ pipenv run pytest tests --browser webkit
    ```
5. By default tests will run by one browser but if you want to parallelize it add number precesses:
    ```
    $ pipenv run pytest tests -n=2
    ```
6. If you want to look at the result via html reports, run this command
   ```
   $ pipenv run pytest tests -n=2 --browser webkit --html=report.html

   ```  

## Authors

Andrii Grom