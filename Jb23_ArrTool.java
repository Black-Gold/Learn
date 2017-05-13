/**
文档注释
创建一个操作数组的工具类，包含对数组操作的函数
@author XiaoMing
@version V1.0
*/

public class Jb23_ArrTool
{
	/*该类的方法都是静态的，固该类不需要创建对象，节省内存
	为了确保不让其他程序创建该类对象，将该类的构造函数进行初始化。*/
    private Jb23_ArrTool(){}

	/**获取整数数组的最大值
	@param arr 接收一个元素为int类型的数组
	@return 该数组中的最大元素值*/
    public static int getMax(int[] arr)
    {
        int maxIndex = 0;
        for (int x=1;x<arr.length ;x++ )
        {
            if (arr[x]>arr[maxIndex])
            {
                arr[maxIndex] = arr[x];
            }
        }
        return arr[maxIndex];
    }
	//数组选择排序
	public static void selectSort(int[] arr)
	{
		for (int x=0;x<arr.length-1 ;x++ )
		{
			for (int y=x+1; y<arr.length; y++)
			{
				if (arr[x]>arr[y])
				{
					swap(arr,x,y);
				}
			}
		}
	}
	//数组元素的位置换位
	public static void swap (int[] arr,int x,int y)
	{
		int temp = arr[x];
		arr[x] = arr[y];
		arr[y] = temp;
	}
	//获取指定元素在指定数组的角标，不存在返回-1
	public static int getIndex(int[] arr,int key)
	{
		for (int x=0;x<arr.length ;x++ )
		{
			if (arr[x]==key)
			{
				return x;
			}
		}
		return -1;
	}
	//将int数组转换成字符串
	public static String arrayToString(int[] arr)
	{
		String s = "";
		for (int x=0; x<arr.length;x++ )
		{
			if (x!=arr.length-1)
				s = s + arr[x]+",";
			else
				s = s + arr[x];
		}
		return s;
	}
}

