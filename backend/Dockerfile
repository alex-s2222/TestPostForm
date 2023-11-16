FROM python:3.11

WORKDIR /backend
COPY . . 

# RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

ENV HOST=mongodb
ENV PORT=27017
ENV USER=root
ENV PASSWORD=rootpassword

EXPOSE 8080

CMD ["python", "app.py"]