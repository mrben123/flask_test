import sys

if(sys.prefix == sys.base_prefix):
    print('项目在真实环境中')
else:
    print('项目在虚拟环境中')


if hasattr(sys, 'real_prefix'):
    print('第二个检验办法也有效了')

## 如果为true则不在虚拟环境中，如果为false则为虚拟环境
## prefix指向虚拟环境，base_prefix为创建virtualenv的系统python前缀