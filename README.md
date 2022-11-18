# Qt Translation Generator
Translates Qt Linguist TS file to different languages via Google Translate API.
# Installation
Download the package.
```
git clone https://github.com/yakupc/qt-translation-generator.git
cd qt-translation-generator
```
Open terminal and enter:
```
python setup.py install
```
#Usage
```
from qttranslationgenerator import * 

if __name__ == "__main__":
    try:
        qtTranslationFileGenerator = QtTranslationFileGenerator('Test_tr.ts')
        qtTranslationFileGenerator.translate('tr')
        qtTranslationFileGenerator.write_translated_texts_to_file('tr')
    except Exception as e:
        print('Exception {0}'.format(str(e)))
```
