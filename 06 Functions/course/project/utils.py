def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def bold_text(text):
    return f"\033[1m{text}\033[0m"

def italic_text(text):
    return f"\033[3m{text}\033[0m"

def room_name_text(name):
    return bold_text(name)

def room_desc_text(desc):
    return color_text(italic_text(desc), "93")

def item_text(item):
    return color_text(item, "92")

def command_text(cmd):
    return color_text(cmd, "94")

def error_text(msg):
    return color_text(msg, "91")

def success_text(msg):
    return color_text(msg, "92")
