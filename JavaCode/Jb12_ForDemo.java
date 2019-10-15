public class Jb12_ForDemo
{
	public static void main(String[] args) 
	{
	/*
	for (初始化表达式;循环条件表达式;循环后的操作表达式)
	{
		执行语句;(循环体)
	}
	while与for可互换，
	区别：for为循环定义的变量在循环结束后就从内存释放
	while循环使用的变量在循环结束后仍可以继续使用
	*/
	//for完成累加
		int sum = 0;
		for (int x=1; x<=100; x++)
		{
			sum+=x;
		}
		System.out.println(sum);
		//System.out.println(x);	此处会提示找不到变量x错误，因x已在内存中释放	
	}
}
