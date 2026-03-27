import os
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_file_path = os.path.commonpath([absolute_path, target_file]) == absolute_path

        if not valid_file_path:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
            
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        f = open(target_file)
        MAX_CHARS = 10000
        file_content = f.read(MAX_CHARS)
        
        if f.read(1):
            file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content
            
    except Exception as e:
        return f'Error: {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves file content relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to file content from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)