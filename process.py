import sys, re


DATA_MASK = r".*(\d{4}-\d{2}-\d{2})\s*(\d{2}:\d{2}:\d{2})\s*-* Check \#(\d{1,5}) -*"
data_expression = re.compile(DATA_MASK)

def scrape_data(data: str) -> list[str]:
    return data_expression.findall(data)

def process(data: list[str]) -> list[str]:
    processed_data = []
    for record in data:
        processed_data.append(scrape_data(record))
    return processed_data

if __name__ == "__main__":
    from utils.utils import read_files
    d_data = read_files(sys.argv[1:])
    print(process(d_data))