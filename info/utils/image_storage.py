from qiniu import Auth, put_data

access_key = "lN9h_mk5hA5k4drxepQFhhLcCxu5Ht-x4jqQd82-"
secret_key = "c7uK0bs96L8TBgv2CyJSZhnkUytsW-vIDRL2pEh-"
bucket_name = "mypic"


def storage(data):
    try:
        q = Auth(access_key, secret_key)
        token = q.upload_token(bucket_name)
        ret, info = put_data(token, None, data)
        print(ret, info)
    except Exception as e:
        raise e;

    if info.status_code != 200:
        raise Exception("上传图片失败")
    return ret["key"]


if __name__ == '__main__':
    file = input('请输入文件路径')
    with open(file, 'rb') as f:
        storage(f.read())