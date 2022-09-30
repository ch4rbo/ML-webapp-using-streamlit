# primero en consola: pip install -r requirements.txt
import pandas as pd
import numpy as np
import sklearn
import streamlit as st
import pickle

def main():

    st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
    st.title('Welcome to my coffee specialty prediction app using Streamlit')

    # hay que ver bien cuales son los rangos de valores de las variables del modelo
    country = st.selectbox("Select a country:", ('Brazil', 'Colombia', 'Guatemala', 'Mexico', 'Taiwan', 'Other'))
    variety = st.selectbox("Select a variety:", ('Bourbon', 'Catuai', 'Caturra', 'Typica', 'Other'))
    aroma = st.slider("Choose an aroma: ", min_value=0.00, max_value=10.00, value=0.00, step=0.01)
    aftertaste = st.slider("Choose an aftertaste: ", min_value=0.00, max_value=10.00, value=0.00, step=0.01)
    acidity = st.slider("Choose an acidity: ", min_value=0.00, max_value=10.00, value=0.00, step=0.01)
    body = st.slider("Choose a body: ", min_value=0.00, max_value=10.00, value=0.00, step=0.01)
    balance = st.slider("Choose a balance: ", min_value=0.00, max_value=10.00, value=0.00, step=0.01)
    moisture = st.slider("Choose a moisture: ", min_value=0.00, max_value=1.00, value=0.00, step=0.01)

    # cargar el modelo
    loaded_model = pickle.load(open('coffee_model.pkl', 'rb'))

    # data frame a predecir
    cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']
    data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns = cols)

    posted_default = pd.DataFrame(np.array(['Brazil', 'Bourbon', 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]).reshape(1,8), columns = cols)

    if posted.equals(posted_default):
        st.markdown('### **Select the parameters to analyze coffee specialty prediction**')
    else:
        # predicción
        result = loaded_model.predict(posted)

        # salida a mostrar
        text_result = result.tolist()[0]
        if text_result == 'Yes':
            st.markdown('### **It is a specialty coffee**')
        else:
            st.markdown('### **It is not a specialty coffee**')

if __name__ == "__main__":
    main()

# desde consola: streamlit run app.py

## prueba para si: Guatemala/Bourbon/7.83/7.67/7.33/7.67/7.67/0.11
# ## prueba para no: Other/Other/7.25/6.83/7.17/7.00/7.17/0.11
