import json
def task() -> float:
    file_name = 'input.json'
    sum_ = 0
    with open(file_name) as f:
        json_data = json.load(f)
    for item in json_data:
        sum_ += item['score'] * item['weight']
    return round(sum_, 3)


print(task())
