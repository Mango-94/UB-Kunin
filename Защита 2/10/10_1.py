def task(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()

    N = int(data[0].strip())
    A = [list(map(int, data[i + 1].split())) for i in range(N)]
    pos = 0
    s = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] > 0:
                pos += 1
                s += A[i][j]

    with open(output_file, 'w') as file:
        file.write(f"Sum: {s}\n")
        file.write(f"Count: {pos}\n")

# Файлы
input_file = "КМА_УБ-41_vvod_1.txt"
output_file = "КМА_УБ-41_vivod_1.txt"

task(input_file, output_file)
print("Результаты сохранены в файл", output_file)
