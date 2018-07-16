
Git y GitHub:

Creación de:
•	Repositorio
•	Proyecto

Ref: https://guides.github.com/activities/hello-world/

Conexión con Visual Studio Code mediante SSH: 

Ref: https://help.github.com/articles/connecting-to-github-with-ssh/
https://www.digitalocean.com/community/tutorials/how-to-use-git-branches#merging-code-between-branches

Añadir un repositorio: git remote add origin(nombre que se quiera) direccSSH o direccHTTP

Añadir archivo: `git add NombreArchivo` `git commit -m "develop file" NombreArchivo`

Cambiar de branch: `git checkout NombreBranch`

Merge (Fusionar; desde una branch1): `git merge NBranch2 --no-ff`
 
-----------------------------------------------------------------------------
	  
Mininet:

Instalación: 

Ver issue Instalación Mininet con Git.

Guía: http://mininet.org/walkthrough

Comandos:

•	Limpiar Mininet: sudo mn -c
•	Crear escenario con comandos: sudo mn --topo TipoTopo,NHost
o	Topología; single = 1 switch, linear = 1 switch por host
•	Link variations: sudo mn --link tc,bw=10,delay=10ms
•	Other Switch Types: 
o	sudo mn --switch user     
o	sudo mn --switch ovsk   (OVS, Open vSwitch)
•	Everything in its own Namespace (user switch only): S y C normalmente en root con esto no.
o	sudo mn --innamespace --switch user
•	MAC simplificada: --mac
•	Python commands: py loquequierasejecutar
•	Links Up/Down: Tirar un enlace: link s1 h1 down (o up)
•	Ver terminales: xterm h1
