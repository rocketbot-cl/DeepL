# coding: utf-8

"""
Module to work with excel opened or created with rocketbot.

Rocketbot Functions:
    - GetParams("module"): Get the command name running. Module params in the package.json
    - GetParams("id"): Get the information sent by the user. Id params in the package.json
        var = GetParams(variable)
    - SetVar("variable_name", "dato"): Set a value to a variable.
    - GetVar("variable_name"): Get the value of a variable.
        var = GetVar("variable_name")

To install libraries use in the module path:
    pip install <package> -t ./libs 
"""

# Import globals or rocketbot libs
# -----------------------------------

import os
import sys
import traceback

# This lines is to linter
# -----------------------------------
GetParams = GetParams #type:ignore
tmp_global_obj = tmp_global_obj #type:ignore
PrintException = PrintException #type:ignore
SetVar = SetVar #type:ignore
GetGlobals = GetGlobals #type:ignore

# Add modules libraries to Rocektbot
# -----------------------------------
base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'DeepL', 'libs')
if cur_path not in sys.path:
    sys.path.append(cur_path)

import deepl

module = GetParams("module")

try:
    if module == 'translate':
        
        api_key = GetParams("api_key")
        acc_type = GetParams("acc_type")
        path = GetParams("path") # str
        text = GetParams("text") # str
        target = GetParams("target") # str
        split_sentences = GetParams("split_sentences") # str
        preserve_formatting = GetParams("preserve_formatting") # bool
        formality = GetParams("formality") # bool
        tag_handling = GetParams("tag_handling") # str
        outline_detection = GetParams("outline_detection") # bool
        non_splitting_tags = GetParams("non_splitting_tags") # list
        splitting_tags = GetParams("splitting_tags") # list
        ignore_tags = GetParams("ignore_tags") # list
        var_ = GetParams("var_")
        
        if acc_type == "free":
            server = "https://api-free.deepl.com/"
        if acc_type == "pro":
            server = "https://api.deepl.com/"
        
        if path:
            to_translate = open(path, 'r').read()

        if text:
            to_translate = text
        
        split_sentences = split_sentences if split_sentences else None
        preserve_formatting = eval(preserve_formatting) if preserve_formatting else None
        formality = formality if formality else None
        tag_handling = tag_handling if tag_handling else None
        outline_detection = eval(outline_detection) if outline_detection else None
        non_splitting_tags = eval(non_splitting_tags) if non_splitting_tags else None
        splitting_tags = eval(splitting_tags) if splitting_tags else None
        ignore_tags = eval(ignore_tags) if ignore_tags else None

        
        translator = deepl.Translator(auth_key = api_key, server_url = server)
        result = translator.translate_text(text = to_translate, 
                                            target_lang = target,
                                            split_sentences = split_sentences,
                                            preserve_formatting = preserve_formatting,
                                            formality = formality,
                                            tag_handling = tag_handling,
                                            outline_detection = outline_detection,
                                            non_splitting_tags = non_splitting_tags,
                                            splitting_tags = splitting_tags,
                                            ignore_tags = ignore_tags)
        SetVar(var_, result)
        
    if module == "translate_document":
        api_key = GetParams("api_key")
        acc_type = GetParams("acc_type")
        path = GetParams("path")
        save_path = GetParams("save_path")
        target = GetParams("target")
        var_ = GetParams("var_")
        
        if acc_type == "free":
            server = "https://api-free.deepl.com/"
        if acc_type == "pro":
            server = "https://api.deepl.com/"
        
        translator = deepl.Translator(auth_key = api_key, server_url = server)
        result = translator.translate_document_from_filepath(input_path=path, output_path=save_path, target_lang=target)
        SetVar(var_, result)
            
except Exception as e:
    traceback.print_exc()
    print("\x1B[" + "31;40mError\x1B[" + "0m")
    PrintException()
    SetVar(var_, False)
    raise e