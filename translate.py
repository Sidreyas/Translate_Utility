

import transformers
import streamlit as st
from googletrans import Translator
import time



st.title("Translate Utility")
language = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
# languages_pre_train = {'English': 'en', 'German': 'de', 'French': 'fr', 'Spanish': 'es', 'Italian': 'it', 'Dutch': 'nl', 'Portuguese': 'pt', 'Russian': 'ru', 'Chinese': 'zh', 'Japanese': 'ja', 'Korean': 'ko', 'Arabic': 'ar', 'Hebrew': 'he', 'Turkish': 'tr', 'Polish': 'pl', 'Romanian': 'ro', 'Greek': 'el', 'Swedish': 'sv', 'Norwegian': 'no', 'Danish': 'da'}


source_lan = st.selectbox("Select the source language",list(language.keys()),index=21)
destination_lan  = st.selectbox("Select the destination language",list(language.keys()),index=30)

# src_pre_train= st.selectbox("Select the source for pre train model",list(languages_pre_train.keys()))
# dst_pre_train = st.selectbox("Select the destination for pre train model",list(languages_pre_train.keys()))

# task_name = f"translation_{languages_pre_train[src_pre_train]}_to_{languages_pre_train[dst_pre_train]}"
# model_name = f"Helsinki-NLP/opus-mt-{languages_pre_train[src_pre_train]}-{languages_pre_train[dst_pre_train]}"


text_area = st.text_area("Enter the text")


googletrans_translator = Translator()

# from translate import Translator
# translate_translator = Translator(from_lang=language[source_lan], to_lang=language[destination_lan])



translate_button = st.button("translate")

if translate_button:
    
    st.subheader('GOOGLETRANS_MODULE')

    start_googletrans = time.time()
    googletrans_result = googletrans_translator.translate(text_area,src= language[source_lan], dest= language[destination_lan])
    end_googletrans = time.time()
    st.success(googletrans_result.text)
    st.info("Run Time for googletrans = " + str((end_googletrans - start_googletrans)*1000))


#     st.subheader('Translate_MODULE')
    
#     start_Translate_MODULE = time.time()
#     translate_results = translate_translator.translate(text_area)
#     end_Translate_MODULE = time.time()
#     st.success(translate_results)
#     st.info("Run Time for Translate_MODULE  =  " + str((end_Translate_MODULE - start_Translate_MODULE)*1000))



#     st.subheader("Transformer model based")

#     result_pre_train  = transformers.pipeline(task_name, model=model_name, tokenizer=model_name, use_auth_token=False)
#     start_pre_train = time.time()
#     output =  result_pre_train(text_area)[0]["translation_text"]
#     end_pre_train = time.time()
#     st.success(output)
#     st.info("Run Time for pre_trained model  =  " + str((end_pre_train - start_pre_train)*1000))

    







    
