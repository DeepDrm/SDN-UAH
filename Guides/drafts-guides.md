
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


Link paper sobre In-band:
https://www.researchgate.net/publication/291952929_In-band_control_queuing_and_failure_recovery_functionalities_for_openflow

REF: Sharma, Sachin & Staessens, Dimitri & Colle, Didier & Pickavet, Mario & Demeester, Piet. (2016). In-band control, queuing, and failure recovery functionalities for openflow. IEEE Network. 30. 106-112. 10.1109/MNET.2016.7389839. 

Resumen:

Requisitos:

1. Cada Sw necesita su propia IP.
2. Cada Sw debe conocer la IP y puerto TCP del controlador.
3. Se debe configurar el path de los Sw no conectados directamente al controlador.

Soluciones:

- 1. y 2. : 
        - Cada Sw ejecuta un cliente DHCP
        - Cada Sw ejecuta un hybrid stack para su propio tráfico DHCP.
        - Serv. DHCP se configura con vendor-especific option con la IP y puerto de Co.
        - DHCP server en el Co.
- 3. :
        - DHCP serv. establece path en los Sw que ya tienen una sesión OpenFlow.

Realización:

1. Notificación de los parámetros de red requeridos:
2. Establecimiento de conexión TCP con Co.
3. Establecimiento sesión OpenFlow.
4. Descubrimiento topología.

![Alt Text](https://github.com/DeepDrm/SDN-UAH/blob/develop/Images/D-Estados-PaperIn-Band.jpg)



