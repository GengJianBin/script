import importlib
import ast
import os
import format_log

# 方式一
# desc 导入指定的包，如果包不存在，则使用pip安装后在导入
# param 要安装的包名称
def install_package(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        format_log.log(f"Package '{package_name}' is not installed.Installing...")
        try:
            import pip
        except ImportError:
            format_log.log("Failed to import 'pip'. Please make sure pip is installed.")
            return
        try:
            pip.main(['install',package_name])
            format_log.log(f"Package '{package_name}' has been installed sucessfully.")
        except Exception as e:
            format_log.log(f"Failed to install package '{package_name}': {str(e)}")

# 方式二
def find_imports_in_file(file_path):
    with open(file_path, 'r') as file:
        source = file.read()
        tree = ast.parse(source)
        return {node.name for node in ast.walk(tree) if isinstance(node, ast.Import)}

# desc 递归查找指定路径下的python所引用的包，并安装
# param
#    path 要查找包的路径
def find_and_install(path):
    required_packages = set()
    # 查找指定目录下的py文件中所引用的库
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py'):
                required_packages.update(find_imports_in_file(os.path.join(root, file)))

    # 安装找到的所有包
    for package in required_packages:
        format_log.log(f"Installing {package}")
        pip.main(['install', package])

# 方式三
# 有一些第三方库，如pipreqs，可以扫描你的项目并生成一个requirements.txt文件，
# 其中包含了项目所需的所有包。你可以在部署前运行这样的工具，然后使用
# pip install -r requirements.txt来安装所有依赖。

if __name__ == '__main__' :
    # 使用示例
    required_packages = ['requests','tqdm']
    for package in required_packages :
        install_package(package)