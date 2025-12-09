#!/bin/bash

/usr/local/bin/ngrok http --domain=willing-just-penguin.ngrok-free.app 8080 &
/usr/bin/python3 /home/aron/AI-n8n-website/backend/api.py &