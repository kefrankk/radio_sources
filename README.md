# Checking for radio sources on FIRST Catalog


### ✍🏻 Description

This script is used to cross information about a sample of Dwarf galaxies from [Molina et al. 2021](https://iopscience.iop.org/article/10.3847/1538-4357/ac1ffa), candidates to host supermassive black holes, with observed radio sources from the [FIRST Catalog](https://sundog.stsci.edu/first/catalogs.html). 



### ✅ Requirements


* Python (>= 3.6)
* Pandas (>= 1.3.5)
* requests (>= 2.26.0)
* tqdm (>= 4.65.0)
* Beautiful Soup (>= 4.12.2)
* Selenium (>= 4.11.2)


To install the necessary Python libraries, copy and paste the following command into your terminal:

`pip install requests pandas tqdm beautifulsoup4 selenium  ` 

*Make sure to have the **Chrome WebDriver** installed and in your PATH.*

### 🗒️ Repository Files

In this section, you'll find information about each file in the repository and its specific purpose.

⭐ **webscrap.py**: main code for program execution.

⭐ **Molina_Dwarf_sample.txt**: contain informations about the sample of Dwarf galaxies as SDSS NSA ID name, galaxy position, redshift and more obtained from [Molina et al. 2021](https://iopscience.iop.org/article/10.3847/1538-4357/ac1ffa).

⭐ **radio_sources.txt**: output file containing the galaxy position in degrees (RA and dec).








