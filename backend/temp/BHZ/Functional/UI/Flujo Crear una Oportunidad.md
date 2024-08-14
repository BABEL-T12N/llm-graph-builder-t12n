---
tags:
  - UI_Component
---

Para crear una [[Oportunidad]] se utilizará un flujo de Pantallas y Componentes para hacer más fácil el proceso.

A continuación se describe el flujo de Pantallas:
- Selección del [[Cliente]] de la Oportunidad. (ver [[Componente Selector de Clientes]])
- Formulario de Datos Principales de la Oportunidad. 
- Selección de Contactos. [[Componente Selector de Contactos]]
- Formulario de Detalle de la Oportunidad. 

Esta secuencia de pasos incluyen las siguientes acciones:
- Continuar. Valida y permite avanzar en el flujo
- Guardar. Guarda los datos y cierra el Flujo. La Oportunidad se crea en estado Borrador



## Selección del Cliente
Se invoca al  [[Componente Selector de Clientes]] para seleccionar al [[Cliente]]. 
Si se cancela este paso, la Oportunidad no se crea.
## Formulario de Datos Principales de la Oportunidad


![[Formulario Datos Principales Oportunidad Page.png]]


Este Componente cuenta con los siguientes campos:
- Título
- Descripción. 
- [[Responsable de la Oportunidad]]
- [[Sociedad]]
- [[Unidad de Negocio]]
- [[Colaborador|Colaboradores]]. [[Componente Selector Múltiple con Filtro]]

Tiene las siguientes acciones:
- Guardar. Permite guardar la Oportunidad en estado Identificada. 
- Continuar. Permite guardar la Oportunidad en estado Identificada y continuar con el flujo. 

## Selección de Contacto
En este paso del flujo se selecciona un Contacto asociado a dicho Cliente.
Desde la pantalla del [[Componente Selector de Contactos]] el Usuario podrá seleccionar un Contacto existente o incluso [[Crear un Contacto]]
## Formulario Detalle Oportunidad
En este paso se muestra el siguiente formulario:
![[Formulario Detalle Oportunidad Component.png]]