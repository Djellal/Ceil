#!/bin/bash

source /home/djellal/workspace/Ceil/venv/bin/activate
cd /home/djellal/workspace/Ceil/
python manage.py collectstatic
cp -r /home/djellal/workspace/Ceil/* /var/www/CeilUfas/