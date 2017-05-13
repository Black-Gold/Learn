public class Jb09_SwitchDemo
{
	public static void main(String[] args) 
	{
	//	选择结构：Switch
	/*
		switch (表达式)
		{
		case 取值1:
			执行语句;
			break;
		case 取值2:
			执行语句2;
			break;
			......
		default:
			执行语句;
			break;
		}
	*/
		//根据输入数字，输出对应季节
		int month = 3;
		switch (month)
		{
		case 3:
		case 4:
		case 5:
			System.out.println("是春季");
			break;
		default:
			System.out.println("没有对应的季节");
			break;	//此处break可省略
		}
		/*
	if与switch的应用场景：
if:
	1、对具体的值进行判断
	2、对区间判断
	3、对运算结果是boolean类型的表达式进行判断
switch：
	1、对具体的值进行判断
	2、值的个数是固定的，对于只有几个固定的数值进行判断，建议用switch，效率更高。
	*/
	}
}
