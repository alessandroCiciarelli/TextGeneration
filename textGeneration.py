#Librerie
#Impostazioni pagina
import random
import streamlit as st
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;margin:0;}
    .css-18e3th9 { 
    flex: 1 1 0%; 
    width: 100%;
    padding: 1rem!important;
    }
    @media (min-width: 576px)
    .css-18e3th9 {
    padding: 0.5rem!important;
    }

    """
st.markdown(hide_st_style, unsafe_allow_html=True)

try:
    from deep_translator import GoogleTranslator
    from aitextgen import aitextgen
    from streamlit_option_menu import option_menu


    def traduttore(testo, lingua_traduzione):
        try:
            testo_tradotto = GoogleTranslator(source='auto', target=lingua_traduzione).translate(testo)
            return testo_tradotto
        except:
            return 'Traduction Error :('

    #Funzioni di uso genrale
    @st.cache(allow_output_mutation=True, show_spinner=False)
    def load_text_gen_model():
        a = aitextgen()
        return a

    @st.cache()
    def ai_text(inp,lunghezza, temp, num):
        listaTesti = []
        try:
            ai = load_text_gen_model()
            for i in range(num):
                generated_text = ai.generate_one(max_length = lunghezza, prompt = inp, no_repeat_ngram_size = random.randint(3, 5) , temperature = temp)
                listaTesti.append(generated_text)
            ai = None
            return listaTesti
        except:
            return ["Errore","Riprova più tardi"]



    choose = option_menu("Intelligenza Artificiale e SEO 🤖", ["Genera Contenuti"],
                    icons=['keyboard'],
                    menu_icon="app-indicator", default_index=0 ,orientation='horizontal',
                    styles={
    "container": {"color": "blak","padding": "0!important", "background-color": "transparent", "width": "100%"},
    "icon": {"color": "blak", "font-size": "13px", "margin":"0px"}, 
    "nav-link": {"color": "blak!important","font-size": "15px", "text-align": "left", "padding": "5px!important", "margin":"0px", "--hover-color": "#eee"},
    "nav-link-selected": {"color": "blak","background-color": "#02ab21"},
    }
    )

    listLang = ["Italiano", "English", "German", "Spanish", "French", "Portuguese", "Russian", "Japanese", "Chinese", "Korean", "Arabic", "Polish", "Turkish", "Thai", "Vietnamese", "Indonesian", "Czech", "Dutch", "Greek", "Hindi", "Hungarian", "Norwegian", "Swedish", "Ukrainian", "Afrikaans", "Bengali", "Bulgarian", "Danish", "Finnish", "Filipino", "Georgian", "Hebrew", "Hmong", "Hungarian", "Kazakh", "Kyrgyz", "Latvian", "Lithuanian", "Malay", "Mongolian", "Myanmar", "Nepali", "Norwegian", "Pashto", "Persian", "Punjabi", "Romanian", "Serbian", "Somali", "Sotho", "Sundanese", "Tajik", "Tagalog", "Tamil", "Telugu", "Thai", "Turkish", "Uzbek", "Urdu", "Uighur", "Yiddish"]

    tfLang = ["it", "en", "de", "es", "fr", "pt", "ru", "ja", "zh", "ko", "ar", "pl", "tr", "th", "vi", "id", "cs", "nl", "el", "hi", "no", "sv", "uk", "af", "bn", "bg", "da", "fi", "fil", "ka", "kk", "lv", "lt", "ms", "mn", "ne", "nb", "ps", "fa", "fa", "ro", "sr", "so", "su", "tg", "tl", "ta", "te", "th", "tk", "uz", "ur", "ug", "yi"]
    Lang_selectbox = st.selectbox("In che mercato vuoi cercare", listLang)
    idxL = listLang.index(Lang_selectbox)
    selected_lang = tfLang[idxL]
    inp = st.text_area('Scrivi una frase o un paragrafo di ispirazione per la nostra I.A.',height=200)
    c1, c2, c3 = st.columns(3)
    lunghezza = c1.slider('Lunghezza massima del testo generato :', 50, 700,200,10)
    follia = c2.slider('Imposta la "follia" del testo  :', 0.5, 1.0,0.6,0.1)
    numTesti = c3.slider('Numero di testi da generare :', 1, 5,1,1)

    try:
        if st.button("Genera testo🤘") :
            nuovo = traduttore(inp,"en")
            try:
                ai = load_text_gen_model()
                with st.spinner('Aspetta mentre rapiamo un COPYWRITER ... 🤖 Potrebbe volerci qualche minuto 🙏'):
                    inp = ai_text(nuovo,lunghezza,follia,numTesti)
                    ai = None
                    for i in range(len(inp)):
                        with st.expander(f"Genero il testo {str(i+1)}"):
                            st.write(traduttore(inp[i],selected_lang))
                    inp = None  
            except:
                st.error("Il COPYWRITER è riuscito a scappare, riprova 🤔")
    except Exception as e:
        st.error(e)
    finally:
        st.stop()

except Exception as e:
    st.error("Errore: {}".format(e))

