'''
1. $ATAF_TEST_CASE/TC/A4.ts를 읽어 들임
2. 파일 안의 ts, sql, tc파일 읽어서 목록화
3. ts파일의 경우 재귀적으로 호출해서 다시 그 안의 ts, sql, tc파일 목록 만듬
4. 읽으면서 Init, init으로 시작하는 tc, sql 파일이 있으면 따로 저장
'''

import os
import sys
import re

root_testsuite_list = []
testcase_list_with_init = []
initialize_list = []
finalize_list = []

TEST_CASE_ROOT = "/Users/hjjun/natc/TC/A4.ts"

def print_list(aList):
    for item in aList:
        print(item)

'''
def make_testsuite_list(root_path):
    for (path, dir, files) in os.walk(root_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.ts':
                root_testsuite_list.append(path + filename)
'''

def make_testsuite_list(root_testsuite_path):
    rf = open(root_testsuite_path)
    temp_list = rf.readlines()
    testsuite_list = []

    rePath = re.compile(r'(?P<path>.+/)*(?P<file>.+\.(t[sc]|sql))')

    for item in temp_list:
        if rePath.search(item) == None:
            pass
        else:
            testsuite_list.append(rePath.search(item).group())
    return testsuite_list


def create_metafile(testcase):
    print("create meta file")


def create_metafile_with_init(testcase_list, init_list, final_list):
    print("create meta file with initialize and finalize")


def traverse_testsuite(testsuite_list):
    init_flag = False
    traverse_testsuite_list = []
    for item in testsuite_list:
        if ".ts" in item:
            print("traverse_testsuite")
            traverse_testsuite_list = make_testsuite_list(item)
            traverse_testsuite(traverse_testsuite_list)
        elif ".tc" in item or "*.sql" in item:
            if init_flag == False:
                create_metafile(item)
            else:
                testcase_list_with_init.append(item)
        elif "init" in item.lower():
            initialize_list.append(item)
            init_flag = True
        elif "final" in item.lower():
            finalize_list.append(item)
            create_metafile_with_init(testcase_list_with_init, initialize_list, finalize_list)


root_testsuite_list = make_testsuite_list(TEST_CASE_ROOT)
traverse_testsuite(root_testsuite_list)
print_list(root_testsuite_list)
print_list(testcase_list_with_init)
print_list(initialize_list)
print_list(finalize_list)