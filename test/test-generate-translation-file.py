from qttranslationgenerator import * 

if __name__ == "__main__":
    try:
        qtTranslationFileGenerator = QtTranslationFileGenerator('Test_tr.ts')
        qtTranslationFileGenerator.translate('tr')
        qtTranslationFileGenerator.write_translated_texts_to_file('tr')
    except Exception as e:
        print('Exception {0}'.format(str(e)))
