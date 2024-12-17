with open("names.txt","r") as names_file:
    names_content = names_file.readlines()
for name in names_content:
    name = name[:-1]
    ready_to_send_file = open(f"letter_for_{name}","x")
    format_file = open("format.txt","r")
    fmt = format_file.readlines()
    for traverse in fmt:
        if '[NAME]' in traverse:
            t = traverse.split('[NAME]')
            fmt[fmt.index(traverse)] = t[0] + name + t[1]
        if '[YOUR NAME]' in traverse:
            fmt[fmt.index(traverse)] = "Aaditya"
    ready_to_send_file.writelines(fmt)
    fmt_read = format_file.read()