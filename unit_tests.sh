docker build -t putt_tracker:test .

docker run -it putt_tracker:test python3 /tmp/unit_tests.py
