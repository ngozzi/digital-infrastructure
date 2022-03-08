# The adoption of non-pharmaceutical interventions and the role of digital infrastructure during the COVID-19 Pandemic in Colombia, Ecuador, and El Salvador

Code and data for the paper at: https://arxiv.org/abs/2202.12088

Abstract: Adherence to the non-pharmaceutical interventions (NPIs) put in place to mitigate the spreading of infectious diseases is a multifaceted problem. Socio-demographic, socio-economic, and epidemiological factors can influence the perceived susceptibility and risk which are known to affect behavior. Furthermore, the adoption of NPIs is dependent upon the barriers, real or perceived, associated with their implementation. We study the determinants of NPIs adherence during the first wave of the COVID-19 Pandemic in Colombia, Ecuador, and El Salvador. Analyses are performed at the level of municipalities and include socio-economic, socio-demographic, and epidemiological indicators. Furthermore, by leveraging a unique dataset comprising tens of millions of internet Speedtest measurements from Ookla, we investigate the quality of the digital infrastructure as a possible barrier to adoption. We use publicly available data provided by Meta capturing aggregated mobility changes as a proxy of adherence to NPIs. Across the three countries considered, we find a significant correlation between mobility drops and digital infrastructure quality. The relationship remains significant after controlling for several factors including socio-economic status, population size, and reported COVID-19 cases. This finding suggests that municipalities with better connectivity were able to afford higher mobility reductions. The link between mobility drops and digital infrastructure quality is stronger at the peak of NPIs stringency. We also find that mobility reductions were more pronounced in larger, denser, and wealthier municipalities. Our work provides new insights on the significance of access to digital tools as an additional factor influencing the ability to follow social distancing guidelines during a health emergency 


### Instructions
The folder ```data``` contains a subfolder for each country (```colombia```, ```ecuador```, ```el-salvador```). Each subfolder contains the data for the analysis:
- ```master-files```: ```.shp``` files with all the information regarding the municipalities of the country (geopgraphic polygons, population, GDP, HDI, population density, demographic, internet speed, etc)
- ```fb-movement-range-maps```: Movement Range Maps data from Data for Good at Meta Program
- ```oxford-policy-report```: Oxford Covid-19 Government Response Tracker (OxCGRT) data
- ```epidemiological-data```: number of new cases / deaths in different municipalities


The folder ```code``` contains the Python code to reproduce the main analyses of the paper, in particular:
- ```correlations```: static and time-varying correlation analysis, partial correlations with several controls 
- ```regressions```: static and time-varying regression analysis, with single or multiple regressors, multicollinearity analysis
- ```npis-adherence-viz```: visualisation of mobility changes across 2020 in the three countries together with the Stringency Index evolution
- ```functions```: scripts to correctly load datasets, compute (partial) correlations, Bootstrap regression, plotting style


### Data sources
All the dataset but the internet Speedtest measurements from Ookla are publicly available. <ins> The Ookla dataset is instead proprietary and cannot be shared publicly </ins>. Therefore, in the ```data``` folder, variables that are derived from Ookla datasets are either intentionally set to constant or missing. As a consequence, running the code will return errors or results that are inconsistent with those reported in the paper. Nonetheless, we report in ```code/correlations/correlations-in-time```, ```code/regressions/output-static```, and ```code/regressions/output-time``` the values of correlations and regression parameters obtained with the full dataset.


List of data sources:
- Movement Range Maps: https://data.humdata.org/dataset/movement-range-maps?
- Oxford Covid-19 Government Response Tracker: https://www.bsg.ox.ac.uk/research/research-projects/covid-19-government-response-tracker
- High-Resolution Density Maps: https://dataforgood.facebook.com/dfg/tools/high-resolution-population-density-maps
- Colombia - Municipality Population: https://www.dane.gov.co/index.php/estadisticas-por-tema/demografia-y-poblacion/proyecciones-de-poblacion
- Relative Wealth Index: https://data.humdata.org/dataset/relative-wealth-index
- Geographic data: https://gadm.org/download_country.html
- Epidemiological data:
  - Colombia: https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data
  - Ecuador: https://www.covid19ecuador.org/cantones
  - El Salvador: https://diario.innovacion.gob.sv
- GDP data:
  - Colombia:https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales/cuentas-nacionales-departamentales
  - Ecuador: J. Illingworth and F. Campana. Informe sobre Desarrollo Humano del Ecuador. Fundacion Ecuador, 2019
  - El Salvador:  https://www.sv.undp.org/content/el_salvador/es/home/library/hiv_aids/almanaque-262.html
- HDI/MDP data:
  - Colombia: https://www.dane.gov.co/index.php/estadisticas-por-tema/pobreza-y-condiciones-de-vida/pobreza-y-desigualdad/medida-de-pobreza-multidimensional-de-fuente-censal
  - Ecuador: J. Illingworth and F. Campana. Informe sobre Desarrollo Humano del Ecuador. Fundacion Ecuador, 2019
  - El Salvador: https://www.sv.undp.org/content/el_salvador/es/home/library/hiv_aids/almanaque-262.html
- Colombia - Fixed Internet Penetration at the Municipal Level: https://www.datos.gov.co/Ciencia-Tecnolog-a-e-Innovaci-n/Internet-Fijo-Penetraci-n-Municipio/fut2-keu8
- Colombia - Employment: http://datlascolombia.com/#/downloads
