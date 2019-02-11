# Иванов Сергей
# Практическое задание №8. Задание №2.
# Закодируйте любую строку из трех слов по алгоритму Хаффмана.
# Программа взята с сайта
# https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding
# Только разобрался как работает, с классами (как показывали в лекции) не сделал


def assign_code(nodes, label, result, prefix=''):
    childs = nodes[label]
    tree = {}
    if len(childs) == 2:
        tree['0'] = assign_code(nodes, childs[0], result, prefix + '0')
        tree['1'] = assign_code(nodes, childs[1], result, prefix + '1')
        return tree
    else:
        result[label] = prefix
        return label


def Huffman_code(_vals):
    vals = _vals.copy()
    nodes = {}
    for n in vals.keys():  # leafs initialization
        nodes[n] = []

    while len(vals) > 1:  # binary tree creation
        s_vals = sorted(vals.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1 + a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1 + a2] = [a1, a2]
    code = {}
    root = a1 + a2
    tree = {}
    tree = assign_code(nodes, root, code)  # Присваивание кода в переменной code
    return code, tree   # tree в данной программе не используется


text = 'класс курс алгоритм'
#text = 'hello lolly'
print(f'Текст для кодирования: {text}')
d = dict.fromkeys(text, 0)
for el in text:
    d[el] += 1
print(f'Подсчет количества повторений символов: {d}')

code, tree = Huffman_code(d)

print(f'Таблица кодирования: {code}')
print(f'Дерево кодирования: {tree}')
encoded = ''.join([code[t] for t in text])
print('Encoded text:', encoded)
