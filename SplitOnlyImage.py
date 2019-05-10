import os
import numpy as np
import cv2
import copy
import dota_utils as util
import time
import ResultMerge

def Getvalidpath(srcpath, dstpath):
    '''
    srcpath is the path of split image
    dstpath is the path that you want your valid_dir.txt to be saved
    (about dstpath：remenber to add \ at the end )
    '''
    dirs = os.listdir(srcpath)
    filename = dstpath + 'valid_dir.txt'
    f = open(filename, 'w')
    for txtdir in dirs:
        txtdir = '/darknet/DOTA/images/' + txtdir
        f.write("%s\n" % txtdir)
    f.close

class splitbase():
    def __init__(self,
                 srcpath,
                 dstpath,
                 gap=100,
                 subsize=1024,
                 ext='.png'):
        self.srcpath = srcpath
        self.outpath = dstpath
        self.gap = gap
        self.subsize = subsize
        self.slide = self.subsize - self.gap
        self.srcpath = srcpath
        self.dstpath = dstpath
        self.ext = ext
    def saveimagepatches(self, img, subimgname, left, up, ext='.png'):
        subimg = copy.deepcopy(img[up: (up + self.subsize), left: (left + self.subsize)])
        outdir = os.path.join(self.dstpath, subimgname + ext)
        cv2.imwrite(outdir, subimg)

    def SplitSingle(self, name, rate, extent):
        img = cv2.imread(os.path.join(self.srcpath, name + extent))
        assert np.shape(img) != ()

        if (rate != 1):
            resizeimg = cv2.resize(img, None, fx=rate, fy=rate, interpolation = cv2.INTER_CUBIC)
        else:
            resizeimg = img
        outbasename = name + '__' + str(rate) + '__'

        weight = np.shape(resizeimg)[1]
        height = np.shape(resizeimg)[0]
        
        left, up = 0, 0
        while (left < weight):
            if (left + self.subsize >= weight):
                left = max(weight - self.subsize, 0)
            up = 0
            while (up < height):
                if (up + self.subsize >= height):
                    up = max(height - self.subsize, 0)
                subimgname = outbasename + str(left) + '___' + str(up)
                self.saveimagepatches(resizeimg, subimgname, left, up)
                if (up + self.subsize >= height):
                    break
                else:
                    up = up + self.slide
            if (left + self.subsize >= weight):
                break
            else:
                left = left + self.slide

    def splitdata(self, rate):
        
        imagelist = util.GetFileFromThisRootDir(self.srcpath)
        imagenames = [util.custombasename(x) for x in imagelist if (util.custombasename(x) != 'Thumbs')]
        for name in imagenames:
            self.SplitSingle(name, rate, self.ext)
if __name__ == '__main__':
    start = time.time()
    split = splitbase(r'C:\Users\Hust\Desktop\pipeline\example\images',
                      r'C:\Users\Hust\Desktop\pipeline\split_example')
    split.splitdata(1)
    # Getvalidpath(srcpath=r'C:\Users\Hust\Desktop\pipeline\split_example' , \
    #     dstpath=r'C:\Users\Hust\Desktop\pipeline\validtxt\\' )
    print('time:', time.time()-start, "second")
    #############################################
    os.system("/home/lfl/darknet detector valid cfg/dota.data cfg/yolo-dota.cfg yolo-dota_final.weights")
    #############################################
    ResultMerge(a,b)

