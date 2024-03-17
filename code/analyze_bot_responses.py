import os
import re
import logging
import json
import random
import time
import sqlite3

import pandas as pd
from dotenv import load_dotenv

load_dotenv('secrets.env')
BOT_DB_SQLITE = os.environ.get('BOT_DB_SQLITE')

conn = sqlite3.connect(BOT_DB_SQLITE)
cursor = conn.cursor()
cursor.execute("SELECT * FROM conversations")
conversations = cursor.fetchall()
cursor.close()
conn.close()      

conv = json.loads(conversations[0][2])
questions = []
for message in conv:
    if 'role' in message:
        if message['role'] == 'assistant':
            try:
                cont = json.loads(message['content'])
                if 'questions' in cont:
                    for q in cont['questions']: questions.append(q)
            except:
                logging.info(
                    f"message :'{message['content']}' failed to load as json"
                )
                continue

print(questions)