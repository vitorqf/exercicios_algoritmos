from get_info_from_breach import get_info_from_breach

contents = []

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")

while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

print(get_info_from_breach(contents))


