import load_data

def sign(z):
    return 1 if z >= 0 else -1

def prediction(w, b, x):
    return w[0]*x[0] + w[1]*x[1] + b #w[0] used to indicate the number

def update(w, b, x, y, learning_rate):
    w[0] += learning_rate * y * x[0]
    w[1] += learning_rate * y * x[1]
    b += learning_rate * y
    return w, b

def train(data, labels, learning_rate=0.01, max_iter=100):
    w = [0.0, 0.0]
    b = 0.0
    for epoch in range(max_iter):
        print(f"第 {epoch+1} 轮训练")
        for i in range(len(data)): #len(data) 
            z = prediction(w, b, data[i])
            y_pred = sign(z)
            if y_pred != labels[i]:
                w, b = update(w, b, data[i], labels[i], learning_rate)
        print("w =", w, ", b =", b)

    with open("parameter.txt", "w") as g:
        g.write(f"{w[0]} {w[1]} {b}\n")
    return w, b

data, labels = load_data.load_data_from_txt()
train(data, labels)
