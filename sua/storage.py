from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


class FileStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(
        self,
        location=settings.MEDIA_ROOT,
        base_url=settings.MEDIA_URL
    ):
        # 初始化
        super(FileStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # name为上传文件名称
        import os
        import time
        import random
        # 文件扩展名
        ext = os.path.splitext(name)[1]
        # 文件目录
        d = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(3455660, 123456789)  # TODO:设计文件名加密算法
        # 重写合成文件名
        name = os.path.join(d, fn + ext)
        # 调用父类方法
        return super(FileStorage, self)._save(name, content)
