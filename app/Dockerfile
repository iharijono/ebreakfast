FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /app/ui
RUN pip install -e .
# WORKDIR /app
# RUN chmod +x script.sh
# ENTRYPOINT ["./script.sh"]
# CMD ["tail", "-f", "/dev/null"]
CMD ["solara", "run", "ui.pages", "--host=0.0.0.0"]
