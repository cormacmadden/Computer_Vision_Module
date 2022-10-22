from ctypes import resize
from MidTermAssignment import *
from os import listdir
from os.path import isfile, join

def run():
    cv.destroyAllWindows()

    mypath='../Photos/Part1'
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    images = np.empty(len(onlyfiles), dtype=object)
    for n in range(0, len(onlyfiles)):
        images[n] = cv.imread(join(mypath,onlyfiles[n]),cv.IMREAD_UNCHANGED )
        
    images[0] = scale_image(images[0],0.15)
    images[1] = scale_image(images[1],0.3)
    images[2] = scale_image(images[2],0.1)

    for img in images:
        brightened = brighten_image(img,50)
        saturated = saturate_image(img,2)
        contrasted = contrast_image(img,1.5,50)
        solarized = solarization(img)
        Hori = np.concatenate((img, brightened), axis=1)
        Hori = np.concatenate((Hori, saturated), axis=1)
        Hori = np.concatenate((Hori, contrasted), axis=1)
        Hori = np.concatenate((Hori, solarized), axis=1)
        cv.imshow("Before/After", Hori)     
    
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    run()