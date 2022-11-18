from qttranslationgenerator import * 

if __name__ == "__main__":
    try:
        for key in language_dict:
            target_lang_code = key
            qtTranslationFileGenerator = QtTranslationFileGenerator('Test_tr.ts')
            qtTranslationFileGenerator.translate(target_lang_code)
            qtTranslationFileGenerator.write_translated_texts_to_file(target_lang_code)
    except Exception as e:
        print('Exception {0}'.format(str(e)))
