import re

dataset = "labeled_data.csv"

def joint_text():
    with open(dataset, "r", encoding="utf-8") as file:
        # Skip the header 
        file.readline()
        data = []

        prev_line = ""
        for line in file:
            id = line.split(",")[0]
            
            is_valid_id = False
            try:
                int(id.strip())
                is_valid_id = True
            except:
                continue

            if (is_valid_id):
                data.append(prev_line)
                prev_line = line
            else:
                prev_line += line.strip()

        with open("dataset_clean.csv", "w", encoding="utf-8") as file:
            for line in data:
                file.write(line)

def standarize():
    with open("dataset_clean.csv", "r", encoding="utf-8") as file:
        # Skip the header 
        file.readline()

        data = []
        for line in file:
            text = line.split(",")[6:]
            ln = line.split(",")[:6]
            text_join = ",".join(text)
            strip = text_join.strip("\"").strip()
            fmt = strip.replace('"', '""').replace("'", "''")
            fmt = f"\"{fmt}\""
            ln.append(fmt)
            data.append(",".join(ln))

        with open("dataset_clean_v2.csv", "w", encoding="utf-8") as file:
            for line in data:
                file.write(f"{line}\n")

def strip_html_emoji():
    re_expr = re.compile("&#\d{4,8};")
    with open("dataset_clean_v2.csv", "r", encoding="utf-8") as file:
        data = []
        for line in file:
            d = re_expr.sub("", line)
            data.append(d)

        with open("dataset_clean_v3.csv", "w", encoding="utf-8") as file:
            for entry in data:
                file.write(f"{entry}")

def clean_ascii():
    with open("dataset_clean_v3.csv", "r", encoding="utf-8") as file:
        data = []
        for line in file:
            ln = line.replace('"', '').replace("'", "").strip().strip()
            data.append(ln)

        with open("dataset_clean_v4.csv", "w", encoding="utf-8") as file:
            for entry in data:
                file.write(f"{entry}\n")

def restructure_quotes():
    with open("dataset_clean_v4.csv", "r", encoding="utf-8") as file:
        data = []
        for line in file:
            text = line.split(",")[6:]
            ln = line.split(",")[:6]
            text_join = ",".join(text).strip()
            ln.append(f"\"{text_join}\"")
            data.append(ln)

        with open("dataset_clean_v5.csv", "w", encoding="utf-8") as file:
            for entry in data:
                file.write(f"{','.join(entry)}\n")

restructure_quotes()
