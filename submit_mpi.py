import subprocess


def read_node_status():
    process = subprocess.Popen('pestat -f', shell=True,
                               stdout=subprocess.PIPE)
    process.wait()
    return process.stdout

if __name__ == '__main__':
    stdout = read_node_status()
