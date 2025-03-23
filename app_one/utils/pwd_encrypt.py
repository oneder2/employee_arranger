import hashlib
from MyProject.settings import SECRET_KEY

def md5(data):
    obj_md5 = hashlib.md5(SECRET_KEY.encode("utf-8"))
    obj_md5.update(data.encode("utf-8"))
    return obj_md5.hexdigest()
