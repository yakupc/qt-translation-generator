# Qt Translation Generator
Translates Qt Linguist TS file to different languages via Google Translate API. Supported languages are listed in [Language Codes](#language-codes) section.

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

Use following command to install the package in **editable/development mode**.
```
python setup.py install -e .
```
#Usage
Following code used to translate all texts from Test_tr.ts file and generate Test_tr_generated.tr.ts file. 
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
Following code can be used to generate translation files for all supported languages.
```
for key in language_dict:
    target_lang_code = key
    qtTranslationFileGenerator = QtTranslationFileGenerator('Test_tr.ts')
    qtTranslationFileGenerator.translate(target_lang_code)
    qtTranslationFileGenerator.write_translated_texts_to_file(target_lang_code)
```
# Language Codes
Google translate API supports following languages
```
'af': 'Afrikaans',
'sq': 'Albanian',
'ar': 'Arabic',
'az': 'Azerbaijani',
'eu': 'Basque',
'bn': 'Bengali',
'be': 'Belarusian',
'bg': 'Bulgarian',
'ca': 'Catalan',
'zh-CN': 'Chinese Simplified',
'zh-TW': 'Chinese Traditional',
'hr': 'Croatian',
'cs': 'Czech',
'da': 'Danish',
'nl': 'Dutch',
'en': 'English',
'eo': 'Esperanto',
'et': 'Estonian',
'tl': 'Filipino',
'fi': 'Finnish',
'fr': 'French',
'gl': 'Galician',
'ka': 'Georgian',
'de': 'German',
'el': 'Greek',
'gu': 'Gujarati',
'ht': 'Haitian Creole',
'iw': 'Hebrew',
'hi': 'Hindi',
'hu': 'Hungarian',
'is': 'Icelandic',
'id': 'Indonesian',
'ga': 'Irish',
'it': 'Italian',
'ja': 'Japanese',
'kn': 'Kannada',
'ko': 'Korean',
'la': 'Latin',
'lv': 'Latvian',
'lt': 'Lithuanian',
'mk': 'Macedonian',
'ms': 'Malay',
'mt': 'Maltese',
'no': 'Norwegian',
'fa': 'Persian',
'pl': 'Polish',
'pt': 'Portuguese',
'ro': 'Romanian',
'ru': 'Russian',
'sr': 'Serbian',
'sk': 'Slovak ',
'sl': 'Slovenian',
'es': 'Spanish',
'sw': 'Swahili',
'sv': 'Swedish',
'ta': 'Tamil',
'te': 'Telugu ',
'th': 'Thai',
'tr': 'Turkish',
'uk': 'Ukrainian',
'ur': 'Urdu',
'vi': 'Vietnamese',
'cy': 'Welsh',
'yi': 'Yiddish'
```