import os
import random

from captcha.image import ImageCaptcha, random_color

"""
使用 captcha 依赖包生成验证码
"""


def main():
    savepath = 'tmp/'
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    listname = savepath+'/result.txt'
    writers = open(listname,'w')
    n_gen = 12000
    dir_num = 12000
    # characters = string.digits +string.ascii_letters
    characters = "3456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(characters)

    width, height, n_len, n_class = 200, 75, 4, len(characters)

    fonts_my = [
        "AppleSDGothicNeo.ttc",
        "Standout.ttf"
    ]

    font_sizes_my = [62,65]



    generator = ImageCaptcha(width=width, height=height,fonts=fonts_my, font_sizes=font_sizes_my)


    for i in range(n_gen):
        random_str = ''.join([random.choice(characters) for j in range(4)])

        img = generator.generate_image(random_str)


        dir_count = i//dir_num
        dirpath= savepath+"/part{}/".format(dir_count)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        

        img.save(dirpath+"{}_{}.jpg".format(random_str,i))
        writers.write(dirpath+"{}_{}.jpg {}\n".format(random_str,i,random_str))
    writers.close()

if __name__ == '__main__':
    main()
