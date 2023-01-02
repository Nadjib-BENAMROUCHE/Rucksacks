FROM python:3.8.10
#here the dockerfile is pulling the python 3.8 from docker hub

COPY test.py .
COPY input.txt .
# Here we added the python file and  the input file


RUN pip install datetime
RUN pip install psycopg2
# Here we installed the dependencies
# We can also freeze python file in requirments.txt and do : RUN pip install -r requirments.txt 


CMD [ "python3", "test.py", "input.txt"]
# Lastly we specified the entry command 