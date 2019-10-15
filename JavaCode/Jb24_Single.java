public class Jb24_Single
{
	//单例设计模式
	//解决问题：确保一个类在内存中的对象唯一性
	public static void main(String[] args) 
	{
		//Single sDemo = Single.getInstance();
		Single sDemo = Single.s;	//等同于Single sDemo = Single.getInstance();
	}
}

class Single
{
	static Single s = new single();
	private Single(){};
	public static Single getInstance()
	{
		return s;
	}
}
