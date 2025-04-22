package main

import (
	"fmt"
)

func main() {
	tableau := []string{"hello", "kevine", "jaques"}
	for i := range tableau {
		fmt.Println(i, tableau[i])
	}
	fmt.Println("===Deuxieme boucle===")
	for i := 0; i <= 2; i++ {
		fmt.Println(i, tableau[i])
	}

	fmt.Println("===Deuxieme boucle===")

	for _, index := range tableau {
		fmt.Println(index)
	}

}
