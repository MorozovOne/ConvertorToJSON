import os
import json



def parse_netscape_cookie_line(line):
    fields = line.strip().split('\t')
    if len(fields) != 7:
        return None

    cookie = {
        "domain": fields[0],
        "flag": fields[1] == "TRUE",
        "path": fields[2],
        "secure": fields[3] == "TRUE",
        "expiration": int(fields[4]),
        "name": fields[5],
        "value": fields[6]
    }
    return cookie



def convert_netscape_to_json(netscape_file, json_file):
    cookies = []
    with open(netscape_file, 'r') as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            cookie = parse_netscape_cookie_line(line)
            if cookie:
                cookies.append(cookie)


    with open(json_file, 'w') as f:
        json.dump(cookies, f, indent=4)



def process_all_cookie_files(input_directory, output_directory):

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)


    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_name = f"{os.path.splitext(filename)[0]}.json"
            output_file_path = os.path.join(output_directory, output_file_name)


            convert_netscape_to_json(input_file_path, output_file_path)
            print(f"Обработан файл: {input_file_path}, сохранен как: {output_file_path}")


# Вот здесь поменяй полный путь на тот где ты сохранил проект, до папки cooks
input_directory = r'C:\Users\Вот здесь укажи полный путь до папки cooks'  # Директория с текстовыми файлами cookies
output_directory = r'C:\Users\Вот здесь укажи полный путь до папки CooksJSON'  # Директория для сохранения JSON файлов

# Запускаем обработку всех файлов
process_all_cookie_files(input_directory, output_directory)
