import xml.etree.ElementTree as elementTree
import time
from googletrans import Translator
import os
from .language_codes import language_dict


class DictionaryTranslationFileGenerator:
    def __init__(self, src_translation_file_path, output_dir='.') -> None:
        """Initializes dictionary translation file generator
        
        Expected XML file format:
            <LANGUAGE>
                <DICTIONARY>
                    <KEY name="" value="" source="" />
                    <KEY name="" value="" source="" />
                    ..
                </DICTIONARY>
                ..
                ..
                <DICTIONARY>
                ..
                ..
                </DICTIONARY>
            </LANGUAGE>

        Args:
            src_translation_file_path (string): Source translation file path
        """
        self.src_translation_file_path = src_translation_file_path
        self.src_translation_file_name = os.path.basename(
            self.src_translation_file_path)
        # get file name without extension
        self.src_translation_file_name = os.path.splitext(
            self.src_translation_file_name)[0]
        self.output_dir = output_dir
        self.translated_text_map = {}

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        if self.src_translation_file_name is None:
            raise ValueError("Translation file name is not valid.")

        print(self.src_translation_file_name)

    def get_generated_translation_file_name(self, dest_lang_code):
        return '{0}_generated.xml'.format(self.src_translation_file_name)

    def get_generated_translation_file_path(self, dest_lang_code):
        return '{0}/{1}'.format(self.output_dir, self.get_generated_translation_file_name(dest_lang_code))

    def translate(self, dest_lang_code):
        """Generates new Qt translation file that includes translation texts for language specified in the given dest_lang_code

        Args:
            dest_lang_code (string): dest_lang_code (string): Destination translation language code
        """
        try:
            language_name = language_dict[dest_lang_code]
            print(
                '{0} [{1}] -> Language code is valid.'.format(language_name, dest_lang_code))
        except KeyError:
            print('{0} is not in language code dictionary.'.format(dest_lang_code))
            raise LookupError(
                '{0} is not in language code dictionary.'.format(dest_lang_code))

        with open(self.src_translation_file_path, 'rt', encoding="utf8") as f:
            tree = elementTree.parse(f)

        self.__translate(tree, dest_lang_code)

    def __translate(self, tree, dest_lang_code):
        """translate texts from given XML tree

        Args:
            tree (XML document): Translation XML document
            dest_lang_code (string): destination language code
        """
        root = tree.getroot()
        google_translator = Translator()
        for child_node in root:
            if child_node.tag == 'DICTIONARY':
                self.__parse_translation_context(
                    google_translator, child_node, dest_lang_code)

        print(self.get_generated_translation_file_path(dest_lang_code))
        tree.write(self.get_generated_translation_file_path(
            dest_lang_code), encoding="UTF-8", xml_declaration=True)

    def __parse_translation_context(self, google_translator, context_node, dest_lang_code):
        for message_node in context_node.iter('KEY'):
            self.__parse_message_node(
                google_translator, message_node, dest_lang_code)

    def __parse_message_node(self, google_translator, key_node, dest_lang_code):
        try:
            #attr_key_name = key_node.attrib['name']
            if "source" in key_node.attrib:
                source_text = key_node.attrib['source']
            elif "value" in key_node.attrib:
                source_text = key_node.attrib['value']
                key_node.set('source', source_text)
            else:
                print('source text not found!')
                return

            if source_text in self.translated_text_map:
                translated_text = self.translated_text_map[source_text]
                print('{0} has already been translated to {1}'.format(
                    source_text, translated_text))
                key_node.set('value', translated_text)
            else:
                #print('Translating {0} ...'.format(source_text))
                translated_text = google_translator.translate(
                    source_text, src='en', dest=dest_lang_code).text
                key_node.set('value', translated_text)
                self.translated_text_map[source_text] = translated_text
                print('{0} : {1}'.format(source_text, translated_text))
                time.sleep(1)
        except Exception as e:
            print('parse_message_node : Exception during translation of {0}. Exception : {1}'.format(
                source_text, str(e)))

    def replace_special_characters(self, str_in):
        """Replaces escape sequence in XML file with special characters 
        Special Character   Escape Sequence Purpose  
         &                   &amp;           Ampersand sign 
         '                   &apos;          Single quote 
         "                   &quot;          Double quote
         >                   &gt;            Greater than 
         <                   &lt;            Less than

        Args:
            str_in (string): input string to be replaced
        """
        str_out = str_in
        str_out = str_out.replace("&quot;", "\"")
        str_out = str_out.replace("&apos;", "\'")
        str_out = str_out.replace("&lt;",   "<")
        str_out = str_out.replace("&gt;",   ">")
        str_out = str_out.replace("&amp;",  "\&")
        str_out = str_out.replace("&",      "")
        return str_out

    def write_translated_texts_to_file(self, dest_lang_code):
        translation_file_path = self.get_generated_translation_file_path(
            dest_lang_code)

        with open(translation_file_path, 'rt', encoding="utf8") as f:
            tree = elementTree.parse(f)

        output_file_name = '{0}/translated_texts_{1}_{2}.txt'.format(
            self.output_dir, self.src_translation_file_name, dest_lang_code)
        print('Writing all translated text from {0} to file {1} ...'.format(
            translation_file_path, output_file_name))

        out_file = open(output_file_name, "w", encoding="utf-8")
        root = tree.getroot()

        for child_node in root:
            if child_node.tag == 'context':
                context_node = child_node
                for message_node in context_node.iter('message'):
                    source_node = message_node.find('source')
                    translate_node = message_node.find('translation')
                    if translate_node is not None:
                        try:
                            out_file.write('{0}:{1}\n'.format(
                                source_node.text, translate_node.text))
                        except Exception as e:
                            print('Exception during writing of {0} to file. Exception : {1}'.format(
                                source_node.text, str(e)))
        out_file.close()
