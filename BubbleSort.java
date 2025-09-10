/**
 * The BubbleSort class provides a static method to sort an array of integers
 * in ascending order using the bubble sort algorithm.
 *
 * <p>Example usage:
 * <pre>
 *     int[] arr = {64, 34, 25, 12, 22, 11, 90};
 *     BubbleSort.bubbleSort(arr);
 * </pre>
 * </p>
 */
public class BubbleSort {

    /**
     * Sorts the specified array of integers in ascending order using
     * the bubble sort algorithm. The sorting is done in-place.
     *
     * @param arr the array of integers to be sorted
     * @throws NullPointerException if the input array is null
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    /**
     * The main method demonstrates the usage of the bubbleSort method.
     * It creates an example array, sorts it, and prints the sorted result.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(arr);
        System.out.println("Sorted array is:");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}

