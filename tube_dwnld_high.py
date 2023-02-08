import pytube


def link_catcher(some_link, line_num, path):
    print(some_link, 'is downloading...')
    try:
        link = some_link
        yt = pytube.YouTube(link)
        yt.streams.get_highest_resolution().download(output_path='C:/test')
        print(f'downloaded at {path}')
    except Exception:
        text_file_reader(path, line_num)


def text_file_reader(path, line_num=1):
    print(path)
    with open(path) as file:
        for line_num, lines in enumerate(file, start=line_num):
            print(link_catcher(lines, line_num, path))
        return ''


print(text_file_reader(input('path...///')))

# C:\Users\user\Documents\juicy_j.txt