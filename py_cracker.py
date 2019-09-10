from urllib.request import urlopen
import sys, os, getopt
from time import sleep
import subprocess as sp


def clear_html(html):
    html = html.replace('&nbsp;', '')
    html = html.replace('&lt;', '<')
    html = html.replace('&gt;', '>')
    html = html.replace('<br>', '')
    html = html.replace('<p>', '')
    html = html.replace('</p>', '')
    html = html.replace('”', '"')
    html = html.replace('“', '"')
    #html = html.replace('\234', '')

    return html

def find_start_index(html):
    start_index = 999999
    if html.find('int main') != -1:
        start_index = min(html.find('int main'), start_index)
    else:
        start_index = 999999
    if html.find('struct ') != -1:
        start_index = min(html.find('struct '), start_index)
    if html.find('typedef ') != -1:
        start_index = min(html.find('typedef '), start_index)
    return start_index

def find_end_index(html, start_index):
    end_index = 0
    end = html[start_index:len(html)].find("<script>") + start_index
    end = min(end, html[start_index+1:len(html)].find('</div>') + start_index)
    if end == -1:
        end = len(html)
    for index in range(start_index, end):
        if (html[index]) == '}':
            end_index = index
    
    return end_index


def create_code(input_html):
    file = open("programm.cpp","w+")
    file.write("#include <stdio.h>\n#include <string.h>\n#include <algorithm>\n")
    html = clear_html(input_html)
    start_index = find_start_index(html)
    end_index = find_end_index(html, start_index)
    file.write(str(html[start_index:end_index + 1]))
    sp.call(r"gcc /home/kichyr/Desktop/crack_technotrack/programm.cpp")
        

def main():
    
    while(True):
        url = str(input())
        response = urlopen(url)
        html = str(response.read().decode())
        create_code(html)
        

if (__name__ == "__main__"):
    main()