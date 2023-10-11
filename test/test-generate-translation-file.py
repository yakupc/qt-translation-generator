from qttranslationgenerator import * 

def translate_to(src_translation_file, target_lang_code):
    try:
        qt_translation_file_generator = QtTranslationFileGenerator(src_translation_file, target_lang_code)
        qt_translation_file_generator.translate(target_lang_code)
        qt_translation_file_generator.write_translated_texts_to_file(target_lang_code)
    except Exception as e:
        print('Exception {0}'.format(str(e)))

def translate_dictionary_xml(src_translation_file, target_lang_code):
    try:
        qt_translation_file_generator = DictionaryTranslationFileGenerator(src_translation_file, target_lang_code)
        qt_translation_file_generator.translate(target_lang_code)
        qt_translation_file_generator.write_translated_texts_to_file(target_lang_code)
    except Exception as e:
        print('Exception {0}'.format(str(e)))

def translate_to_all_languages(src_translation_file):
    try:
        for key in language_dict:
            translate_to(src_translation_file, key)
    except Exception as e:
        print('Exception {0}'.format(str(e)))


if __name__ == "__main__":
    try:
        #translate_to('Test_tr.ts', 'tr')
        #translate_to_all_languages('Test_tr.ts')
        translate_dictionary_xml('Test.xml', 'vi');
    except Exception as e:
        print('Exception {0}'.format(str(e)))