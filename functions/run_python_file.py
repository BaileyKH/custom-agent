import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_file_path = os.path.commonpath([absolute_path, target_file]) == absolute_path
        output = ''

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ['python', target_file]

        if args:
            command.extend(args)

        sub_return = subprocess.run(command, cwd=absolute_path, capture_output=True, text=True, timeout=30)

        if sub_return.returncode != 0:
            output += f'Process exited with code {sub_return.returncode}'
        elif not sub_return.stdout and not sub_return.stderr:
            output += 'No output produced'
        else:
            output += f'STDOUT: {sub_return.stdout}'
            output += f'STDERR: {sub_return.stderr}'

        return output



    except Exception as e:
        return f'Error: executing Python file: {e}'