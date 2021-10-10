csv = "D:\\PROG\\SASEhack-2021\\dataset\\dataset_clean_v5.csv"\

cols = ["tweet", "hate_speech"]
targets = ["text", "isHate"]
with open(csv, "r") as file:
    headers = [i.strip('"').strip() for i in file.readline().split(",")]
    col_index = []
    for col in cols:
        col_index.append(headers.index(col))

    csv_data = []
    for line in file:
        data = line.split(",")
        ld = []
        for index in col_index:
            ld.append(data[index].strip().strip('"'))
        csv_data.append(ld)
    
    with open("out.csv", "w") as f:
        f.write(",".join(targets) + "\n")
        for d in csv_data:
            f.write(",".join(d) + "\n")
