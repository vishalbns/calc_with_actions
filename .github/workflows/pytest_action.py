name: Testing with Pytest
on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests and generate XML report
      run: pytest --junitxml=pytest-report.xml
      continue-on-error: false

    - name: Upload test results
      if: always()
      uses: actions/upload-artifact@v2
      with:
        name: test-results
        path: pytest-report.xml

    - name: Notify on success
      if: success()
      run: echo "Tests passed successfully"

    - name: Notify on failure
      if: failure()
      run: echo "Tests failed"