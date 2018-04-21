public class Jb19_ArrSearch
{
	public static void main(String[] args) 
	{
		int[] arr = {0,1,2,3,4,5,6,7,8,9};
		int index = binarySearch_2(arr,7);
		System.out.println(index);
	}
	/*数组查找功能
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
	*/
	//二分查找法
	public static int binarySearch(int arr[],int key)
	{
		int max,min,mid;
		min = 0;
		max = arr.length-1;
		mid = (max+min)/2;
		while (arr[mid]!=key)
		{
			if (key>arr[mid])
				min = mid + 1;
			else if (key<arr[mid])
				max = mid - 1;
			if (max<min)
				return -1;
			mid = (max+min)/2;
		}
		return mid;
	}
	//第二种写法
	public static int binarySearch_2(int[] arr,int key)
	{
		int max,mid,min;
		min = 0;
		max = arr.length-1;
		while (min<=max)
		{
			mid = (max+min)>>1;	//右移一位相当于除以2的一次幂
			if(key>arr[mid])
				min = mid + 1;
			else if(key<arr[mid])
				max = mid - 1;
			else
				return mid;
		}
		return -1;
	}
}
