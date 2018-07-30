
Git y GitHub:

Creación del repositorio y proyecto.
Ref: https://guides.github.com/activities/hello-world/

Conexión con Visual Studio Code mediante SSH: 
Ref: https://help.github.com/articles/connecting-to-github-with-ssh/
https://www.digitalocean.com/community/tutorials/how-to-use-git-branches#merging-code-between-branches

Añadir un repositorio: `git remote add origin(nombre que se quiera) direccSSH o direccHTTP`

Añadir archivo: `git add NombreArchivo` `git commit -m "develop file" NombreArchivo`

Cambiar de branch: `git checkout NombreBranch`

Merge (Fusionar; desde una branch1): `git merge NBranch2 --no-ff`
 
-----------------------------------------------------------------------------
	  
Mininet:

Instalación: 

Ver issue Instalación Mininet con Git.

Guía: http://mininet.org/walkthrough

Comandos:

- Limpiar Mininet: `sudo mn -c`
- Crear escenario con comandos: `sudo mn --topo TipoTopo,NHos` Topología; single = 1 switch, linear = 1 switch por host
- Link variations: `sudo mn --link tc,bw=10,delay=10ms`
- Other Switch Types: `sudo mn --switch user` `sudo mn --switch ovsk   (OVS, Open vSwitch)`
- Everything in its own Namespace (user switch only): S y C normalmente en root con esto no. `sudo mn --innamespace --switch user`
- MAC simplificada: `--mac`
- Python commands: `py loquequierasejecutar`
- Links Up/Down: Tirar un enlace: `link s1 h1 down (o up)`
- Ver terminales: `xterm h1`

-------------------------------------------------------------------------------------

Ryu:

Instalar Ryu: `sudo apt install python-pip` `pip install ryu`

Nota: para ejecutar, hacerlo en /home/ser/ryu 

---------------------------------------------------------------------------------------

In-Band: SDN Control

Note: Todos los gráficos han sido creados mediante draw.io.

1. Creación por defecto de Mininet: 

Topología de 3 switch conectados a un controlador:

Todos ellos cuentan con una conexión TCP al controlador y además se interconectan entre ellos. Para su creación; `sudo mn

![Alt text](https://github.com/DeepDrm/SDN-UAH/blob/develop/Images/Out-of-band-Sw-TCP-ALL.jpg)






