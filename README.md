## Installation
```bash
git clone https://github.com/baoanh1310/template_classifier_predict.git
cd template_classifier_predict
python install -r requirements.txt
```

## Running
```bash
python main.py --api <API_URL> --path <PATH_TO_TEST_FOLDER>
```

- Example: If your test folder name 'test' and your subfolders are named by template name like '1', '2', '3', ...
- Structure of 'test' folder:
```bash
D:/FPT_DATA/test
├───1
└───2
```
- Then the this command work
```bash
python main.py --api https://bk-ocr.ai/fpt/predict/ --path D:/FPT_DATA/test
```