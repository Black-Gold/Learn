public class Jb17_ArrDemo
{
	public static void main(String[] args) 
	{
		/*数组定义格式1：
		元素类型[] 数组名 = new 元素类型[元素个数或数组长度];
		格式2：
		元素类型[] 数组名 = new 元素类型[] {元素,元素,........};
		数组的操作，对角标进行操作，从0角标开始。
		*/
		//int [] arr = new int[]{2,54,4,5,4,4,5,79};
		int [] arr = {-2,-5,-79,-9};
		for (int x=0;x<arr.length ; x++)
		{
			System.out.println("arr["+x+"] = "+arr[x]);
		}

		int max = getMax(arr);
		System.out.println("最大值是"+max);
	}
	//定义功能求数组最大值
	public static int getMax(int[] arr)
	{
		int max = arr[0];
		for (int x=1 ;x<arr.length ;x++ )
		{
			if (arr[x]>max)
			{
				max = arr[x];
			}
		}
		return max;
	}
}
