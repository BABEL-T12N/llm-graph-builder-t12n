---
tags:
  - UI_Component
---
Permite seleccionar varios [[Contacto|Contactos]] o crear un nuevo contacto si no existe. 


![[Selector de Contactos Component.png]]

Este componente puede instanciarse con parámetros de inicio para que muestre únicamente el subconjunto deseado. Por ejemplo, puede pasarse el Código de Cliente para que muestre sólo los Contactos de un Cliente (seleccionado previamente)


El Componente incluye:
- Título dinámico. Al instanciar este componente se puede pasar por parámetro el título para integrarlo mejor en el flujo
- Contador de número de Contactos mostrados. Si se ha aplicado algún filtro mostrará sólo el número total de Contactos filtrados
- Buscador por nombre del Contacto
- Lista de Contactos, mostrando el botón de Añadir a la lista, el nombre del Contacto y su rol.
- Sección de Contactos seleccionados: muestra la lista de Contactos seleccionados (nombre y rol) junto con el botón de eliminar de la lista de seleccionados.

## Acciones

- Botón Continuar, para proceder con el resto del flujo 