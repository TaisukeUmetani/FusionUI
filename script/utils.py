def reload_module(module_name) -> object:
    import importlib
    importlib.reload(module_name)
    module_name = list(str(module_name).split())[1]
    return f'Reload {module_name} correct!'


def terminal():
    script = str(input('bash script: '))

    # 文字列(script)が空白/NULLか判定
    if script:
        import subprocess
        script_list = script.split()
        output = subprocess.run(script_list)
        print(f'finished run \'{script}\'')
    else:
        print('No command entered')


if __name__ == '__main__':
    for i in range(4):
        terminal()

