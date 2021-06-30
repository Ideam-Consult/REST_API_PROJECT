FROM python

#set woriking directory in the container
WORKDIR /code

#copy the dependencies file to the working directory
COPY requirements.txt .

#install dependencies
RUN pip install -r requirements.txt

COPY src/ .
ENTRYPOINT ["python"]
CMD ["app.py"]