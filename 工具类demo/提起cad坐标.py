
# https://juejin.cn/post/6844904146525487118
import io
from PIL import Image
import struct

# ================= #
# dwg 文件缩略图提取  #
# ================= #

def read_fmt(fmt, fp):
    fmt_size = struct.calcsize(fmt)
    data = fp.read(fmt_size)
    try:
        assert len(data) == fmt_size, 'read=%d, expected=%d' % (len(data), fmt_size)
    except AssertionError:
        fp.seek(-len(data), 1)
        raise
    return struct.unpack(fmt, data)

def thumbnail(filePath, savePath):
    with open(filePath, 'rb') as fd:
        fd.seek(13, 0)
        pos_sentinel = read_fmt('I', fd)[0] # I 表示读取4个字节整数
        fd.seek(pos_sentinel+26, 0)
        header_size = read_fmt('I', fd)[0]
        fd.seek(5, 1)
        data_size = read_fmt('I', fd)[0]
        fd.seek(header_size, 1)

        png_data = fd.read(data_size)

        print(header_size, data_size)
        if data_size != len(png_data):
            raise Exception("dwg 解析错误!")

        imgio = io.BytesIO(png_data)
        with Image.open(imgio) as image:
            image.save(savePath, 'PNG')

if __name__ == "__main__":
    thumbnail('/Users/zoujunping/python采集资源/豆瓣排行榜/项目.dwg', '/Users/zoujunping/python采集资源/豆瓣排行榜/dwgpic2.png')

