# 同一套代码运行在多台设备上
for i in `adb devices|grep 'device$'|awk '{print $1}'`
do
    echo $i
    udid=$i pytest test_case.py --alluredir ./result_$i &
done

# 指定测试用例运行在哪个设备上