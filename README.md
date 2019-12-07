# RIR-Generator

加混响代码，编译后可在python3环境下使用

## 环境配置

要在python3的环境下进行，setup.py需要相应的运行环境

```
$ pip install -r requirements.txt
```

## 编译

```
$ make
```

`make`成功后会生成`librirgen.so`, `pyrirgen.cpp`, `rirgen.o`, `pyrirgen.cpython-35m-x86_64-linux-gnu.so`四个文件，以及一个文件夹`build`。实际使用中保留`librirgen.so`和`pyrirgen.cpython-35m-x86_64-linux-gnu.so`即可。

使用python加载时，如果出现找不到`.so`库的情况，需要添加环境变量

```
$ export LD_LIBRARY_PATH=/home/phecda/project/RIR-Generator:$LD_LIBRARY_PATH
```
