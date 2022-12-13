#!/usr/bin/env python3
'''
Processes data to return dicts for visualisation
'''

import sys
import re

from datetime import datetime

DATA_MASK = r".*(\d{4}-\d{2}-\d{2})\s*(\d{2}:\d{2}:\d{2})\s*-* Check \#(\d{1,5}) -*"
data_expression = re.compile(DATA_MASK)

def scrape_data(data: str) -> list[str]:
    """get list of fields from text input"""
    return data_expression.findall(data)

def process_data(data: list[str]) -> dict:
    """loops over list of gathered data and returns a more structured form"""
    init = True
    processed_data = { }

    for date, time, n in data:
        if not init:
            if processed_data["day"] != date:
                sys.exit("date changed through log, check the files")
            time_diff = datetime.strptime(time, "%H:%M:%S")-datetime.strptime(prev_time, "%H:%M:%S")
            processed_data["check_time"].append(prev_time)
            processed_data["check_dura"].append(time_diff)
            prev_time = time
        if init:
            init = False
            processed_data["day"] = date
            processed_data["check_time"] = []
            processed_data["check_dura"] = []
            prev_time = time
    return processed_data

def process(data: list[str]) -> list[str]:
    """performs calcuations on passed data"""
    scraped_data_set = []
    processed_data_set = []
    for record in data:
        scraped_data_set.append(scrape_data(record))
    for scraped_data in scraped_data_set:
        processed_data_set.append(process_data(scraped_data))
    return processed_data_set

if __name__ == "__main__":
    import utils
    d_data = utils.read_files(sys.argv[1:])
    result = (process(d_data))

    for res_rec in result:
        if "day" not in res_rec.keys():
            print("caution! file had no usable data")
        else:
            utils.write_to_txt(res_rec)
