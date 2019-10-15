public class Jb37_ObjExcep
{
	/*异常：运行时发生的不正常情况
	分类：
		Throwable:Error和Exception

		异常处理:捕捉形式
	格式：
	try
	{
		需要被检测异常的代码
	}
	catch (异常类 变量) 变量用于接收发生异常的对象
	{
		处理异常的代码
	}
	finally
	{
		一定被执行的代码
	}
	*/
	
	public static void main(String[] args)	//声明：throws MinusIndexException
	{
		int [] arr = new int[3];
		Demo d = new Demo();
		try
		{
			int num = d.method(arr,-27);
			System.out.println("Hello World!"+num);
		}
		catch (MinusIndexException m)	//多个catch，要把父类exception放在最后
		{
			m.printStackTrace();//JVM默认的异常处理机制
			System.out.println("角标不为负");
			//System.exit(0);//退出JVM
		}
		finally	//通常用于释放资源
		{
			System.out.println("finally");
		}
	}
}

class Demo
{
	public int method (int[] arr,int index)throws MinusIndexException	//声明:
	{
		if (arr==null)
		{
			throw new NullPointerException("数组引用不能为空");
		}
		if (index>=arr.length)
		{
			throw new ArrayIndexOutOfBoundsException("角标越界"+index);
		}
		if (index<0)
		{
			throw new MinusIndexException();
		}
		return arr[index];
	}
}

/*自定义异常类
想要一个类成为异常类，必须继承异常体系。
只有异常体系的子类具有可抛性，才能被关键字throws和throw所操作
*/
class MinusIndexException extends Exception
{
	MinusIndexException()
	{
	}
	MinusIndexException(String msg)
	{
		super(msg);
	}
}