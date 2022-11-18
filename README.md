# Qt Translation Generator
Translates Qt Linguist TS file to different languages via Google Translate API. Supported languages are listed in [Language Codes](#language-codes) section. **The package is under development!**

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

# Requirements
To install all dependencies used in the package, use following command. No need to run if you install by using setup.py 
```
pip install -r /path/to/requirements.txt
```

# Usage
Following code used to translate all texts from Test_tr.ts file and generate Test_tr_generated.tr.ts file. 
```
def translate_to(src_translation_file, target_lang_code):
    try:
        qt_translation_file_generator = QtTranslationFileGenerator(src_translation_file, target_lang_code)
        qt_translation_file_generator.translate(target_lang_code)
        qt_translation_file_generator.write_translated_texts_to_file(target_lang_code)
    except Exception as e:
        print('Exception {0}'.format(str(e)))
```
Following code can be used to generate translation files for all supported languages.
```
def translate_to_all_languages(src_translation_file):
    try:
        for key in language_dict:
            translate_to(src_translation_file, key)
    except Exception as e:
        print('Exception {0}'.format(str(e)))
```

main function
```
if __name__ == "__main__":
    try:
        #translate_to('Test_tr.ts', 'tr')
        translate_to_all_languages('Test_tr.ts')
    except Exception as e:
        print('Exception {0}'.format(str(e)))
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
