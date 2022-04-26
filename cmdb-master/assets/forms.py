from django import forms


class SoftwareForm(forms.Form):
    subassettype = forms.IntegerField(label="软件类型")
    licensenum = forms.IntegerField(label="授权数量")
    version = forms.CharField(label="软件/系统版本", min_length=1, max_length=64)

class TesterForm(forms.Form):
    licensenum = forms.CharField(label="项目名称", min_length=1, max_length=64)
    subassettype = forms.IntegerField(label='平台')

class InterfaceForm(forms.Form):

    # interfaceid = forms.CharField(max_length=64,  label='接口编号')
    interfaceurl = forms.CharField(label="接口地址",  min_length=1, max_length=200)
    interfacetype = forms.CharField(label="请求类型",  min_length=1, max_length=64)
    paramtype = forms.CharField(label="参数类型",  min_length=1, max_length=64)
    testdata = forms.CharField(label="参数类型",max_length=3000)
    Expectedresults = forms.CharField(label="预期结果",  min_length=1, max_length=64)
    testresults = forms.CharField(label="测试结果",  min_length=1, max_length=64)



