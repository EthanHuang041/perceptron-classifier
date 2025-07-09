def load_data_from_txt():
    data = []
    labels = [] #variables initialization
    
    with open("data.txt", "r") as f:
        for line in f:  #detects every line in the file 
            parts = line.strip().split() 
            if len(parts) != 3: #wash data**important**
                continue 
            x1, x2, y = map(float, parts) #change value type**important**
            data.append([x1, x2])
            labels.append(int(y)) 
    
    return data, labels

data, labels = load_data_from_txt()

