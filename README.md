# 2019_new_tax_calculator
2019 累计预扣 个税计算器
# 介绍。
## 第一步：new一个对象。。
* 默认参数是上海的社保基数和社保上限，请根据自己所在城市酌情修改

    tax_cal = FcckingTax()

## 第二步：调用get_new_tax()方法
* 第一个参数：薪水
* 第二个参数： 附加扣除总额（子女1000 + 老人1000 + 贷款 ，等等）

    tax_cal.get_new_tax(20000, 3000)
    
    [261.0,
     261.0,
     261.0,
     261.0,
     786.0,
     870.0,
     870.0,
     870.0,
     870.0,
     870.0,
     870.0,
     870.0]
