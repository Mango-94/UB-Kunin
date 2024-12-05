def task(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()

    M = int(data[0].strip())
    B = [list(map(int, data[i + 2].split())) for i in range(M)]
    for row in B:
        maxim = minim = 0
        for j, elem in enumerate(row):
            if elem > row[maxim]:
                maxim = j
            if elem < row[minim]:
                minim = j
            row[maxim], row[0] = row[0], row[maxim]
            row[minim], row[-1] = row[-1], row[minim]

    with open(output_file, 'w') as file:
        file.write("Task Result:\n")
        for row in B:
            file.write(' '.join(map(str, row)) + '\n')

# Файлы
input_file = "КМА_УБ-41_vvod_2.txt"
output_file = "КМА_УБ-41_vivod_2.txt"

task(input_file, output_file)
print("Результаты сохранены в файл", output_file)
