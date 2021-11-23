import os, sys, io


class RedirectStdout:  # import os, sys, cStringIO
    def __init__(self):
        self.content = ''
        self.savedStdout = sys.stdout
        self.memObj, self.fileObj, self.nulObj = None, None, None

    # 外部的print语句将执行本write()方法，并由当前sys.stdout输出
    def write(self, outStr):
        # self.content.append(outStr)
        self.content += outStr

    def toCons(self):  # 标准输出重定向至控制台
        sys.stdout = self.savedStdout  # sys.__stdout__

    def toMemo(self):  # 标准输出重定向至内存
        self.memObj = io.StringIO()
        sys.stdout = self.memObj

    def toFile(self, file='out.txt'):  # 标准输出重定向至文件
        self.fileObj = open(file, 'a+', 1)  # 改为行缓冲
        sys.stdout = self.fileObj

    def toMute(self):  # 抑制输出
        self.nulObj = open(os.devnull, 'w')
        sys.stdout = self.nulObj

    def restore(self):
        self.content = ''
        if self.memObj.closed != True:
            self.memObj.close()
        if self.fileObj.closed != True:
            self.fileObj.close()
        if self.nulObj.closed != True:
            self.nulObj.close()
        sys.stdout = self.savedStdout  # sys.__stdout__
