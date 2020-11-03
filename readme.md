LOCUST POC
To get up and running
- Install Python
- Run 'pip3 install locust'
- Confirm with 'locust -v'

Run the test via the website
locust -f starWarsApi/getData.py
http://localhost:8089/

Run the test with a minimum number of requests for debug
locust -f starWarsApi/getData.py --headless --csv=example --run-time=10s




