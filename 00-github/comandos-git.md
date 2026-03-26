# Comandos básicos de Git

Este archivo contiene una breve descripción de algunos comandos útiles de Git.

## Comandos

### `git status`
Muestra el estado del repositorio, indicando:
- Archivos modificados.
- Archivos nuevos no rastreados.
- Cambios listos para ser confirmados (staged).

### `git add .`
Añade todos los archivos modificados y nuevos al área de preparación (staging area), preparándolos para ser confirmados.

### `git commit -m "lorem ipsum"`
Registra los cambios en el repositorio con un mensaje descriptivo, en este caso "lorem ipsum".

### `git push`
Envía los commits locales al repositorio remoto.

### `git diff --name-status main`
Muestra una lista de archivos con sus nombres y el estado de los cambios (modificado, añadido o eliminado) comparados con la rama principal (`main`).

### `git difftool main`
Permite visualizar las diferencias entre la rama actual y la rama principal (`main`) utilizando una herramienta gráfica o de comparación externa configurada en Git.

### `git checkout -b nombre_branch`
Crea una nueva rama llamada `nombre_branch` y cambia a ella de forma inmediata.

### `git reset --hard [SHA-Commit al que quieres volver]`
Restaura el estado del repositorio al commit especificado por su SHA. Este comando sobrescribe los cambios no confirmados y los elimina definitivamente.

### `git merge develop`
Fusiona los cambios de la rama `develop` en la rama actual. Si hay conflictos, Git solicitará resolverlos antes de completar la fusión.

### `git log`
Muestra el historial de commits en el repositorio, incluyendo mensajes de commit, autores y hashes.

### `git branch`
Lista todas las ramas en el repositorio. La rama actual se marca con un asterisco.

### `git branch -d nombre_branch`
Elimina una rama local llamada `nombre_branch`.

### `git branch -D nombre_branch`
Elimina forzadamente una rama local, incluso si tiene cambios no fusionados.

### `git branch -a`
Muestra todas las ramas del repositorio, tanto locales como remotas.

### `git stash`
Guarda los cambios no confirmados en un área temporal (stash) para que puedas trabajar en algo más sin perder el progreso.

### `git stash pop`
Recupera los cambios guardados en el stash y los aplica a la rama actual.

### `git fetch`
Descarga los cambios del repositorio remoto sin aplicarlos a tu rama local.

### `git pull`
Combina `git fetch` y `git merge`. Descarga los cambios del repositorio remoto y los fusiona con tu rama actual.

### `git rebase main`
Reaplica los commits de la rama actual sobre la rama principal (`main`). Útil para mantener un historial de commits limpio.

### `git clone [URL]`
Crea una copia local de un repositorio remoto desde la URL proporcionada.

### `git remote -v`
Lista las URL de los repositorios remotos asociados con tu repositorio local.

### `git restore <file>`
Restaura un archivo específico al estado del último commit confirmado, descartando los cambios no confirmados.

### `git checkout main`
Cambia a la rama principal llamada `main`. Útil para moverte rápidamente entre ramas.

### `git fetch origin`
Descarga los cambios de `main` desde el repositorio remoto sin fusionarlos automáticamente.

### `git pull origin main`
Descarga y fusiona los últimos cambios de la rama `main` desde el repositorio remoto.

### `git merge origin/main`
Fusiona manualmente los cambios de `main` desde el repositorio remoto en tu rama actual.

### `git merge feature-x`
Para fusionar los cambios comiteados de branch feature-x con tu rama actual.

### `git add archivo-con-conflicto`
### `git commit`
Git te avisará qué archivos están en conflicto. Debés abrirlos, resolver los conflictos manualmente, y luego ejecutar estos 2 comandos.

### `git push -u origin release/v1.0.0`
Sube una rama `release` (u otra cualquiera) al repositorio remoto y establece el seguimiento entre la rama local y remota. Luego podrás usar simplemente `git push` o `git pull` sin especificar el nombre de la rama.


### `git rm -r --cached .dart_tool`
Elimina la carpeta `.dart_tool` del índice de Git (control de versiones) sin borrarla del disco, útil para corregir archivos que deberían estar ignorados.

---

Estos comandos son útiles para trabajar de manera eficiente con Git. ¡Practícalos para familiarizarte con su funcionamiento!
