FROM python:3.6

COPY . /cuenca_queens
WORKDIR /cuenca_queens

RUN pip install -r requirements.txt

Expose 3000

CMD ["python3", "./nqueens/queens.py"]
