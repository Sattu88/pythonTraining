import urllib2

__author__ = 'shankar'


FILTER_LIST = [',', '\n', '\r', '\t', '.']


def read_file(path):
    if path is None:
        return None
    try:
        with open(path) as f:
            return f.readlines()
    except:
        print("Got error!!!")


def get_count(line):
    if line is None or type(line) is not str:
        return 0

    words = line.split()
    sum = 0
    for word in words:
        if word not in FILTER_LIST:
            sum += 1

    return sum


def read_file_from_web(url):

    response = urllib2.urlopen(url)
    return response.readlines()


def get_sum_from_lines(lines):
    sum = 0
    for line in lines:
        sum = sum + get_count(line)

    return sum


if __name__ == "__main__":
    path = "/Users/admin/code/gitStash/gundiProject/resources/gundi_test"
    lines = read_file(path)
    print("Number of words in file = %s" % get_sum_from_lines(lines))
    print("------------------------- Getting file from web now!!! ---------------")
    url = "http://reliance.com"
    text = read_file_from_web(url)
    print(get_sum_from_lines(text))
