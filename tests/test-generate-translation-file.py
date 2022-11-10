from qt_translation_file_generator import QtTranslationFileGenerator

if __name__ == "__main__":
    try:
        qtTranslationFileGenerator = QtTranslationFileGenerator('GUI_tr_TR.ts')
        qtTranslationFileGenerator.translate('tr')
        qtTranslationFileGenerator.write_translated_texts_to_file('tr')
    except Exception as e:
        print('Exception {0}'.format(str(e)))
