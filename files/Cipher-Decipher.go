package main

import (
	"bufio"
	"fmt"
	"os"
)

func encrypt(value string) {

	ciphered := ""
	ran := 0
	i := true
	op := ""
	for i {
		op = string(value[ran] + 1)

		ciphered += op
		ran++
		if ran == len(value) {
			i = false
		}

	}
	println("Ciphered:~ ", ciphered)

}

func decipher(value string) {
	Deciphered := ""
	ran := 0
	i := true
	op := ""
	for i {
		op = string(value[ran] - 1)

		Deciphered += op
		ran++
		if ran == len(value) {
			i = false
		}

	}
	println("Deciphered:~ ", Deciphered)

}

func execute() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Welcome to Cyber-Cryto Lab")
	var text string
	fmt.Printf("\n[1] Encrypt Text\n[2] Decrypt Text\n\n->  ")
	var options int8
	fmt.Scanf("%d", &options)
	if options == 1 {
		fmt.Printf("\nEnter text: ")
		text, _ := reader.ReadString('\n')

		encrypt(text)
	} else if options == 2 {
		fmt.Printf("Enter text: ")
		text, _ = reader.ReadString('\n')
		decipher(text)
	} else {
		println("Go back to home")
	}
}
func main() {
	check := true

	for check {
		execute()
		fmt.Print("\n______________________________________________________________________\n")

	}
}
