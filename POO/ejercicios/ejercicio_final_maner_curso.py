from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimientos(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"

analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimientos("Im so happy")
print(resultado)