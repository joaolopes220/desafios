def justify(text, width):
    """
    :param text: Input text to justify
    :param width: The max width per line
    :return: The lines that are justified
    """

    # create a list of all the words in the text
    words = text.split()
    # Initialize some varaible
    current_len = 0
    line_words = []
    lines = [line_words]
    
    # Create the lines with the correct character width
    # Part One of the Challenge
    for word in words:
        if current_len + len(word) > width:
            line_words = [word]
            lines.append(line_words)
            current_len = len(word) + 1
        else:
            line_words.append(word)
            current_len += len(word) + 1

    # Make the text justified
    # Part 2 of the Challenge
    for i in range(len(lines)):
        line_words = lines[i]
        space_need = width - sum(len(word) for word in line_words)
        while space_need:
            for index in range(len(line_words) - 1):
                if space_need == 0:
                    break
                line_words[index] += ' '
                space_need -= 1
        lines[i] = ''.join(line_words) + '\n'
    return lines


def getoutput(filepath, outputpath, width):
    """
    :param filepath: Path to the text file
    :param outputname: name to save final file as
    :return: None
    """
    file_lines = []
    f = open(filepath, 'r')
    for line in f:
        file_lines.append(line)

    fil = open(outputpath, 'w')
    for lines in file_lines:
        if lines == "\n":
            fil.write("\n")
        else:
            newlines = justify(lines, width)
            for lines2 in newlines:
                fil.write(lines2)
    f.close()
    fil.close()
    return None


if __name__ == '__main__':
    filedir = './TextFile/text1.txt'
    outputname = './TextFile/output.txt'
    getoutput(filedir, outputname, 40)
