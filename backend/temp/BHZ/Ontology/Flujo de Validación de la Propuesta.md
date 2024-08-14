---
tags:
  - Entity
aliases:
  - Flujos de Validación
---

Los flujos de validación indican qué perfiles deben realizar la validación en cada paso. 

Un Flujo de Validación es una secuencia de aprobadores (pasos), indicando qué Rol debe realizar la Validación.

Si se superan todos los pasos, la [[Oportunidad]] pasa al estado **Validada**; si no, vuelve al estado **En Preparación**.

# Atributos

| Atributo | Descripción                                                                                                                                                                                                                                                                                                                 | Tipo             |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Código*  | Código de flujo.                                                                                                                                                                                                                                                                                                            | Autonumérico     |
| Nombre*  | Nombre del flujo                                                                                                                                                                                                                                                                                                            | Alfanumérico     |
| Paso*    | Número de paso. Indica el perfil que realizará la validación en cada uno de los pasos                                                                                                                                                                                                                                       | Numérico         |
| Perfil*  | Perfil que realiza la validación en el paso asociado del flujo. Posibles valores:<br>- CONTROL DE GESTIÓN. <br>- RESPONSABLE UNIDAD NEGOCIO<br>- RESPONSABLE OFICINA<br>- DIRECTOR OPERACIONES <br><br>Nota: Si la Oficina no tiene Unidades de Negocio el paso de validación de Responsable de Unidad de Negocio se salta. | Lista de valores |

Ejemplo:

| Cod Flujo | Nombre Flujo | Paso | Perfil Validador     |
| --------- | ------------ | ---- | -------------------- |
| 1         | OP Sencilla  | 1    | CONTROL GESTION      |
| 2         | OP Media     | 1    | CONTROL GESTION      |
| 2         | OP Media     | 2    | RESP OFICINA         |
| 3         | OP Compleja  | 1    | CONTROL GESTION      |
| 3         | OP Compleja  | 2    | RESP OFICINA         |
| 3         | OP Compleja  | 3    | Director Operaciones |
Si al evaluar las [[Regla de Validación|Reglas de Validación]] resultara como Flujo de Validación el 2, entonces la [[Oportunidad]] debe ser aprobada por:
- Control de Gestión
- Responsable de la Oficina
