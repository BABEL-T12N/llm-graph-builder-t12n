---
tags:
  - UI_Component
aliases:
  - Ficha de la Oportunidad
---

![[Detalle Oportunidad Page.png]]

Pantalla que muestra el detalle de una [[Oportunidad]] en modo consulta.
Contiene las acciones necesarias para editar y completar su información. 

Esta pantalla incluye las siguientes secciones:
- Principal:
	- Título de la Oportunidad
	- [[Cliente]]
	- Estado. Componente de tipo Selector que permite cambiar de estado la Oportunidad. Las opciones disponibles dependerán del estado actual, y se muestran los estados a los que se pueden transitar desde allí (ver sección Ciclo de Vida de la Oportunidad)
	- [[Colaborador | Colaboradores]]. Se muestra la foto de los Colaboradores. 
	- Histórico de Comentarios. 
- Detalle de la Oportunidad:
	- Importe
	- Moneda
	- Probabilidad.
- Subactividades. Mostradas en formato tabla con las siguientes columnas: [[Actividad]], [[Subactividad]], Porcentaje y [[Línea de Servicio]]. 
	- Incluye la acción de Añadir una nueva Actividad
- [[Contactos]]. 
- Oportunidades Relacionadas. Tabla indicando Oportunidades que pueden tener relación a nivel de Cliente, Actividades o Tecnologías. Se muestras las columnas: Código, Nombre, Cliente, Fecha de Última Modificación y Estado. 
- 

# Acciones
- Crear una copia de la Oportunidad
- Consultar el histórico de Versiones
- Editar la Sección Principal. Botón con el icono de lapiz.
- Editar la Sección Detalle de la Oportunidad
- Añadir Subactividades

# Comportamiento
- Cuando una Oportunidad pasa a un estado final no se podrá modificar ningún dato, y por tanto los botones de Edición quedarán deshabilitados
- Cuando una Oportunidad está en estado En Validación no se puede modificar ningún dato de la Oportunidad, excepto el estado y los comentarios
- 