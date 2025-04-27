# Analisis Ajedrez
Flujo de Power Automate Desktop realiza un análisis de la partida con comentarios por cada jugada y una estimación del ELO que cada jugador ha tenido en la partida y la importa en un estudio en Lichess.

Para utilizarlo, instalar el Power Automate Desktop en Windows, crear un nuevo flujo, llamarlo Análisis Ajedrez y copiar el contenido del archivo "Análisis Ajedrez.txt" y hacer control-V en el flujo que acabamos de crear vacío.

Luego crear las siguientes variables de entrada:

Información:
------------
Nombre de variable y Nombre externo: Información

Valor predeterminado: 

Este proceso realiza un análisis de la partida con comentarios por
cada jugada y una estimación del ELO que cada jugador ha 
tenido en la partida y la importa en un estudio en Lichess.

El proceso se inicia en una partida de Chess.com, obteniendo el 
PGN de la partida e importándolo en Lichess. Obtemos el análisis
de la partida que hace Lichess y los datos de las jugadas (con más
detalle gracias al script de TamperMonkey).

Llamamos a la IA de Gemini para que nos realice los comentarios 
de cada jugada y finalmente importamos la partida en un estudio
privado en Lichess.

Requisitos
------------
Nombre de variable y Nombre externo: Requisitos

Valor predeterminado: 

Esta versión fue probada con el navegador Brave, la extensión
de Tampermonkey v5.3.3 y el script de  Lichess - Detailed Moves
(Games & Studies), que es una versión modificada por mi de 
Lichess - Detailed Moves (con este también funciona). 
La IA utilizada es Gemini 2.5 Pro Preview 03/25

Uso:
----
Nombre de variable y Nombre externo: Uso

Valor predeterminado: 

Cuando termines una partida en chess.com, no le des al botón de
revisar la partida, solo dale a iniciar este proceso.
