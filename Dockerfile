# Use an official lightweight Python image.
# Python is used here for scripting. You can use other images like Node or even just Bash.
FROM python:3.8-slim

# Install Vault
RUN apt-get update && apt-get install -y curl jq \
    && curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - \
    && apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
    && apt-get update && apt-get install vault

# Copy the script that fetches secrets
COPY fetch_secrets.py /fetch_secrets.py

# This is the script that will be run by the container
ENTRYPOINT ["python", "/fetch_secrets.py"]
