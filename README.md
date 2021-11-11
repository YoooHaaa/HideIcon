# HideIcon
本工具主要用于筛选有隐藏图标行为的特征的样本

解析步骤：
1 先根据提供的hash下载apk文件
2 利用 aapt 工具解析出apk中的AndroidManifest.xml文件，筛选出AndroidManifest.xml文件中有 activity-alias 标签，且该标签下同时拥有 label、icon 属性的样本，不满足条件的样本则删除
3 利用 apktool.jar 工具反编译步骤2中初筛的apk文件，只需要反编译出AndroidManifest.xml文件和res文件夹即可，然后解析出AndroidManifest.xml中的 activity-alias标签的 label属性和icon属性的值
4 通过label属性的值，在反编译出的 /res/values/string.xml 中查找对应字符串(大多label属性的值需要二次解析)，然后将{hash，label，icon} 的值保存到xlsx

