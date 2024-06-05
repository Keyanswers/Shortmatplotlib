# Importando las librerias que voy a usar
import pandas as pd
import matplotlib.pyplot as plt

# Crear una serie G1 con datos de abundancia de diferentes géneros
# y sus índices correspondientes
G1 = pd.Series([15, 45, 86, 79, 35, 25, 7, 45, 79, 12],
               index=["Lobatus", "Callinectes", "Tellina", "Chione", "Penaeus",
                      "Americoliva", "Posidonia", "Cliona", "Achelous", "Porites"])
# Ordenar la serie G1 en orden descendente
G1 = G1.sort_values(ascending=False)

# Crear una serie G2 con datos de abundancia de más géneros
# y sus índices correspondientes
G2 = pd.Series([15, 45, 86, 79, 35, 25, 7, 45,
                79, 12, 5, 34, 18, 25, 23, 26, 78, 128, 96, 25,
                45, 63, 78, 98, 87, 54, 56, 21, 16, 74],
               index=["Lobatus", "Callinectes", "Tellina",
                      "Chione", "Penaeus", "Americoliva",
                      "Posidonia", "Cliona", "Achelous",
                      "Porites", "Craniella", "Corymorpha",
                      "Ectopleura", "Kaburakia", "Parviplana",
                      "Enchiridium", "Chaetoderma", "Lottia",
                      "Haliotis", "Calliostoma", "Pomaulax",
                      "Lirobittium", "Melanoides", "Crucibulum",
                      "Felimare", "Doriopsilla", "Ancula",
                      "Acteocina", "Aplysiopsis", "Nucula"])

# Mostrar la serie G2
G2

# Crear una nueva figura y graficar G2 como
# un gráfico de barras
plt.figure()
G2.plot(kind='bar')
plt.show()

# Graficar G2 en diferentes tipos de gráficos
G2.plot(kind='barh')  # Gráfico de barras horizontal
G2.plot(kind='hist')  # Histograma
G2.plot(kind='box')   # Gráfico de caja (boxplot)
G2.plot(kind='area')  # Gráfico de área
G2.plot(kind='kde')   # Estimación de densidad del núcleo (KDE)
plt.clf()  # Limpiar la figura actual
G2.plot(kind='pie')   # Gráfico de pastel (pie chart)

# Ordenar la serie G2 en orden descendente y graficar como un
# gráfico de barras con estilo personalizado
G3 = G2.sort_values(ascending=False)
G3.plot(kind='bar', color='firebrick')
plt.title('Abundance by Genera',
          fontsize=30,
          fontname='Times New Roman',
          fontweight='bold')
plt.xlabel('Genera',
           fontsize=21,
           fontname='Times New Roman',
           fontweight='bold')
plt.ylabel('Abundance Ind $Km^2$',
           fontsize=21,
           fontname='Times New Roman',
           fontweight='bold')
plt.xticks(fontsize=16,
           fontname='Times New Roman',
           fontstyle='italic',
           rotation=90)
plt.yticks(fontsize=21,
           fontname='Times New Roman')

# Crear una nueva figura y ejes para un gráfico
# de pastel de la serie G1
fig, ax = plt.subplots()
patches, texts, autotexts = ax.pie(G1,
                                   labels=G1.index, autopct='%1.1f%%',
                                   pctdistance=0.85)

# Personalizar el estilo de las etiquetas de los segmentos
# del gráfico de pastel
for text in texts:
    text.set_fontstyle('italic')
    text.set_fontsize(19)

# Personalizar el estilo de los textos automáticos que muestran
# los porcentajes en el gráfico de pastel
for autotext in autotexts:
    autotext.set_fontsize(19)
