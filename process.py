#!/usr/bin/env python3

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
    processed_data = {
    }

    for date, time, n in data:
        if init:
            init = False
            print(f"Running analysis for {date}")
            processed_data["day"] = date
            processed_data["check_time"] = []
            processed_data["check_dura"] = []
            prev_time = time
        if not init:
            if processed_data["day"] != date:
                sys.exit("date changed through log, check the files")
            time_diff = datetime.strptime(time, "%H:%M:%S")-datetime.strptime(prev_time, "%H:%M:%S")
            print(f"Check fom: {time}, runtime: {time_diff}")
            processed_data["check_time"].append(time)
            processed_data["check_dura"].append(time_diff)
            prev_time = time

def process(data: list[str]) -> list[str]:
    scraped_data_set = []
    for record in data:
        scraped_data_set.append(scrape_data(record))
    for proc_dat_set in scraped_data_set:
        return process_data(proc_dat_set)

if __name__ == "__main__":
    from utils.utils import read_files
    d_data = read_files(sys.argv[1:])
    print(process(d_data))