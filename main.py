import csv
import numpy as np
import statistics
import matplotlib.pyplot as plt


def write_csv(matrix):
    with open('csw_data.csv', 'w') as f:
        writer = csv.writer(f)
        for row in matrix:
            writer.writerow(row)


def read_csv():
    with open('csw_data.csv', 'r') as f:
        matrix = list()
        reader = csv.reader(f)
        for row in reader:
            if row:
                row_of_numbres = [int(k) for k in row]
                matrix.append(row_of_numbres)
        return np.array(matrix)


number_of_points = 200
matr = np.random.randint(-5, 5, (number_of_points, 2))

write_csv(matr)

matrix_from_csv = read_csv()
print(matrix_from_csv)

m = 7
step = 2
nx, ny = (m, m)
x = np.linspace(-6, 6, nx)
y = np.linspace(6, -6, ny)
xv, yv = np.meshgrid(x, y)

# Создали матрицу из точек координат, поделив плоскость на m отрезоков по оси X, и m отрезокв по оси Y
# for i in range(nx):
#     for j in range(ny):
#         print("(", xv[i, j], ",", yv[i, j], end=")")
#     print("")

right_border = xv[m - 1, m - 1]
lower_border = yv[m - 1, m - 1]

current_up_border = xv[0, 0]
current_left_border = yv[0, 0]

current_right_border = xv[0, 0]
current_low_border = yv[0, 0]

num = 1
squared_dots_sizes = list()
# Идем сверху вниз, слева направо
while current_low_border > lower_border:
    current_up_border = current_low_border
    current_right_border = xv[0, 0]
    current_low_border -= 2
    while current_right_border < right_border:
        current_left_border = current_right_border
        current_right_border += 2
        print(f"Текущий квадрат {num}", end="")
        num += 1
        print(
            f"({current_left_border}, {current_up_border}) ({current_right_border, current_up_border}) ({current_left_border}, {current_low_border}) ({current_right_border, current_low_border})")
        dots = np.where(
            np.logical_and(matrix_from_csv[:, 0] >= current_left_border, matrix_from_csv[:, 1] <= current_up_border) &
            np.logical_and(matrix_from_csv[:, 0] <= current_right_border, matrix_from_csv[:, 1] >= current_low_border))
        squared_dots = matrix_from_csv[dots]
        squared_dots_sizes.append(squared_dots.size / 2)
        print("Точки, входящие в данный квадрат:")
        print(squared_dots)
        print("")

print("Среднее количество точек в квадрате:")
print(statistics.mean(squared_dots_sizes))
print("Стандартное отклонение по количеству точек на квадрат:")
print(np.std(squared_dots_sizes))
print("Дисперсия (по кол-ву точек на квадрат):")
print(np.var(squared_dots_sizes))

# Для визуализации точек
# plt.plot(xv, yv, marker='o', color='k', linestyle='none')
# plt.show()
