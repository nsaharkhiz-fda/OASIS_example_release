import os
import glob
import json
from PIL import Image
import tqdm
import random
import shutil

folder="/projects01/VICTRE/niloufar.saharkhiz/ssynth_artifact/data/images_and_masks/10k_calChart/output"
output="/projects01/didsr-aiml/consult-tool/oasis/images"

maxCount=100

data=[]
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if os.path.isdir(output):
    shutil.rmtree(output)

os.makedirs(output)

count=0
pbar = tqdm.tqdm(total=maxCount)
for case in glob.glob(folder+"/*"):
    for hair in glob.glob(case+"/*"):
        for mel in glob.glob(hair+"/*"):
            if random.random()>0.05:
                break

            finish=False
            path=mel
            meta=[]
            while True:
                nextFolder=glob.glob(path+"/*")
                if os.path.exists(nextFolder[0]+"/image.png"):
                    break
                meta.append(path.split('/')[-1])
                path=nextFolder[0]
            

            meta.append(path.split('/')[-1])
            path=nextFolder[0]
            meta.append(path.split('/')[-1])

            skinCase=case.split('/')[-1].split('_')[1]
            hairCase=hair.split('/')[-1].split('_')[1]
            melCase=mel.split('/')[-1].split('_')[1]
            Image.open(path+"/image.png").convert("RGB").save(output+f"/S{skinCase}_H{hairCase}_M{melCase}.jpg",quality=70)
            # shutil.copyfile(path+"/image.png",
            #     output+f"/S{skinCase}_H{hairCase}_M{melCase}.png")
            
            data.append({
                "skin":num(skinCase),
                "hair":num(hairCase),
                "melatonin":num(melCase),
                "blood":num(meta[1].split("_")[1]),
                "lesion":num(meta[2].split("_")[1]),
                "timepoint":num(meta[3].split("_")[1]),
                "material":meta[4],
                "hair_albedo":meta[5].split("_")[1],
                # "lesion_scale":num(meta[6].split("_")[-1]),
                "lighting":"_".join(meta[7].split("_")[1:]),
                "camera_distance":num(meta[8].split("_")[-1]),
                "frame":False if num(meta[10].split("_")[1])==-1 else True,
                "calibration_chart":False if num(meta[11].split("_")[1])==-1 else True,
                "ruler":False if num(meta[12].split("_")[1])==-1 else True,
                "filename":f"S{skinCase}_H{hairCase}_M{melCase}.jpg"
            })

            count+=1
            pbar.update(1)
            if(count==maxCount):
                with open(output+"/../metadata.json","w",encoding="utf8") as f:
                    json.dump(data,f,indent=2)
                exit()
