import re
t= "Cerca de un bosque hermoso vivían tres osos. Estos sos eran muy buenos y amables. Habían construido una  casa cómoda solamente con una puerta y una ventana. Unode los osos era muy pequeño, uno de tamaño mediano y el otro muy grande. Tenían en la casa todo lo necesario. Tenían un plato pequeño para el oso pequeño, un plato mediano para el oso  mediano, y un plato grande para el oso grande. Tenían una silla pequeña para el oso pequeño, una silla mediana para el oso mediano, y una silla grande para el oso grande. Tenían una cama pequeña para el oso pequeño, una cama mediana para el oso mediano, y una cama grande para el oso grande. Y esto era todo. Una mañana tenían sopa para el almuerzo. Echaron la sopa en los platos. Pero la sopa estaba tan caliente que no podían tocarla con la lengua. Los osos, como Vds. saben, no emplean ni cucharas, ni cuchillos, ni tenedores. Los platos  de sopa estaban en el suelo, porque los osos no emplean mesas.  –Vamos a dar un paseo,–dijo el oso grande;–y cuando volvamos podemos tomar la sopa. Los osos tenían hambre, mucha hambre, pero eran muy pacientes y salieron todos a dar un paseo por el bosque; primero  el oso grande, después el oso mediano y por último el oso pequeño. Poco después entró una niña en el bosque. Vio la pequeña casa pero no sabía de quién era. Pensaba que la casa era muy hermosa y quería entrar para verla. Así, llamó a la puerta. Nadie respondió. Ella creía que todas las personas de la casa estaban dormidas. Llamó otra vez, pero nadie respondió. Ahora creía la niña que nadie estaba en la casa. Abrió la puerta y entró. Todo parecía tan cómodo que quería quedarse allí algunos minutos. Estaba muy cansada y quería descansar. Vio la niña los tres platos en el suelo. Tenía mucha hambre y quería probar la sopa. Probó la sopa que estaba en el plato grande. Estaba muy fría. Entonces probó la sopa que estaba en el plato mediano; pero estaba muy caliente. Entonces  probó la sopa que estaba en el plato pequeño y le gustó tanto que se la tomó toda. Al otro lado del cuarto estaban las tres sillas. La niña quería descansar antes de ir a casa. Primero probó la silla grande; pero era muy alta. Después probó la silla mediana; pero era muy ancha. Por último probó la silla pequeña; pero al sentarse en ella la hizo pedazos. Luego vio las camas en la alcoba, y quería dormir la siesta antes de ir a casa. Primero probó la cama grande; pero era demasiado blanda. Después probó la cama mediana; pero era demasiado dura. Por último probó la cama pequeña y como era muy cómoda y le gustó, se echó en ella y se durmió. Mientras dormía los tres osos volvieron a casa. Tenían hambre después de su paseo y querían tomar la sopa. El oso  grande levantó su plato y bramó: –¡Alguien ha probado mi sopa! Entonces el oso mediano levantó su plato y gruñó: –¡Alguien ha probado mi sopa también! Por último el oso pequeño levantó su plato y gritó: –¡Alguien ha probado mi sopa y se la ha tomado! Entonces fueron todos al otro lado del cuarto a sentarse en sus sillas. Primero el oso grande probó su silla y bramó: –¡Alguien se ha sentado en mi silla! Entonces el oso mediano probó su silla y gruñó: –¡Alguien se ha sentado en mi silla también! Entonces el oso pequeño probó su silla y gritó: –¡Alguien se ha sentado en mi silla y la ha hecho pedazos! Después entraron todos en la alcoba. El oso grande fue el primero que vio su cama y bramó: –¡Alguien ha dormido en mi cama! Entonces el oso mediano vio su cama y gruñó: –¡Alguien ha dormido en mi cama también! Por último vio su cama el oso pequeño y gritó con voz aguda: –¡Alguien ha dormido en mi cama y aquí está! Este ruido despertó a la niña. Cuando abrió los ojos y vio a los osos, estaba muy asustada. Se levantó y huyó de la casa.  Los tres osos fueron a la puerta para mirar tras ella. Vieron que ella corría por el bosque hacia su casa. No la persiguieron, porque eran buenos y amables. Y eso es todo lo que sé acerca de la niña y de los tres osos que vivían en el hermoso bosque en la pequeña casa con solamente una ventana y una puerta."
iterador = len(re.findall('oso', t))
print(iterador)
lista = re.findall('..os', t)
print(lista)
patron = re.compile("oso")
nueva_clave = patron.sub("peresozo", t)
print(nueva_clave)
patron2 = re.compile("osos")
nueva_clave2 = patron2.sub("peresozos", t)
print(nueva_clave2)
print(type(patron) + type(patron2))