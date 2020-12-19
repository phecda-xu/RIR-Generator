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

使用python加载时，如果出现找不到`.so`库的情况，需要将生成的so文件的路径添加到环境变量，比如:

```
$ export LD_LIBRARY_PATH=/*/*/*/RIR-Generator:$LD_LIBRARY_PATH
```


注：没找到原代码的仓库链接，如有了解的烦请告知，感谢原作者的共享。

参考：
[RIR-Generator](https://github.com/ehabets/RIR-Generator/tree/5eb70f066b74ff18c2be61c97e8e666f8492c149)
[py-RIR-Generator](https://github.com/srikanthrajch/py-RIR-Generator)
