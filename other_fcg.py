import os
import networkx as nx
import matplotlib.pyplot as plt
import csv

def build_fcg(folder_path):
    G = nx.DiGraph()

    # Duyệt qua tất cả các tệp trong thư mục và thư mục con
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                functions = extract_functions(file_path)
                add_functions_to_graph(G, functions)

    return G

def extract_functions(file_path):
    functions = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        current_function = None
        for line in lines:
            if line.strip().startswith("void") or line.strip().startswith("public void"):
                # Bắt đầu của một hàm mới
                current_function = line.strip().split()[1].split("(")[0]
                functions.append(current_function)
            elif "{" in line:
                # Bắt đầu của một block mã
                pass
            elif "}" in line:
                # Kết thúc của một block mã
                pass
            elif current_function is not None:
                # Thêm dòng mã vào hàm hiện tại
                pass
    return functions

def add_functions_to_graph(G, functions):
    for i in range(len(functions) - 1):
        G.add_edge(functions[i], functions[i+1])

# Đường dẫn tới thư mục chứa các tệp Java
folder_path = "D:\BTL_Python\Output_file"

# Xây dựng đồ thị FCG từ thư mục
fcg = build_fcg(folder_path)

# Vẽ đồ thị
plt.figure(figsize=(10, 8))
nx.draw(fcg, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
plt.title("Flow Control Graph")

# Lưu đồ thị vào file hình ảnh
plt.savefig("fcg_graph.png")

# Lưu tọa độ của các nút vào file CSV
output_file = "fcg_coordinates.csv"
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Function", "X", "Y"])
    pos = nx.spring_layout(fcg)  # Tính toán tọa độ của các nút
    for node, (x, y) in pos.items():
        writer.writerow([node, x, y])

print("FCG đã được lưu vào file ảnh:", "fcg_graph.png")
print("Tọa độ của các nút đã được lưu vào file CSV:", output_file)
