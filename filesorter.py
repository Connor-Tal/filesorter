linecount = 0

with open("test.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line1 = lines[linecount]
        line2 = lines[linecount + 1]
        print(line1, line2)
        if line1 > line2:
            print('hi')
            linecount += 1
        elif line1.startswith == line2.startswith:
            equal1 = line1[1]
            equal2 = line2[1]
            if equal1 > equal2:
                linecount += 1
            else:
                with open('test.txt', 'w') as f:
                    lines[linecount] = line2
                    lines[linecount + 1] = line1
                    f.writelines(lines)
                    f.close()
        else:
            lines[linecount] = line2
            lines[linecount + 1] = line1 
            f.close()
            with open("test.txt", "w", encoding='utf-8') as f:
                f.writelines(lines)
                f.close()
            linecount += 1
