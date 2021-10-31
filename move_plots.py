import os
import time
import shutil

input_path = 'D:\\NFT'

dirs = ['C:\\Chia Plots\\Farm16',
        'Z:\\',
        'I:\\',
        'G:\\']

buffer_size = 13

while True:
    for ri, di, fi in os.walk(input_path):
        print(len(fi), "NFT plots ready to move")
        done = False
        if len(fi) > buffer_size:
            for dir in dirs:
                export_path = os.path.join(dir, 'Export')
                nft_path = os.path.join(dir, 'NFT')
                for r, d, f in os.walk(export_path):
                    if len(f) > 0 and not done:
                        print(len(f), "remaining in",  export_path)
                        os.remove(os.path.join(export_path, f[0]))
                        print("Moving",fi[0],'to', nft_path)

                        shutil.move(
                            os.path.join(input_path, fi[0]),
                            os.path.join(nft_path, fi[0]+'.tmp'))
                        shutil.move(
                            os.path.join(nft_path, fi[0]+'.tmp'),
                            os.path.join(nft_path, fi[0]))
                        print("Moved", fi[0], 'to', nft_path)
                        done = True
        else:

            time.sleep(700)
