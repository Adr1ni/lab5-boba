FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD python hello_ipython.py && python hello_requests.py && python hello_geopy.py && python hello_argparse.py && python hello_re.py && python hello_river.py && python hello_scipy.py
