def rgb(r,g,b,bg=False):
    """
    Can set text to any color on the rgb spectrum.
    USAGE:
        print("Hello" + rgb(255, 128, 0) + "World!")
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)



reset = '\033[0m'
err = '│ ' + rgb(153, 0, 0) + 'ERROR' + reset + ': '
suc = rgb(0, 179, 0)
info = '│ ' + rgb(230, 230, 0) + 'INFO' + reset + ': '
warn = '│ ' + rgb(255, 117, 26) + 'WARN' + reset + ': '
success = '│ ' + rgb(51, 204, 51) + 'SUCCESS' + reset + ': '
line = rgb(179, 204, 255)
highlight = rgb(102, 0, 102)
prefix = rgb(89, 89, 89)
gs = rgb(128, 128, 255)
file_high = rgb(0, 179, 179)
bold = '\x1b[1m'