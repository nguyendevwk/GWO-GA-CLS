# Description: Đây là file chính của chương trình, chứa các hàm để chạy thuật toán và vẽ biểu đồ so sánh kết quả giữa các thuật toán
# Import các thư viện cần thiết
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from benchmark import *
from genetic_algorithm import GeneticAlgorithm
from grey_wolf_optimizer import GWO
from grey_wolf_genetic_algorithm import GWO_GA

#
# Hàm để chạy thuật toán và lấy lịch sử fitness
def run_algorithm(algorithm, function_index, popSize, max_iter, mutation_rate, crossover_rate):
    function_name, lb, ub, dim = Get_Functions_details2(function_index)
    fitness_func = function_name
    if algorithm == "GA":
        ga  = GeneticAlgorithm(dim=dim, popSize=popSize, Iter=max_iter, lb=lb, ub=ub, mutation_rate=mutation_rate, crossover_rate=crossover_rate, fitness_func=fitness_func)
        fitness_history, array_fitness = ga.optimize()
    elif algorithm == "GWO-GA":
        gwo_ga = GWO_GA(dim=dim, popSize=popSize, Iter=max_iter, lb=lb, ub=ub, mutation_rate=mutation_rate, crossover_rate=crossover_rate, fitness_func=fitness_func)
        fitness_history, array_fitness = gwo_ga.optimize6()
    elif algorithm == "GWO":
        gwo = GWO(dim=dim, popSize=popSize, Iter=max_iter, lb=lb, ub=ub, fitness_func=fitness_func)
        fitness_history, array_fitness = gwo.optimize()
    else:
        raise ValueError("Invalid algorithm name")
    return fitness_history, array_fitness

def save_to_csv(function_index, algorithms, fitness_histories):
    filename = f"comparison_function_{function_index}_10.csv"
    data = {"Iteration": list(range(1, len(fitness_histories[0]) + 1))}

    for algorithm, fitness_history in zip(algorithms, fitness_histories):
        data[f"{algorithm}_Fitness"] = fitness_history

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"File {filename} đã được lưu thành công!")



def plot_comparison(algorithms, function_indices, max_iter):
    markers = ['o', 's', '^', 'D', 'v', 'p', '*', '+', 'x']

    fig, axs = plt.subplots(3, 3, figsize=(15, 10))
    axs = axs.flatten()

    for i, function_index in enumerate(function_indices):
        ax = axs[i]
        print("function: ", function_index)
        fitness_histories = []
        for j, algorithm in enumerate(algorithms):
            fitness_history, array_fitness = run_algorithm(algorithm, function_index, popSize, max_iter, mutation_rate, crossover_rate)
            fitness_histories.append(array_fitness)

            # Đảm bảo các ký hiệu có khoảng cách hợp lý
            markevery = max(1, len(fitness_history) //5)  # Increase this value to reduce overlap

            ax.plot(fitness_history, label=algorithm, marker=markers[j % len(markers)], markevery=markevery)  # Use different markers and set markevery
        save_to_csv(function_index, algorithms, fitness_histories)
        ax.set_title(f"{function_indices[i]}", fontsize=10)
        ax.set_xlabel("Iterations", fontsize=8)
        ax.set_ylabel("Fitness", fontsize=8)
        ax.set_yscale('log')
        ax.legend(fontsize=6)

    # Hide the last subplot if it's not used
    if len(function_indices) < len(axs):
        axs[len(function_indices)].set_visible(False)

    plt.tight_layout()
    plt.show()


# Chạy thuật toán và vẽ biểu đồ so sánh
algorithms = ["GA",  "GWO","GWO-GA",]

# Chọn các hàm thử nghiệm
function_indices = ['F1', 'F2', 'F3', 'F4', 'F5','F6', 'F7',  'F8',  'F9']  # Chọn các hàm thử nghiệm

# Các tham số cần thiết
max_iter = 10  # Số lượng lặp tối đa (giảm xuống cho mục đích minh họa)
popSize = 50
mutation_rate = 0.1
crossover_rate = 0.8
plot_comparison(algorithms, function_indices, max_iter)
