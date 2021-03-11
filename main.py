from selenium import webdriver

DRIVER_PATH = '/home/eric/Desktop/chromedriver'
LOGIN_URL = 'https://formulario-ddjj.argentina.gob.ar/certificado/santa-fe/categoria/8'

driver = webdriver.Chrome(DRIVER_PATH)
driver.get(LOGIN_URL)

nombre = 'Eric'
apellido = 'Luna'
dni = '37845645'
nro_tramite = '11111'
genero = '(M) Masculino'
cuil = '20378456457'
cel_code_area = '343'
cel_numero = '4102055'
email = 'hello@ericluna.dev'
domicilio = 'Cruz Roja Argentina 1556'
domicilio_info_extra = '9A'
cod_postal = '3000'
provincia = 'Santa Fe'
localidad = 'Santa Fe'
patente = 'AA489CC'

driver.find_element_by_id('nombre').send_keys(nombre)
driver.find_element_by_id('apellido').send_keys(apellido)
driver.find_element_by_id('dni').send_keys(dni)
driver.find_element_by_id('dni_confirm').send_keys(dni)
driver.find_element_by_id('nro_tramite').send_keys(nro_tramite)
driver.find_element_by_id('nro_tramite_confirm').send_keys(nro_tramite)
driver.find_element_by_id('genero').send_keys(genero)
driver.find_element_by_id('cuil').send_keys(cuil)
driver.find_element_by_id('cel_cod_area').send_keys(cel_code_area)
driver.find_element_by_id('cel_numero').send_keys(cel_numero)
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('email_confirm').send_keys(email)
driver.find_element_by_id('domicilio_domicilio').send_keys(domicilio)
driver.find_element_by_id('domicilio_domicilio_info_adicional').send_keys(domicilio_info_extra)
driver.find_element_by_id('domicilio_cod_postal').send_keys(cod_postal)
driver.find_element_by_id('domicilio_provincia_iso').send_keys(provincia)
driver.find_element_by_id('domicilio_localidad').send_keys(localidad)
driver.find_element_by_css_selector("label[for='laboral_medios_transporte_Vehículo - Moto']").click()
driver.find_element_by_id('patente_vehiculo1').send_keys(patente)
driver.find_element_by_css_selector("label[for='declaracion_jurada_salud_Sin-sintomas-contacto']").click()
driver.find_element_by_css_selector("label[for='declaracion_jurada_salud_1_No-hisopado-prc']").click()
