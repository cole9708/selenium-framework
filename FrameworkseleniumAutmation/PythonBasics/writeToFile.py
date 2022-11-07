with open('test.txt', 'r') as reader:
    context_list = reader.readlines()
    reverse_list=reversed(context_list)


    with open('test.txt', 'w') as writer:
        for line in reverse_list:
            writer.write(line)



