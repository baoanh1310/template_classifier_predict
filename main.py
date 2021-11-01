import requests
import glob
import os
import shutil
from tqdm import tqdm
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--api", help="Predict API", required=True)
    parser.add_argument("-p", "--path", help="Path to test folder", required=True)
    args = parser.parse_args()

    # url = 'https://bk-ocr.ai/fpt/predict/'
    url = args.api

    if not os.path.exists('results'):
        os.mkdir('results')

    # raw_path = "D:/FPT_DATA/test"
    raw_path = args.path
    label_list = os.listdir(raw_path)

    for label in label_list:
        count = 0
        good = 0
        wrong_list = []
        for _, img_path in tqdm(enumerate(glob.glob(os.path.join(raw_path, label, "*.jpg")))):
            my_img = {'file': open(img_path, 'rb')}
            r = requests.post(url, files=my_img)
            img_name = img_path.split('\\')[-1]
            predict_label = r.json().split()[-1]
            count += 1
            if predict_label == label:
                good += 1
            else:
                wrong_list.append(img_name)
        wrong_file_name = '{}_wrong.txt'.format(label)
        wrong_file_path = os.path.join('results', wrong_file_name)
        with open(wrong_file_path, 'w') as f:
            for name in wrong_list:
                f.write(name + '\n')

        stat_file_name = 'stats.txt'
        stats_file_path = os.path.join('results', stat_file_name)
        with open(stats_file_path, 'a') as f:
            f.write("Template {}: {}/{}\n".format(label, good, count))
        print("Template {}: {}/{}".format(label, good, count))