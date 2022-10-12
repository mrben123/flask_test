import getpass
import socket
import sys

# _user = getpass.getuser()
_hostname = socket.gethostname()

print('>>>')
print('当前用户是:',_hostname)

if(sys.prefix == sys.base_prefix):
    print('项目在真实环境中')
else:
    print('项目在虚拟环境中')

print('检查结束，请继续~')
print('<<< \n')

# if hasattr(sys, 'real_prefix'):
#     print('第二个检验办法也有效了')


## 如果为true则不在虚拟环境中，如果为false则为虚拟环境
## prefix指向虚拟环境，base_prefix为创建virtualenv的系统python前缀
