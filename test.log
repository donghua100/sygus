from subprocess import Popen, PIPE

process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE,encoding='utf-8')

stdout, stderr = process.communicate()

print(stdout)
f = open("test.log","w",encoding='utf-8')
f.write(stdout)