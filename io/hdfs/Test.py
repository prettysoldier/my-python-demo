from hdfs.client import Client

def read_hdfs_file(client, filename):
    # with client.read('samples.csv', encoding='utf-8', delimiter='\n') as reader:
    #  for line in reader:
    # pass
    lines = []
    with client.read(filename, encoding='utf-8', delimiter='\n') as reader:
        for line in reader:
            # pass
            # print line.strip()
            lines.append(line.strip())
    return lines


# 创建目录
def mkdirs(client, hdfs_path):
    client.makedirs(hdfs_path)


# 删除hdfs文件
def delete_hdfs_file(client, hdfs_path):
    client.delete(hdfs_path)


# 上传文件到hdfs
def put_to_hdfs(client, local_path, hdfs_path):
    client.upload(hdfs_path, local_path, cleanup=True)


# 从hdfs获取文件到本地
# def get_from_hdfs(client, hdfs_path, local_path):
#     download(hdfs_path, local_path, overwrite=False)


# 追加数据到hdfs文件
def append_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, overwrite=False, append=True)


# 覆盖数据写到hdfs文件
def write_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, overwrite=True, append=False)


# 移动或者修改文件
def move_or_rename(client, hdfs_src_path, hdfs_dst_path):
    client.rename(hdfs_src_path, hdfs_dst_path)


# 返回目录下的文件
def list(client, hdfs_path):
    return client.list(hdfs_path, status=False)


client = Client("http://hadoop1:9870/")

# print(read_hdfs_file(client, '/input/file1.txt'))

# move_or_rename(client, '/input/file2.txt', '/input/file3.txt')

# put_to_hdfs(client, '/test/图片.png', '/input/')

# append_to_hdfs(client, '/input/file1.txt', '啦啦\n'.encode('utf-8'))
# print(read_hdfs_file(client, '/input/file1.txt'))

# write_to_hdfs(client, '/input/file4.txt', '啦啦啦啦啦啦我是卖报的小行家\n'.encode('utf-8'))
print(read_hdfs_file(client, '/input/file4.txt'))

mkdirs(client, '/input/python')
print(list(client, '/input'))
