FROM python

WORKDIR /app

COPY . .

EXPOSE 7812

CMD ["python", "lab1.py", "methods.py"]