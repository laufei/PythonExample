# coding: utf-8

# @Time    : 2019/8/25 8:28 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 批量copy文件夹下的文件到另一个文件夹下.py
# @Software: PyCharm

import os, time
from multiprocessing import Pool, Manager

def copy_file(filename, folder_path, new_folder_name, queue):
    old = folder_path+os.sep+filename
    new = new_folder_name+os.sep+filename
    if os.path.exists(new):
        os.rmdir(new)
        print "%s文件夹存在, 并已删除!"

    with open(old, "rb") as fr:
        frc = fr.read()
        with open(new, "wb") as fw:
            fw.write(frc)
    queue.put(filename)

def main():
    folder_path = raw_input("请输入文件夹的路径:")
    filenames = os.listdir(folder_path)
    new_folder_name = folder_path + "_new"
    if os.path.exists(new_folder_name):
        os.system("rm -rf %s" % new_folder_name)
        print "%s文件夹存在, 并已删除!" % new_folder_name
    os.mkdir(new_folder_name)

    p = Pool(5)
    q = Manager().Queue()
    for f in filenames:
        p.apply_async(func=copy_file, args=(f, folder_path, new_folder_name, q,))

    done_num = 0.0
    all_num = len(filenames)
    while all_num > done_num:
        done_file = q.get()
        done_num += 1
        done_rate = done_num/all_num
        print "\r[Done] %s, 当前复制进度--%.2f%%" % (done_file, done_rate*100)

if __name__ == "__main__":
    main()