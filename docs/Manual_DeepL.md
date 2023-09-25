



# DeepL
  
Translate words, texts and entire files using the DeepL API  

*Read this in other languages: [English](Manual_DeepL.md), [Português](Manual_DeepL.pr.md), [Español](Manual_DeepL.es.md)*
  
![banner](imgs/Banner_DeepL.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module
To use this module, you must have a DeepL account with an API subscription. 


## Description of the commands

### Translate
  
Translates text or a text, HTML, or XML file and stores the response in a variable.
|Parameters|Description|example|
| --- | --- | --- |
|Auth Key|Account authentication key to access the API|279a2e9d-83b3-c416-7e2d-f721593e42a0:fx|
|Account type|REST API Account Plan|Select|
|Text|Text to translate.||
|Path to XML/HTML file (optional)|Path of the XML/HTML file to translate.||
|Target language|Language to translate to.|Select|
|Split sentences (optional)|Criterion for dividing sentences.|Select|
|Preserve formatting (optional)|Respects original format or let the engine correct some aspects Punctuation at the beginning and end of the sentence; Upper/lower case at the beginning of the sentence.||
|Formality (optional)|Sets whether the translated text should lean towards formal or informal language.||
|Tags to handle (optional)|By default, the translation engine does not take XML/HTML tags into account. By setting the parameter, the API will process input by extracting text out of the structure, splitting it into individual sentences, translating them, and placing them back into the structure.|Select|
|Automatic structure detection (optional)|Use engine authomatic detection of the struture.||
|Non splitting tags (optional)|The specified tags are not considered as text separators.|['p'] > HTML ['document','content'] > XML|
|Non splitting tags (optional)|The specified tags are considered text separators.|['tr', 'div'] > HTML ['title','pal'] > XML|
|Tags to ignore (optional)|The specified tags will be ignored in the translation.|['a'] > HTML ['meta'] > XML|
|Assign result to variable |Variable where the result will be stored.|traslation|

### Translate Document
  
Translates docx, pptx, pdf, htm / html, txt or xlf / xliff files.
|Parameters|Description|example|
| --- | --- | --- |
|Auth Key|Account authentication key to access the API.|279a2e9d-83b3-c416-7e2d-f721593e42a0:fx|
|Account type|REST API Account Plan.|Select|
|Path to file|Path of the file to translate.||
|Saving path|Path where the translated file will be saved.||
|Target language|Language to translate to.|Select|
|Assign result to variable |Variable where the result will be stored.|traslation|
