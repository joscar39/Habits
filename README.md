# qa_automation

Desglose de contenido

	1. Carpeta .idea : Contenido que conforma el entorno de desarrollo de pruebas

	2. Carpeta .pytest_cache: Cache de ejecuciones de pruebas en pytest

	3. Carpeta _pycache__ : Listado de ejecuciones de test mediante pytest

	4. Carpeta AutoAPI: esta carpeta pertenece al proceso de automatizaciones en API REST, la herramienta utilizada es Jmeter, el contenido de la carpeta es:

		- Login y Dashboard.jmx : Contiene el codigo de ejecucion de pruebas automatizadas en el inicio de la app donde cargan los recursos graficos y se muestra el inicio de la app en la seccion dashboard
		
		- ModuloLogin.jmx: Ejecucion de prueba sobre 100 usaurio iniciando sesion en un intervalo de 5 min, este archivo puede modificarse para simular distinto lote de usaurio para diferentes escenarios de prueba

		- ModuloRegistro.jmx: Ejecucion de prueba sobre simulacion en carga extrema de usaurio que intentan registrarse en un intervalo de tiempo determinado, este archivo puede modificarse para cambiar los distintos parametros de usuarios en distintos escenarios

		- Summary.csv : Archivo con el resultado de la ejecucion de la prueba, arrojando muestreo de tiempos de ejecucion, porcentaje de efectividad de lso request y peticiones realizadas en la prueba

	5. Carpeta PageObjectModel: Contiene archivos .py que contienen las clases donde se almacenan todos los localizadores utilzados tanto en web concola como en app habits
		
		- Carpeta action_app: Contiene los archivos:
			
			* Element_constant.py: Agrupa las funciones que ejecutan acciones que no varian dentro del app como lo es pulsar boton volver atras, abrir menu de hamburguesa entre otros

			* RequesUtils.py: Contiene todas las funciones para ejecutar request dentro de un flujo de prueba
			* Scroll_utils.py: Contiene las funciones que permiten hacer diversos tipos de scroll dentro del app
			* Tap_Drag_Utils.py : Contiene funciones que permiten hacer click, gestos y otras acciones dentro del app
		- Carpeta FlowsConstant: Contiene los archivos:
			
			* LoginAndRegister.py: Funciones de flujos completos donde se realizar la accion de iniciar sesion sencillo e inciar sesion configurando el modo develop o modo produccion

		- Carpeta Global_variables: Contiene los archivos:

			* Path_Data-py: Se encuentran todos las funciones que guardan valores constantes dentro de las rutas para llamar archivo de data driven, path de almacenamiento de evidencia entre otras

			* Set_Dev_Mode: Contiene las funciones que permiten configurar el modo desarrollo, modo produccion o modo personalizado que almacena un path para debuggear el app
	
	6. Archivo recursos.zip : Este archivo es un comprimido con todos los recursos de los distintos file.py, donde es importante descompimir usando la opcion "Extraer aqui", es necesario descomprimir el archivo para que se puedan acceder a los distintos archivos que fungen como BD de pruebas y para generar evidencia y acceder a los controladores y driver de selenium y appium. Al mismo tiempo se encuentr alojados todos lso reportes de pruebas ejecutados organizados por carpeta de apk y sub carpetas pro fecha y modulo corrido


	7. Carpetas Script: Esta carpeta contiene todos los archivos .py, los cuales son los distintos modulos automatizados dentro de los flujos de prueba de la aplicacion, estan ordenados alfabeticamente segun su orden de ejecucion, para ejecutar dichos archivos valga la redundancia.
	
	Nota: El archivo conftest.py Contiene la configuracion de appium driver la cual hace el llamado al cap desire donde se modifica el modelo de dispositivo a usar para automatizaciones y tambien el remote webdriver para colocar la ipa del server a usar para correr pruebas

	8. Carpeta UnitTest: Esta carpeta contiene archivos.py que ayudan a complementar las pruebas unitarias o para realizar flujos puntuales que faciliten la pruebas manuales como por ejemplo:
		Correr cronjob para procesar un reto
		Correr el habito diario de los usaurio por 28 dias, simulando un dia a la vez
		Inyectar data de salud para un usuario en especifico
		Procesar retos mediante el waiting room de retos grupales
		RetoGrupal, permite procesar un reto en especifico mediante la posicion de data de la empresa que este creada dicho reto



::::::::::::::::: IMPORTANTE ::::::::::::::::

Para las automatizaciones de API, es importante cambiar las rutas de los sampler de CSV con la ruta donde descargaran la carpeta de recursos, de esta forma el proyecto se ejecutara sin problemas

Para correr las automatizaciones de appium es necesario contar con:

	- Appium Desktop (Se descarga desde la direccion appium.io)
	- Java sdk
	- python 3.0 en adelante
	- pychamr community Edition 2021.3.2
	- Android studio SDK
	- selenium 4.0
NOTA: Descargar y actualziar el chromedriver a la misma version que mantenga en el navegador del equipo donde se correran las pruebas, una vez descargado el archivo chromedriver.exe, sustituirlo por que se encuentra ubicado en la ruta /qa_automation/recursos

Para ejecutar las automatizaciones se debera:

	1. configurar en el archivo /Scripts/conftest.py los capabilities de la funcion "appium_server"
 		- cambiar los datos de platformVersion donde se debera colocar la version de android del dispositivo donde se correra la prueba
		-Cambiar los datos de deviceName donde se colocara el nombre del dispositivo conectado al ordenador o laptop (Este deviceName se obtiene desde un terminal teniendo instalado el SDK de android, se ejecutara el comando: adn devices -l)
	2. Abrir el Appium server, y en la direccion ip colocar: localhost


