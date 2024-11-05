import re
import nltk
from collections import Counter
import fitz # PyMuPDF

# Carga de Documentos (PDFs)
def extraer_texto_pdf(archivo_path):
  texto = ""
  with fitz.open(archivo_path) as pdf:
    for pagina in pdf:
      texto += pagina.get_text()
  return texto

def extraer_palabras_clave(texto):
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    
    # Eliminar caracteres especiales y dividir el texto en palabras
    palabras = re.findall(r'\w+', texto.lower())
    
    # Filtrar palabras comunes usando una lista de stopwords
    stop_words = set(stopwords.words('spanish'))
    palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words]
    
    # Contar la frecuencia de cada palabra y devolver las más comunes
    frecuencia = Counter(palabras_filtradas)
    palabras_clave = [palabra for palabra, _ in frecuencia.most_common(10)]  # Top 10 palabras clave
    
    return palabras_clave