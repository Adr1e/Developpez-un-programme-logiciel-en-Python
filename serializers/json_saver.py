import json


def save_data(obj_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([obj.to_dict() for obj in obj_list], f, indent=4, ensure_ascii=False)


def load_data(filename, cls):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [cls.from_dict(item) for item in data]
