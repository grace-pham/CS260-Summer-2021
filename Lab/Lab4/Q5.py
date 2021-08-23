def Q5(file_name):
    with open(file_name, 'r') as file:
        result = {}
        for line in file:
            for word in line.split():
                first_letter = word[0].upper()
                if first_letter not in result.keys():
                    result[first_letter] = 1
                else:
                    result[first_letter] += 1
    return result


if __name__ == "__main__":
    fn = input("Enter name of file to read :")
    dict = Q5(fn)
    print("| Letter | Count |")
    for pair in dict:
        print("| %4s   | %4s  | " % (pair[0], dict[pair[0]]))
