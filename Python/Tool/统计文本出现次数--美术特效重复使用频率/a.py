def count_lines(filename):
    line_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # 去除行首和行尾的空白字符
            if line in line_counts:
                line_counts[line] += 1
            else:
                line_counts[line] = 1
    sorted_lines = sorted(line_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_lines

result = count_lines('C:\\Users\\Administrator\\Desktop\\Test\\test.txt')
for line, count in result:
    print(f'"{line}" 出现了 {count} 次')
