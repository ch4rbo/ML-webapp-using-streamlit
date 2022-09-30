# Resumen del proceso

1. Se crea app para el modelo coffee_model.pkl usando Streamlit.

2. El modelo toma valores de las siguientes variables:
* country, una de las siguientes opciones: Brazil, Colombia, Guatemala, Mexico, Taiwan, Other
* variety, una de las siguientes opciones: Bourbon, Catuai, Caturra, Typica, Other
* aroma, una barra deslizante que toma valores flotantes entre 0.00 y 10.00 con paso 0.01
* aftertaste, idem variety
* acidity, idem variety
* body, idem variety
* balance, idem variety
* moisture, una barra deslizante que toma valores flotantes entre 0.00 y 1.00 con paso 0.01

3. Por defecto country=Brazil, variety=Bourbon y las demás valen 0.00. Se imprime texto que indica que deben cargarse valores para realizar la predicción.

4. A medida que se completa cada campo se actualiza el resultado, siendo las opciones de respuesta dos (en función del resultado de la predicción):
* Es un café de especialidad.
* No es un café de especialidad.

Esto permite visualizar la sensibilidad de los parámetros respecto al resultado de la predicción

https://coffeeapii.herokuapp.com/