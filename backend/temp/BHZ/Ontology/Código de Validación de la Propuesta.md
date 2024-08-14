---
tags:
  - Entity
---
Identificador de la [[Propuesta]] Validadas. 

El código es una cadena de texto con la siguiente estrucutra:

"Validada (AÑO.MES.ID-COD_CLIENTE.OFERTA.VERSION)” 

- AÑO: 2 últimas cifras del año actual. 
- MES: Número del mes.
- ID: código correlativo
- COD_CLIENTE: Código del cliente asociado a la oportunidad. 
- OFERTA: Es el número de oportunidades(ofertas) creadas para un mismo cliente 
- VERSIÓN: Número de propuestas validadas, es decir, han llegado a estar en el estado "Validada" y antes de ganarla o perderla se han modificado. Esta acción automática se ejecutará en el momento que [[Control de Gestión]] valide completamente el flujo de la [[Propuesta]].

En formato RegExp:
\\d{2}\\.\\d{1,2}\\.\\d+\\-\\d+\\.\\d+\\.\\d+

Ejemplo de Código de Validación: 24.7.9319-682.68.2