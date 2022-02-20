package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}
	array := testFunc(n)
	for _, i := range array {
		fmt.Println(len(i), i)
	}
}

func testFunc(n int) [][]int {
	if n < 1 {
		return nil
	}
	var mainArray [][]int
	lenArray := func(arr []int) []int {
		for i := 0; i < n; i++ {
			arr[i] += 1
		}
		return arr
	}(rand.Perm(n))

	for i := 0; i < n; i++ {
		tmpArray := func() (result []int) {
			for j := 0; j < lenArray[i]; j++ {
				result = append(result, rand.Int()%1000)
			}
			return
		}()
		mainArray = append(mainArray, tmpArray)
	}
	for i := 0; i < n; i++ {
		sort.Ints(mainArray[i])
		if i%2 != 0 {
			for j := 0; j < len(mainArray[i])/2; j++ {
				mainArray[i][j], mainArray[i][len(mainArray[i])-j-1] = mainArray[i][len(mainArray[i])-j-1], mainArray[i][j]
			}
		}
	}
	return mainArray
}
