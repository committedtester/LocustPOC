LOCUST POC
To get up and running
- Install Python
- Run 'pip3 install locust'
- Confirm with 'locust -v'

Run the test via the website
locust -f starWarsApi/getData.py
http://localhost:8089/

Run the test as CI
locust -f starWarsApi/getData.py --headless --csv=example -t2m




