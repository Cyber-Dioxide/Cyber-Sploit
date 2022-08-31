package main

import (
	"fmt"
)

var colorReset = "\033[0m"

var colorRed = "\033[31m"
var colorGreen = "\033[32m"
var colorYellow = "\033[33m"
var colorBlue = "\033[34m"
var colorPurple = "\033[35m"
var colorCyan = "\033[36m"
var colorWhite = "\033[37m"

func color_print(str string, color string) {
	var c_c = color
	switch c_c {
	case "blue":
		c_c := colorBlue
		fmt.Println(string(c_c), str)
	case "red":
		c_c := colorRed
		fmt.Println(string(c_c), str)

	case "white":
		c_c := colorWhite
		fmt.Println(string(c_c), str)
	case "yellow":
		c_c := colorYellow
		fmt.Println(string(c_c), str)
	case "green":
		c_c := colorGreen
		fmt.Println(string(c_c), str)
	case "purple":
		c_c := colorPurple
		fmt.Println(string(c_c), str)
	case "cyan":
		c_c := colorCyan
		fmt.Println(string(c_c), str)
	default:
		c_c := colorWhite
		fmt.Println(string(c_c), str)

	}

}

func main() {
	var col_name string
	fmt.Printf("Enter color name:~ ")
	var decription string
	fmt.Scan(&col_name)
	fmt.Printf("\nEnnter description to colorize:~ ")
	fmt.Scan(&decription)
	color_print(decription, col_name)

}
