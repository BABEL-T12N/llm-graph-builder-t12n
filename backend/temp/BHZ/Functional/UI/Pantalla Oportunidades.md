---
tags:
  - UI_Component
---

# Descripción

Esta Pantalla muestra una tabla con las Oportunidades del sistema, la cual puede ser filtrada por varios criterios. 

![[Oportunidades Page.png]]

La Pantalla muestra dos filtros rápidos:
- Selector de categorías de Oportunidades
- Filtro por nombre

Las [[Oportunidad|Oportunidades]] se muestran en formato de tabla indicando los siguientes campos:
- Código
- Nombre 
- [[Cliente]]
- [[Gerente|Responsable]]
- [[Unidad de Negocio]]
- Importe
- Última Modificación
- Estado

La tabla de Oportunidades muestra sólo 10 filas y tiene un elemento paginador. 

# Acciones
- Paginación. Muestra un nuevo número de Oportunidades
- Ver Oportunidad. salta a la pantalla [[Pantalla Detalle Oportunidad]]
- Exportar listado en un fichero con formato EXCEL
- Filtrar utilizando un formulario avanzado
- Filtrado rápido por:
	- Grupos de Oportunidades, seleccionable de una lista. 
		- Todas las Oportunidades
		- Todas mis Oportunidades
		- 
	- texto a nivel  de Nombre de la Oportunidad, o el Código de la Oportunidad


## Filtro avanzado
El filtro avanzado nos permite buscar por los siguientes campos:
- Sociedad. 
- [[Unidad de Negocio]]. Lista o seleccionable de una opción.
- [[Área de Operaciones]]. 
- Responsable. 
- [[Colaborador]].
- Estado. 
- Fecha de Creación. Especificando un rango de fechas
- Fecha de Cierre. Especificando un rango de fechas.
- Importe. Especificando un rango numérico.
- [[Actividad]] Principal. 
- Subactividad. 
- [[Tecnología]]
- [[Código de Validación de la Propuesta]]
- [[Línea de Servicio]]
- [[Modelo de Ejecución]]


![[Filtro Oportunidades Component.png]]