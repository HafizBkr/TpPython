package main

import (
	"fmt"
)

func main() {
	tableau := []string{"hello", "kevine", "jaques"}

	fmt.Println("===Deuxieme boucle===")
	for i := 0; i <= 2; i++ {
		fmt.Println(i, tableau[i])
	}

}
