# 这是hitsz的2024大物XA与XB的实验报告的latex模板，以及个人做的实验的相关数据以及程序（python）

# 愿天下没有被物理实验折磨的孩子

## 食用方法
建议在overleaf中直接运行（编译器用XeLatex）,在vscode中运行的方法实在是过于麻烦

**本地编译方法：**

在`texlive2023`下测试可以正常编译。

要求编译时激活python环境，并pip下载`pygmentize`包。
```bash
pip install pygmentize
```

若没有安装该包编译，会输出如下异常：

```latex
system returned with code 1


! Package minted Error: You must have `pygmentize' installed to use this packag
e.

See the minted package documentation for explanation.
Type  H <return>  for immediate help.
 ...

l.18 \begin{document}

?
```

完成后，运行下面的命令即可成功编译：

```sh
xelatex --shell-escape <name>.tex
```

若出现形如下面的输出则编译成功。
```
(d:/Program Files-Study/texlive/2023/texmf-dist/tex/latex/amsfonts/umsa.fd)
(d:/Program Files-Study/texlive/2023/texmf-dist/tex/latex/amsfonts/umsb.fd)
[1] [2] [3] [4] (./磁耦合共振式无线电力传输实验.aux) )
(see the transcript file for additional information)
Output written on 磁耦合共振式无线电力传输实验.pdf (4 pages).
Transcript written on 磁耦合共振式无线电力传输实验.log. 
```

## 致谢
大部分代码源自 https://github.com/LittleYe233/hitsz-physics-ib-reports.git

## 暂不支持首行缩进，待修复
不修了

merge.py用来合并pdf,手写的前两页和电子的后两页

scanner.py用于扫描，可一定程度上消除拍摄照片角度带来的影响

