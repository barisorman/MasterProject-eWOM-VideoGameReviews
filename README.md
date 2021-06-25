# Master Project tool online review extraction and text classification


Owner: Baris Orman

Student Number: 500736999

This tool conists of 3 elements to extract video game details, sales data and online reviews and reviews to eventually classify the review text and measure the sales performance of the video games with a multivariate regression model

The webagent scrapers within this tool are designed specifically for the websites: mobygames.com, vgchartz.com and metacritic.com.

The text classification tools classify the text each on the overall sentimental value, overall innovativeness value and on the topic contribution score of the LDA model.

Please note the following before running the application:

1. Please make sure to download all files within this repository and include all files and folder strucutre.
2. Scrapy framework, Python and jupyter notebook should be installed on the used device.
3. The spider will have to be run in the terminal (or powershell in the case of a windows device) by going to the spider's native directory and executing the command: scrapy runspider (required spider name) -o (required spider name).csv.
4. Autothrottling should be enabled and settings should be adjusted in the setting.py file before running the vgchartz (strart delay: 500, max delay: 5000, target currency: 60.0) and metacritic (strart delay: 500, max delay: 5000, target currency: 60.0) spider, and be carried out during night time (CEST).
5. Please make sure to install the NLTK, Gensim, statsmodel and matplotlib library within your Python environment.
6. The analysis tool should be carried out within the jupyter notebook program, and the folders within the application should be set towards own directories.
7. After the directories within the tools are set in a correct manner, the tool can be performed by running the 'run all button' of the jupyter notebook program.

(8). In case the user wants to apply the text-classification to other datasets, add the data the same way as done in the application and make sure the right columns are selected that has to be analysed.

If there are any questions, comments or error messages, please contact me at the following email address: baris.orman@hva.nl
