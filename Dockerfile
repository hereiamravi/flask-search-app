# use the official python image as the base
FROM python:latest

# set the working directory to /app
WORKDIR /app

# copy the requirements.txt file to the working directory
COPY requirements.txt ./

# install the dependencies
RUN pip install -r requirements.txt

# copy the rest of the app files to the working directory
COPY . .

# set the environment variable for flask app
ENV FLASK_APP=app.py
ENV AUTH_KEY=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

# expose port 5000 for flask app
EXPOSE 5000

# run the app
CMD ["flask", "run", "--host=0.0.0.0"]
