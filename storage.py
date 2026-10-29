"""Penyimpanan data tiket ke file JSON."""

import json
import os
import random
import string
from datetime import datetime

DB_FILE = "tiket_kampus.json"


def muat_tiket():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def simpan_tiket(tiket):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(tiket, f, indent=2, ensure_ascii=False)


def buat_id():
    acak = "".join(random.choices(string.digits, k=5))
    return f"HD-{datetime.now():%y%m%d}-{acak}"