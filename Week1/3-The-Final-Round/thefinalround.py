import calendar


def count_words(arr):
    result = {}
    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(count_words(["apple", "banana", "apple", "pie"]))


def unique_words_count(arr):
    return len(set(arr))
    # result = {}
    # for word in arr:
    #     if word in result:
    #         result[word] += 1
    #     else:
    #         result[word] = 1
    # return len(result)

print(unique_words_count(["python", "python", "python", "ruby"]))


def nan_expand(times):
    result = 0
    if times == 0:
        return "\"\""
    else:
        for time in range(0, times):
            result += 1
        list_r = []
        for element in range(0, result):
            list_r.append(element)
        str_r = '\"'
        for n in list_r:
            str_r += ("Not a ")
        str_r += ("NaN\"")
    return str_r

print(nan_expand(4))


def iterations_of_nan_expand(expanded):
    string = 'Not a'
    if expanded.count(string) == 0:
        return False
    else:
        return expanded.count(string)

print(iterations_of_nan_expand(
    'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand("Show these people!"))


def is_prime(n):
    if n in [0, 1]:
        return False
    elif n == 2:
        return True
    elif n < 0:
        return False
    else:
        for number in range(2, n):
            if (number != n) and (n % number == 0):
                return False
            else:
                return True


def prime_factorization(n):
    primes = []
    for i in range(0, n):
        if is_prime(i) == True:
            if n % i == 0:
                n = n // i
                primes.append(i)
                if n % i == 0:
                    n = n // i
                    primes.append(i)
    result = {}
    for prime in primes:
        if prime in result:
            result[prime] += 1
        else:
            result[prime] = 1
    return sorted(result.items())

print(prime_factorization(356))


def group(list_int):
    big_tuple = []
    small_tuple = []
    for element in range(0, len(list_int)):
        if list_int[element] in small_tuple or small_tuple == []:
            small_tuple.append(list_int[element])
        else:
            big_tuple.append(small_tuple)
            small_tuple = []
            small_tuple.append(list_int[element])
    big_tuple.append(small_tuple)
    return big_tuple

print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    counter = 0
    group_list = group(items)
    for element in group_list:
        if counter < len(element):
            counter = len(element)
        elif counter >= len(element):
            continue
    return counter

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))


def groupby(func, seq):
    dictionary = {}
    for index in seq:
        if func(index) not in dictionary:
            dictionary[func(index)] = [index]
        elif func(index) in dictionary:
            dictionary[func(index)].append(index)
    return dictionary

print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))

def prepare_meal(number):
    result = ""
    count3 = 0
    while number % 3 == 0:
        count3 += 1
        number /= 3
        result += 'spam '
    if number % 5 == 0:
        if count3 == 0:
            result += "eggs "
        else:
            result += "and eggs"
    return result.strip(' ')

print(prepare_meal(7))
print(prepare_meal(15))
print(prepare_meal(45))


def reduce_file_path(path):
    result = []
    elements = []
    for element in path.split("/"):
        if element not in [".", ""]:
            elements += [element]
    while len(elements) != 0:
        element = elements.pop()
        if element == "..":
            if len(elements) != 0:
                elements.pop()
        else:
            result.insert(0, element)
    return "/" + "/".join(result)


print(reduce_file_path("/"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))


def is_an_bn(word):
    if word is "":
        return True
    elif len(word) % 2 != 0:
        return False
    counter_for_a = 0
    counter_for_b = 0
    ls = []
    if type(word) == str:
        for element in range(0, len(word)):
            ls.append(word[element])
    else:
        return False
    length = len(ls)
    for element in range(0, length // 2):
        if ls[element] is "a":
            counter_for_a += 1
        else:
            return False
    for element in range(length // 2, length):
        if ls[element] is "b":
            counter_for_b += 1
        else:
            return False
    return True
    if counter_for_a == counter_for_b:
        return True

print (is_an_bn(""))
print (is_an_bn("rado"))
print (is_an_bn("aaabb"))
print (is_an_bn("aaabbb"))
print (is_an_bn("aabbaabb"))
print (is_an_bn("bbbaaa"))
print (is_an_bn("aaaaabbbbb"))


def odd(n):
    return n % 2 != 0


def to_digits(n):
    list_digits = []
    str_number = str(n)
    for element in range(0, len(str_number)):
        list_digits.append(int(str(n)[element]))
    return list_digits


def to_number(digits):
    number = ''
    for i in range(0, len(digits)):
        number = number + str(digits[i])
    return int(number)


def is_credit_card_valid(number):
    digits = to_digits(number)
    length = len(digits)
    if odd(length) is False:
        return False
    list_of_new_numbers = []
    for element in range(0, length):
        if odd(element) is False:
            list_of_new_numbers.append(digits[element])
        else:
            if digits[element] * 2 <= 9:
                list_of_new_numbers.append(digits[element] * 2)
            else:
                big_number = to_digits(digits[element] * 2)
                for index in range(len(big_number)):
                    list_of_new_numbers.append(big_number[index])
    print(list_of_new_numbers)
    print(sum(list_of_new_numbers))
    if sum(list_of_new_numbers) % 10 is 0:
        return True
    else:
        return False

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))


def goldbach(n):
    list_final = []
    for element in range(0, n//2+1):
            if is_prime(element) and is_prime(n - element) == True:
                list_final.append((element, n-element))
    return list_final

print(goldbach(10))


def magic_square(matrix):
    sums = []
    # sums elements in rows
    sum_of_rows = [sum(row) for row in matrix]
    for element in range(len(sum_of_rows)):
        sums.append(sum_of_rows[element])

    # sums elements in columns
    sum_of_cols = [sum([row[i] for row in matrix]) for i in range(0, len(matrix[0]))]
    for element in range(len(sum_of_cols)):
        sums.append(sum_of_cols[element])

    # sums the elements in the first diagonal
    sum_of_first_diagonal = sum(matrix[row][row] for row in range(0, len(matrix)))
    sums.append(sum_of_first_diagonal)

    # sums the elements in the reversed diagonal
    sum_of_second_diagonal = 0
    j = len(matrix) - 1
    for i in range(0, len(matrix)):
        sum_of_second_diagonal += matrix[i][j]
        j -= 1
    sums.append(sum_of_second_diagonal)

    for element in range(len(sums) - 1):
        if sums[element] != sums[element + 1]:
            return False
    return True

print (magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print (magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))


FRIDAY_INDEX = 4

def friday_years(start, end):
    count_friday_years = 0
    year = start
    while year <= end:
        fridays_in_one_year = 0
        for month in range(1, 12 + 1):
            for week in calendar.monthcalendar(year, month):
                if week[FRIDAY_INDEX] != 0:
                    fridays_in_one_year += 1
        if fridays_in_one_year == 53:
            count_friday_years += 1
        year += 1
    return count_friday_years


print(friday_years(1000, 2000))
